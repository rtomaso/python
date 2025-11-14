#-----------------------------------------------------------------------------------#
# CSCI 1620
# Fall 2025
# Lab 12, test_television.py
# Rachael Tomaso

# The test file to our television.py file. We are using pytest. This file will test
# all the functions against the final string. Similar to how we manually checked
# our television.py code against the comments in the main file first.
#-----------------------------------------------------------------------------------#


import pytest
from television import *


class Test:
    def setup_method(self):
        self.tv1 = Television()
        self.tv2 = Television()

    def teardown_method(self):
        del self.tv1
        del self.tv2

    def test_init(self):
        assert self.tv1.__str__() == 'Power = False, Channel = 0, Volume = 0'
        assert self.tv2.__str__() == 'Power = False, Channel = 0, Volume = 0'

    def test_power(self):
        self.tv1.power()
        assert self.tv1.__str__() == 'Power = True, Channel = 0, Volume = 0'
        self.tv1.power()
        assert self.tv1.__str__() == 'Power = False, Channel = 0, Volume = 0'
        self.tv1.power()
        assert self.tv1.__str__() == 'Power = True, Channel = 0, Volume = 0'

        self.tv2.power()
        assert self.tv2.__str__() == 'Power = True, Channel = 0, Volume = 0'
        self.tv2.power()
        assert self.tv2.__str__() == 'Power = False, Channel = 0, Volume = 0'
        self.tv2.power()
        assert self.tv2.__str__() == 'Power = True, Channel = 0, Volume = 0'

    def test_mute(self):
        self.tv1.power()
        self.tv1.volume_up()
        self.tv1.mute()
        assert self.tv1.__str__() == 'Power = True, Channel = 0, Volume = 0'
        self.tv1.mute()
        assert self.tv1.__str__() == 'Power = True, Channel = 0, Volume = 1'

        self.tv2.power()
        self.tv2.volume_up()
        self.tv2.power()
        self.tv2.mute()
        assert self.tv2.__str__() == 'Power = False, Channel = 0, Volume = 1'

    def test_channel_up(self):
        self.tv1.power()
        self.tv1.channel_up()
        assert self.tv1.__str__() == 'Power = True, Channel = 1, Volume = 0'
        self.tv1.channel_up()
        assert self.tv1.__str__() == 'Power = True, Channel = 2, Volume = 0'
        self.tv1.channel_up()
        assert self.tv1.__str__() == 'Power = True, Channel = 3, Volume = 0'
        self.tv1.channel_up()
        assert self.tv1.__str__() == 'Power = True, Channel = 0, Volume = 0'

        self.tv2.channel_up()
        assert self.tv2.__str__() == 'Power = False, Channel = 0, Volume = 0'

    def test_channel_down(self):
        self.tv1.power()
        self.tv1.channel_up()
        self.tv1.channel_up()
        self.tv1.channel_up() # Channel is at 3
        self.tv1.channel_down()
        assert self.tv1.__str__() == 'Power = True, Channel = 2, Volume = 0'
        self.tv1.channel_down()
        assert self.tv1.__str__() == 'Power = True, Channel = 1, Volume = 0'
        self.tv1.channel_down()
        assert self.tv1.__str__() == 'Power = True, Channel = 0, Volume = 0'
        self.tv1.channel_down()
        assert self.tv1.__str__() == 'Power = True, Channel = 3, Volume = 0'

        self.tv2.channel_down()
        assert self.tv2.__str__() == 'Power = False, Channel = 0, Volume = 0'

    def test_volume_up(self):
        self.tv1.power()
        self.tv1.volume_up()
        assert self.tv1.__str__() == 'Power = True, Channel = 0, Volume = 1'
        self.tv1.volume_up()
        assert self.tv1.__str__() == 'Power = True, Channel = 0, Volume = 2'
        self.tv1.volume_down()
        self.tv1.mute()
        self.tv1.volume_up()
        assert self.tv1.__str__() == 'Power = True, Channel = 0, Volume = 2'
        self.tv1.volume_up()
        assert self.tv1.__str__() == 'Power = True, Channel = 0, Volume = 2'

        self.tv2.volume_up()
        assert self.tv2.__str__() == 'Power = False, Channel = 0, Volume = 0'

    def test_volume_down(self):
        self.tv1.power()
        self.tv1.volume_up()
        self.tv1.volume_up() # Volume at 2
        self.tv1.volume_down()
        assert self.tv1.__str__() == 'Power = True, Channel = 0, Volume = 1'
        self.tv1.volume_up()
        self.tv1.mute()
        self.tv1.volume_down()
        assert self.tv1.__str__() == 'Power = True, Channel = 0, Volume = 1'
        self.tv1.volume_down()
        assert self.tv1.__str__() == 'Power = True, Channel = 0, Volume = 0'
        self.tv1.volume_down()
        assert self.tv1.__str__() == 'Power = True, Channel = 0, Volume = 0'

        self.tv2.volume_down()
        assert self.tv2.__str__() == 'Power = False, Channel = 0, Volume = 0'

