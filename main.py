#from kivy.app import App
from kivy.app import App

from kivy.properties import BooleanProperty, ObjectProperty

from kivy.uix.widget import Widget
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.treeview import TreeView, TreeViewLabel
from kivy.uix.filechooser import FileChooserListView

#class FolderColumn(Widget):
#    pass
#def build(self):
#    box_root = BoxLayout(orientation="horizontal")
#    tree = TreeView(root_options=dict(text="Documents"),
#                    hide_root=False,
#                    indent_level=2,
#                    size_hint=(.3, 1))
#    for file in ["file1", "file2", "file3"]:
#        node = TreeViewLabel(text=file, padding_x=[20,20])
#        tree.add_node(node)
#    l2 = FileChooserListView()
#    box_root.add_widget(tree)
#    box_root.add_widget(l2)
#    return box_root

class SupMe(Widget):
    pass


class MyRemarkableApp(App):

    def build(self):
        return SupMe()


if __name__ == "__main__":
    MyRemarkableApp().run()
