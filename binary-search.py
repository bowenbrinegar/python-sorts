import unittest

def binarySearch(arr, low, high, find):
    mid = int(low + (high - low / 2) - 1)
    if arr[mid] == find:
        return mid
    elif arr[mid] > find:
        return binarySearch(arr, low, mid, find)
    elif arr[mid] < find:
        return binarySearch(arr, mid, high, find)


def main(arr, find):
    return binarySearch(arr, 0, len(arr), find)

class tests(unittest.TestCase):
    def test1(self):
        index = main([1,13,14,19,29,40,75,142], 29)
        self.assertEqual(4, index)




unittest.main()