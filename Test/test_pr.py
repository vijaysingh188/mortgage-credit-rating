# import pytest
        
# @pytest.mark.parametrize("num","execpted",[(2,4),(4,16),(9,81)])
# def test_square(num,execpted):
#     assert num**2 == execpted


# import pytest


# @pytest.mark.parametrize("num, expected", [(2, 4), (4, 16), (9, 81)])
# def test_square(num, expected):
#     assert num ** 2 == expected


# def add_func(x,y):
#     return x+y


# def test_add():
#     assert  (2,2)==4


import pytest


class Database:
    def connect(self):
        return "connenction successful"
    def close(self):
        return "connection closed"


@pytest.fixture
def db_connection():
    db = Database()
    yield db

def test_check(db_connection):
    assert db_connection.connect() == "connenction successful"

