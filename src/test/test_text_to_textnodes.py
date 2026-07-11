import unittest
from textnode import TextNode, TextType
from split_inline import text_to_textnodes

class TestTextToTextNodes(unittest.TestCase):
    def test_text_to_textnodes_with_every_inline_type(self):
        text = "This is *text* with an _italic_ word and a `code block` and an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) and a [link](https://boot.dev)"
        self.assertListEqual(
            [
                TextNode("This is ", TextType.TEXT),
                TextNode("text", TextType.BOLD),
                TextNode(" with an ", TextType.TEXT),
                TextNode("italic", TextType.ITALIC),
                TextNode(" word and a ", TextType.TEXT),
                TextNode("code block", TextType.CODE),
                TextNode(" and an ", TextType.TEXT),
                TextNode("obi wan image", TextType.IMAGE, "https://i.imgur.com/fJRm4Vk.jpeg"),
                TextNode(" and a ", TextType.TEXT),
                TextNode("link", TextType.LINK, "https://boot.dev"),
            ],
            text_to_textnodes(text),
        )

    def test_text_to_textnodes_plain_text(self):
        self.assertListEqual(
            [TextNode("Just plain text", TextType.TEXT)],
            text_to_textnodes("Just plain text"),
        )

    def test_text_to_textnodes_empty_string(self):
        self.assertListEqual([], text_to_textnodes(""))

    def test_text_to_textnodes_only_bold(self):
        self.assertListEqual(
            [TextNode("bold", TextType.BOLD)],
            text_to_textnodes("*bold*"),
        )

    def test_text_to_textnodes_multiple_of_same_type(self):
        self.assertListEqual(
            [
                TextNode("one", TextType.BOLD),
                TextNode(" and ", TextType.TEXT),
                TextNode("two", TextType.BOLD),
            ],
            text_to_textnodes("*one* and *two*"),
        )

    def test_text_to_textnodes_image_and_link_together(self):
        self.assertListEqual(
            [
                TextNode("see ", TextType.TEXT),
                TextNode("img", TextType.IMAGE, "https://example.com/a.png"),
                TextNode(" then ", TextType.TEXT),
                TextNode("link", TextType.LINK, "https://example.com"),
            ],
            text_to_textnodes("see ![img](https://example.com/a.png) then [link](https://example.com)"),
        )

    def test_text_to_textnodes_leaves_delimiters_inside_code_alone(self):
        self.assertListEqual(
            [
                TextNode("run ", TextType.TEXT),
                TextNode("a_b_c", TextType.CODE),
            ],
            text_to_textnodes("run `a_b_c`"),
        )

    def test_text_to_textnodes_code_span_with_bold_delimiter(self):
        self.assertListEqual(
            [
                TextNode("glob ", TextType.TEXT),
                TextNode("*.py", TextType.CODE),
                TextNode(" here", TextType.TEXT),
            ],
            text_to_textnodes("glob `*.py` here"),
        )

    def test_text_to_textnodes_raises_on_unbalanced_delimiter(self):
        self.assertRaises(ValueError, lambda: text_to_textnodes("This is *bold with no end"))


if __name__ == "__main__":
    unittest.main()
