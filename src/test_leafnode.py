import unittest
from htmlnode import LeafNode

class TestLeafNode(unittest.TestCase):
    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")

    def test_leaf_to_html_a_with_props(self):
        node = LeafNode("a", "Website", {"href":"https://example.com"})
        self.assertEqual(node.to_html(), '<a href="https://example.com">Website</a>')

    def test_leaf_to_html_with_raw_value(self):
        node = LeafNode("", "Raw Value")
        self.assertEqual(node.to_html(), "Raw Value")

    def test_leaf_to_html_none_tag_raw_value(self):
        node = LeafNode(None, "Raw Value")
        self.assertEqual(node.to_html(), "Raw Value")

    def test_leaf_to_html_none_value_raises(self):
        node = LeafNode("p", None)
        self.assertRaises(ValueError, node.to_html)

    def test_leaf_to_html_empty_value_renders(self):
        # empty string is a valid value (e.g. <img>), it must not raise
        node = LeafNode("img", "", {"src": "cat.png", "alt": "a cat"})
        self.assertEqual(node.to_html(), '<img src="cat.png" alt="a cat"></img>')

    def test_leaf_to_html_no_props(self):
        node = LeafNode("span", "hi")
        self.assertEqual(node.to_html(), "<span>hi</span>")


if __name__ == "__main__":
    unittest.main()

