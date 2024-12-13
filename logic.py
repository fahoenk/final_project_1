from tkinter import *
from tkinter.ttk import Progressbar
import time

class Logic:
    """
    Class containing logic and TV window
    """
    MIN_VOLUME = 0
    MAX_VOLUME = 10
    MIN_CHANNEL = 0
    MAX_CHANNEL = 8

    def __init__(self) -> None:
        """
        Initializing method
        """
        self.__power_status = False
        self.__muted = False
        self.__volume = Logic.MIN_VOLUME
        self.__channel = Logic.MIN_CHANNEL

        self.weather_chan = PhotoImage(file = "weather_channel.png")
        self.history_chan = PhotoImage(file="history_channel.png")
        self.syfy_chan = PhotoImage(file="syfy_channel.png")
        self.discovery_chan = PhotoImage(file = "discovery_channel.png")
        self.food_chan = PhotoImage(file = "food_channel.png")
        self.hgtv_chan = PhotoImage(file = "hgtv_channel.png")
        self.fx_chan = PhotoImage(file = "fx_channel.png")
        self.cartoon_network = PhotoImage(file = "cartoon_network_channel.png")
        self.disney_chan = PhotoImage(file = "disney_channel.png")

        self.channel_list = [self.weather_chan, self.history_chan, self.syfy_chan, self.discovery_chan, self.food_chan,
                             self.hgtv_chan, self.fx_chan, self.cartoon_network, self.disney_chan]

    def top_level(self) -> None:
        """
        Method that creates the TV screen
        """
        self.top = Toplevel()
        self.top.title("TV")
        self.top.geometry('550x350+425+30')
        self.top.resizable(False, False)

        self.frame_tv = Frame(self.top, width = 550, height = 350)
        self.label_image = Label(self.frame_tv, width = 550, height = 350)

        self.frame_tv.pack()
        self.label_image.pack()

    def show_volume_bar(self, volume: int) -> None:
        """
        Method that shows and updates the volume bar when volume is changed
        :param volume: volume of TV
        """
        self.volume_bar = Progressbar(self.frame_tv, orient=HORIZONTAL, length=200, mode="determinate")
        self.mute_symbol = Label(self.frame_tv)
        self.label_volume_value = Label(self.frame_tv, text = str(self.__volume))

        self.mute_image = PhotoImage(file="mute_image.png")
        self.vol_image = PhotoImage(file="volume_image.png")
        if self.__muted or self.__volume == 0:
            self.mute_symbol.config(image = self.mute_image, height = 18)
        else:
            self.mute_symbol.config(image = self.vol_image, height = 18)

        self.volume_bar['value'] = volume * 10

        self.volume_bar.place(x = 175, y = 320)
        self.mute_symbol.place(x= 152, y = 320)
        self.label_volume_value.place(x=375, y=320)

        self.top.update_idletasks()

        time.sleep(1)
        self.volume_bar.destroy()
        self.mute_symbol.destroy()
        self.label_volume_value.destroy()

    def update_channel(self, channel: int)-> None:
        """
        Method that changes the channel image when channel is changed
        """
        self.__channel = channel
        self.label_image.config(image = self.channel_list[channel], anchor = 'center')
        self.label_image.pack()

    def power(self) -> None:
        """
        Method that turns TV on or off and calls function to open TV
        """
        if not self.__power_status:
            self.__power_status = True
            self.top_level()
            self.update_channel(self.__channel)
        elif self.__power_status:
            self.__power_status = False
            self.top.destroy()

    def volume_up(self) -> None:
        """
        Method that increases the volume and shows volume bar
        """
        if self.__power_status:
            self.__muted = False
            if self.__volume < Logic.MAX_VOLUME:
                self.__volume += 1
                self.show_volume_bar(self.__volume)
            else:
                self.show_volume_bar(self.__volume)

    def volume_down(self) -> None:
        """
        Method that decreases the volume and shows volume bar
        """
        if self.__power_status:
            self.__muted = False
            if self.__volume > Logic.MIN_VOLUME:
                self.__volume -= 1
                self.show_volume_bar(self.__volume)
            else:
                self.show_volume_bar(self.__volume)

    def mute(self) -> None:
        """
        Method that mutes the TV and shows volume bar
        """
        if self.__power_status:
            if self.__muted:
                self.__muted = False
                self.show_volume_bar(self.__volume)
            else:
                self.__muted = True
                self.show_volume_bar(self.__volume)

    def channel_up(self) -> None:
        """
        Method that increases the channel
        """
        if self.__power_status:
            if self.__channel < Logic.MAX_CHANNEL:
                self.__channel += 1
                self.update_channel(self.__channel)
            else:
                self.__channel = Logic.MIN_CHANNEL
                self.update_channel(self.__channel)

    def channel_down(self) -> None:
        """
        Method that decreases the channel
        """
        if self.__power_status:
            if self.__channel > Logic.MIN_CHANNEL:
                self.__channel -= 1
                self.update_channel(self.__channel)
            else:
                self.__channel = Logic.MAX_CHANNEL
                self.update_channel(self.__channel)

    def channel_one(self) -> None:
        """
        Method that goes to channel 1
        """
        if self.__power_status:
            self.__channel = 0
            self.update_channel(0)

    def channel_two(self) -> None:
        """
        Method that goes to channel 2
        """
        if self.__power_status:
            self.__channel = 1
            self.update_channel(1)

    def channel_three(self)-> None:
        """
        Method that goes to channel 3
        """
        if self.__power_status:
            self.__channel = 2
            self.update_channel(2)

    def channel_four(self)-> None:
        """
        Method that goes to channel 4
        """
        if self.__power_status:
            self.__channel = 3
            self.update_channel(3)

    def channel_five(self) -> None:
        """
        Method that goes to channel 5
        """
        if self.__power_status:
            self.__channel = 4
            self.update_channel(4)

    def channel_six(self)-> None:
        """
        Method that goes to channel 6
        """
        if self.__power_status:
            self.__channel = 5
            self.update_channel(5)

    def channel_seven(self)-> None:
        """
        Method that goes to channel 7
        """
        if self.__power_status:
            self.__channel = 6
            self.update_channel(6)

    def channel_eight(self)-> None:
        """
        Method that goes to channel 8
        """
        if self.__power_status:
            self.__channel = 7
            self.update_channel(7)

    def channel_nine(self)-> None:
        """
        Method that goes to channel 9
        """
        if self.__power_status:
            self.__channel = 8
            self.update_channel(8)