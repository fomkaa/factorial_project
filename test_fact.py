from main import factorial, hand_fact, get_elements, extract_links
import pytest
import random

numbers1 = [random.randint(0, 170) for i in range(3)]

@pytest.mark.parametrize("a, rez",[
                                   (numbers1[0],hand_fact(numbers1[0])),
                                   (numbers1[1],hand_fact(numbers1[1])),
                                   (numbers1[2],hand_fact(numbers1[2])),
                                   (171,'Infinity'),
                                   (588,'Infinity'),
                                   (999,'Infinity')
                                   ])

def test_func (a,rez):
    assert factorial(a) == rez

def test_links():
    a = [('/privacy', 'Privacy'), ('/terms', 'Terms and Conditions')]
    assert extract_links(get_elements('https://qa-test.emcd.io')) == a

@pytest.mark.parametrize("a, rez",[('a.s4', 'Please enter an integer'),
                                   ('%^3', 'Please enter an integer'),
                                   ('1,5', 'Please enter an integer'),
                                   (1.55, 'Please enter an integer'),
                                   (1/5, 'Please enter an integer')
                                 ])
def test_integer(a, rez):
    assert (factorial(a)) == rez

@pytest.mark.parametrize("a",[random.randint(-100, -1) for i in range(2)])
def test_under_zero(a):
    assert (factorial(a)) == 'it is impossible to calculate the factorial of a negative number. Please enter a positive integer'

#link='https://qa-test.emcd.io'

