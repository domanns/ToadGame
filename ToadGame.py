#!/usr/bin/env python3

import kivy

from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.popup import Popup
from kivy.uix.floatlayout import FloatLayout
from kivy.properties import ListProperty
from kivy.properties import StringProperty
from kivy.properties import ObjectProperty
from kivy.base import ExceptionHandler
from kivy.base import ExceptionManager
from kivy.base import Logger

kivy.require('2.0.0')

def show_rules():

    show = RulesWindow()
    rules = Popup(title="Rules", content=show, size_hint=(None,None), size=(650,500))
    rules.open()


def show_scores(new_cur, z):

    show = ScoresWindow()
    scores = Popup(title="Best scores", content=show, size_hint=(None, None), size=(650,500))
    scores.open()


class RulesWindow(FloatLayout):
    pass


class ScoresWindow(FloatLayout):
    pass



class Interface(FloatLayout):

    def show_rules(self):
        show_rules()



class ToadGameApp(App):
    def build(self):
        return Interface()


if __name__ == '__main__':

   ToadGameApp().run()