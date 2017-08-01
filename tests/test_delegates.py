import pathlib
import sys

import pytest

from scripting import delegates, execution


class TestLogger:

    def test_logs_file_name(self, caplog):
        delegate = delegates.Logger()
        executor = execution.Executor(delegate=delegate)
        script = execution.Script(pathlib.Path('script.py'), lambda: 200)

        executor.execute(script)
        assert script.file.name in caplog.text

    def test_logs_result(self, caplog):
        delegate = delegates.Logger()
        executor = execution.Executor(delegate=delegate)
        script = execution.Script(pathlib.Path('script.py'), lambda: 200)

        executor.execute(script)
        assert str(200) in caplog.text

    def test_logs_exception_info(self, caplog):
        delegate = delegates.Logger()
        executor = execution.Executor(delegate=delegate)
        script = execution.Script(pathlib.Path('script.py'), lambda: 1 / 0)

        executor.execute(script)
        assert ZeroDivisionError.__name__ in caplog.text


class _RepeatingTerminalController(delegates.TerminalController):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.repeated = False

    def _offer_reentry(self):
        if not self.repeated:
            self.repeated = True
            return True
        else:
            return False


class TestTerminalController:

    def test_reentry(self, capsys):
        delegate = _RepeatingTerminalController()
        executor = execution.Executor(delegate=delegate)
        script = execution.Script(pathlib.Path('script.py'), lambda: sys.stdout.write('result'))

        executor.execute(script)

        output, error = capsys.readouterr()

        assert output.count('result') == 2
        # FIXME: pytest behaves weirdly and leaks stdout if this test fails
