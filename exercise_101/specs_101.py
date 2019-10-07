from exercise_101 import *

def test_hello_human1():
    assert hello_human('Jefferson') == 'Hello Jefferson, you are a humman'

def test_hello_human2():
    assert hello_human('Joana') == 'Hello Joana, you are a humman'

def test_area_square():
    assert area_square(10) == 100

def test_area_square1():
    assert area_square(13) == 169

def test_area_triangle():
    assert area_triangle(10, 10) == 50

def test_area_triangle2():
    assert area_triangle(10, 13) == 65

def test_area_of_circle():
    assert area_of_circle(5) == 78.54