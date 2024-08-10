from main import factorial, hand_fact
import pytest
import random

numbers = [random.randint(0, 5) for i in range(5)]
@pytest.mark.parametrize("a, rez",[
                                   (numbers[0],hand_fact(numbers[0])),
                                   (numbers[1],hand_fact(numbers[1])),
                                   (numbers[2],hand_fact(numbers[2])),
                                   (numbers[3],hand_fact(numbers[3])),
                                   (numbers[4],hand_fact(numbers[4]))
                                   ])
def test_func (a,rez):
    assert (factorial(a)) == rez

@pytest.mark.parametrize("a, rez",[('a.s4', 'Please enter an integer'),
                                   ('%^3', 'Please enter an integer'),
                                   ('1,5', 'Please enter an integer'),
                                   (1.55, 'Please enter an integer'),
                                   (1/5, 'Please enter an integer')
                                 ])
def test_integer(a, rez):
    assert (factorial(a)) == rez

@pytest.mark.parametrize("a",[random.randint(-100, -1) for i in range(5)])
def test_under_zero(a):
    assert (factorial(a)) == '500'
