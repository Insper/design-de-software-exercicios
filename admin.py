#!/usr/bin/env python
from pathlib import Path
import sys
import os
import json
import click
from strtest import str_test

from cmd_utils import success, danger, info


CUR_DIR = Path(__file__).parent
CHALLENGES = CUR_DIR / 'challenges'
RAW_DIR = 'raw'
DETAILS = 'details.json'
QUESTION = 'question.md'
TESTS = 'tests.py'
with open(CUR_DIR / 'tags.txt') as f:
    TAGS = [t for t in f.read().split() if t]


TEMPLATE_DETAILS = '''{
    "title": "",
    "published": true,
    "terminal": true,
    "function_name": null,
    "tags": ""
}
'''

TEMPLATE_TESTS = '''"""
Read strtest docs for more details: https://github.com/Insper/python-string-test-runner

Quick Guide:
===========
TestCaseWrapper has the following attributes:
    - function: function given by the user
    - program: function that executes the program given by the user
    - module: python module loaded from the file given by the user
Useful asserts:
    - assert_similar(self, string1, string2, dist_max=1, case_sensitive=False, msg=None)
    - assert_printed(self, value, index=None, msg=None)
    - assert_printed_all(self, values, msg=None, **kwargs)
Mocks (all functions have the attributes calls, args, and kwargs, that store the call count and arguments):
    - mock_print: printed attribute stores a list of printed strings
    - mock_input: set input_list with a sequence of inputs to be used
    - mock_open: the attribute opened is a list of files that have not been closed and it is possible to add mock files in the dictionary attribute 'files' (keys are the filenames and values are their content)
    - mock_random: keys are tuples with the expected arguments and the values are sequences of numbers

If you implement the methods setUpClass, setUp, or tearDown, remember to call the superclass implementation.
"""
from strtest import str_test


class TestCase(str_test.TestCaseWrapper):
    TIMEOUT = 3  # Seconds

    def test_1(self):
        # Implement as many test functions as you need. You just need to start the method names with test_
        pass
'''


@click.group(help='Admin for Software Design challenges.')
def cli():
    pass


@cli.command(help='Create new challenge.')
@click.argument('slug')
def new(slug):
    info('Creating challenge', slug)
    ch_dir = CHALLENGES / slug
    if ch_dir.is_dir():
        danger(f'There is already a challenge called {slug}')
        sys.exit()

    os.mkdir(ch_dir)
    (ch_dir / RAW_DIR / slug).mkdir(parents=True, exist_ok=True)
    create_file(ch_dir / DETAILS, TEMPLATE_DETAILS)
    create_file(ch_dir / QUESTION)
    create_file(ch_dir / TESTS, TEMPLATE_TESTS)
    create_file(ch_dir / 'solution.py')
    create_file(ch_dir / 'wrong.py')


@cli.command(help='Run tests and validations. The challenge name is optional.')
@click.argument('challenge_name', default=None, required=False)
def validate(challenge_name):
    if challenge_name:
        if not (CHALLENGES / challenge_name).is_dir():
            danger(f'The challenge {challenge_name} does not exist.')
            sys.exit()
        validate_challenge(CHALLENGES / challenge_name)
    else:
        info('Testing all challenges')
        ok = True
        for ch_dir in CHALLENGES.iterdir():
            if not ch_dir.is_dir(): continue
            if not validate_challenge(ch_dir):
                ok = False
        if ok:
            success('Everything ok!')
        else:
            danger('Failed for some validation')


def validate_challenge(ch_dir):
    info('Validating challenge', ch_dir)
    ok = True
    try:
        details = validate_details(ch_dir)
        validate_question(ch_dir)
        run_tests_for_challenge(ch_dir, details.get('function_name'))
    except AssertionError as e:
        danger('Validation error:', e)
        ok = False
    if ok:
        success("OK")
    else:
        danger('FAIL')
    return ok


def validate_details(ch_dir):
    details_file = ch_dir / DETAILS
    details_str = load_file(details_file)
    try:
        details = json.loads(details_str)
    except json.decoder.JSONDecodeError:
        raise AssertionError(f'File {details_file} is not a valid JSON.')
    assert isinstance(details, dict), f'File {details_file} should be a JSON dictionary.'
    assert details.get('title'), f'File {details_file} should have a key "title".'
    assert details.get('published'), f'File {details_file} should have a key "published".'
    assert details.get('terminal'), f'File {details_file} should have a key "terminal".'
    assert details.get('tags'), f'File {details_file} should have a key "tags".'
    tags = details['tags'].split(',')
    for tag in tags:
        if tag:
            assert tag in TAGS, f'The tag {tag} does not exist'
    return details


def validate_question(ch_dir):
    question_file = ch_dir / QUESTION
    question = load_file(question_file)
    assert question.strip(), f'File {question_file} should not be empty.'


def run_tests_for_challenge(ch_dir, function_name):
    correct = list(ch_dir.glob('solution*.py'))
    wrong = list(ch_dir.glob('wrong*.py'))
    test_files = ch_dir / TESTS
    assert correct, 'There should be at least one correct solution file.'
    assert wrong, 'There should be at least one wrong solution file.'
    for code_file in correct + wrong:
        run_test(code_file, test_files, function_name)


def run_test(code_file, test_file, function_name):
    code = load_file(code_file)
    tests = load_file(test_file)
    result = str_test.run_tests(code, tests, function_name)
    expected = 'solution' in str(code_file)
    assert expected == result.success, f'Result was different than the expected for the file {code_file}'

def load_file(file_path):
    if not file_path.is_file():
        raise AssertionError(f'File {file_path} does not exist.')
    with open(file_path) as f:
        return f.read()


def create_file(filename, content=None):
    if not content:
        content = ''
    with open(filename, 'w') as f:
        f.write(content)


if __name__ == "__main__":
    cli()
