import os, shutil 
import sys

from html_generation import generate_pages_recursive

STATIC_FILES_DIRECTORY = "static"
CONTENT_FILES_DIRECTORY = "content"
DOCS_DIRECTORY = "docs"


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
    basepath = "/" if not sys.argv[1] else sys.argv[1]

    copy_files_to_target_dir(STATIC_FILES_DIRECTORY, DOCS_DIRECTORY)
    generate_pages_recursive(basepath, CONTENT_FILES_DIRECTORY, "template.html", DOCS_DIRECTORY)




if __name__ == "__main__":
    main()
