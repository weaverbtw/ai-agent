import os

def get_files_info(working_directory: str, directory: str = ".") -> str:
    try:
        abs_path_work_dir = os.path.abspath(working_directory)
        target_dir_path = os.path.normpath(os.path.join(abs_path_work_dir, directory))
        valid_dir_path = os.path.commonpath([abs_path_work_dir, target_dir_path]) == abs_path_work_dir

        if not valid_dir_path:
            return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'
            
        if not os.path.isdir(target_dir_path):
            return f'Error: "{directory}" is not a directory'
        return f'Success: "{directory}" is within the working directory'
    
    except Exception as e:
        return(f"Error: {e}")