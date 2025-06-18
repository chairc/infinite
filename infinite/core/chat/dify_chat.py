#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
    @Date   : 2025/5/22 11:00
    @Author : chairc
    @Site   : https://github.com/chairc
"""
from infinite.core.chat.base import BaseChat


class DifyChat(BaseChat):
    """
    Dify chat class
    """

    def __init__(self, **kwargs):
        """
        Init Dify chat
        """
        super().__init__(**kwargs)

    def chat(self, user_input: str | dict, **kwargs):
        pass

    async def chat_async(self, user_input: str | dict, **kwargs):
        pass

    def save_history_messages(self, current_message: dict):
        pass
