from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.app import App
from kivy.lang import Builder

import wikipedia
import requests

Builder.load_file("front.kv")


class FirstScreen(Screen):
    def search_image(self):
        user_query = self.manager.current_screen.ids.input.text
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) '
                                 'Chrome/56.0.2924.76 Safari/537.36'}
        with open("files/image.jpg", "wb") as image:
            image.write(requests.get(wikipedia.page(user_query).images[0], headers=headers).content)
        self.manager.current_screen.ids.img.source = "files/image.jpg"


class RootWidget(ScreenManager):
    pass


class MainApp(App):

    def build(self):
        return RootWidget()


MainApp().run()
