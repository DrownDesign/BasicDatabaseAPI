class database:
    
    def __init__(self, file):
        print("Creating new database...")
        
        self.entries = []

        file_array = file.read().split("\n")

        index = 0
        for line in file_array:
            #Skip first line of database containing categories rather than entries
            if index is not 0:
                line = line.split(",")
                if len(line) > 2:
                    current_entry = entry(line[0],line[1],line[2])
                    self.entries.append(current_entry)
                
            index+=1

    def display_database(self, data):
        print("Name, Address, Number\n")
        for x in data:
            print(x)

    def add_entry(self, name, address, number):
        new_entry = entry(name, address, number)
        self.entries.append(new_entry)

    def filter(self, category, search):
        data = []
        for current_entry in self.entries:
            if category.lower() == 'name' and search.lower() in current_entry.name.lower():
                data.append(current_entry)
            elif category.lower() == 'address' and search.lower() in current_entry.address.lower():
                data.append(current_entry)
            elif category.lower() == 'number' and search.lower() in current_entry.number.lower():
                data.append(current_entry)
                
        return data

    def export(self, format, filepath):
        file = open(filepath, "w")

        if format.lower() == 'csv':
            file.write("Name,Address,Number\n")
            for entry in self.entries:
                file.write(f"{entry.name},{entry.address},{entry.number}\n")
        elif format.lower() == 'json':
            file.write('{\n "Database":[\n')
            for entry in self.entries:
                file.write('{\n' + f'"name": "{entry.name}",\n "address": "{entry.address}",\n "number": "{entry.number}"\n' + "},\n")
            file.write('}')
        else:
            print('Format not supported')
        file.close()
        
class entry:

    def __init__(self,name,address,number):
        self.name = name
        self.address = address
        self.number = number

    def __str__(self):
        return str(f"{self.name}, {self.address}, {self.number}")