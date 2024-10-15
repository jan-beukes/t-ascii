import cv2
import ascii
from textual.app import App
from textual.widgets import *
from textual import events
import asyncio

class ASCIIWebcamApp(App):
    def __init__(self):
        super().__init__()
        self.running = True
        self.table = 0
        self.cam_index = 0
        self.vid = cv2.VideoCapture(self.cam_index)

    def on_mount(self):
        self.frame = Static()
        self.button = Button("Click me")
        self.mount(self.frame, self.button)
        self.update_frame()
        asyncio.create_task(self.update_frame())
        
    async def update_frame(self):
        while self.running:
            ret, frame = self.vid.read()
            art = ascii.get_art(frame,0.15,self.table)
            ascii_frame = ascii.get_frame(art)
            self.frame.update(ascii_frame)
            await asyncio.sleep(0.02)


    async def on_key(self, event: events.Key):
        if event.key == "q":
            self.running = False
            self.exit()

if __name__ == "__main__":
    app = ASCIIWebcamApp()
    app.run()

