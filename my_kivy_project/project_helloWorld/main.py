from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.image import Image

class MainApp(App):
    def build(self):
        # Items are called 'WIDGETS' in Kivy
        label = Label(text='Hello from Kivy', # The words to display 
                    size_hint=(.5, .5),   # This seems to have no effect whatsoever??
                                        # Notes say this is the proportion of distortion??
                                        # Default is (1,1) ??
                    pos_hint={'center_x': .5, 'center_y': .05}) # Looks like this is (x,y)
                                                                # (0,0) is bottom left, (1,1) is top right?

        img = Image(source='./love.jpg',
                    size_hint=(.25, .25),
                    pos_hint={'center_x':.5, 'center_y':.5})

        return img; label #unable to show both label and image at the same time??

if __name__ == '__main__':
    app = MainApp()
    app.run()
