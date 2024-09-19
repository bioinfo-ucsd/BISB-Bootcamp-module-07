from bootcamp.core.student_01 import count_substring  # noqa


def test_count_substring_single():
    test_string = "CGCTAGCGT"
    test_substring = "TAG"

    expected_count = 1
    observed_count = count_substring(test_string, test_substring)
    print("expect_count:", expected_count, "observed_count:", observed_count)
    assert expected_count == observed_count


def test_count_substring_repeated():
    test_string = "AGCTAGCAGT"
    test_substring = "AGC"

    expected_count = 2
    observed_count = count_substring(test_string, test_substring)
    print("expect_count:", expected_count, "observed_count:", observed_count)
    assert expected_count == observed_count


def test_count_substring_none():
    test_string = "AGTCCCCTAGA"
    test_substring = "AAA"

    expected_count = 0
    observed_count = count_substring(test_string, test_substring)
    print("expect_count:", expected_count, "observed_count:", observed_count)
    assert expected_count == observed_count
    

print(test_count_substring_single(), test_count_substring_repeated(), test_count_substring_none())
