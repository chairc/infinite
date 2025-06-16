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

    def __init__(self, user_input: str, messages: list, history: bool, configs: dict, **kwargs):
        """
        Init base chat
        :param user_input: User input message
        :param messages: History messages list
        :param history: Chat with history
        :param configs: Model all configuration information
        :param kwargs: Other parameters
        """
        if history is True:
            self.messages = messages
        else:
            self.messages = None
        self.user_input = user_input
        self.history = history
        self.configs = configs
        self.use_stream = self.check_is_stream()

    def check_is_stream(self):
        """
        Check if the model supports streaming
        :return: True if the model supports streaming, False otherwise
        """
        return self.configs["stream"]

    @abstractmethod
    def chat(self):
        """
        Base chat
        :return: None
        """
        pass

    @abstractmethod
    def chat_async(self):
        """
        Base async chat
        :return: None
        """
        pass
