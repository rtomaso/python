#-----------------------------------------------------------------------------------#
# CSCI 1620
# Fall 2025
# Lab 12, television.py
# Rachael Tomaso

# Create a simple program for a television remote. This lab is mainly to
# become familiar with Git. The main file was given to us, and we need to ensure the
# output matches the comments in main.
#-----------------------------------------------------------------------------------#


class Television:
    """
    A class for television settings

    Attributes
    MIN_VOLUME (int): Minimum Volume the TV can be set to
    MAX_VOLUME (int): Maximum Volume the TV can be set to
    MIN_CHANNEL (int):  Minimum Channel the TV can be set to
    MAX_CHANNEL (int):  Maximum Channel the TV can be set to
    """
    MIN_VOLUME = 0
    MAX_VOLUME = 2
    MIN_CHANNEL = 0
    MAX_CHANNEL = 3

    def __init__(self) -> None:
        """
        Method that creates an initial Television object / remote settings.

        Attributes
        status (bool): Power status of the Television
        muted (bool) : Mute status of the Television
        volume (int): Volume of the Television
        channel (int): Channel on the Television
        stored_volume (int): Stored volume of the Television when muted
        """
        self.__status: bool = False
        self.__muted: bool = False
        self.__volume: int = Television.MIN_VOLUME
        self.__channel: int = Television.MIN_CHANNEL
        self.__stored_volume: int = 0

    def power(self) -> None:
        """
        Method that powers the television on and off.
        """
        if self.__status:
            self.__status = False
        else:
            self.__status = True

    def mute(self) -> None:
        """
        Method that mutes the television and stores the current volume.
        """
        if self.__status:
            if self.__muted:
                self.__muted = False
                self.__volume = self.__stored_volume
            else:
                self.__muted = True
                self.__stored_volume = self.__volume
                self.__volume = Television.MIN_VOLUME

    def channel_up(self) -> None:
        """
        Method that channels up the television. If on highest channel, will go to the lowest channel.
        """
        if self.__status:
            if self.__channel == Television.MAX_CHANNEL:
                self.__channel = Television.MIN_CHANNEL
            else:
                self.__channel += 1

    def channel_down(self) -> None:
        """
        Method that channels down the television. If on lowest channel, will go to the highest channel.
        """
        if self.__status:
            if self.__channel > Television.MIN_CHANNEL:
                self.__channel -= 1
            else:
                self.__channel = Television.MAX_CHANNEL

    def volume_up(self) -> None:
        """
        Method that volumes up the television. If the TV is muted, turn the mute off and restore volume.
        """
        if self.__status:
            if self.__muted:
                self.__volume = self.__stored_volume
                self.__muted = False
            if self.__volume < Television.MAX_VOLUME:
                self.__volume += 1

    def volume_down(self) -> None:
        """
        Method that volumes down the television. If muted, turn the mute off and restore volume.
        """
        if self.__status:
            if self.__muted:
                self.__volume = self.__stored_volume
                self.__muted = False
            if self.__volume > Television.MIN_VOLUME:
                self.__volume -= 1

    def __str__(self) -> str:
        """
        Method that returns a string of the television settings.
        :return: A string of the television settings.
        """
        return f"Power = {self.__status}, Channel = {self.__channel}, Volume = {self.__volume}"
