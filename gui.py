from logic import *

class Gui(Logic):
    """
    Class containing remote GUI
    """

    def __init__(self, window) -> None:
        """
        Initializing method
        """
        super().__init__()

        #window
        self.window_remote = window

        #power button
        self.frame_one = Frame(self.window_remote)
        #command below
        self.button_power = Button(self.frame_one, text = "O", anchor = 'center', command = self.power)

        self.frame_one.pack(anchor='e', pady=5, padx=5)
        self.button_power.pack(side = 'right')

        #first row of channel buttons
        self.frame_two = Frame(self.window_remote)
        self.button1 = Button(self.frame_two, text = '1', width = 6, height = 3, command = self.channel_one)
        self.button2 = Button(self.frame_two, text = '2', width = 6, height = 3, command = self.channel_two)
        self.button3 = Button(self.frame_two, text = '3', width = 6, height = 3, command = self.channel_three)

        self.frame_two.pack(anchor='w', pady=10, padx=10)
        self.button1.pack(side='left', padx=5)
        self.button2.pack(side='left', padx=5)
        self.button3.pack(side='left', padx=5)

        #second row of channel buttons
        self.frame_three = Frame(self.window_remote)
        self.button4 = Button(self.frame_three, text = '4', width = 6, height = 3, command = self.channel_four)
        self.button5 = Button(self.frame_three, text='5', width=6, height=3, command = self.channel_five)
        self.button6 = Button(self.frame_three, text='6', width=6, height=3, command = self.channel_six)

        self.frame_three.pack(anchor='w', padx=10)
        self.button4.pack(side='left', padx=5)
        self.button5.pack(side='left', padx=5)
        self.button6.pack(side='left', padx=5)

        #third row of channel buttons
        self.frame_four = Frame(self.window_remote)
        self.button7 = Button(self.frame_four, text='7', width=6, height=3, command = self.channel_seven)
        self.button8 = Button(self.frame_four, text='8', width=6, height=3, command = self.channel_eight)
        self.button9 = Button(self.frame_four, text='9', width=6, height=3, command = self.channel_nine)

        self.frame_four.pack(anchor='w', pady=10, padx=10)
        self.button7.pack(side='left', padx=5)
        self.button8.pack(side='left', padx=5)
        self.button9.pack(side='left', padx=5)

        #vol and chan increase
        self.frame_five = Frame(self.window_remote, width = 210)
        self.button_vol_up = Button(self.frame_five, text = '+', width = 2, height = 1, command = self.volume_up)
        self.button_chan_up = Button(self.frame_five, text = '+', width = 2, height = 1, command = self.channel_up)

        self.frame_five.pack(anchor = 'n', pady=5)
        self.button_vol_up.pack(side = 'left', padx = 20)
        self.button_chan_up.pack(side = 'right', padx = 20)

        #vol and chan labels
        self.frame_six = Frame(self.window_remote, width = 210)
        self.label_vol = Label(self.frame_six, text = 'Vol', anchor = 'ne', width = 2, height = 1)
        self.label_chan = Label(self.frame_six, text = 'Ch', anchor = 'sw', width = 2, height = 1)

        self.frame_six.pack(anchor = 'n')
        self.label_vol.pack(side = 'left', padx = 20)
        self.label_chan.pack(side = 'right', padx = 20)

        #vol and chan decrease
        self.frame_seven = Frame(self.window_remote, width = 210)
        self.button_vol_down = Button(self.frame_seven, text = '-', width = 2, height = 1, command = self.volume_down)
        self.button_chan_down = Button(self.frame_seven, text = '-', width = 2, height = 1, command = self.channel_down)

        self.frame_seven.pack(anchor = 'n', pady=5)
        self.button_vol_down.pack(side = 'left', padx = 20)
        self.button_chan_down.pack(side = 'right', padx = 20)

        #mute button
        self.frame_eight = Frame(self.window_remote, width = 210)
        self.button_mute = Button(self.frame_eight, text = "mute", width = 4, height = 1, command = self.mute)

        self.frame_eight.pack(anchor = 'n', pady = 5)
        self.button_mute.pack(anchor = 'center')