import argparse
import os
import sys

def main():
    print("Welcome. Please enter desired database file for reading:")

    loadFile()
    

def loadFile():
    while True:
        #Recieve input for desired path
        filepath = input()

        if not os.path.exists(filepath):
            print("File not found. Please try again")
            loadFile()
        
        file = open(filepath, "r")
        print(file.read())

if __name__ == "__main__":
    main()