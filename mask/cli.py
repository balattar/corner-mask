import click


@click.command
@click.argument(
    "path",
    # help="Path to image file"
)
def cli():
    """
    Mask a square region of the image according
    to an RGB value of any other point in the image.

    PATH: the file path of the image.

    """
    pass
