# BasicDatabaseAPI
## System Overview
This basic database API allows users to take a set of personal data in CSV format, with each element containing a name, address, and phone number, and run certain tasks. Currently, a user can display the information in text and JSON formatting, filter the database by category and key, and export the database to CSV, or JSON. All information and controls can be run in console through the provided DataAPI.bat.

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
