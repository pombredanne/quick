from guick import gui_it, gui_option
import click

@click.group()
@click.option('--debug/--no-debug', default=False)
def cli(debug):
    print(debug)


@cli.command()
@click.argument("arg", nargs=-1)
@click.option("--hello", default="world", help="say hello")
@click.option("--add", type=int, help="input an integer number",\
              hide_input=True)
@click.option("--times", type=float, help="input a double number")
@click.option("--minus", type=float, help="input two numbers", nargs=2)
@click.option("--flag", is_flag=True)
@click.option('--shout/--no-shout', default=True)
@click.option('--language', type=click.Choice(['c', 'c++']))
@click.option('-v', '--verbose', count=True)
def example_cmd(**argvs):
    for k, v in argvs.items():
        print(k, v, type(v))


@cli.command()
@click.option("--hello")
def sync(hello):
    print('Synching', hello)

@cli.command()
def func():
    print("func")

@gui_option
@click.command()
def option_gui():
    """run with
    python test.py --gui
    """
    print("gui_option")


if __name__ == "__main__":
    # gui_it(example_cmd, run_exit=True)
    # option_gui()
    gui_it(cli, run_exit=False)
