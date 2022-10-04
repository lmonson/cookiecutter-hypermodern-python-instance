"""Command-line interface."""
import click


@click.command()
@click.version_option()
def main() -> None:
    """Hypermodern_Python_Template."""


if __name__ == "__main__":
    main(prog_name="hypermodern_python_template")  # pragma: no cover
