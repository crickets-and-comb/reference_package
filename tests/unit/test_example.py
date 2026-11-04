"""This is just an example test."""

import time

import pytest
from click.testing import CliRunner

from reference_package import wait_a_second
from reference_package.api import internal
from reference_package.cli import example
from reference_package.lib import example as lib_example


def test_example(cli_runner: CliRunner) -> None:
    """Test that we wait at least as long as we expect to wait, using CLI."""
    start_time = time.time()
    result = cli_runner.invoke(example.main)
    end_time = time.time()
    assert result.exit_code == 0, result.output
    assert end_time - start_time >= 1


def test_public_wraps_internal(monkeypatch: pytest.MonkeyPatch) -> None:
    """Test that the public API delegates to the internal API, not straight to lib."""
    calls: list[dict] = []
    monkeypatch.setattr(internal, "wait_a_second", lambda **kwargs: calls.append(kwargs))

    wait_a_second(seconds=0)

    assert calls == [{"seconds": 0}]


def test_internal_wraps_lib(monkeypatch: pytest.MonkeyPatch) -> None:
    """Test that the internal API normalizes `extra_string` before calling lib."""
    calls: list[dict] = []
    monkeypatch.setattr(lib_example, "wait_a_second", lambda **kwargs: calls.append(kwargs))

    internal.wait_a_second(seconds=0, extra_string="  hello ")

    assert calls == [{"seconds": 0, "extra_string": "HELLO"}]
