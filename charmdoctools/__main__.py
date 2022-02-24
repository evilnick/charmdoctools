import click  # pragma: no cover
import pkgutil  # pragma: no cover
from . import BaseClass, base_function  # pragma: no cover

v = pkgutil.get_data(__name__, "VERSION")
__version__ = str(v, "utf-8").strip()  # type: ignore

@click.group()
@click.pass_context
def main(ctx) -> None:
    """charmdoctools is a collection of utilities for working with documentation, 
    managed and maintained by Canonical's technical authors."""

    ctx.ensure_object(dict)
    #ctx.verbose = verbose
    click.echo("Hello World!")
    click.echo("Version is {}".format(__version__))
    


@main.command()
@click.pass_context
def version(ctx) -> None:
    """Returns the current version."""
    click.echo(click.style(f"{__version__}", bold=True))


if __name__ == "__main__":  # pragma: no cover
    main(obj={})
