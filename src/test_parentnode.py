import unittest

from htmlnode import LeafNode, ParentNode

class TestParentNode(unittest.TestCase):
    def test_to_html_with_children(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(), "<div><span>child</span></div>")

    def test_to_html_with_grandchildren(self):
        grandchild_node = LeafNode("b", "grandchild")
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(
            parent_node.to_html(),
            "<div><span><b>grandchild</b></span></div>",
        )

    def test_to_html_with_grandchildren_and_props(self):
        grandchild_node = LeafNode("b", "grandchild")
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node], {"description":"hell nah!"})
        self.assertEqual(
            parent_node.to_html(),
            '<div description="hell nah!"><span><b>grandchild</b></span></div>',
        )

    def test_to_html_multiple_children(self):
        parent_node = ParentNode(
            "p",
            [LeafNode("b", "Bold"), LeafNode(None, " and "), LeafNode("i", "italic")],
        )
        self.assertEqual(parent_node.to_html(), "<p><b>Bold</b> and <i>italic</i></p>")

    def test_to_html_no_tag_raises(self):
        parent_node = ParentNode(None, [LeafNode("span", "child")])
        self.assertRaises(ValueError, parent_node.to_html)

    def test_to_html_none_children_raises(self):
        parent_node = ParentNode("div", None)
        self.assertRaises(ValueError, parent_node.to_html)

    def test_to_html_empty_children_raises(self):
        parent_node = ParentNode("div", [])
        self.assertRaises(ValueError, parent_node.to_html)


if __name__ == "__main__":
    unittest.main()
