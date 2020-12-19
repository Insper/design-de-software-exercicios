#!/usr/bin/env python
import click

from challenge_admin import new_challenge, validate_challenge
from trace_admin import new_trace, validate_trace, build_trace


@click.group(help='Admin for Software Design challenges.')
def cli():
    pass


cli.command(help='Create new coding challenge.')(new_challenge)
cli.command(help='Run coding challenge tests and validations. The challenge name is optional.')(validate_challenge)
cli.command(help='Create new trace challenge.')(new_trace)
cli.command(help='Validate trace challenge. The trace name is optional.')(validate_trace)
cli.command(help='Build code traces. The trace name is optional.')(build_trace)

@cli.command(help="Validate all challenges")
def validate():
    validate_challenge()
    validate_trace()


if __name__ == "__main__":
    cli()
