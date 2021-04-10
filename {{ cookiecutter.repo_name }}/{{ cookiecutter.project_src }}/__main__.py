import typer

app = typer.Typer(
    name='{{ cookiecutter.project_src }}',
    add_completion=False,
    help='{{ cookiecutter.description }}'
)


if __name__ == '__main__':
    app()
