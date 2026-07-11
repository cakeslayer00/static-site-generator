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

    def test_props_to_html_none(self):
        node = HTMLNode("p", "text")
        self.assertEqual(node.props_to_html(), "")

    def test_props_to_html_empty_dict(self):
        node = HTMLNode("p", "text", props={})
        self.assertEqual(node.props_to_html(), "")

    def test_props_to_html_multiple(self):
        node = HTMLNode("a", "link", props={"href": "https://x.com", "target": "_blank"})
        self.assertEqual(
            node.props_to_html(), ' href="https://x.com" target="_blank"'
        )

    def test_defaults_all_none(self):
        node = HTMLNode()
        self.assertIsNone(node.tag)
        self.assertIsNone(node.value)
        self.assertIsNone(node.children)
        self.assertIsNone(node.props)

if __name__ == "__main__":
    unittest.main()

