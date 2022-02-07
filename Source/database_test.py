from database import database, entry
import unittest
import os

class Test_TestDatabase(unittest.TestCase):

    def test_add_entry(self):
        f = open(f"{os.getcwd()}\\Tests\\blankTest.csv", "r")
        active_database = database(f)
        active_database.add_entry("Red", "12 Test St", "12122542")
        for current_entry in active_database.entries:
            print(current_entry.name)
            if current_entry.name == 'Red' and current_entry.address == '12 Test St' and current_entry.number == '12122542':
                assert(True)
                return
        assert(False)

    def test_create_JSON(self):
        if(os.path.exists(f"{os.getcwd()}\\Tests\\JSONTest.json")):
            os.remove(f"{os.getcwd()}\\Tests\\JSONTest.json")
        f = open(f"{os.getcwd()}\\Tests\\GeneratedMaterial.csv", "r")
        active_database = database(f)
        active_database.export("json", f"{os.getcwd()}\\Tests\\JSONTest.json")
        assert(os.path.exists(f"{os.getcwd()}\\Tests\\JSONTest.json"))

    def test_create_CSV(self):
        if(os.path.exists(f"{os.getcwd()}\\Tests\\CSVTest.csv")):
            os.remove(f"{os.getcwd()}\\Tests\\CSVTest.csv")
        f = open(f"{os.getcwd()}\\Tests\\GeneratedMaterial.csv", "r")
        active_database = database(f)
        active_database.export("csv", f"{os.getcwd()}\\Tests\\CSVTest.csv")
        assert(os.path.exists(f"{os.getcwd()}\\Tests\\CSVTest.csv"))

    def test_filter_name(self):
        f = open(f"{os.getcwd()}\\Tests\\GeneratedMaterial.csv", "r")
        active_database = database(f)
        data = active_database.filter("name", "frank")
        assert(len(data) == 2)

    def test_filter_address(self):
        f = open(f"{os.getcwd()}\\Tests\\GeneratedMaterial.csv", "r")
        active_database = database(f)
        data = active_database.filter("address", "/")
        assert(len(data)==2)


    def test_filter_number(self):
        f = open(f"{os.getcwd()}\\Tests\\GeneratedMaterial.csv", "r")
        active_database = database(f)
        data = active_database.filter("number", "5661836518")
        assert(len(data) == 1)


    def test_filter_no_category(self):
        f = open(f"{os.getcwd()}\\Tests\\GeneratedMaterial.csv", "r")
        active_database = database(f)
        data = active_database.filter("age", "12")
        assert(len(data) == 0)

    def test_filter_wrong_category(self):
        f = open(f"{os.getcwd()}\\Tests\\GeneratedMaterial.csv", "r")
        active_database = database(f)
        data = active_database.filter("name", "12")
        assert(len(data) == 0)

if __name__ == '__main__':
    unittest.main()