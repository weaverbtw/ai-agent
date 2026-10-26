import os

def get_file_content(working_directory: str, file_path: str) -> str:
    try:
        abs_path_work_dir = os.path.abspath(working_directory)
        abs_file_path = os.path.normpath(os.path.join(abs_path_work_dir, file_path))
        valid_file_path = os.path.commonpath([abs_path_work_dir, abs_file_path]) == abs_path_work_dir

        if not valid_file_path:
            return(f'Error: Cannot read "{file_path}" as it is outside the permitted working directory')

        if not os.path.isfile(abs_file_path):
            return(f'Error: File not found or is not a regular file: "{file_path}"')

        MAX_CHARS = 10000
        with open(abs_file_path, "r") as f:
            content = f.read(MAX_CHARS)

            if f.read(1):
                content += f'[...File "{file_path}" truncated at {MAX_CHARS} characters]'

        return content
    
    except Exception as e:
        return(f"Error: {e}")

schema_get_file_content = {
    "type": "function",
    "function": {
        "name": "get_file_content",
        "description": "Lists the content of files in a specified file/directory relative to the working directory, providing contents of the file",
        "parameters": {
            "type": "object",
            "required": ["file_path"],
            "properties": {
                "file_path": {
                    "type": "string",
                    "description": "File path to list content of the file from, relative to the working directory (default is the working directory itself)",
                },
            },
        },
    },
}