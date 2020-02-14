import time
import kivy
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.boxlayout import BoxLayout
from kivy.config import Config
from kivy.uix.button import Button
from kivy.uix.checkbox import CheckBox
from kivy.uix.camera import Camera
from kivy.uix.slider import Slider
from kivy.uix.label import Label
from kivy.uix.switch import Switch
kivy.require('1.10.1')

class TestApp(App):

	def build(self):
		Config.set('graphics', 'width', 320)
		Config.set('graphics', 'height', 512)
		print(kivy.__version__)

		# -------- funciones -------------
		def sw(instance, value):
			print('the switch', instance, 'is', value)
			print(layout.size)
			if value:
				labelMensaje.text = "ACTIVADO."
				print(kivy.__version__)
			else:
				labelMensaje.text = "DESACTIVADO."

		# capas layout
		layout = BoxLayout(spacing=2, orientation="horizontal", padding=30)
		layout2 = BoxLayout(spacing=10, orientation="vertical", padding=30)
		
		# elementos widgets
		labelsw1 = Label(text="Luz del pasillo:")
		btn1 = Button(text='Entrar')
		labelMensaje = Label(text="DESACTIVADO.", font_size=30)
		switch = Switch()

		layout.add_widget(switch, index=0)
		layout.add_widget(labelsw1, index=1)
		layout2.add_widget(layout, index=2)
		layout2.add_widget(btn1, index=0)
		layout2.add_widget(labelMensaje, index=1)

		switch.bind(active=sw)

		return layout2


if __name__ == '__main__':
	print(kivy.__version__)
	TestApp().run()