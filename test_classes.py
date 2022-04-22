import unittest
from classes import *


class MyTestCase(unittest.TestCase):
    def test_power(self):
        self.tv = Television()
        assert self.tv.__str__() == 'TV status: Is on = False, Channel = 0, Volume = 0'
        self.tv.power()
        assert self.tv.__str__() == 'TV status: Is on = True, Channel = 0, Volume = 0'
        self.tv.power()
        assert self.tv.__str__() == 'TV status: Is on = False, Channel = 0, Volume = 0'

    def test_channel_up(self):
        self.tv = Television()
        assert self.tv.__str__() == 'TV status: Is on = False, Channel = 0, Volume = 0'
        self.tv.channel_up()
        assert self.tv.__str__() == 'TV status: Is on = False, Channel = 0, Volume = 0'
        self.tv.power()
        self.tv.channel_up()
        assert self.tv.__str__() == 'TV status: Is on = True, Channel = 1, Volume = 0'
        self.tv.channel_up()
        assert self.tv.__str__() == 'TV status: Is on = True, Channel = 2, Volume = 0'
        self.tv.channel_up()
        assert self.tv.__str__() == 'TV status: Is on = True, Channel = 3, Volume = 0'
        self.tv.channel_up()
        assert self.tv.__str__() == 'TV status: Is on = True, Channel = 0, Volume = 0'
        self.tv.channel_up()
        self.tv.channel_up()
        self.tv.power()
        assert self.tv.__str__() == 'TV status: Is on = False, Channel = 2, Volume = 0'
        self.tv.channel_up()
        assert self.tv.__str__() == 'TV status: Is on = False, Channel = 2, Volume = 0'

    def test_channel_down(self):
        self.tv = Television()
        assert self.tv.__str__() == 'TV status: Is on = False, Channel = 0, Volume = 0'
        self.tv.channel_down()
        assert self.tv.__str__() == 'TV status: Is on = False, Channel = 0, Volume = 0'
        self.tv.power()
        self.tv.channel_down()
        assert self.tv.__str__() == 'TV status: Is on = True, Channel = 3, Volume = 0'
        self.tv.channel_down()
        assert self.tv.__str__() == 'TV status: Is on = True, Channel = 2, Volume = 0'
        self.tv.channel_down()
        assert self.tv.__str__() == 'TV status: Is on = True, Channel = 1, Volume = 0'
        self.tv.channel_down()
        assert self.tv.__str__() == 'TV status: Is on = True, Channel = 0, Volume = 0'
        self.tv.channel_down()
        self.tv.channel_down()
        self.tv.power()
        assert self.tv.__str__() == 'TV status: Is on = False, Channel = 2, Volume = 0'
        self.tv.channel_down()
        assert self.tv.__str__() == 'TV status: Is on = False, Channel = 2, Volume = 0'

    def test_volume_up(self):
        self.tv = Television()
        assert self.tv.__str__() == 'TV status: Is on = False, Channel = 0, Volume = 0'
        self.tv.volume_up()
        assert self.tv.__str__() == 'TV status: Is on = False, Channel = 0, Volume = 0'
        self.tv.power()
        self.tv.volume_up()
        self.tv.volume_up()
        assert self.tv.__str__() == 'TV status: Is on = True, Channel = 0, Volume = 2'
        self.tv.volume_up()
        assert self.tv.__str__() == 'TV status: Is on = True, Channel = 0, Volume = 2'
        self.tv.volume_down()
        self.tv.volume_down()
        self.tv.volume_up()
        assert self.tv.__str__() == 'TV status: Is on = True, Channel = 0, Volume = 1'
        self.tv.power()
        self.tv.volume_up()
        assert self.tv.__str__() == 'TV status: Is on = False, Channel = 0, Volume = 1'

    def test_volume_down(self):
        self.tv = Television()
        assert self.tv.__str__() == 'TV status: Is on = False, Channel = 0, Volume = 0'
        self.tv.volume_down()
        assert self.tv.__str__() == 'TV status: Is on = False, Channel = 0, Volume = 0'
        self.tv.power()
        self.tv.volume_up()
        self.tv.volume_up()
        assert self.tv.__str__() == 'TV status: Is on = True, Channel = 0, Volume = 2'
        self.tv.volume_down()
        assert self.tv.__str__() == 'TV status: Is on = True, Channel = 0, Volume = 1'
        self.tv.volume_up()
        self.tv.volume_down()
        self.tv.volume_down()
        assert self.tv.__str__() == 'TV status: Is on = True, Channel = 0, Volume = 0'
        self.tv.volume_up()
        self.tv.power()
        self.tv.volume_down()
        assert self.tv.__str__() == 'TV status: Is on = False, Channel = 0, Volume = 1'

if __name__ == '__main__':
    unittest.main()
