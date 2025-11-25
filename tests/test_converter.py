from mini_converter import *

def test_length():
    assert round(cm_to_inch(2.54), 2) == 1.00
    assert round(inch_to_cm(1), 2) == 2.54

def test_weight():
    assert round(kg_to_lb(1), 2) == 2.2
    assert round(lb_to_kg(2.2), 1) == 1.0

def test_temperature():
    assert c_to_f(0) == 32
    assert round(f_to_c(32), 1) == 0.0

def test_volume():
    assert round(liter_to_gallon(1), 2) == 0.26
    assert round(gallon_to_liter(1), 2) == 3.79
