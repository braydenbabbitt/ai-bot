import os

def get_files_info(working_directory: str, directory: str = "."):
    abs_working_dir = os.path.abspath(working_directory)
    abs_target_dir = os.path.normpath(os.path.join(abs_working_dir, directory))
    target_dir_is_valid = os.path.commonpath([abs_working_dir, abs_target_dir]) == abs_working_dir
    if not target_dir_is_valid:
        return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'
    if not os.path.isdir(abs_target_dir):
        return f'Error: "{directory}" is not a directory'

    result_str = ""
    for item in os.listdir(abs_target_dir):
        try:
            path_segments = item.split("/")
            name = path_segments[len(path_segments) - 1]
            is_file = os.path.isfile(item)
            file_size = 123 if not is_file else os.path.getsize(item)
            result_str = result_str + f'- {name}: file_size={file_size} bytes, is_dir={not is_file}\n'
        except:
            return f"Error: An unknown error occurred"

    result_title = f"Result for current directory:\n" if directory == "." else f"Result for '{directory}' directory:\n"
    return result_title + result_str
