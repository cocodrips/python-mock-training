"""
Pass test
"""
from unittest.mock import patch
from simple_package import hello


@patch('simple_package.hello.return_hello', return_value='mock')
def test_patch_context_manager(p):
    target = hello.return_hello()
    assert target == 'mock'


def test_patch_in_func():
    with patch('simple_package.hello.return_hello', return_value='mock') as p:
        target = hello.return_hello()
        assert target == 'mock'

