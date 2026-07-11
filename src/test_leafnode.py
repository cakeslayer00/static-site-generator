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


if __name__ == "__main__":
    unittest.main()

