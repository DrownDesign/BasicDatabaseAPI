from file_types import file_format_base

class csv_format(file_format_base.file_format):

    def build_database(self, file):
        print("Creating Database from CSV...")

        data_array = []
        file_array = file.read().split("\n")

        if file_array is not None:
            for line in file_array:
                #Skip category names
                if 'name' in line.lower() or line == "":
                    continue

                line = line.split(",")
                data_array.append(line)
        return data_array

    def export_file(self, data, path):
        print("Exporting CSV...")
        file = open(path, "w")

        file.write("Name,Address,Number\n")

        for entry in data:
            try:
                file.write(f"{entry.name},{entry.address},{entry.number}\n")
            except Exception as e:
                print(f"Error with write: {e}")
        file.close()

    def print_data(self, data):
        print("\nName, Address, Number\n")
        for x in data:
            print(x)

    @property
    def extension(self):
        return ".csv"