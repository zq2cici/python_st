# -*- coding: utf-8 -*-
"""
Created on Sat Sep  2 09:16:48 2017

@author: pc-541
"""
from nose.tools import *
import NAME

def setup():
    print( "SETUP!")

def teardown():
    print( "TEAR DOWN!")

def test_basic():
    print( "I RAN!")
