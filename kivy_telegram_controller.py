import requests
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput

TOKEN = '7938115120:AAG_0QKw5yl1JMjxPfdTMdBwcmHnEFqLE8o'
CHAT_ID = '8178344048'


def send_telegram_message(message):
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
    data = {"chat_id": CHAT_ID, "text": message}
    requests.post(url, data=data)

class RemoteControlUI(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(orientation='vertical', **kwargs)
        self.textbox = TextInput(hint_text="Enter movie name", size_hint_y=0.125)
        self.add_widget(self.textbox)

        buttons = [
            ("Start", "start"),
            ("Pause", "0"),
            ("Rewind", "1"),
            ("Forward", "-1"),
            ("Movie", lambda: f"movie {self.textbox.text}"),
            ("Close", "close")
        ]

        for label, command in buttons:
            action = command if isinstance(command, str) else command
            btn = Button(text=label, size_hint_y=0.125)
            btn.bind(on_press=lambda instance, cmd=action: send_telegram_message(cmd() if callable(cmd) else cmd))
            self.add_widget(btn)

class RemoteControlApp(App):
    def build(self):
        return RemoteControlUI()

if __name__ == "__main__":
    RemoteControlApp().run()
