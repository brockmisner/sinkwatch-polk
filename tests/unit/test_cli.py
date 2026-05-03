from typer.testing import CliRunner

from sinkwatch.cli import app


def test_cli_root_help() -> None:
    runner = CliRunner()
    result = runner.invoke(app, ["--help"])
    assert result.exit_code == 0
    assert "SinkWatch" in result.stdout
