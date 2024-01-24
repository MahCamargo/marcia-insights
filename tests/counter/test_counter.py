from src.pre_built.counter import count_ocurrences


def test_counter():
    result = count_ocurrences('data/jobs.csv', 'Python')
    assert result == count_ocurrences('data/jobs.csv', 'Python')
    assert result == count_ocurrences('data/jobs.csv', 'PYTHON')
    assert result == count_ocurrences('data/jobs.csv', 'python')
    assert result == count_ocurrences('data/jobs.csv', 'Python')

