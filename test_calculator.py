
import pytest
from calculator import divide, calculate_average, multiply


def test_divide():
    assert divide(10, 2) == 5
    assert divide(9, 3) == 3


def test_divide_by_zero():
    with pytest.raises(ValueError):
        divide(10, 0)


def test_average():
    assert calculate_average([2, 4, 6]) == 4
    assert calculate_average([10, 20]) == 15


def test_average_empty():
    with pytest.raises(ValueError):
        calculate_average([])


def test_multiply():
    assert multiply(3, 4) == 12
    assert multiply(5, 0) == 0

def test_main(capsys):
    from calculator import main

    main()
    captured = capsys.readouterr()

    assert "Average:" in captured.out
    assert "Division:" in captured.out
    assert "Multiplication:" in captured.out
