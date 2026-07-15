import os, shutil 

from html_generation import generate_pages_recursive

STATIC_FILES_DIRECTORY = "static"
CONTENT_FILES_DIRECTORY = "content"
PUBLIC_FILES_DIRECTORY = "public"


def copy_files_to_target_dir(source_dir: str, target_dir: str):
    if not os.path.exists(source_dir):
        raise Exception("Given source directory doens't exist")
    if os.path.exists(target_dir):
        shutil.rmtree(target_dir)
    os.mkdir(target_dir)

    for name in os.listdir(source_dir):
        source = os.path.join(source_dir, name)
        target = os.path.join(target_dir, name)
        if os.path.isfile(source):
            shutil.copy2(source, target)
            print(f"Copy source {source} to {target}")
        else:
            print(f"\nEntering directory {source}\n")
            copy_files_to_target_dir(source, target)

def main() -> None:
    copy_files_to_target_dir(STATIC_FILES_DIRECTORY, PUBLIC_FILES_DIRECTORY)
    generate_pages_recursive(CONTENT_FILES_DIRECTORY, "template.html", PUBLIC_FILES_DIRECTORY)




if __name__ == "__main__":
    main()
