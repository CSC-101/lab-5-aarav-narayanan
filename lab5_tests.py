import data
import lab5
import unittest

from lab5 import largest_between


# Write your test cases for each part below.

class TestCases(unittest.TestCase):
    # Part 1
    #    Part 1 tests should be in data_tests.py.

    # Part 2
    #    Part 2 tests should be in data_tests.py.


    # Part 3
    def test_time_add(self):
        time1=data.Time(2,4,5)
        time2=data.Time(4,2,0)
        result=lab5.time_add(time1,time2)
        expected=data.Time(6,6,5)
        self.assertEqual(result,expected)
    def test_time_add2(self):
        time1=data.Time(3,50,30)
        time2=data.Time(4,20,30)
        result=lab5.time_add(time1,time2)
        expected=data.Time(8,11,0)
        self.assertEqual(result,expected)

    # Part 4
    def test_is_descending(self):
        list=[6,5,3,4]
        result=lab5.is_descending(list)
        expected=False
        self.assertEqual(result,expected)
    def test_is_descending2(self):
        list=[6,5,4,3]
        result=lab5.is_descending(list)
        expected=True
        self.assertEqual(result,expected)

    # Part 5
    def test_largest_between(self):
        lst=[3,7,2,5,8]
        result=largest_between(lst,0,3)
        expected=1
        self.assertEqual(result, expected)
    def test_largest_between2(self):
        lst=[9,3,6,10,54]
        result=largest_between(lst,1,4)
        expected=4
        self.assertEqual(result, expected)

    # Part 6
    def test_furthest(self):
        points_list=[data.Point(1,4),data.Point(0,2),data.Point(40,9)]
        result=lab5.furthest_from_origin(points_list)
        expected=2
        self.assertEqual(result,expected)
    def test_furthest2(self):
        points_list=[data.Point(4,8),data.Point(7,9),data.Point(0,3)]
        result=lab5.furthest_from_origin(points_list)
        expected=1
        self.assertEqual(result,expected)




if __name__ == '__main__':
    unittest.main()
