import unittest

from htmlnode import ParentNode
from block_markdown import markdown_to_html_node

class TestMarkdownToHTML(unittest.TestCase):
    def test_paragraphs(self):
        md = """
    This is **bolded** paragraph
    text in a p
    tag here

    This is another paragraph with _italic_ text and `code` here

    """

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><p>This is <b>bolded</b> paragraph text in a p tag here</p><p>This is another paragraph with <i>italic</i> text and <code>code</code> here</p></div>",
        )

    def test_codeblock(self):
        md = """
    ```
    This is text that _should_ remain
    the **same** even with inline stuff
    ```
    """

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><pre><code>This is text that _should_ remain\nthe **same** even with inline stuff\n</code></pre></div>",
        )

    def test_headings_all_levels(self):
        md = """
# Heading 1

## Heading 2

### Heading 3

#### Heading 4

##### Heading 5

###### Heading 6
"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><h1>Heading 1</h1><h2>Heading 2</h2><h3>Heading 3</h3>"
            "<h4>Heading 4</h4><h5>Heading 5</h5><h6>Heading 6</h6></div>",
        )

    def test_heading_with_inline(self):
        md = "# Title with **bold**, _italic_ and `code`"

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><h1>Title with <b>bold</b>, <i>italic</i> and <code>code</code></h1></div>",
        )

    def test_unordered_list(self):
        md = """
- first item with **bold**
- second item with _italic_
- third item with `code`
"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><ul><li>first item with <b>bold</b></li>"
            "<li>second item with <i>italic</i></li>"
            "<li>third item with <code>code</code></li></ul></div>",
        )

    def test_ordered_list(self):
        md = """
1. one
2. two with **bold**
3. three
"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><ol><li>one</li><li>two with <b>bold</b></li><li>three</li></ol></div>",
        )

    def test_quote(self):
        md = """
> a quote with **bold** and _italic_
> spanning two lines
"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><blockquote>a quote with <b>bold</b> and <i>italic</i> "
            "spanning two lines</blockquote></div>",
        )

    def test_links_and_images(self):
        md = "A [link](https://boot.dev) and an ![image](https://i.imgur.com/x.png) inline"

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            '<div><p>A <a href="https://boot.dev">link</a> and an '
            '<img src="https://i.imgur.com/x.png" alt="image"></img> inline</p></div>',
        )

    def test_mixed_document(self):
        md = """
# Title

A paragraph with **bold**.

- item one
- item two

```
code here
```

> a quote
"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><h1>Title</h1><p>A paragraph with <b>bold</b>.</p>"
            "<ul><li>item one</li><li>item two</li></ul>"
            "<pre><code>code here\n</code></pre>"
            "<blockquote>a quote</blockquote></div>",
        )

    def test_returns_div_parent_node(self):
        node = markdown_to_html_node("just a paragraph")
        self.assertIsInstance(node, ParentNode)
        self.assertEqual(node.tag, "div")

    def test_empty_markdown_has_no_children(self):
        with self.assertRaises(ValueError):
            markdown_to_html_node("").to_html()
