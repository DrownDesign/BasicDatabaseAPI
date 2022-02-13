from file_types import file_format_base


class json_format(file_format_base.file_format):


    def build_database(self, file):
        print("Creating Database from JSON...")

        data_array = []

        file_array = file.read().split("\n")

        entry = []
        for line in file_array:
            if "name" in line:
                name = line.split('"')[3]
                entry.append(name)
                continue

            if "address" in line:
                address = line.split('"')[3]
                entry.append(address)
                continue

            if "number" in line:
                number = line.split('"')[3]
                entry.append(number)

                data_array.append(entry)
                entry = []
                continue

        return data_array

    def export_file(self, data, path):
        file = open(path, "w")
        file.write('{\n "Database":[\n')
        index = 0
        for entry in data:
            file.write(
                '{\n' + f'"name": "{entry.name}",\n "address": "{entry.address}",\n "number": "{entry.number}"\n' + "}")
            if index < len(data) - 1:
                file.write(",\n")
            else:
                file.write('\n]\n}')
            index += 1

    def print_data(self, data):
        print('{\n "Database": [\n')
        index = 0
        for entry in data:
            print('{\n' + f'"name": "{entry.name}",\n "address": "{entry.address}",\n "number": "{entry.number}"\n' + "}")
            if index < len(data) - 1:
                print(",\n")
            else:
                print('\n]\n}')
            index+=1

    @property
    def extension(self):
        return ".json"
