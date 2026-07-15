import os

from block_markdown import markdown_to_html_node, extract_title

def generate_page(basepath, from_path, template_path, dest_path):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")

    with open(from_path, "r",  encoding="utf-8") as f:
        file_content = f.read()

    with open(template_path, "r", encoding="utf-8") as tf:
        template_content = tf.read()

    html_string = markdown_to_html_node(file_content).to_html()
    template_content = template_content.replace("{{ Title }}", extract_title(file_content))
    template_content = template_content.replace("{{ Content }}", html_string)
    template_content = template_content.replace("href=\"/", f"href=\"{basepath}")
    template_content = template_content.replace("src=\"/", f"src=\"{basepath}")

    os.makedirs(os.path.dirname(dest_path), exist_ok=True)

    with open(dest_path, "w", encoding="utf-8") as df:
        df.write(template_content)

def generate_pages_recursive(basepath, source_dir_path, template_path, dest_dir_path):
    if not os.path.exists(source_dir_path):
        raise Exception("Invalid source directory to gather content's from")
    if os.path.isfile(source_dir_path):
        raise Exception("File path given instead of directory")

    for resource in os.listdir(source_dir_path):
        source_path = os.path.join(source_dir_path, resource)
        dest_path = os.path.join(dest_dir_path, resource)
        if os.path.isfile(source_path):
            if dest_path.endswith(".md"):
                dest_path = dest_path[:-len(".md")] + ".html"
            generate_page(basepath, source_path, template_path, dest_path)
        else:
            generate_pages_recursive(basepath, source_path, template_path, dest_path)


