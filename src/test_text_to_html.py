import unittest
from textnode import TextNode, TextType, text_node_to_html_node

class TestTextToHtml(unittest.TestCase):
    def test_text(self):
        node = TextNode("This is a text node", TextType.TEXT)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, None)
        self.assertEqual(html_node.value, "This is a text node")

    def test_bold(self):
        html_node = text_node_to_html_node(TextNode("bold", TextType.BOLD))
        self.assertEqual(html_node.to_html(), "<b>bold</b>")

    def test_italic(self):
        html_node = text_node_to_html_node(TextNode("italic", TextType.ITALIC))
        self.assertEqual(html_node.to_html(), "<i>italic</i>")

    def test_code(self):
        html_node = text_node_to_html_node(TextNode("print()", TextType.CODE))
        self.assertEqual(html_node.to_html(), "<code>print()</code>")

    def test_link(self):
        node = TextNode("boot.dev", TextType.LINK, "https://boot.dev")
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.to_html(), '<a href="https://boot.dev">boot.dev</a>')

    def test_link_without_url(self):
        # missing url currently degrades to an empty href rather than raising
        node = TextNode("boot.dev", TextType.LINK)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.to_html(), '<a href="">boot.dev</a>')

    def test_image(self):
        node = TextNode("a cat", TextType.IMAGE, "cat.png")
        html_node = text_node_to_html_node(node)
        self.assertEqual(
            html_node.to_html(), '<img src="cat.png" alt="a cat"></img>'
        )

    def test_unsupported_type_raises(self):
        node = TextNode("x", TextType.TEXT)
        node.text_type = "not-a-real-type"
        self.assertRaises(Exception, text_node_to_html_node, node)

if __name__ == "__main__":
    unittest.main()


