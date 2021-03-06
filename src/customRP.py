from pypresence import Presence

import time


class Select:
    def __init__(self, s: str, d: str, l_img: str, l_img_txt: str, tkn: str):
        self.state = s
        self.details = d
        self.largeImage = l_img
        self.largeImageText = l_img_txt
        self.token = tkn

    def choose(self):
        if len(self.state) != 0 and len(self.details) != 0 and len(self.token) != 0:

            rpc = Presence(self.token)
            rpc.connect()
            rpc.update(
                state=self.state,
                details=self.details,
                large_image=self.largeImage,
                large_text=self.largeImageText,
                start=time.time(),
            )
            status = print("Rich presence is running perfectly fine!")
            while True:
                time.sleep(15)
        else:
            input("Error, required data is not found!\nPress any key to close app!")

print("(✿◡‿◡)Welcome to my custom Rich Presence Creator! O(∩_∩)O(*^_^*)")

select = Select(
    input("Enter the state: "),
    input("Enter the details: "),
    input("Enter the large image name: "),
    input("Enter the large image hover text info: "),
    input("Enter your app token: "),
)
select.choose()
