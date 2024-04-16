#Test case with an assertion and entry point. When ran in terminal from directory receive
#successful result "Everything passed"
def test_sum():
    assert sum([1, 2, 3]) == 6, "Should be 6"

if __name__ == "__main__":
    test_sum()
    print("Everything passed")