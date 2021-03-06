# -*- coding: utf-8 -*-
"""
Created on Sat Sep  2 09:16:48 2017

@author: pc-541
"""
from nose.tools import *
from game.eg48 import lexicon

#每个测试函数运行前运行
def setup():
    print( "SETUP!")
	
#每个测试函数运行完后执行
def teardown():
    print( "TEAR DOWN!")

def test_basic():
    print( "I RAN!")
    
def test_direction():
    assert_equal(lexicon.scan("north"),[('direction','north')])    
    result = lexicon.scan("north south east")
    assert_equal(result,[('direction','north'),
                         ('direction','south'),
                         ('direction','east')])
    
def test_verbs():
    assert_equal(lexicon.scan("go"),[('verb','go')])
    result = lexicon.scan("go kill eat")
    assert_equal(result,[('verb','go'),
                         ('verb','kill'),
                         ('verb','eat')])

def test_stops():
    assert_equal(lexicon.scan("the"),[('stop','the')])
    result = lexicon.scan("the in of")
    assert_equal(result,[('stop','the'),
                         ('stop','in'),
                         ('stop','of')])
    
def test_nouns():
    assert_equal(lexicon.scan("bear"),[('noun','bear')])
    result = lexicon.scan("bear princess")
    assert_equal(result,[('noun','bear'),
                         ('noun','princess')])
 
def test_numbers():
    assert_equal(lexicon.scan("1234"), [('number', 1234)])
    result = lexicon.scan("3 91234")
    assert_equal(result, [('number', 3),
                          ('number', 91234)])

def test_errors():
    assert_equal(lexicon.scan('ASDFADFASDF'), [('error','ASDFADFASDF')])
    result = lexicon.scan("bear IAS princess")
    assert_equal(result, [('noun', 'bear'),
                          ('error', 'IAS'),
                          ('noun', 'princess')]) 
    
    
    
    
    