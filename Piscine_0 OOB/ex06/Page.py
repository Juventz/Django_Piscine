from elem import Elem, Text
from elements import Html, Head, Body, Title, Meta, Table, Th, Tr, Td, \
    Ul, Ol, Li, H1, H2, P, Div, Span


class Page:
    def __init__(self, root):
        if not isinstance(root, Elem):
            raise TypeError("root must be an Elem")
        self.root = root

    def is_valid(self):
        return self._check_node(self.root)

    def _check_node(self, node):
        tag = node.tag

        if tag not in ['html', 'head', 'body', 'title', 'meta', 'img', 'table',
                       'th', 'tr', 'td', 'ul', 'ol',
                       'li', 'h1', 'h2', 'p', 'div', 'span',
                       'hr', 'br', Text]:
            return False

        if tag == "html":
            return self._check_html(node)
        elif tag == "head":
            return self._check_head(node)
        elif tag == "body":
            return self._check_body(node)
        elif tag == "title":
            return self._check_single_text_node(node, "title")
        elif tag in ["h1", "h2", "li", "th", "td"]:
            return self._check_single_text_node(node, tag)
        elif tag == "p":
            return self._check_only_text(node)
        elif tag == "span":
            return self._check_text_or_p(node)
        elif tag in ["ul", "ol"]:
            return self._check_only_li(node)
        elif tag == "tr":
            return self._check_tr(node)
        elif tag == "table":
            return self._check_table(node)
        elif tag == "div":
            return self._check_div(node)
        elif tag in ["hr", "br"]:
            return self._check_empty(node)

        return True

    def _check_html(self, node):
        if len(node.content) != 2:
            return False

        return (isinstance(node.content[0], Head) and
                isinstance(node.content[1], Body))

    def _check_head(self, node):
        title_count = sum(1 for elem in node.content
                          if isinstance(elem, Title))
        return title_count == 1 and all(isinstance(elem, (Title, Meta))
                                        for elem in node.content)

    def _check_body(self, node):
        allowed_types = {H1, H2, Div, Table, Ul, Ol, Span, Text}
        return all(type(elem) in allowed_types for elem in node.content)

    def _check_single_text_node(self, node):
        return len(node.content) == 1 and isinstance(node.content[0], Text)

    def _check_only_text(self, node):
        return all(isinstance(elem, Text) for elem in node.content)

    def _check_text_or_p(self, node):
        return all(isinstance(elem, (Text, P)) for elem in node.content)

    def _check_only_li(self, node):
        return len(node.content) > 0 and all(isinstance(elem, Li)
                                             for elem in node.content)

    def _check_tr(self, node):
        if not node.content:
            return False
        first_type = type(node.content[0])
        return (all(isinstance(elem, first_type) for elem in node.content)
                and first_type in {Th, Td})

    def _check_table(self, node):
        return all(isinstance(elem, Tr) for elem in node.content)

    def _check_div(self, node):
        allowed_types = {H1, H2, Div, Table, Ul, Ol, Span, Text}
        return all(type(elem) in allowed_types for elem in node.content)

    def _check_empty(self, node):
        return len(node.content) == 0

    def __str__(self):
        doc_type = "<!DOCTYPE html>\n" if isinstance(self.root, Html) else ""
        return doc_type + str(self.root)

    def write_to_file(self, filename):
        with open(filename, 'w') as f:
            f.write(str(self))
