from utils import identify_and_split


def test_identify_and_split_equals():
    expected = ({"module_name": "pandas", "version": "1.3.0"}, "equals")
    assert identify_and_split("pandas==1.3.0") == expected


def test_identify_and_split_greather_than():
    expected = ({"module_name": "redis", "version": "3.5.2"}, "greater_than")
    assert identify_and_split("redis>=3.5.2") == expected


def test_identify_and_split_standard():
    expected = ({"module_name": "uvicorn", "version": None}, "latest")
    assert identify_and_split("uvicorn[standard]") == expected


def test_identify_and_split_latest():
    expected = ({"module_name": "numpy", "version": None}, "latest")
    assert identify_and_split("numpy") == expected
