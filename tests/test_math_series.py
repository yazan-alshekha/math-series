from math_series import __version__
from math_series.series import fibonacci,lucas,sum_series

def test_version():
    assert __version__ == '0.1.0'


def test_fibonacci():
    expected=13
    actual=fibonacci(7)
    assert actual==expected

def test_lucas ():
    expected=29
    actual=lucas(7)
    assert actual==expected

def test_sum_series():
    expected=7
    actual=sum_series(4,2,1)
    assert actual==expected

def test2_sum_series():
    expected=1
    actual=sum_series(2,0,1)
    assert actual==expected

def test3_sum_series():
    expected=13
    actual=sum_series(4,2,3)
    assert actual==expected

