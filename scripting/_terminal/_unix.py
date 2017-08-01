import contextlib
import os
import termios
import tty

from . import _escapes


_MAX_CHARACTER_BYTE_LENGTH = 4


@contextlib.contextmanager
def _tty_reset(file_descriptor):
    """
    A context manager that saves the tty flags of a file descriptor upon
    entering and restores them upon exiting.
    """
    old_settings = termios.tcgetattr(file_descriptor)
    try:
        yield
    finally:
        termios.tcsetattr(file_descriptor, termios.TCSADRAIN, old_settings)


def get_character(stream):
    """
    Read a single character from the given input stream (defaults to sys.stdin).
    """
    file_descriptor = stream.fileno()
    with _tty_reset(file_descriptor):
        tty.setcbreak(file_descriptor)
        return os.read(file_descriptor, _MAX_CHARACTER_BYTE_LENGTH)


def clear(stream):
    stream.write(_escapes.CLEAR_SCREEN_ESCAPE_SEQUENCE + _escapes.RESET_CURSOR_ESCAPE_SEQUENCE)
