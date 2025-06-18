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

    def _check_chat_user_input_type(self, user_input: str | dict):
        """
        Check the type of user input type
        :param user_input: User input message
        :return: User message
        """
        if isinstance(user_input, str):
            return self.ollama_message.create_message(role="user", content=user_input)
        elif isinstance(user_input, dict):
            return user_input
        else:
            raise TypeError("User input must be a string or a dictionary")

    def chat(self, user_input: str | dict, **kwargs):
        """
        Ollama default chat
        :return: No stream data
        """
        # Chat
        # Create user message input
        user_message = self._check_chat_user_input_type(user_input)
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

    async def chat_async(self, user_input: str | dict, **kwargs):
        """
        Ollama async chat client, work with asyncio
        :return: Stream data
        """
        # Create user message input
        user_message = self._check_chat_user_input_type(user_input)
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

    def save_history_messages(self, current_message: dict):
        """
        Save history messages
        :param current_message: Current message to save
        :return: None
        """
        # Save the current message to history messages
        self.messages.append(current_message)
        if self.save_history:
            # TODO: Update the OllamaMessage class to save history messages in database or file
            pass
        return self.messages
