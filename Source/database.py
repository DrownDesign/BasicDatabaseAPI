class database:
    
    def __init__(self, file):
        print("Creating new database...")
        
        self.entries = []
        self.display_format = "text"

        file_array = file.read().split("\n")

        for line in file_array:
            #Skip category names
            if 'name' in line.lower():
                continue

            line = line.split(",")
            if len(line) > 2:
                current_entry = entry(line[0],line[1],line[2])
                self.entries.append(current_entry)

    #Display's the database based on incoming data, and the current state of the Display_Format variable
    def display_database(self, data):
        if self.display_format.lower() == "text":
            print("\nName, Address, Number\n")
            for x in data:
                print(x)
        elif self.display_format.lower() == "json":
            print('{\n "Database": [\n')
            index = 0
            for entry in data:
                print('{\n' + f'"name": "{entry.name}",\n "address": "{entry.address}",\n "number": "{entry.number}"\n' + "}")
                if index < len(data) - 1:
                    print(",\n")
                else:
                    print('\n]\n}')
                index+=1

    #Adds a new entry to the database
    def add_entry(self, name, address, number):
        new_entry = entry(name, address, number)
        self.entries.append(new_entry)

    #Filters the database based on a category and key
    def filter(self, category, search):
        data = []
        for current_entry in self.entries:
            if category.lower() == 'name' and search.lower() in current_entry.name.lower():
                data.append(current_entry)
            elif category.lower() == 'address' and search.lower() in current_entry.address.lower():
                data.append(current_entry)
            elif category.lower() == 'number' and search.lower() in current_entry.number.lower():
                data.append(current_entry)
        print(len(data))
        return data

    #Exports the file in a user specified file format and filepath
    def export(self, format, filepath):
        file = open(filepath, "w")

        if format.lower() == 'csv':
            file.write("Name,Address,Number\n")
            for entry in self.entries:
                file.write(f"{entry.name},{entry.address},{entry.number}\n")
        elif format.lower() == 'json':
            file.write('{\n "Database":[\n')
            index = 0
            for entry in self.entries:
                file.write('{\n' + f'"name": "{entry.name}",\n "address": "{entry.address}",\n "number": "{entry.number}"\n' + "}")
                if index < len(self.entries) - 1:
                    file.write(",\n")
                else:
                    file.write('\n]\n}')
                index+=1
        else:
            print('Format not supported')
        file.close()
        
#Class for defining on person in the entry.
class entry:

    #To extend the entries in the database, add variables here.
    def __init__(self,name,address,number):
        self.name = name
        self.address = address
        self.number = number

    #Defines how an entry is printed
    def __str__(self):
        return str(f"{self.name}, {self.address}, {self.number}")