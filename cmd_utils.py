import os
import click
from config import CONCEPTS


def load_file(file_path, msg=None):
    if not msg:
        msg = f'File {file_path} does not exist.'
    if not file_path.is_file():
        raise AssertionError(msg)
    with open(file_path) as f:
        return f.read()


def create_file(filename, content=None):
    if not content:
        content = ''
    with open(filename, 'w') as f:
        f.write(content)


def open_in_editor(filename):
    try:
        with open('.open_cmd') as f:
            open_cmd = f.read().strip()
    except FileNotFoundError:
        danger('File .open_cmd does not exist. Create one and write the open command (e.g. code, gedit, etc.)')
    os.system(f'{open_cmd} {filename} &')


def echo_cmd(cmd, txt, color):
    click.echo(f'{color(cmd)}: {txt}')


def _make_color_text(color):
    def color_text(text):
        return click.style(str(text), fg=color)
    return color_text


def _make_cmd(color):
    def cmd(cmd, txt=None):
        cmd = str(cmd)
        if txt:
            txt = str(txt)
            echo_cmd(cmd, txt, color)
        else:
            click.echo(color(cmd))
    return cmd


def choose_concept(func):
    concept_options = '\n'.join(f'{i + 1}) {c}' for i, c in enumerate(CONCEPTS))
    prompt = f'Select the concept:\n{concept_options}\nChoice'
    return click.option('--concept', prompt=prompt, type=click.IntRange(1, len(CONCEPTS)+1))(func)


# Colors
yellow = _make_color_text('yellow')
blue = _make_color_text('blue')
green = _make_color_text('green')
red = _make_color_text('red')

# Cmd
success = _make_cmd(green)
danger = _make_cmd(red)
info = _make_cmd(yellow)
