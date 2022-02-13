import os
from typing import List

FILE_FORMAT_PACKAGE = "file_types"
FILE_FORMATS_PATH = os.path.join(os.path.dirname(__file__))

def find_available_formats():
    format_modules: List[str] = []

    format_subdirs = next(os.walk(FILE_FORMATS_PATH))[1]

    for subdir in format_subdirs:
        if subdir.lower() == '__pycache__':
            continue
        module_name = f'{subdir}_format'

        path = os.path.join(FILE_FORMATS_PATH, subdir, module_name + '.py')

        if os.path.exists(path):
            module = ".".join([FILE_FORMAT_PACKAGE, subdir, module_name])
            format_modules.append(module)

    return format_modules
