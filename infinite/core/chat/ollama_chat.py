#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
    @Date   : 2025/5/22 9:50
    @Author : chairc
    @Site   : https://github.com/chairc
"""
import ollama

from infinite.core.chat.base import BaseChat


class OllamaChat(BaseChat):
    """
    Ollama chat class
    """

    def __init__(self, **kwargs):
        """
        Init ollama chat
        """
        super().__init__(**kwargs)

    def return_ollama_response_data(self, response):
        """
        Return response data
        :param response: Ollama chat response data
        :return: Stream data or no stream data
        """
        # Stream
        if self.use_stream is True:
            for chunk in response:
                yield chunk.message.content
        else:
            return response.message.content

    def chat(self):
        """
        Ollama default chat
        :return: Stream data or no stream data
        """
        # Chat
        response = ollama.chat(
            model=self.configs["model"],
            messages=[*self.messages, {"role": "user", "content": self.user_input}],
            stream=self.use_stream,
            format=self.configs["format"],
            keep_alive=self.configs["keep_alive"],
        )
        return self.return_ollama_response_data(response=response)

    async def chat_async(self):
        """
        Ollama async chat client, work with asyncio
        :return: Stream data or no stream data
        """
        response = await ollama.AsyncClient().chat(
            model=self.configs["model"],
            messages=[*self.messages, {"role": "user", "content": self.user_input}],
            stream=self.use_stream,
            format=self.configs["format"],
            keep_alive=self.configs["keep_alive"],
        )
        return self.return_ollama_response_data(response=response)
