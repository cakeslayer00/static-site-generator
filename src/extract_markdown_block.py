import re

MARKDOWN_IMAGE_REGEX = r"!\[([^\[\]]*)\]\(([^\(\)]*)\)"
MARKDOWN_LINK_REGEX = r"(?<!!)\[([^\[\]]*)\]\(([^\(\)]*)\)"

def extract_markdown_images(text: str) -> list[tuple[str, str]]:
    return re.findall(MARKDOWN_IMAGE_REGEX, text)

def extract_markdown_links(text: str) -> list[tuple[str, str]]:
    return re.findall(MARKDOWN_LINK_REGEX, text)

