from kivy.app import App
from kivy.lang import global_idmap
from kivy.properties import OptionProperty

from translation import Translator


class I18n(App):
    language = OptionProperty('en', options=('en', 'fr'))

    def run(self):
        self.translator = translator = Translator()
        translator.compile_languages()
        translator.language = self.language
        self.bind(language=translator.setter('language'))
        global_idmap['_'] = translator
        super().run()


if __name__ == '__main__':
    I18n().run()
