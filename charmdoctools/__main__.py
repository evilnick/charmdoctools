import click  # pragma: no cover
import pkgutil  # pragma: no cover
from . import BaseClass, base_function  # pragma: no cover

v = pkgutil.get_data(__name__, "VERSION")
__version__ = str(v, "utf-8").strip()  # type: ignore


@click.command()
@click.pass_context()
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
