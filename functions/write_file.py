import os

def write_file(working_directory: str, file_path: str, content: str) -> str:
    try:
        abs_path_work_dir = os.path.abspath(working_directory)
        file_path = os.path.normpath(os.path.join(abs_path_work_dir, file_path))
        valid_file_path = os.path.commonpath([abs_path_work_dir, file_path]) == abs_path_work_dir

        if not valid_file_path:
            return(f'Error: Cannot write to "{file_path}" as it is outside the permitted working directory')

        if os.path.isdir(file_path):
            return(f'Error: Cannot write to "{file_path}" as it is a directory')

        parent_dir = os.path.dirname(file_path)

        os.makedirs(parent_dir, exist_ok=True)

        with open(file_path, "w") as f:
            f.write(content)
            return(f'Successfully wrote to "{file_path}" ({len(content)} characters written)')
        
    except Exception as e:
        return(f"Error: {e}")
