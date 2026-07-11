class HTMLNode:
    def __init__(self, tag: str | None = None, value: str | None = None, children: list[HTMLNode] | None = None, props: dict[str, str] | None = None) -> None:
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props 

    def to_html(self):
        raise NotImplementedError()

    def props_to_html(self):
        if not self.props or len(self.props) == 0:
            return ""

        return " " + " ".join(map(lambda x: f'{x}="{self.props[x]}"', self.props.keys()))

    def __repr__(self):
        return (
            f"""
        tag = {self.tag},
        value = {self.value},
        children = {self.children},
        props = {self.props_to_html()}
        """
        )

class LeafNode(HTMLNode):
    def __init__(self, tag: str | None, value: str,  props: dict[str, str] | None = None) -> None:
        super().__init__(tag, value, props=props)

    def to_html(self):
        if not self.value:
            raise ValueError("Value is empty or None")
        if not self.tag:
            return self.value

        return f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>"

    def __repr__(self):
        return (
            f"""
        tag = {self.tag},
        value = {self.value},
        props = {self.props_to_html()}
        """
        )

class ParentNode(HTMLNode):
    def __init__(self, tag: str,  children: list[HTMLNode], props: dict[str, str] | None = None) -> None:
        super().__init__(tag, children=children, props=props)

    def to_html(self):
        if not self.tag:
            raise ValueError("Tag is empty or None")
        if not self.children:
            raise ValueError("Children is empty or None")

        return f"<{self.tag}{self.props_to_html()}>" + "".join(map(lambda x: x.to_html(), self.children)) + f"</{self.tag}>"

    def __repr__(self):
        return (
            f"""
        tag = {self.tag},
        children = {self.children}
        props = {self.props_to_html()}
        """
        )
