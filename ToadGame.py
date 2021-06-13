#!/usr/bin/env python3

import kivy
import os
import saving_scores

from kivy.app import App
from kivy.uix.popup import Popup
from kivy.uix.floatlayout import FloatLayout
from kivy.properties import ObjectProperty

kivy.require('2.0.0')

def show_rules():

    show = RulesWindow()
    rules = Popup(title="Rules", content=show, size_hint=(None,None), size=(650,450))
    rules.open()


def show_scores():

    show = ScoresWindow()
    scores = Popup(title="Best scores", content=show, size_hint=(None, None), size=(650,500))
    scores.open()


def show_about_author():

    show = AuthorWindow()
    about_author = Popup(title="About author", content=show, size_hint=(None,None), size=(650,450))
    about_author.open()


def start_game():

    os.system("python main.py")


def clean_scores():

    saving_scores.init_csv()


class RulesWindow(FloatLayout):
    pass


class ScoresWindow(FloatLayout):

    scores_content = ObjectProperty()
    score1 = ObjectProperty()
    score2 = ObjectProperty()
    score3 = ObjectProperty()
    date1 = ObjectProperty()
    date2 = ObjectProperty()
    date3 = ObjectProperty()

    no, scores, dates = saving_scores.read_csv()

    score1 = scores[0]
    score2 = scores[1]
    score3 = scores[2]

    date1 = dates[0]
    date2 = dates[1]
    date3 = dates[2]

    def clean_scores(self):
        clean_scores()


class AuthorWindow(FloatLayout):
    pass


class Interface(FloatLayout):

    def show_rules(self):
        show_rules()
    def show_about_author(self):
        show_about_author()
    def start_game(self):
        start_game()
    def show_scores(self):
        show_scores()


class ToadGameApp(App):
    def build(self):
        return Interface()


if __name__ == '__main__':

   ToadGameApp().run()