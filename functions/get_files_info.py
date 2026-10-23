import os

def get_files_info(working_directory: str, directory: str = ".") -> str:
    try:
        abs_path_work_dir = os.path.abspath(working_directory)
        target_dir_path = os.path.normpath(os.path.join(abs_path_work_dir, directory))
        valid_dir_path = os.path.commonpath([abs_path_work_dir, target_dir_path]) == abs_path_work_dir

        if not valid_dir_path:
            return f'    Error: Cannot list "{directory}" as it is outside the permitted working directory'
        if not os.path.isdir(target_dir_path):
                    return f'Error: "{directory}" is not a directory'

        target_dir_list = os.listdir(target_dir_path)
        contents: list[str] = []
        for i in target_dir_list:
            full_path = target_dir_path + "/" + i
            size = os.path.getsize(full_path)
            is_dir = os.path.isdir(full_path)
            contents.append(f"  - {i}: file_size={size} bytes, is_dir={is_dir}")
        return "\n".join(contents) # type: ignore
    
    except Exception as e:
        return(f"Error: {e}")
