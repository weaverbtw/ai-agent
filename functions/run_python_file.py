import os
import subprocess

def run_python_file(working_directory: str, file_path: str, args: list[str] | None = None) -> str:
    try:
        abs_path_work_dir = os.path.abspath(working_directory)
        abs_file_path = os.path.normpath(os.path.join(abs_path_work_dir, file_path))
        valid_file_path = os.path.commonpath([abs_path_work_dir, abs_file_path]) == abs_path_work_dir

        if not valid_file_path:
            return(f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory')

        if not os.path.isfile(abs_file_path):
            return(f'Error: "{file_path}" does not exist or is not a regular file')

        if not file_path.endswith(".py"):
                    return(f'Error: "{file_path}" is not a Python file')

        command = ["python", abs_file_path]

        if args:
            command.extend(args)

        cmd_obj = subprocess.run(command, text=True, timeout=30.0, cwd=abs_path_work_dir, capture_output=True)

        output = ""
        if cmd_obj.returncode != 0:
            output += (f"Process exited with code {cmd_obj.returncode}\n")
        if cmd_obj.stdout:
            output += f"STDOUT: {cmd_obj.stdout}\n"
        if cmd_obj.stderr:
            output += f"STDERR: {cmd_obj.stderr}"
        if not cmd_obj.stdout and not cmd_obj.stderr:
            output += "No output produced"
        return output

    except Exception as e:
         return(f"Error: executing Python file: {e}")

schema_run_python_file = {
    "type": "function",
    "function": {
        "name": "run_python_file",
        "description": "Run the python file in a specified file/directory relative to the working directory, running the file and returning its output",
        "parameters": {
            "type": "object",
            "required": ["file_path"],
            "properties": {
                 "args": {
                    "type": "array",
                    "description": "Optional arguments to pass to the script",
                    "items": {
                        "type": "string",
                    },
                },
                "file_path": {
                    "type": "string",
                    "description": "File path to run python file from, relative to the working directory (default is the working directory itself)",
                },
            },
        },
    },
}