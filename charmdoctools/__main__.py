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
    #click.echo("Hello World!")
    #click.echo("Version is {}".format(__version__))
    


@main.command()
@click.pass_context
def version(ctx) -> None:
    """Returns the current version."""
    click.echo(click.style(f"{__version__}", bold=True))


@main.command()
@click.pass_context
@click.option('--quiet', type = click.BOOL, help="Do not return a diff if the files don't match, just an error")
@click.argument('base', nargs=1)
@click.argument('comparison', nargs=1)
def diff(ctx,base,comparison,quiet) -> None:
    """Returns either 0 or the diff between supplied files or urls
    
    BASE is the first file (or url e.g. to a discourse topic).\n
    COMPARISON is the text to compare to the base (from a file or url).\n
    
    Note that in the case of urls, it is recommended to use the full resource uri,
    for example:\n
            https://discourse.ubuntu.com/t/some_text/6319/
    
     """
    exit(0)
if __name__ == "__main__":  # pragma: no cover
    main(obj={})
