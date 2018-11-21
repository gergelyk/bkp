#!/usr/bin/env python
import click
import inspect
from pathlib import Path
from types import SimpleNamespace

from bkp.action_backup import backup
from bkp.action_restore import restore
from bkp.action_info import info
from bkp.exceptions import ExpectedError, InvalidInput
from bkp.resources import APP_VERSION
from bkp.terminal import echo_err, echo_inf

def check_invalid_options(command, params, kwargs):
    cmd_name = command.__name__
    cmd_args = inspect.getargspec(command).args

    all_options = filter(lambda p: isinstance(p, click.core.Option), params)
    provided_options = list(p.name for p in all_options if p.default != kwargs.get(p.name, p.default))
    if cmd_name in provided_options:
        provided_options.remove(cmd_name)

    for opt in provided_options:
        if opt not in cmd_args:
            raise InvalidInput(f"Option {opt!r} cannot be combined with {cmd_name!r} action")


def ensure_at_least_one_item(ctx, param, value):
    if not value:
        raise click.BadParameter("At least one path needs to be provided.")
    return value


def print_version(ctx, param, value):
    if not value or ctx.resilient_parsing:
        return
    click.echo(APP_VERSION)
    ctx.exit()

def app(**kwargs):
    kw = SimpleNamespace(**kwargs)

    if kw.restore:
        check_invalid_options(restore, main.params, kwargs)
        action = lambda path: restore(path, kw.delete, kw.yes)
    elif kw.info:
        check_invalid_options(info, main.params, kwargs)
        action = lambda path: info(path)
    else:
        # backup
        check_invalid_options(backup, main.params, kwargs)
        action = lambda path: backup(path, kw.delete, kw.yes, kw.archive, kw.message, kw.message_edit)

    last_idx = len(kw.paths) - 1
    for idx, path in enumerate(kw.paths):
        action(Path(path))
        if idx != last_idx:
            echo_inf('')


@click.command()
@click.argument('paths', nargs=-1, type=click.Path(exists=True), callback=ensure_at_least_one_item)
@click.option('-r', '--restore', default=False, is_flag=True, help="Restore resources from backup(s).")
@click.option('-d', '--delete', default=False, is_flag=True, help="Delete source file/directory.")
@click.option('-a', '--archive', default=False, is_flag=True, help="Create an archive.")
@click.option('-y', '--yes', default=False, is_flag=True, help="Answer 'yes' to all the questions.")
@click.option('-m', '--message', help="Message to be included.")
@click.option('-M', '--message-edit', default=False, is_flag=True, help="The same as '--message' but opens text editor.")
@click.option('-i', '--info', default=False, is_flag=True, help="Read metadata.")
@click.option('--version', is_flag=True, callback=print_version, expose_value=False, is_eager=True, help="Print version.")
def main(**kwargs):
    """Create/restore backups of your files/directories."""
    try:
        app(**kwargs)
    except ExpectedError as exc:
        echo_err(exc)
        exit(exc.exit_code)


if __name__ == '__main__':
    main()
