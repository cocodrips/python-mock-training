"""
Pass test
"""
from unittest.mock import patch
import simple_package


@patch('simple_package.hello.return_hello', return_value='mock')
def test_patch_context_manager(p):
    target = simple_package.hello.return_hello()
    assert target == 'mock'


def test_patch_in_func():
    with patch('simple_package.hello.return_hello', return_value='mock') as p:
        target = simple_package.hello.return_hello()
        assert target == 'mock'

