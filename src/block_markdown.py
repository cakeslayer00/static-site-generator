import re

from enum import Enum

from htmlnode import HTMLNode, ParentNode
from textnode import text_node_to_html_node, TextNode, TextType
from inline_markdown import text_to_textnodes


class BlockType(Enum):
    PARAGRAPH = "paragraph"
    HEADING = "heading"
    CODE = "code"
    QUOTE = "quote"
    UNORDERED_LIST = "unordered_list"
    ORDERED_LIST = "ordered_list"

HEADING_REGEX = re.compile(r"^(#{1,6})(?!#)\s+(.+)$")
QUOTE_REGEX = re.compile(r">.*(?:\r?\n>.*)*")
UNORDERED_REGEX = re.compile(r"- .*(?:\r?\n- .*)*")
ORDERED_REGEX = re.compile(r"[0-9]+\. .*(?:\r?\n[0-9]+\. .*)*")
CODE_REGEX = re.compile(r"(`{3,})[^\n]*\n[\s\S]*?\n\1")

def is_heading(line: str) -> bool:
    return HEADING_REGEX.fullmatch(line) is not None

def is_codeblock(lines: str) -> bool:
    return CODE_REGEX.fullmatch(lines) is not None

def is_quote(lines: str) -> bool:
    return QUOTE_REGEX.fullmatch(lines) is not None

def is_unordered(lines: str) -> bool:
    return UNORDERED_REGEX.fullmatch(lines) is not None

def is_ordered(s):
    if ORDERED_REGEX.fullmatch(s) is None:
        return False
    nums = [int(n) for n in re.findall(r"^([0-9]+)\. ", s, re.M)]
    return nums == list(range(1, len(nums) + 1))

def block_to_block_type(markdown_block: str) -> BlockType:
    if is_heading(markdown_block):
        return BlockType.HEADING
    if is_codeblock(markdown_block):
        return BlockType.CODE
    if is_quote(markdown_block):
        return BlockType.QUOTE
    if is_unordered(markdown_block):
        return BlockType.UNORDERED_LIST
    if is_ordered(markdown_block):
        return BlockType.ORDERED_LIST
    return BlockType.PARAGRAPH

def markdown_to_blocks(markdown: str) -> list[str]:
    blocks = []
    for raw in markdown.split("\n\n"):
        block = "\n".join(line.strip() for line in raw.split("\n")).strip()
        if block:
            blocks.append(block)
    return blocks

def block_to_children(block: str) -> list[HTMLNode]:
    block_nodes: list[TextNode] = text_to_textnodes(block)

    return list(map(
        lambda x: text_node_to_html_node(x), 
        block_nodes
    ))


def extract_title(markdown: str) -> str:
    if not markdown.startswith("# "):
        raise Exception("Given markdown doesn't have h1 header")

    return markdown.split("\n", 1)[0][2:].strip()

def markdown_to_html_node(markdown: str) -> HTMLNode:
    blocks = markdown_to_blocks(markdown)

    children_nodes: list[HTMLNode] = []
    for block in blocks:
        match block_to_block_type(block):
            case BlockType.PARAGRAPH:
                children: list[HTMLNode] = block_to_children(block.replace("\n", " "))
                children_nodes.append(ParentNode("p", children))
            case BlockType.HEADING:
                hashes_and_content = block.split(" ", 1)

                children: list[HTMLNode] = block_to_children(hashes_and_content[1])
                children_nodes.append(ParentNode(f"h{len(hashes_and_content[0])}", children))
            case BlockType.CODE:
                lines = block.split("\n")

                block_node = TextNode("\n".join(lines[1 : len(lines) - 1]) + "\n", TextType.CODE)
                children_nodes.append(ParentNode("pre", [text_node_to_html_node(block_node)]))
            case BlockType.ORDERED_LIST:
                list_items = map(lambda x: x.split(" ", 1)[1], block.split("\n"))

                children: list[HTMLNode] = [ParentNode("li", block_to_children(item)) for item in list_items]
                children_nodes.append(ParentNode("ol", children))
            case BlockType.UNORDERED_LIST: 
                list_items = map(lambda x: x.split(" ", 1)[1], block.split("\n"))

                children: list[HTMLNode] = [ParentNode("li", block_to_children(item)) for item in list_items]
                children_nodes.append(ParentNode("ul", children))
            case BlockType.QUOTE:
                block = " ".join(map(lambda x: x.lstrip("> "), block.split("\n")))
                children: list[HTMLNode] = block_to_children(block)
                children_nodes.append(ParentNode("blockquote", children))
                
    return ParentNode("div", children_nodes)
        





