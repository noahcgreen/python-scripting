import functools
import pathlib

import pytest

from scripting import execution


def _raise(exception):
    raise exception


_Script = functools.partial(execution.Script, pathlib.Path('script.py'))


class TestExecutor:

    def test_execution_captures_exceptions(self):
        script = _Script(lambda: 1 / 0)
        executor = execution.Executor()

        executor.execute(script)

    def test_execution_does_not_capture_base_exceptions(self):
        script = _Script(lambda: _raise(KeyboardInterrupt))
        executor = execution.Executor()

        with pytest.raises(KeyboardInterrupt):
            executor.execute(script)
