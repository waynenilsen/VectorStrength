
import unittest
import database

class TestDatabase(unittest.TestCase):

    def setUp(self):
        pass

    def test_insert(self):
        database.add_record({
            'x' : 5,
            'y' : 5,
            'z' : 5,
            'alpha' : 5,
            'beta' : 5,
            'gamma' : 5,
            'utc_set_start_time' : 5,
            'utc_measure_time' : 5,
            'fk_activity' : -999,
        })


if __name__ == '__main__':
    unittest.main()
