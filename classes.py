class Television:
    MIN_CHANNEL = 0     # Minimum TV channel
    MAX_CHANNEL = 3     # Maximum TV channel

    MIN_VOLUME = 0      # Minimum TV volume
    MAX_VOLUME = 2      # Maximum TV volume

    def __init__(self):
        self.__channel = self.MIN_CHANNEL
        self.__volume = self.MIN_VOLUME
        self.__status = False

    def power(self):
        if self.__status is False:
            self.__status = True
        else:
            self.__status = False

    def channel_up(self):
        if self.__status is True:
            if self.__channel == self.MAX_CHANNEL:
                self.__channel = self.MIN_CHANNEL
            else:
                self.__channel += 1

    def channel_down(self):
        if self.__status is True:
            if self.__channel == self.MIN_CHANNEL:
                self.__channel = self.MAX_CHANNEL
            else:
                self.__channel -= 1

    def volume_up(self):
        if self.__status is True:
            if self.__volume != self.MAX_VOLUME:
                self.__volume += 1

    def volume_down(self):
        if self.__status is True:
            if self.__volume != self.MIN_VOLUME:
                self.__volume -= 1

    def __str__(self):
        c_status = str(self.__channel)
        v_status = str(self.__volume)
        return f'TV status: Is on = {self.__status}, Channel = {c_status}, Volume = {v_status}'
