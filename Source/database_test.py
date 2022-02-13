import unittest
import os
from file_types.csv import csv_format
from file_types.json import json_format
from database import database

class Test_TestDatabase(unittest.TestCase):

    def test_create_database_csv(self):
        file = open(f"{os.getcwd()}\\Tests\\GeneratedMaterial.csv", "r")
        format = csv_format.csv_format()
        active_database = database(file, format)
        assert(len(active_database.get_entries()) > 0)

    def test_create_database_json(self):
        file = open(f"{os.getcwd()}\\Tests\\JSONTest.json", "r")
        format = json_format.json_format()
        active_database = database(file, format)
        assert(len(active_database.get_entries()) > 0)

    def test_add_entry(self):
        file = open(f"{os.getcwd()}\\Tests\\GeneratedMaterial.csv", "r")
        format = csv_format.csv_format()
        active_database = database(file, format)
        active_database.add_entry("Red", "12 Test St", "12122542")
        for current_entry in active_database.entries:
            print(current_entry.name)
            if current_entry.name == 'Red' and current_entry.address == '12 Test St' and current_entry.number == '12122542':
                assert(True)
                return
        assert(False)

    def test_export_csv(self):
        if(os.path.exists(f"{os.getcwd()}\\Tests\\CSVTest.csv")):
            os.remove(f"{os.getcwd()}\\Tests\\CSVTest.csv")
        f = open(f"{os.getcwd()}\\Tests\\GeneratedMaterial.csv", "r")
        format = csv_format.csv_format()
        active_database = database(f, format)
        format.export_file(active_database.get_entries(),
                           f"{os.getcwd()}\\Tests\\CSVTest.csv")
        assert(os.path.exists(f"{os.getcwd()}\\Tests\\CSVTest.csv"))

    def test_export_json(self):
        if(os.path.exists(f"{os.getcwd()}\\Tests\\JSONTest.json")):
            os.remove(f"{os.getcwd()}\\Tests\\JSONTest.json")
        f = open(f"{os.getcwd()}\\Tests\\GeneratedMaterial.json", "r")
        format = csv_format.csv_format()
        active_database = database(f, format)
        format.export_file(active_database.get_entries(),
                           f"{os.getcwd()}\\Tests\\JSONTest.json")
        assert(os.path.exists(f"{os.getcwd()}\\Tests\\JSONTest.json"))

    def test_filter_name(self):
        f = open(f"{os.getcwd()}\\Tests\\GeneratedMaterial.csv", "r")
        format = csv_format.csv_format()
        active_database = database(f, format)
        data = active_database.filter("name", "frank")
        assert(len(data) == 2)

    def test_filter_address(self):
        f = open(f"{os.getcwd()}\\Tests\\GeneratedMaterial.csv", "r")
        format = csv_format.csv_format()
        active_database = database(f, format)
        data = active_database.filter("address", "/")
        assert(len(data)==2)


    def test_filter_number(self):
        f = open(f"{os.getcwd()}\\Tests\\GeneratedMaterial.csv", "r")
        format = csv_format.csv_format()
        active_database = database(f, format)
        data = active_database.filter("number", "5661836518")
        assert(len(data) == 1)

    def test_filter_no_category(self):
        f = open(f"{os.getcwd()}\\Tests\\GeneratedMaterial.csv", "r")
        format = csv_format.csv_format()
        active_database = database(f, format)
        data = active_database.filter("age", "12")
        assert(len(data) == 0)

    def test_filter_wrong_category(self):
        f = open(f"{os.getcwd()}\\Tests\\GeneratedMaterial.csv", "r")
        format = csv_format.csv_format()
        active_database = database(f, format)
        data = active_database.filter("name", "12")
        assert(len(data) == 0)

if __name__ == '__main__':
    unittest.main()