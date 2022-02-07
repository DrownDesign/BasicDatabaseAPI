import argparse
import os
import sys
from database import database

def main():
    print("------- Basic Database API -------")

    loadFile()

def loadFile():
    while True:
        #Recieve input for desired path
        filepath = input('Please enter desired database file for reading: ')

        if not os.path.exists(filepath):
            print("ERROR: File not found. Please try again")
            loadFile()
        
        file = open(filepath, "r")
        active_database = database(file)
        active_database.display_database(active_database.entries)

        while True:
            command = input("\nWhat would you like to do? (Help for options): ")

            if command.lower() == 'help':
                #Print options and what they do
                print('\nDisplay == Change the current display format (Current options are Text and JSON\n)')
                print('Add == Add an entry to the current database\n')
                print('Filter == Search the database for entries containing specific data\n')
                print('Export == Export the database to a specified format and directory (Current options are CSV and JSON\n)')
            if command.lower() == 'display':
                new_format = input("New format (Text, JSON): ")
                if new_format.lower() != 'text' and new_format.lower() != 'json':
                    print('Format specified not supported. Please specify CSV or JSON.')
                else:
                    active_database.display_format = new_format
                active_database.display_database(active_database.entries)
            if command.lower() == 'add':
                name = input("Name: ")
                address = input("Address: ")
                number = input("Number: ")
                active_database.add_entry(name, address, number)
                active_database.display_database(active_database.entries)
            if command.lower() == 'filter':
                category = input('Category (Name, Address, Number): ')
                search = input('Search Key: ')
                data = active_database.filter(category, search)
                active_database.display_database(data)
            if command.lower() == 'export':
                chosen_format = input("Format (CSV, JSON): ")
                desired_directory = input('File directory: ')
                if not os.path.exists(desired_directory):
                    print('ERROR: Cant find specified Directory')
                file_name = input('File Name: ')
                file_path = desired_directory + "\\" + file_name + "." + chosen_format.lower()
                if os.path.exists(file_path):
                    overwrite_prompt = input('File already exists. Do you wish to overwrite? (Y/N): ')
                    if overwrite_prompt.lower() == 'y':
                        active_database.export(chosen_format, file_path)
                else: 
                    active_database.export(chosen_format, file_path)
         
        

if __name__ == "__main__":
    main()