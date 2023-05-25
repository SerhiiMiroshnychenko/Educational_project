import pytest

@pytest.fixture
def open_file():
    with open('some_file.txt', 'w') as f:
        f.write('Python')
    return open('some_file.txt', 'r')

def test_file_length_count(open_file):
    text = open_file.read()
    open_file.close()
    assert len(text) == 6
