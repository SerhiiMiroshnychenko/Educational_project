import re
import pathlib
from task_1 import BinaryTree, Trunk, show_tree  # type: ignore


class HtmlParser:

    def __init__(self, filename):
        self.filename = filename
        self.__content = None
        self.__tags = []
        self.__tree = None
        self.__pars_file()

    def __pars_file(self):
        self.__write_content()
        self.__find_tags()
        self.__raise_tree()

    def __write_content(self):
        self.__content = pathlib.Path(self.filename).read_text()

    def __find_tags(self):
        pre_tags = re.findall(r'<[^/>][^>]*>', self.__content)
        pre_tags = [tag for tag in pre_tags if tag[1] != '!']
        tags = []
        for tag in pre_tags:
            for i, c in enumerate(tag):
                tag = tag.strip('<').strip('>')
                if c == ' ':
                    tag = tag[:i-1]
            tags.append(tag)
        self.__tags = tags

    def __raise_tree(self):
        tree = None
        main_tag = None
        for tag in self.__tags:
            text_pattern = fr'<{tag}>(.*)</{tag}>'
            text = re.findall(text_pattern, self.__content)
            text = text[0] if text else ''
            if tag in ('head', 'body'):
                main_tag = tag
            if not tree:
                tree = BinaryTree(tag)
                if text:
                    tree.set_root_val(text)
            elif tag == 'head':
                tree.insert_right(tag, text)
            elif tag == 'body':
                tree.insert_left(tag, text)
            elif main_tag == 'head':
                tree.right_child.add_leaf(tag, 'right', text)
            elif main_tag == 'body':
                tree.left_child.add_leaf(tag, 'left', text)
        self.__tree = tree

    def show_structure(self):
        show_tree(self.__tree)

    def show_tag_text(self, tag):
        print(f'\nThe tag <{tag}> contains text: "{self.__tree.show_value(tag)}".')


if __name__ == "__main__":
    my_parser = HtmlParser('task_2.html')
    my_parser.show_structure()
    my_parser.show_tag_text('title')
    my_parser.show_tag_text('h1')
