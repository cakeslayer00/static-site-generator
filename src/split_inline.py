from textnode import TextNode, TextType
from extract_markdown_block import extract_markdown_images, extract_markdown_links

def split_nodes_delimiter(old_nodes: list[TextNode], delimiter: str, text_type: TextType) -> list[TextNode]:
    new_nodes: list[TextNode] = []

    for node in old_nodes:
        if node.text_type is not TextType.TEXT:
            new_nodes.append(node)
            continue

        split = node.text.split(delimiter)

        if len(split) == 1:
            new_nodes.append(node)
            continue

        if len(split) % 2 == 0:
            raise ValueError(f"unbalanced {delimiter!r} in: {node.text!r}")

        for i, string in enumerate(split):
            if not string:
                continue
            new_nodes.append(TextNode(string, TextType.TEXT if i % 2 == 0 else text_type))

    return new_nodes

def split_nodes_image(old_nodes: list[TextNode]) -> list[TextNode]:
    new_nodes: list[TextNode] = []

    for node in old_nodes:
        if node.text_type is not TextType.TEXT:
            new_nodes.append(node)
            continue

        images = extract_markdown_images(node.text)

        text_to_split = node.text
        for image in images:
            sections = text_to_split.split(f"![{image[0]}]({image[1]})", 1)
            new_nodes.append(TextNode(sections[0], TextType.TEXT))
            new_nodes.append(TextNode(image[0], TextType.IMAGE, image[1]))
            text_to_split = sections[1]

        if text_to_split:
            new_nodes.append(TextNode(text_to_split, TextType.TEXT))
    
    return new_nodes


def split_nodes_link(old_nodes: list[TextNode]) -> list[TextNode]:
    new_nodes: list[TextNode] = []

    for node in old_nodes:
        if node.text_type is not TextType.TEXT:
            new_nodes.append(node)
            continue

        links = extract_markdown_links(node.text)

        text_to_split = node.text
        for link in links:
            sections = text_to_split.split(f"[{link[0]}]({link[1]})", 1)
            new_nodes.append(TextNode(sections[0], TextType.TEXT))
            new_nodes.append(TextNode(link[0], TextType.LINK , link[1]))
            text_to_split = sections[1]

        if text_to_split:
            new_nodes.append(TextNode(text_to_split, TextType.TEXT))
    
    return new_nodes

def text_to_textnodes(text: str) -> list[TextNode]:
    base = [TextNode(text, TextType.TEXT)]
    # code first: a CODE node is skipped by later passes, so delimiters inside a
    # code span stay literal
    code = split_nodes_delimiter(base, "`", TextType.CODE)
    bold = split_nodes_delimiter(code, "*", TextType.BOLD)
    italic = split_nodes_delimiter(bold, "_", TextType.ITALIC)
    image = split_nodes_image(italic)
    link = split_nodes_link(image)
    return link


