from kivy.app import App
from kivy.uix.button import Button

class MyKivyApp(App):
    def build(self):
        # Create a button widget
        button = Button(text='Click Me!')
        
        # Bind the button to an event when it's clicked
        button.bind(on_press=self.on_button_click)
        
        # Return the button to be displayed in the app window
        return button

    def on_button_click(self, instance):
        print("Hello, Kivy!")

# Run the Kivy app
if __name__ == '__main__':
    MyKivyApp().run()