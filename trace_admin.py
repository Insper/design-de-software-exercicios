import click
import json
import sys
import os
from autotracer.auto_tracer import AutoTracer

from config import TRACES, DETAILS, CONCEPTS, TRACE_CODE, TRACE_DATA
from cmd_utils import success, danger, info, create_file, load_file, choose_concept


def build_details(concept, title, published=True):
    return json.dumps({
        'concept': concept,
        'title': title,
        'published': published,
    })


@click.option('--slug', prompt='Trace slug')
@choose_concept
@click.option('--title', prompt='Title of the trace challenge')
@click.option('--published/--no-published', default=True)
def new_trace(slug, concept, title, published):
    concept = CONCEPTS[concept-1]
    info('Creating trace challenge', slug)
    ch_dir = TRACES / slug
    if ch_dir.is_dir():
        danger(f'There is already a trace called {slug}')
        sys.exit()

    os.mkdir(ch_dir)
    create_file(ch_dir / DETAILS, build_details(concept, title, published))
    create_file(ch_dir / TRACE_CODE)


@click.argument('slug', default=None, required=False)
def validate_trace(slug=None):
    if slug:
        if not (TRACES / slug).is_dir():
            danger(f'The trace challenge {slug} does not exist.')
            sys.exit()
        validate_trace_dir(TRACES / slug)
    else:
        info('Testing all trace challenges')
        failures = []
        for ch_dir in TRACES.iterdir():
            if not ch_dir.is_dir(): continue
            if not validate_trace_dir(ch_dir):
                failures.append(ch_dir.name)
        if failures:
            danger('Failed for the following traces')
            for failure in failures:
                danger(f'  {failure}')
        else:
            success('Everything ok!')


@click.argument('slug', default=None, required=False)
@click.option('--force', '-f', is_flag=True)
def build_trace(slug=None, force=False):
    if slug:
        if not (TRACES / slug).is_dir():
            danger(f'The trace challenge {slug} does not exist.')
            sys.exit()
        run_autotracer(slug)
    else:
        info('Building all missing trace challenges')
        count = 0
        for ch_dir in TRACES.iterdir():
            if not ch_dir.is_dir(): continue
            if not force and (ch_dir / TRACE_DATA).is_file(): continue
            run_autotracer(ch_dir.name)
            count += 1
        success(f'Built {count} traces')


def validate_trace_dir(ch_dir):
    info('Validating trace challenge', ch_dir)
    ok = True
    try:
        validate_trace_details(ch_dir)
        validate_not_empty(ch_dir / TRACE_CODE)
        validate_not_empty(ch_dir / TRACE_DATA, msg='Trace file does not exist. Build it with admin.py build-trace')
    except AssertionError as e:
        danger('Validation error:', e)
        ok = False
    if ok:
        success("OK")
    else:
        danger('FAIL')
    return ok


def validate_trace_details(ch_dir):
    details_file = ch_dir / DETAILS
    details = validate_json(details_file)
    assert isinstance(details, dict), f'File {details_file} should be a JSON dictionary.'
    assert details.get('title'), f'File {details_file} should have a key "title".'
    assert details.get('published'), f'File {details_file} should have a key "published".'
    assert details.get('concept'), f'File {details_file} should have a key "concept".'
    concept = details['concept']
    assert concept in CONCEPTS, f'The concept {concept} does not exist'
    return details


def validate_not_empty(target, msg=None):
    content = load_file(target, msg)
    if not msg:
        msg = f'File {target} should not be empty.'
    assert content.strip(), msg


def validate_json(json_file):
    json_str = load_file(json_file)
    try:
        return json.loads(json_str)
    except json.decoder.JSONDecodeError:
        raise AssertionError(f'File {json_file} is not a valid JSON.')


def run_autotracer(slug):
    with AutoTracer() as tracer:
        tracer.trace_file(TRACES / slug / TRACE_CODE)
    trace = tracer.trace

    trace_data = []
    for entry in trace:
        trace_data.append({
            'line_i': entry.line_i,
            'line': entry.line,
            'name_dicts': entry.name_dicts,
            'call_line_i': entry.call_line_i,
            'retval': entry.retval,
            'stdout': [{'out': s.std_output, 'in': s.user_input} for s in entry.stdout],
        })
    with open(TRACES / slug / TRACE_DATA, 'w') as f:
        json.dump(trace_data, f)
