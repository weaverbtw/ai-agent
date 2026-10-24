import os

def get_file_content(working_directory: str, file_path: str) -> str:
    try:
        abs_path_work_dir = os.path.abspath(working_directory)
        file_path = os.path.normpath(os.path.join(abs_path_work_dir, file_path))
        valid_file_path = os.path.commonpath([abs_path_work_dir, file_path]) == abs_path_work_dir

        if not valid_file_path:
            return(f'Error: Cannot read "{file_path}" as it is outside the permitted working directory')

        if not os.path.isfile(file_path):
            return(f'Error: File not found or is not a regular file: "{file_path}"')

        MAX_CHARS = 10000
        with open(file_path, "r") as f:
            content = f.read(MAX_CHARS)

            if f.read(1):
                content += f'[...File "{file_path}" truncated at {MAX_CHARS} characters]'

        return content
    
    except Exception as e:
        return(f"Error: {e}")
