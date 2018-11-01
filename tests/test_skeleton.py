#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pytest
from scraping_constantino.skeleton import fib

__author__ = "Andrea Titton"
__copyright__ = "Andrea Titton"
__license__ = "mit"


def test_fib():
    assert fib(1) == 1
    assert fib(2) == 1
    assert fib(7) == 13
    with pytest.raises(AssertionError):
        fib(-10)
