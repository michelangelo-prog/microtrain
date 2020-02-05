import subprocess

from flask.cli import FlaskGroup

from train.app.rest import create_app

cli = FlaskGroup(create_app=create_app)


@cli.command()
def test_pytest_with_plugins():
    """Runs pytest with plugins on the train."""
    subprocess.run(["pytest", "--ignore=migrations", "--black", "--isort", "--flakes"])


@cli.command()
def test_pytest():
    """Runs pytest on the train."""
    subprocess.run(["pytest"])


if __name__ == "__main__":
    cli()
