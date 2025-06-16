#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
    @Date   : 2025/5/22 9:50
    @Author : chairc
    @Site   : https://github.com/chairc
"""
import ollama

from infinite.core.chat.base import BaseChat
from infinite.core.messages.ollama_message import OllamaMessage


class OllamaChat(BaseChat):
    """
    Ollama chat class
    """

    def __init__(self, **kwargs):
        """
        Init ollama chat
        """
        super().__init__(**kwargs)
        # Init a new OllamaMessage class
        self.ollama_message = OllamaMessage()

    def chat(self, user_input: str, **kwargs):
        """
        Ollama default chat
        :return: No stream data
        """
        # Chat
        # Create user message
        user_message = self.ollama_message.create_message(role="user", content=user_input)
        response = ollama.Client(host=self.configs["server"]).chat(
            model=self.configs["model"],
            messages=[*self.messages, user_message],
            stream=False,
            think=self.configs["think"],
            format=self.configs["format"],
            keep_alive=self.configs["keep_alive"],
            options=self.configs["options"],
        )
        return response.message

    async def chat_async(self, user_input: str, **kwargs):
        """
        Ollama async chat client, work with asyncio
        :return: Stream data
        """
        # Create user message
        user_message = self.ollama_message.create_message(role="user", content=user_input)
        async for part in await ollama.AsyncClient(host=self.configs["server"]).chat(
            model=self.configs["model"],
            messages=[*self.messages, user_message],
            stream=True,
            think=self.configs["think"],
            format=self.configs["format"],
            keep_alive=self.configs["keep_alive"],
            options=self.configs["options"],
        ):
            # print(part.message.role, end="", flush=True)
            # print(part.message.content, end="", flush=True)
            yield part.message
