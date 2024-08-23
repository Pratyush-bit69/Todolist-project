import webbrowser
from kivy.core.audio import SoundLoader
from kivy.core.window import Window
from kivy.lang import Builder
from kivy.properties import ObjectProperty
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.screenmanager import Screen
from kivymd.uix.scrollview import MDScrollView
from kivy.metrics import dp
from kivy.properties import StringProperty
from kivymd.app import MDApp
from kivymd.uix.list import OneLineIconListItem
from kivymd.uix.menu import MDDropdownMenu
from kivymd.uix.pickers import MDDatePicker
from kivymd.uix.pickers import MDTimePicker
from kivy.storage.jsonstore import JsonStore
from kivy.uix.label import Label

class CustomLabel(Label):
    pass

class ContentNavigationDrawer(MDScrollView):
    screen_manager = ObjectProperty()
    nav_drawer = ObjectProperty()

class IconListItem(OneLineIconListItem):
    icon = StringProperty()



class Example(MDApp):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.screen = Builder.load_file("background.kv")

        menu = [{"viewclass": "OneLineListItem",
                       "height": dp(56),
                       "text": "ahhhhh",
                       "on_release": lambda x="ahhhhh": self.set_item(x),
                       }, {"viewclass": "OneLineListItem",
                           "height": dp(56),
                           "text": "amongus",
                           "on_release": lambda x="amongus": self.set_item(x), }
            , {"viewclass": "OneLineListItem",
               "height": dp(56),
               "text": "arpeggio",
               "on_release": lambda x="arpeggio": self.set_item(x), }
            , {"viewclass": "OneLineListItem",
               "height": dp(56),
               "text": "bell",
               "on_release": lambda x="bell": self.set_item(x), }
            , {"viewclass": "OneLineListItem",
               "height": dp(56),
               "text": "bongo",
               "on_release": lambda x="bongo": self.set_item(x), }
            , {"viewclass": "OneLineListItem",
               "height": dp(56),
               "text": "chimes",
               "on_release": lambda x="chimes": self.set_item(x), }
            , {"viewclass": "OneLineListItem",
               "height": dp(56),
               "text": "cute lame",
               "on_release": lambda x="cute lame": self.set_item(x), }
            , {"viewclass": "OneLineListItem",
               "height": dp(56),
               "text": "default",
               "on_release": lambda x="default": self.set_item(x), }
            , {"viewclass": "OneLineListItem",
               "height": dp(56),
               "text": "ding",
               "on_release": lambda x="ding": self.set_item(x), }
            , {"viewclass": "OneLineListItem",
               "height": dp(56),
               "text": "ding dong",
               "on_release": lambda x="ding dong": self.set_item(x), }
            , {"viewclass": "OneLineListItem",
               "height": dp(56),
               "text": "eager",
               "on_release": lambda x="eager": self.set_item(x), }
            , {"viewclass": "OneLineListItem",
               "height": dp(56),
               "text": "good bad ugly",
               "on_release": lambda x="good bad ugly": self.set_item(x), }
            , {"viewclass": "OneLineListItem",
               "height": dp(56),
               "text": "iphone",
               "on_release": lambda x="iphone": self.set_item(x), }
            , {"viewclass": "OneLineListItem",
               "height": dp(56),
               "text": "iphone ding",
               "on_release": lambda x="iphone ding": self.set_item(x), }
            , {"viewclass": "OneLineListItem",
               "height": dp(56),
               "text": "lazer",
               "on_release": lambda x="lazer": self.set_item(x), }
            , {"viewclass": "OneLineListItem",
               "height": dp(56),
               "text": "lights",
               "on_release": lambda x="lights": self.set_item(x), }
            , {"viewclass": "OneLineListItem",
               "height": dp(56),
               "text": "my name is jeff",
               "on_release": lambda x="my name is jeff": self.set_item(x), }
            , {"viewclass": "OneLineListItem",
               "height": dp(56),
               "text": "ohh no!!!",
               "on_release": lambda x="ohh no!!!": self.set_item(x), }
            , {"viewclass": "OneLineListItem",
               "height": dp(56),
               "text": "old spice",
               "on_release": lambda x="old spice": self.set_item(x), }
            , {"viewclass": "OneLineListItem",
               "height": dp(56),
               "text": "pulse",
               "on_release": lambda x="pulse": self.set_item(x), }
            , {"viewclass": "OneLineListItem",
               "height": dp(56),
               "text": "reliance home",
               "on_release": lambda x="reliance home": self.set_item(x), }
            , {"viewclass": "OneLineListItem",
               "height": dp(56),
               "text": "robot",
               "on_release": lambda x="robot": self.set_item(x), }
            , {"viewclass": "OneLineListItem",
               "height": dp(56),
               "text": "samsung",
               "on_release": lambda x="samsung": self.set_item(x), }
            , {"viewclass": "OneLineListItem",
               "height": dp(56),
               "text": "shooting star",
               "on_release": lambda x="shooting star": self.set_item(x), }
            , {"viewclass": "OneLineListItem",
               "height": dp(56),
               "text": "sweet",
               "on_release": lambda x="sweet": self.set_item(x), }
            , {"viewclass": "OneLineListItem",
               "height": dp(56),
               "text": "tick",
               "on_release": lambda x="tick": self.set_item(x), }
            , {"viewclass": "OneLineListItem",
               "height": dp(56),
               "text": "treasure",
               "on_release": lambda x="treasure": self.set_item(x), }
            , {"viewclass": "OneLineListItem",
               "height": dp(56),
               "text": "wisstle",
               "on_release": lambda x="wisstle": self.set_item(x), }
                      ]
        self.menu_items = MDDropdownMenu(
            caller=self.screen.ids.field,
            items=menu,
            position="bottom",
            width_mult=4,
        )
        menu_items = [
            {
                "viewclass": "IconListItem",
                "text": "Water reminder",
                "height": dp(56),
                "icon": "cup-water",
                "on_release": lambda x="0": self.menu_callback(x)
            },
            {
                "height": dp(56),
                "text": "Exersise",
                "icon": "weight-lifter",
                "viewclass": "IconListItem",
                "on_release": lambda x="1": self.menu_callback(x)
            },
            {
                "text": "Studying",
                "icon": "book-education-outline",
                "height": dp(56),
                "viewclass": "IconListItem",
                "on_release": lambda x="2": self.menu_callback(x)
            },
            {
                "text": "Sleep",
                "icon": "weather-night",
                "height": dp(56),
                "viewclass": "IconListItem",
                "on_release": lambda x="3": self.menu_callback(x)
            },
            {
                "text": "Break",
                "icon": "coffee",
                "height": dp(56),
                "viewclass": "IconListItem",
                "on_release": lambda x="4": self.menu_callback(x)
            },
            {
                "text": "Medicine",
                "icon": "pill",
                "height": dp(56),
                "viewclass": "IconListItem",
                "on_release": lambda x="5": self.menu_callback(x)
            },
            {
                "text": "Shopping",
                "icon": "cart-outline",
                "height": dp(56),
                "viewclass": "IconListItem",
                "on_release": lambda x="6": self.menu_callback(x)
            },
            {
                "text": "Other",
                "icon": "pencil",
                "height": dp(56),
                "viewclass": "IconListItem",
                "on_release": lambda x="6": self.menu_callback(x)
            }
        ]
        self.menu = MDDropdownMenu(
            caller=self.screen.ids.button,
            items=menu_items,
            width_mult=4,
        )

    def submit(self):
        print(self.root.ids.data.text)

    def on_save(self, instance, value, date_range):
        self.root.ids.kyahaidate.text = "Date:" + str(value)

    def show_date_picker(self):
        date_dialog = MDDatePicker()
        date_dialog.bind(on_save=self.on_save)
        date_dialog.open()

    def menu_callback(self, text_item):
        if text_item == '0':
            self.root.ids.button.text = "Water reminder"
            self.root.ids.button.icon = "cup-water"
            self.root.ids.template.text = "Water reminder"
        elif text_item == '1':
            self.root.ids.button.text = "Exersise"
            self.root.ids.button.icon = "weight-lifter"
            self.root.ids.template.text = "Exersise"
        elif text_item == '2':
            self.root.ids.button.text = "Studies"
            self.root.ids.button.icon = "book-education-outline"
            self.root.ids.template.text = "Studies"
        elif text_item == '3':
            self.root.ids.button.text = "Sleep"
            self.root.ids.button.icon = "weather-night"
            self.root.ids.template.text = "Sleep"
        elif text_item == '4':
            self.root.ids.button.text = "Break"
            self.root.ids.button.icon = "coffee"
            self.root.ids.template.text = "Break"
        elif text_item == '5':
            self.root.ids.button.text = "Medicine"
            self.root.ids.button.icon = "pill"
            self.root.ids.template.text = "Medicine"
        elif text_item == '6':
            self.root.ids.button.text = "Shopping"
            self.root.ids.button.icon = "cart-outline"
            self.root.ids.template.text = "Shopping"
        else:
            self.root.ids.button.text = "Choose a template"
            self.root.ids.button.icon = "pencil"

    def show_time_picker(self):
        '''Open time picker dialog.'''
        time_dialog = MDTimePicker()
        time_dialog.bind(time=self.get_time, on_cancel=self.off_clock_cancel, on_save=self.clicked_ok)
        time_dialog.open()

    def get_time(self, instance, time):
        self.store=JsonStore("storage.json")
        self.root.ids.AAAA.text=str(time)
        self.store.put(self.root.ids.AAAA.text)
        self.root.ids.time.text=self.root.ids.AAAA.text
    def off_clock_cancel(self, instance, time):
        print("pressed cancel")

    def clicked_ok(self, instance, time):
        self.root.ids.time.text = "Time:" + str(time)
    def xyz(self,x):
        self.screen.ids.show_themes.text=x
        if x=="0":
            self.root.ids.images.source="nature-images..jpg"
        if x=="1":
            self.root.ids.images.source="hana.jpg"
    def set_item(self, i):
        self.screen.ids.field.text = i
        if i == "ahhhhh":
            self.root.ids.field.text = "[font=font/GothamMedium.ttf][size=28]  Sound[/font][/size]\n" + "[size=23]  ahhhhh[/size]"
            sound = SoundLoader.load("music/ahhhhh.mp3")
            sound.play()
        elif i == "amongus":
            self.root.ids.field.text = "[font=font/GothamMedium.ttf][size=28]  Sound\n[/font][/size]" + "  amongus"
            sound = SoundLoader.load("music/amongus.mp3")
            sound.play()
        elif i == "arpeggio":
            self.root.ids.field.text = "[font=font/GothamMedium.ttf][size=28]  Sound\n[/font][/size]" + "  arpeggio"
            sound = SoundLoader.load("music/arpeggio.mp3")
            sound.play()
        elif i == "bell":
            self.root.ids.field.text = "[font=font/GothamMedium.ttf][size=28]  Sound\n[/font][/size]" + "  bell"
            sound = SoundLoader.load("music/bell.mp3")
            sound.play()
        elif i == "bongo":
            self.root.ids.field.text = "[font=font/GothamMedium.ttf][size=28]  Sound\n[/font][/size]" + "  bongo"
            sound = SoundLoader.load("music/bongo.mp3")
            sound.play()
        elif i == "chimes":
            self.root.ids.field.text = "[font=font/GothamMedium.ttf][size=28]  Sound\n[/font][/size]" + "  chimes"
            sound = SoundLoader.load("music/chimes.mp3")
            sound.play()
        elif i == "cute lame":
            self.root.ids.field.text = "[font=font/GothamMedium.ttf][size=28]  Sound\n[/font][/size]" + "  cute lame"
            sound = SoundLoader.load("music/cute_lame.mp3")
            sound.play()
        elif i == "default":
            self.root.ids.field.text = "[font=font/GothamMedium.ttf][size=28]  Sound\n[/font][/size]" + "  default"
            sound = SoundLoader.load("music/default.mp3")
            sound.play()
        elif i == "ding":
            self.root.ids.field.text = "[font=font/GothamMedium.ttf][size=28]  Sound\n[/font][/size]" + "ding"
            sound = SoundLoader.load("music/ding.mp3")
            sound.play()
        elif i == "ding dong":
            self.root.ids.field.text = "[font=font/GothamMedium.ttf][size=28]  Sound\n[/font][/size]" + "[font=33713_SerpentineBoldItalic.ttf]ding dong[/font]"
            sound = SoundLoader.load("music/ding dong.mp3")
            sound.play()
        elif i == "eager":
            self.root.ids.field.text = "[font=font/GothamMedium.ttf][size=30]Sound\n[/font][/size]" + "[font=33713_SerpentineBoldItalic.ttf]eager[/font]"
            sound = SoundLoader.load("music/eager.mp3")
            sound.play()
        elif i == "good bad ugly":
            self.root.ids.field.text = "[font=font/GothamMedium.ttf][size=30]Sound\n[/font][/size]" + "[font=33713_SerpentineBoldItalic.ttf]good bad ugly[/font]"
            sound = SoundLoader.load("music/good_bad_ugly.mp3")
            sound.play()
        elif i == "iphone":
            self.root.ids.field.text = "[font=font/GothamMedium.ttf][size=30]Sound\n[/font][/size]" + "[font=33713_SerpentineBoldItalic.ttf]iphone[/font]"
            sound = SoundLoader.load("music/bongo.mp3")
            sound.play()
        elif i == "iphone ding":
            self.root.ids.field.text = "[font=font/GothamMedium.ttf][size=30]Sound\n[/font][/size]" + "[font=33713_SerpentineBoldItalic.ttf]iphone ding[/font]"
            sound = SoundLoader.load("music/iphone_ding.mp3")
            sound.play()
        elif i == "lazer":
            self.root.ids.field.text = "[font=font/GothamMedium.ttf][size=30]Sound\n[/font][/size]" + "[font=33713_SerpentineBoldItalic.ttf]lazer[/font]"
            sound = SoundLoader.load("music/lazer.mp3")
            sound.play()
        elif i == "lights":
            self.root.ids.field.text = "[font=font/GothamMedium.ttf][size=30]Sound\n[/font][/size]" + "[font=33713_SerpentineBoldItalic.ttf]lights[/font]"
            sound = SoundLoader.load("music/lights.mp3")
            sound.play()
        elif i == "my name is jeff":
            self.root.ids.field.text = "[font=font/GothamMedium.ttf][size=30]Sound\n[/font][/size]" + "[font=33713_SerpentineBoldItalic.ttf]my name is jeff[/font]"
            sound = SoundLoader.load("music/my_name_is_jeff.mp3")
            sound.play()
        elif i == "ohh no!!!":
            self.root.ids.field.text = "[font=font/GothamMedium.ttf][size=30]Sound\n[/font][/size]" + "[font=33713_SerpentineBoldItalic.ttf]ohh no!!![/font]"
            sound = SoundLoader.load("music/ohh no!!!.mp3")
            sound.play()
        elif i == "old spice":
            self.root.ids.field.text = "[font=font/GothamMedium.ttf][size=30]Sound\n[/font][/size]" + "[font=33713_SerpentineBoldItalic.ttf]old spica[/font]"
            sound = SoundLoader.load("music/old_spice.mp3")
            sound.play()
        elif i == "pulse":
            self.root.ids.field.text = "[font=font/GothamMedium.ttf][size=30]Sound\n[/font][/size]" + "[font=33713_SerpentineBoldItalic.ttf]pulse[/font]"
            sound = SoundLoader.load("music/pulse.mp3")
            sound.play()
        elif i == "reliance home":
            self.root.ids.field.text = "[font=font/GothamMedium.ttf][size=30]Sound\n[/font][/size]" + "[font=33713_SerpentineBoldItalic.ttf]reliance home[/font]"
            sound = SoundLoader.load("music/reliance_home.mp3")
            sound.play()
        elif i == "robot":
            self.root.ids.field.text = "[font=font/GothamMedium.ttf][size=30]Sound\n[/font][/size]" + "[font=33713_SerpentineBoldItalic.ttf]robot[/font]"
            sound = SoundLoader.load("music/robot.mp3")
            sound.play()
        elif i == "samsung":
            self.root.ids.field.text = "[font=font/GothamMedium.ttf][size=30]Sound\n[/font][/size]" + "[font=33713_SerpentineBoldItalic.ttf]samsung[/font]"
            sound = SoundLoader.load("music/samsung.mp3")
            sound.play()
        elif i == "shooting star":
            self.root.ids.field.text = "[font=font/GothamMedium.ttf][size=30]Sound\n[/font][/size]" + "[font=33713_SerpentineBoldItalic.ttf]shooting star[/font]"
            sound = SoundLoader.load("music/shooting_star.mp3")
            sound.play()
        elif i == "sweet":
            self.root.ids.field.text = "[font=font/GothamMedium.ttf][size=30]Sound\n[/font][/size]" + "[font=33713_SerpentineBoldItalic.ttf]sweet[/font]"
            sound = SoundLoader.load("music/sweet.mp3")
            sound.play()
        elif i == "tick":
            self.root.ids.field.text = "[font=font/GothamMedium.ttf][size=30]Sound\n[/font][/size]" + "[font=33713_SerpentineBoldItalic.ttf]tick[/font]"
            sound = SoundLoader.load("music/tick.mp3")
            sound.play()
        elif i == "treasure":
            self.root.ids.field.text = "[font=font/GothamMedium.ttf][size=30]Sound\n[/font][/size]" + "[font=33713_SerpentineBoldItalic.ttf]treasure[/font]"
            sound = SoundLoader.load("music/treasure.mp3")
            sound.play()
        elif i == "wisstle":
            self.root.ids.field.text = "[font=font/GothamMedium.ttf][size=30]Sound\n[/font][/size]" + "[font=33713_SerpentineBoldItalic.ttf]wisstle[/font]"
            sound = SoundLoader.load("music/wisstle.mp3")
            sound.play()
        self.menu.dismiss()
    def cave(self):
        self.root.ids.images.source="images/cave.jpg"
        self.root.ids.images.opacity = 1
    def kmn(self):
        self.root.ids.images.source="images/kmn.jpeg.jpg"
        self.root.ids.images.opacity = 1
    def koko(self):
        self.root.ids.images.source="images/koko.jpeg"
        self.root.ids.images.opacity = 1
    def lamp(self):
        self.root.ids.images.source="images/lamp.jpg"
        self.root.ids.images.opacity = 1
    def no(self):
        self.root.ids.images.source="images/no.jpg"
        self.root.ids.images.opacity = 1
    def ocean_2(self):
        self.root.ids.images.source="images/ocean 2.jpg"
        self.root.ids.images.opacity = 1
    def OIP(self):
        self.root.ids.images.source="images/OIP.jpeg.jpg"
        self.root.ids.images.opacity = 1
    def pb(self):
        self.root.ids.images.source="images/pb.jpg"
        self.root.ids.images.opacity = 1
    def red_space(self):
        self.root.ids.images.source="images/red_space.jpeg.jpg"
        self.root.ids.images.opacity = 1
    def snow(self):
        self.root.ids.images.source="images/snow.jpg"
        self.root.ids.images.opacity = 1
    def space(self):
        self.root.ids.images.source="images/space.jpg"
        self.root.ids.images.opacity = 1
    def star(self):
        self.root.ids.images.source="images/star.jpg"
        self.root.ids.images.opacity = 1
    def starry(self):
        self.root.ids.images.source="images/starry.jpeg"
        self.root.ids.images.opacity = 1
    def stone(self):
        self.root.ids.images.source="images/stone.jpg"
        self.root.ids.images.opacity = 1
    def tree_space(self):
        self.root.ids.images.source="images/tree space.jpg"
        self.root.ids.images.opacity = 1
    def build(self):
        self.theme_cls.theme_style_switch_animation = True
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "Orange"
        return self.screen
    def save_checked(self, checkbox, value, a, b, c):
        if value == True:
            self.root.ids.mm1.secondary_text = "[size=20][font=font/33713_SerpentineBoldItalic.ttf]Enable[/font][/size]"
        else:
            self.root.ids.mm1.secondary_text = "[size=20][font=font/33713_SerpentineBoldItalic.ttf]Disable[/font][/size]"

    def switch_theme_style(self):

        self.theme_cls.primary_palette = (
            "Orange" if self.theme_cls.primary_palette == "Red" else "Red"

        )

        self.theme_cls.theme_style = (
            "Dark" if self.theme_cls.theme_style == "Light" else "Light"
        )

    def any_Function(instance):
        webbrowser.open('https://mail.google.com/mail/u/0/#inbox?compose=DmwnWsCSpFvNnKCScvVGhzDgBxbMkHlZPRVLVGbfJmksbfFsMJwXZnZDVgXVmFMGTFnjTrxPqtRl')
    def facebook(instance):
        webbrowser.open('https://mail.google.com/mail/u/0/#inbox?compose=DmwnWsCSpFvNnKCScvVGhzDgBxbMkHlZPRVLVGbfJmksbfFsMJwXZnZDVgXVmFMGTFnjTrxPqtRl')
    def twitter(instance):
        webbrowser.open('https://mail.google.com/mail/u/0/#inbox?compose=DmwnWsCSpFvNnKCScvVGhzDgBxbMkHlZPRVLVGbfJmksbfFsMJwXZnZDVgXVmFMGTFnjTrxPqtRl')
    def instagram(instance):
        webbrowser.open('https://mail.google.com/mail/u/0/#inbox?compose=DmwnWsCSpFvNnKCScvVGhzDgBxbMkHlZPRVLVGbfJmksbfFsMJwXZnZDVgXVmFMGTFnjTrxPqtRl')
    def moreapp(instance):
        webbrowser.open('https://mail.google.com/mail/u/0/#inbox?compose=DmwnWsCSpFvNnKCScvVGhzDgBxbMkHlZPRVLVGbfJmksbfFsMJwXZnZDVgXVmFMGTFnjTrxPqtRl')
    def open_color_picker(self):
        self.root.ids.Color.md_bg_color = [0,255,255]
        self.root.ids.images.source = ''
        self.root.ids.images.opacity = 0

    def open_color(self):
        self.root.ids.Color.md_bg_color = [48/255,213/255,200/255]
        self.root.ids.images.source = ''
        self.root.ids.images.opacity=0
    def open_color_qw(self):
        self.root.ids.Color.md_bg_color = [0, 0, 1]
        self.root.ids.images.source = ''
        self.root.ids.images.opacity = 0
Example().run()