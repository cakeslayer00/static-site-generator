import unittest

from block_markdown import BlockType, block_to_block_type


class TestBlockToBlockType(unittest.TestCase):
    def test_heading_levels(self):
        for level in range(1, 7):
            block = "#" * level + " Heading"
            self.assertEqual(block_to_block_type(block), BlockType.HEADING)

    def test_heading_requires_space(self):
        self.assertEqual(block_to_block_type("#no space"), BlockType.PARAGRAPH)

    def test_heading_too_many_hashes(self):
        self.assertEqual(block_to_block_type("####### too many"), BlockType.PARAGRAPH)

    def test_code_block(self):
        block = "```\ndef foo():\n    return 1\n```"
        self.assertEqual(block_to_block_type(block), BlockType.CODE)

    def test_code_block_with_language(self):
        block = "```python\nprint('hi')\n```"
        self.assertEqual(block_to_block_type(block), BlockType.CODE)

    def test_inline_code_is_not_code_block(self):
        self.assertEqual(block_to_block_type("`inline`"), BlockType.PARAGRAPH)

    def test_quote_single_line(self):
        self.assertEqual(block_to_block_type("> a quote"), BlockType.QUOTE)

    def test_quote_multiple_lines(self):
        block = "> line one\n> line two\n> line three"
        self.assertEqual(block_to_block_type(block), BlockType.QUOTE)

    def test_unordered_list_single_item(self):
        self.assertEqual(block_to_block_type("- item"), BlockType.UNORDERED_LIST)

    def test_unordered_list_multiple_items(self):
        block = "- one\n- two\n- three"
        self.assertEqual(block_to_block_type(block), BlockType.UNORDERED_LIST)

    def test_ordered_list(self):
        block = "1. one\n2. two\n3. three"
        self.assertEqual(block_to_block_type(block), BlockType.ORDERED_LIST)

    def test_ordered_list_single_item(self):
        self.assertEqual(block_to_block_type("1. one"), BlockType.ORDERED_LIST)

    def test_ordered_list_must_start_at_one(self):
        block = "2. two\n3. three"
        self.assertEqual(block_to_block_type(block), BlockType.PARAGRAPH)

    def test_ordered_list_must_be_sequential(self):
        block = "1. one\n3. three"
        self.assertEqual(block_to_block_type(block), BlockType.PARAGRAPH)

    def test_paragraph(self):
        self.assertEqual(
            block_to_block_type("Just a normal paragraph of text."),
            BlockType.PARAGRAPH,
        )

    def test_paragraph_with_inline_markdown(self):
        block = "This is **bold** and _italic_ text."
        self.assertEqual(block_to_block_type(block), BlockType.PARAGRAPH)


if __name__ == "__main__":
    unittest.main()
