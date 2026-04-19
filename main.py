from kivymd.app import MDApp
from kivymd.uix.screen import MDScreen
from kivymd.uix.button import MDRaisedButton
from kivymd.uix.label import MDLabel
from kivymd.uix.boxlayout import MDBoxLayout
import requests

SERVER = "http://YOUR_SERVER_IP:8000"  # غيره لاحقاً

class MainScreen(MDScreen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        layout = MDBoxLayout(orientation="vertical", padding=30, spacing=20)

        self.status = MDLabel(
            text="Status: Unknown",
            halign="center",
            font_style="H5"
        )

        btn_start = MDRaisedButton(text="تشغيل البوت", pos_hint={"center_x": 0.5})
        btn_stop = MDRaisedButton(text="إيقاف البوت", pos_hint={"center_x": 0.5})
        btn_status = MDRaisedButton(text="تحديث الحالة", pos_hint={"center_x": 0.5})

        btn_start.bind(on_press=self.start_bot)
        btn_stop.bind(on_press=self.stop_bot)
        btn_status.bind(on_press=self.get_status)

        layout.add_widget(self.status)
        layout.add_widget(btn_start)
        layout.add_widget(btn_stop)
        layout.add_widget(btn_status)

        self.add_widget(layout)

    def start_bot(self, instance):
        try:
            r = requests.get(f"{SERVER}/start_bot/main")
            self.status.text = str(r.json())
        except:
            self.status.text = "❌ خطأ"

    def stop_bot(self, instance):
        try:
            r = requests.get(f"{SERVER}/stop_bot/main")
            self.status.text = str(r.json())
        except:
            self.status.text = "❌ خطأ"

    def get_status(self, instance):
        try:
            r = requests.get(f"{SERVER}/status")
            self.status.text = str(r.json())
        except:
            self.status.text = "❌ لا اتصال"

class MyApp(MDApp):
    def build(self):
        self.theme_cls.primary_palette = "Blue"
        self.theme_cls.theme_style = "Dark"
        return MainScreen()

MyApp().run()
