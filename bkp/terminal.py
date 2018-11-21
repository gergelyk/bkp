import textwrap
import click

FILE_INDENT = 2

def _indent(text, cols):
    return textwrap.indent(text, prefix=' ' * cols)

def _preproc(text, indent):
    text = str(text)
    text = _indent(text, indent)
    return text

def _echo(text, indent, fg, **kwargs):
    text = _preproc(text, indent)
    click.secho(text, fg=fg, **kwargs)

def echo_path(text, indent=0, highlight=False, **kwargs):
    fg='green'
    _echo(text, indent, fg, **kwargs)

def echo_inf(text, indent=FILE_INDENT, highlight=False, **kwargs):
    fg = [None, 'yellow'][highlight]
    _echo(text, indent, fg, **kwargs)

def echo_wrn(text, indent=FILE_INDENT, highlight=False, **kwargs):
    fg='magenta'
    _echo(text, indent, fg, **kwargs)

def echo_err(text, indent=FILE_INDENT, highlight=False, **kwargs):
    fg='red'
    _echo(text, indent, fg, **kwargs)

def confirm(text, indent=FILE_INDENT, highlight=False, **kwargs):
    return click.confirm(_preproc(text, indent), **kwargs)
