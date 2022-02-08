import click  # pragma: no cover
from . import BaseClass, base_function  # pragma: no cover

@click.command()
def main() -> None:
    """Example script."""
    click.echo("Hello World!")
    click.echo("Version {}".format(__version__))
    click.echo("Executing main function")
    base = BaseClass()
    click.echo(base.base_method())
    click.echo(base_function())
    click.echo("End of main function")


if __name__ == "__main__":  # pragma: no cover
    main()
