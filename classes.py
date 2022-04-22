class Television:
    MIN_CHANNEL = 0     # Minimum TV channel
    MAX_CHANNEL = 3     # Maximum TV channel

    MIN_VOLUME = 0      # Minimum TV volume
    MAX_VOLUME = 2      # Maximum TV volume

    def __init__(self) -> None:
        '''
        Constructor to create initial state of the television
        channel at minimum, volume at minimum, power is off
        '''
        self.__channel = self.MIN_CHANNEL
        self.__volume = self.MIN_VOLUME
        self.__status = False

    def power(self) -> None:
        '''
        method to determine whether television should be turned on or off
        sets television power status to true to turn television on or false to turn television off
        '''
        if self.__status is False:
            self.__status = True
        else:
            self.__status = False

    def channel_up(self) -> None:
        '''
        method to set the television channel to one higher
        first checks to see if television is powered on
        sets channel to channel + 1, channels will loop to minimum once maximum is reached.
        '''
        if self.__status is True:
            if self.__channel == self.MAX_CHANNEL:
                self.__channel = self.MIN_CHANNEL
            else:
                self.__channel += 1

    def channel_down(self) -> None:
        '''
        method to set the television channel to one lower
        first checks to see if television is powered on
        sets channel to channel - 1, channels will loop to maximum once minimum is reached
        '''
        if self.__status is True:
            if self.__channel == self.MIN_CHANNEL:
                self.__channel = self.MAX_CHANNEL
            else:
                self.__channel -= 1

    def volume_up(self):
        '''
        method to set the television volume to one higher
        first checks to see if television is powered on
        sets television volume to volume + 1, if volume is at maximum level, maxmimum level is returned
        '''
        if self.__status is True:
            if self.__volume != self.MAX_VOLUME:
                self.__volume += 1

    def volume_down(self):
        '''
        method to set the television volume to one lower
        first checks to see if television is powered on
        sets television volume to volume - 1, if volume is at minimum level, minimum level is returned
        '''
        if self.__status is True:
            if self.__volume != self.MIN_VOLUME:
                self.__volume -= 1

    def __str__(self) -> str:
        '''
        method to check the state of the television settings
        :return: print statement including power, channel, and volume settings.
        '''
        c_status = str(self.__channel)
        v_status = str(self.__volume)
        return f'TV status: Is on = {self.__status}, Channel = {c_status}, Volume = {v_status}'
