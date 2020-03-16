#from kivy.app import App
from kivy.app import App

from kivy.properties import BooleanProperty, ObjectProperty

from kivy.uix.widget import Widget
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.treeview import TreeView, TreeViewLabel
from kivy.uix.filechooser import FileChooserListView



class Client(Widget):
    pass


class MyRemarkableApp(App):

    def build(self):
        return Client()


if __name__ == "__main__":
    MyRemarkableApp().run()
