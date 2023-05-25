"""
TV controller
Create a simple prototype of a TV controller in Python. It’ll use the following commands:
first_channel() - turns on the first channel from the list.
last_channel() - turns on the last channel from the list.
turn_channel(N) - turns on the N channel. Pay attention that the channel
 numbers start from 1, not from 0.
next_channel() - turns on the next channel. If the current channel is the
 last one, turns on the first channel.
previous_channel() - turns on the previous channel. If the current channel
 is the first one, turns on the last channel.
current_channel() - returns the name of the current channel.
is_exist(N/'name') - gets 1 argument - the number N or the string 'name'
 and returns "Yes", if the channel N or 'name' exists in the list, or "No" - in the other case.

The default channel turned on before all commands is №1.
Your task is to create the TVController class and methods described above.
CHANNELS = ["BBC", "Discovery", "TV1000"]
 class TVController:
pass
controller = TVController(CHANNELS)
controller.first_channel() == "BBC"
controller.last_channel() == "TV1000"
controller.turn_channel(1) == "BBC"
controller.next_channel() == "Discovery"
controller.previous_channel() == "BBC"
controller.current_channel() == "BBC"
controller.is_exist(4) == "No"
controller.is_exist("BBC") == "Yes"
"""
class TVController:
    def __init__(self, channels: list):
        self.channels = channels
        self.channel_index = 0

    def show_channel(self):
        print(f'{self.channel_index + 1}. Channel: "{self.channels[self.channel_index]}".')

    def first_channel(self):
        self.channel_index = 0
        self.show_channel()

    def last_channel(self):
        self.channel_index = len(self.channels)-1
        self.show_channel()

    def turn_channel(self, channel_number):
        if channel_number in range(1, len(self.channels)):
            self.channel_index = channel_number-1
            self.show_channel()
        else:
            print("Channel number out of range.")

    def next_channel(self):
        if self.channel_index < len(self.channels)-1:
            self.channel_index += 1
        else:
            self.channel_index = 0
        self.show_channel()

    def previous_channel(self):
        if self.channel_index > 1:
            self.channel_index -= 1
        else:
            self.channel_index = len(self.channels)-1
        self.show_channel()

    def current_channel(self):
        self.show_channel()

    def is_exist(self, channel: str or int):
        if type(channel) == str:
            condition = channel in self.channels
        elif type(channel) == int:
            condition = channel in range(1, len(self.channels)+1)
        else:
            print('Incorrect input.')
            return None
        print(f'Yes, the channel {channel} is exist.'
              if condition
              else f'No, the channel {channel} is not exist.')

if __name__ == '__main__':
    from additional_program import tv_controller_program
    tv_controller_program(TVController)
