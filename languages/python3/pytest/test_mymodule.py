#!/usr/bin/env python
# coding: utf-8

import pytest

from mymodule import MyModule
import requests_mock


@pytest.fixture()
def mm():
    """
    This function allow to make traitement BEFORE and AFTER each test 
    (i.e. each function test_*)
    """
    # Call BEFORE each test
    mm = MyModule()
 
    yield mm # Return for the next test (generator mode)
 
    # Call AFTER each test
    pass


# = Function test automaticaly discover by pytest(test_*)
def test_format_message(mm):
    """Test of format message function"""
    message = "toto"
    result = mm.format_message(message)
    assert result == message+"_format"


def test_url_code_without_internet_access(mm):
    """Test url request"""
    ## Mock the request package to allow this test without internet connection
    with requests_mock.Mocker() as m: 
        m.get('http://www.example.comdfgfdd/', text='data')

        result = mm.get_url_code()
        assert result == 200
