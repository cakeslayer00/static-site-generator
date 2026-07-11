import unittest
from htmlnode import HTMLNode

class TestHTMLNode(unittest.TestCase):
    def test_props_to_html_eq(self):
        node = HTMLNode("a", "Website", props={"href":"https://example.com"})
        self.assertEqual(node.props_to_html(), ' href="https://example.com"')

    def test_to_html_throws(self):
        node = HTMLNode("a", "Website", props={"href":"https://example.com"})
        self.assertRaises(NotImplementedError, node.to_html)

    def test_repr_eq(self):
        node = HTMLNode("a", "Website", props={"href":"https://example.com"})
        self.assertEqual(node.tag, "a")
        self.assertEqual(node.value, "Website")

if __name__ == "__main__":
    unittest.main()

