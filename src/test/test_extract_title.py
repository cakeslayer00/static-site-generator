import unittest

from block_markdown import extract_title


class TestExtractTitle(unittest.TestCase):
    def test_extracts_h1(self):
        self.assertEqual(extract_title("# Hello"), "Hello")

    def test_strips_surrounding_whitespace(self):
        self.assertEqual(extract_title("#    Spaced title   "), "Spaced title")

    def test_extracts_only_title_from_document(self):
        md = "# Title\n\nSome body content\n\n## A subheading"
        self.assertEqual(extract_title(md), "Title")

    def test_keeps_inline_markdown_literal(self):
        self.assertEqual(extract_title("# Title with **bold**"), "Title with **bold**")

    def test_raises_on_non_h1_heading(self):
        with self.assertRaises(Exception):
            extract_title("## Not an h1")

    def test_raises_without_heading(self):
        with self.assertRaises(Exception):
            extract_title("just a paragraph")

    def test_raises_on_empty(self):
        with self.assertRaises(Exception):
            extract_title("")


if __name__ == "__main__":
    unittest.main()
