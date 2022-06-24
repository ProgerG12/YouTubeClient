from hmac import new
import kivy, kivymd
from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.utils import get_color_from_hex
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.scrollview import ScrollView
from kivymd.uix.textfield import MDTextFieldRect
from kivy.properties import ObjectProperty
from kivymd.uix.button import MDRectangleFlatIconButton
from kivymd.uix.screen import MDScreen
from kivy.uix.scrollview import ScrollView
from kivymd.uix.list import MDList
from kivymd.uix.card import MDCard
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.utils.fitimage import FitImage

screenManager = None

class videoScreen(MDScreen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        newBox = MDBoxLayout(orientation="vertical")

        newBox.add_widget(self.initSearchField())
        newBox.add_widget(self.initVideoList())

        self.add_widget(newBox)

    def initSearchField(self):
        newAnchorLayout = AnchorLayout(anchor_x = "center", anchor_y = "top")
        newAnchorLayout.padding = "22dp"
        
        #newBox3 = MDBoxLayout(orientation = "horizontal")

        newTextField = MDTextFieldRect()
        newTextField.hint_text = "TEST"
        newTextField.size_hint_y = 0.13

        #newSearchButton = MDRectangleFlatIconButton(text = "Search")

        #newBox3.add_widget(newTextField)
        #newBox3.add_widget(newSearchButton)
        
        #newAnchorLayout.add_widget(newSearchButton)
        newAnchorLayout.add_widget(newTextField)
        return newAnchorLayout
    
    def initVideoList(self):
        newAnchorLayout2 = AnchorLayout(anchor_x = "center", anchor_y = "center")
        newAnchorLayout2.pos_hint = {"center_x": 0.19, "center_y": 0.0}
        newAnchorLayout2.size_hint_y = 0.5
        newAnchorLayout2.size_hint_x = 0.5

        newScrollView = ScrollView()
        newScrollView.size_hint = (1, 0.8)

        newList = MDList()
        newList.spacing = "10dp"

        newCard = MDCard()
        newCard.size_hint = (0.5, None)
        newCard.pos_hint = {"center_x": 1.0, "center_y": 0.5}

        newBox2 = MDBoxLayout(orientation = "horizontal")

        newImage = FitImage()
        newImage.size_hint = (0.5, None)
        newImage.source = "mqdefault.jpg"

        newBox2.add_widget(newImage)

        newCard.add_widget(newBox2)
        newList.add_widget(newCard)
        newScrollView.add_widget(newList)

        
        newAnchorLayout2.add_widget(newScrollView)
        
        return newAnchorLayout2


    
class LibraryScreen(MDScreen):
    pass

class SetingsScreen(MDScreen):
    pass

class YouTube(MDApp):
    def build(self):
        global screenManager
        #self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "Red"
        screenManager = ScreenManager()
        ui = Builder.load_file("mainActivity.kv")
        screenManager.add_widget(videoScreen(name="videoScreen"))
        screenManager.add_widget(SetingsScreen(name="SetingsScreen"))
        ui.add_widget(screenManager)

        return ui
    
    def setScreen(self, screenName):
        screenManager.current = screenName

if __name__ == '__main__':
    YouTube().run()
