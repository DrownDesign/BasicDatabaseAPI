class database:
    
    def __init__(self, file, format):
        print("Creating new database...")
        
        self.entries = []

        file_array = []

        #Try to build the database based on the current format
        try:
            file_array = format.build_database(file)
        except:
            print(f"Error trying to build database {format}")

        for line in file_array:
            if len(line) > 2:
                current_entry = entry(line[0],line[1],line[2])
                self.entries.append(current_entry)

    def get_entries(self):
        return self.entries

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