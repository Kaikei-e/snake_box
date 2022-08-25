from __future__ import print_function

import click
import os
import traceback


@click.group()
def cli():
    pass


def contain(command):
    # TODO: exec command, note the difference between the exec flavours
    #       https://docs.python.org/2/library/os.html#os.execv
    # NOTE: command is an array (the first element is path/file, and the entire
    #       array is exec's args)
    os._exit(0)  # TODO remove after


@cli.command(context_settings=dict(ignore_unknown_options=True, ))
@click.argument('Command', required=True, nargs=-1)
def run(command):
    pid = 0
    if pid == 0:
        try:
            contain(command)

        except Exception:
            traceback.print_exc()
            os._exit(1)

    _, status = os.waitpid(pid, 0)
    print('{} exited with status {}'.format(pid, status))


if __name__ == '__main__':
    cli()
