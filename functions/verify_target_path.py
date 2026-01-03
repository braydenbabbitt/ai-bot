import os

def verify_target_path(working_directory: str, target_path: str) -> tuple[bool, str]:
    abs_working_dir = os.path.abspath(working_directory)
    abs_target_path = os.path.normpath(os.path.join(abs_working_dir, target_path))
    target_path_is_valid = os.path.commonpath([abs_working_dir, abs_target_path]) == abs_working_dir
    return target_path_is_valid, abs_target_path
