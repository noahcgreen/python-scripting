import shlex
import subprocess
import tempfile

import pytest

import scripting


@pytest.fixture
def temp_script():
    file = tempfile.NamedTemporaryFile(mode='w', suffix='.py')
    file.write("""
    print('foo')
    import scripting
    
    @scripting.main
    def succeed():
        return 200
    """)
    return file


@pytest.fixture
def process(temp_script):
    args = shlex.split(f'python {temp_script.name}')
    return subprocess.run(args, stdout=subprocess.PIPE, stderr=subprocess.PIPE, encoding='utf-8')


class TestMainDecorator:

    def test_(self, process):
        assert 0
