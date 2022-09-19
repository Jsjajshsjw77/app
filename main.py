from vidstream import AudioSender
from vidstream import AudioReceiver
import socket
import threading
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.gridlayout import GridLayout
hostname=socket.gethostname()
IPAddr=socket.gethostbyname(hostname)
print(IPAddr)

rec = AudioReceiver(IPAddr,9999)
rec_thread = threading.Thread(target=rec.start_server)

sender = AudioSender('192.168.31.223',5555)
sender_thread = threading.Thread(target=sender.start_stream)
class MainWidget(GridLayout):
	def on_button_click(self):
		sender_thread.start()
class Main(App):
	def on_button_click(self):
		print('Clicked')
Main().run()