import os
from file_types import file_format_base
from database import database
from typing import Dict, Type
import importlib
import inspect
from file_types import file_format_manager

found_formats: Dict[str, Type[file_format_base.file_format]] = {}
used_formats = []

def main():
    print("------- Basic Database API -------")

    discover_formats()
    loadFile()

def discover_formats():
    formats = file_format_manager.find_available_formats()

    for format in formats:
        try:
            format_module = importlib.import_module(format)
        except:
            print(
                f'Error importing {format} {importlib.import_module(format)}')
            continue

        members = inspect.getmembers(format_module, inspect.isclass)

        for (name, c) in members:
            if issubclass(c, file_format_base.file_format) and (c is not file_format_base.file_format):
                if name.endswith("_format"):
                    name = name.split("_")[0]
                found_formats[name] = c


def loadFile():
    while True:
        #Recieve input for desired path
        filepath = input('Please enter desired database file for reading: ')

        if not os.path.exists(filepath):
            print("ERROR: File not found. Please try again")
            loadFile()

        file_extension = filepath.split(".")[-1]

        format_class = None

        for format in found_formats:
            if file_extension in format:
                format_module = found_formats.get(format)

                format_class = format_module()
                used_formats.append(format_class)
                run(filepath)

        if format_class is None:
            print("No format found. Please try a file with the following extension:")
            for format in found_formats:
                print(f"{found_formats.get(format)}")

def run(filepath):
    file = open(filepath, "r")
    active_database = database(file, used_formats[0])
    try:
        used_formats[0].print_data(active_database.get_entries())
    except Exception as e:
        print(f"Error trying to print using format {used_formats[0]}: {e}")

    #Execute command interface on loop
    while True:
        command = input("\nWhat would you like to do? (Help for options): ")

        if command.lower() == 'help':
            command_help()

        if command.lower() == 'display':
            command_display(active_database)    

        if command.lower() == 'add':
            command_add(active_database)

        if command.lower() == 'filter':
            command_filter(active_database)

        if command.lower() == 'export':
            command_export(active_database)

        if command.lower() == 'format':
            command_format()
                        
#Prints the list of available formats and command options 
def command_help():
    print('Available formats:\n ')
    for format in found_formats:
        print(format)
    print('\n===Commands===')
    print('Display == Change the current display format (Current options are Text and JSON\n)')
    print('Add == Add an entry to the current database\n')
    print('Filter == Search the database for entries containing specific data\n')
    print('Export == Export the database to a specified format and directory (Current options are CSV and JSON\n)')
    print('Format == Change the format for displaying and exporting data\n')

#Prints the database to the console using the current format
def command_display(database):
    try:
        used_formats[0].print_data(database.get_entries())
    except:
        print(f"Error trying to print using format {used_formats[0]}")

#Adds an entry to the database and prints the result
def command_add(database):
    name = input("Name: ")
    address = input("Address: ")
    number = input("Number: ")
    database.add_entry(name, address, number)
    used_formats[0].print_data(database.entries)

#Filtes the database using a category and key and displays the results
def command_filter(database):
    category = input('Category (Name, Address, Number): ')
    search = input('Search Key: ')
    data = database.filter(category, search)
    used_formats[0].print_data(data)

#Exports the database using the current format
def command_export(database):
    desired_directory = input('File directory: ')
    if not os.path.exists(desired_directory):
        print('ERROR: Cant find specified Directory')
    file_name = input('File Name: ')
    file_path = desired_directory + "\\" + \
        file_name + used_formats[0].extension
    if os.path.exists(file_path):
        overwrite_prompt = input(
            'File already exists. Do you wish to overwrite? (Y/N): ')
        if overwrite_prompt.lower() == 'y':
            try:
                used_formats[0].export_file(
                    database.get_entries(), file_path)
            except:
                print(
                    f"Error trying to export using format {used_formats[0]}")
    else:
        try:
            used_formats[0].export_file(
                database.get_entries(), file_path)
        except:
            print(
                f"Error trying to export using format {used_formats[0]}")

#Changes the format currently being used for displaying and exporting data
def command_format():
    print("Avaialble Formats: ")
    for format in found_formats:
        print(format)
    new_format = input("Please choose format: ")
    format_changed = False
    for format in found_formats:
        if new_format in format:
            format_module = found_formats.get(format)
            format_class = format_module()
            used_formats[0] = (format_class)
            format_changed = True

    if not format_changed:
        print("Format not changed. Please select one of the available formats format")

if __name__ == "__main__":
    main()