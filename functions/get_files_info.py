import os


def get_files_info(working_directory: str, directory: str = ".") -> str:
    try:
        working_dir_abs = os.path.abspath(working_directory)
        target_dir = os.path.normpath(os.path.join(working_dir_abs, directory))
        valid_target_dir = os.path.commonpath([working_dir_abs, target_dir]) == working_dir_abs
        valid_dir = os.path.isdir(directory)

    except TypeError as e:
        valid_target_dir, valid_dir = False, False
        return f"Error: Invalid path type provided: {e}"

    except ValueError as e:
        valid_target_dir, valid_dir = False, False
        return f"Error: Path value error (e.g., cross-drive paths): {e}"

    except OSError as e:
        valid_target_dir, valid_dir = False, False
        return f"Error: OS error while accessing path: {e}"

    if not valid_target_dir:
        return f"Error: Cannot list \"{directory}\" as it is outside the permitted working directory"

    if not valid_dir:
        return f'Error: "{directory}" is not a directory'
    return f'Success: "{directory}" is within the working directory'
