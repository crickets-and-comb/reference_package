"""This is an example module."""

import time

from typeguard import typechecked

from reference_package.lib.constants import DocStrings


@typechecked
def wait_a_second(  # noqa: D103
    seconds: int = DocStrings.EXAMPLE_INTERNAL.defaults["seconds"],
    extra_string: str = DocStrings.EXAMPLE_INTERNAL.defaults["extra_string"],
) -> None:
    print(f"Waiting {seconds} seconds.{' ' + extra_string if extra_string else ''}")
    time.sleep(seconds)


wait_a_second.__doc__ = DocStrings.EXAMPLE_INTERNAL.api_docstring
