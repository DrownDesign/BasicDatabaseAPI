# BasicDatabaseAPI
## System Overview
This basic database API allows users to take a set of personal data in either CSV or JSON format, with each element containing a name, address, and phone number, and run certain tasks. Currently, a user can display the information in text and JSON formatting, filter the database by category and key, and export the database to CSV, or JSON. All information and controls can be run in console through the provided DataAPI.bat.

## Setup
1. Edit the "DataAPI.bat" and specify the python directory, and the directory to the __main__.py file.
2. Save the file.
3. Run "DataAPI.bat".

## Controls
*  Help -> Shows the current command options
*  Display -> Change the current display format (Current options are Text and JSON)
*  Add -> Add an entry to the current database
*  Filter -> Search the database for entries containing specific data
*  Export -> Export the database to a specified format and directory (Current options are CSV and JSON)
*  Format -> Change the format for displaying and exporting data

## Extending the system
The system currently uses a file discovery feature pointing to the "Source\file_types\" directory. To add your own format to the system, add a folder with the name of your desired format (e.g. "XML") and create a python file in that folder titled formatName_format (e.g. "XML_format.py"). Your file must inherit from the "file_format" class located in "file_format_base.py". Simply reference the functions in that class, and fill out your own functionality. See CSV\csv_format.py for an example.
