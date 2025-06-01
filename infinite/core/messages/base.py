#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
    @Date   : 2025/6/1 17:15
    @Author : chairc
    @Site   : https://github.com/chairc
"""
from abc import ABC, abstractmethod


class BaseMessage(ABC):
    def __init__(self, **kwargs):
        """
        Initialize the base message
        """
        pass

    @abstractmethod
    def create_message(self, **kwargs):
        """
        Create a message dictionary
        """
        pass

    @abstractmethod
    def to_dict(self):
        """
        Convert the message to a dictionary
        """
        pass
