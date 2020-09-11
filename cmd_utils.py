import click


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


# Colors
yellow = _make_color_text('yellow')
blue = _make_color_text('blue')
green = _make_color_text('green')
red = _make_color_text('red')

# Cmd
success = _make_cmd(green)
danger = _make_cmd(red)
info = _make_cmd(yellow)
