import platform
import sys


def test_python_version():
    assert sys.version_info >= (3, 12)


def test_apple_silicon():
    assert platform.machine() == "arm64"
