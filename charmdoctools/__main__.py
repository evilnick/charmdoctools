import click  # pragma: no cover
from . import BaseClass, base_function  # pragma: no cover
import pkgutil
__version__= str(pkgutil.get_data(__name__, "VERSION").decode("utf-8")).strip()

@click.command()
def main() -> None:
    """Example script."""
    click.echo("Hello World!")
    click.echo("Version is {}".format(__version__))
    click.echo("Executing main function")
    base = BaseClass()
    click.echo(base.base_method())
    click.echo(base_function())
    click.echo("End of main function")


if __name__ == "__main__":  # pragma: no cover
    main()
