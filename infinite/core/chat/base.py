#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
    @Date   : 2025/5/22 9:52
    @Author : chairc
    @Site   : https://github.com/chairc
"""
from abc import ABC, abstractmethod


class BaseChat(ABC):
    """
    Base chat class
    """

    def __init__(self, messages: list = None, history: bool = False, configs: dict = None, save_history: bool = True,
                 **kwargs):
        """
        Init base chat
        :param messages: History messages list
        :param history: Chat with history, this is a loading history messages flag, not save history messages flag
        :param configs: Model all configuration information
        :param save_history: Save history messages flag, if True, the chat will save history messages
                             (this is not the same as history parameter)
        :param kwargs: Other parameters
        """
        if history is True and isinstance(messages, list):
            self.messages = messages
        else:
            self.messages = []
        self.history = history
        self.configs = configs
        self.save_history = save_history
        self.use_stream = self.check_is_stream()

    def check_is_stream(self):
        """
        Check if the model supports streaming
        :return: True if the model supports streaming, False otherwise
        """
        return self.configs["stream"]

    @abstractmethod
    def chat(self, user_input: str, **kwargs):
        """
        Base chat
        :param user_input: User input message
        :return: None
        """
        pass

    @abstractmethod
    def chat_async(self, user_input: str, **kwargs):
        """
        Base async chat
        :param user_input: User input message
        :return: None
        """
        pass

    @abstractmethod
    def save_history_messages(self, current_message: dict):
        """
        Save history messages
        :param current_message: Current message to save
        :return: None
        """
        pass
