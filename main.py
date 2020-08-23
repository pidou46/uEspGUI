import kivy
kivy.require('1.0.5')

from kivy.config import Config
Config.set('graphics', 'width', '400')
Config.set('graphics', 'height', '600')

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout

from websocket import create_connection

class EspGui(BoxLayout):
    '''L'interface graphique herite de BoxLayout dont la definition
     est dans le fichier EspGui.kv'''

    # AP default ip address of esp device
    addr='192.168.4.1'
    port='4646'

    def __init__(self):
        #super().__init__() incompatible avec python 2.7 utilise par kivy launcher
        super(EspGui,self).__init__()
        self.ids['l_status'].text="Please bind your device to ESSID MicroPythonxxxx:xxxx"
        self.ids['tb_disconnect'].state='down'

        
    def do_say_hello(self):
        print('ws://%s:%s'%(self.addr,self.port))
        ws=create_connection('ws://%s:%s'%(self.addr,self.port),1)
        ws.send("hello")
        result=ws.recv()
        print("Received '%s'"%result)
        ws.close

class EspGuiApp(App):

    def build(self):
        '''cree l'interface graphique en instanciant la classe EspGui'''
        return EspGui()

if __name__ == '__main__':
	EspGuiApp().run()
