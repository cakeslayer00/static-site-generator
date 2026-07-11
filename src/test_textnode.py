import unittest
from textnode import TextNode, TextType

class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)

    def test_not_eq(self):
        node = TextNode("This is a text node", TextType.BOLD, "http://cake.dev")
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertNotEqual(node, node2)

    def test_text_type_not_eq(self):
        node = TextNode("This is a text node", TextType.CODE, "http://cake.dev")
        node2 = TextNode("This is a text node", TextType.BOLD, "http://cake.dev")
        self.assertNotEqual(node, node2)

    def test_url_is_none(self):
        node = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node.url, None)

    def test_eq_with_url(self):
        node = TextNode("link", TextType.LINK, "http://cake.dev")
        node2 = TextNode("link", TextType.LINK, "http://cake.dev")
        self.assertEqual(node, node2)

    def test_not_eq_different_text(self):
        node = TextNode("one", TextType.TEXT)
        node2 = TextNode("two", TextType.TEXT)
        self.assertNotEqual(node, node2)

    def test_not_eq_non_textnode(self):
        node = TextNode("This is a text node", TextType.BOLD)
        self.assertNotEqual(node, "This is a text node")
        self.assertFalse(node == 42)

    def test_repr(self):
        node = TextNode("hi", TextType.LINK, "http://cake.dev")
        self.assertEqual(node.__repr__(), "TextNode(hi, link, http://cake.dev)")

if __name__ == "__main__":
    unittest.main()
