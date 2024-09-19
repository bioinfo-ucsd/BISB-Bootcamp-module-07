from bootcamp.core.student_08 import count_substring  # noqa


def test_count_substring_single():
    test_string = "CGCTAGCGT"
    test_substring = "TAG"

    expected_count = 1
    observed_count = count_substring(test_string, test_substring)
    assert expected_count == observed_count


def test_count_substring_repeated():
    test_string = "AGCTAGCAGT"
    test_substring = "AGC"

    expected_count = 2
    observed_count = count_substring(test_string, test_substring)
    assert expected_count == observed_count


def test_count_substring_none():
    test_string = "AGTCCCCTAGA"
    test_substring = "AAA"

    expected_count = 0
    observed_count = count_substring(test_string, test_substring)
    assert expected_count == observed_count

# test whether the existing `count_substring()` code is case insensitive.
def test_count_substring_case_insensitive():
    test_string = "AGTCCCCTAGA"
    test_substring = "aaa"

    expected_count = 0
    observed_count = count_substring(test_string, test_substring)
    assert expected_count == observed_count
