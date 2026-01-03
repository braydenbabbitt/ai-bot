import os

from config import MAX_CHAR_READ_LIMIT
from functions.verify_target_path import verify_target_path


def get_file_content(working_directory: str, file_path: str):
    is_valid_path, abs_file_path = verify_target_path(working_directory, file_path)
    if not is_valid_path:
        return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'
    try:
        if not os.path.isfile(abs_file_path):
            return f'Error: Provided path is not a file: "{file_path}"'
        with open(abs_file_path) as file:
            initial_read = file.read(MAX_CHAR_READ_LIMIT)
            if file.read(1):
                initial_read += f'[...File "{file_path}" truncated at {MAX_CHAR_READ_LIMIT} characters]'
            return initial_read
    except:
        return f'Error: An unknown error occurred'
