"""Unit tests for the example CLI."""

import pytest
from click.testing import CliRunner

import reference_package
from reference_package.cli import example


@pytest.mark.parametrize("args, expected_seconds", [([], 1), (["--seconds", "0"], 0)])
def test_cli_calls_public_api(
    cli_runner: CliRunner,
    monkeypatch: pytest.MonkeyPatch,
    args: list[str],
    expected_seconds: int,
) -> None:
    """Test that the CLI delegates to the public API, like the docs say to.

    The CLI is a consumer of the package, so it should go through the public API rather than
    reaching into `lib` and skipping whatever the API layers do.
    """
    calls: list[dict] = []
    monkeypatch.setattr(example, "wait_a_second", lambda **kwargs: calls.append(kwargs))

    result = cli_runner.invoke(example.main, args)

    assert result.exit_code == 0, result.output
    assert calls == [{"seconds": expected_seconds}]


def test_cli_uses_public_function() -> None:
    """Test that the function the CLI calls is the public API, not a lib or internal one."""
    assert example.wait_a_second is reference_package.wait_a_second


def test_cli_rejects_non_int_seconds(cli_runner: CliRunner) -> None:
    """Test that the CLI rejects a non-integer `--seconds`."""
    result = cli_runner.invoke(example.main, ["--seconds", "one"])

    assert result.exit_code == 2
    assert "--seconds" in result.output
