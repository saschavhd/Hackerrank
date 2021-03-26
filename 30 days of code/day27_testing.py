import random

def minimum_index(seq):
    if len(seq) == 0:
        raise ValueError("Cannot get the minimum value index from an empty sequence")
    min_idx = 0
    for i in range(1, len(seq)):
        if seq[i] < seq[min_idx]:
            min_idx = i
    return min_idx

# ---------

unique_vals = []
exactly_two_mins = []

class TestDataEmptyArray(object):

    @staticmethod
    def get_array():
        return []

class TestDataUniqueValues(object):

    @staticmethod
    def get_array():
        global unique_vals
        diff = random.randint(3, 20)
        end = random.randint(100, 10000)
        arr = []
        for i in range(0, end, diff):
            arr.append(i)
        random.shuffle(arr)
        unique_vals = arr
        return arr

    @staticmethod
    def get_expected_result():
        return minimum_index(unique_vals)

class TestDataExactlyTwoDifferentMinimums(object):

    @staticmethod
    def get_array():
        global exactly_two_mins
        min = random.randint(1, 10)
        diff = random.randint(3, 20)
        end = random.randint(100, 10000)
        arr = []
        arr.append(min)
        arr.append(min)
        for i in range(min + diff, end, diff):
            arr.append(i)
        random.shuffle(arr)
        exactly_two_mins = arr
        return arr

    @staticmethod
    def get_expected_result():
        return minimum_index(exactly_two_mins)

# ----------

def TestWithEmptyArray():
    try:
        seq = TestDataEmptyArray.get_array()
        result = minimum_index(seq)
    except ValueError as e:
        pass
    else:
        assert False


def TestWithUniqueValues():
    seq = TestDataUniqueValues.get_array()
    assert len(seq) >= 2

    assert len(list(set(seq))) == len(seq)

    expected_result = TestDataUniqueValues.get_expected_result()
    result = minimum_index(seq)
    assert result == expected_result


def TestiWithExactyTwoDifferentMinimums():
    seq = TestDataExactlyTwoDifferentMinimums.get_array()
    assert len(seq) >= 2
    tmp = sorted(seq)
    assert tmp[0] == tmp[1] and (len(tmp) == 2 or tmp[1] < tmp[2])

    expected_result = TestDataExactlyTwoDifferentMinimums.get_expected_result()
    result = minimum_index(seq)
    assert result == expected_result

TestWithEmptyArray()
TestWithUniqueValues()
TestiWithExactyTwoDifferentMinimums()
print("OK")
