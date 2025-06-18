#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
    @Date   : 2025/5/22 10:29
    @Author : chairc
    @Site   : https://github.com/chairc
"""
import asyncio

from unittest import TestCase

from infinite.configs import load_ollama_yaml_config
from infinite.core.chat.ollama_chat import OllamaChat
from infinite.core.messages.ollama_message import OllamaMessage


class TestOllamaChat(TestCase):
    def __init__(self):
        super().__init__()
        self.ollama_file_name = "ollama_chat_qwen3_1.7b.yml"
        self.ollama_file_type = "chat"

    def test_chat(self):
        try:
            yaml_config = load_ollama_yaml_config(file_name=self.ollama_file_name, file_type=self.ollama_file_type)
            ollama_chat = OllamaChat(messages=None, history=False, configs=yaml_config)
            print("--------------------- user_input set to string ---------------------")
            # user_input set to string, role is user by default
            message = ollama_chat.chat(user_input="Hello, how are you?")
            print(message.role)
            print(message.content)
            # user_input set to dict
            print("--------------------- user_input set to dict ---------------------")
            user_input = {
                "role": "user",
                "content": "Hello, how are you?"
            }
            message = ollama_chat.chat(user_input=user_input)
            print(message.role)
            print(message.content)
            # user_input set to OllamaMessages dict 1
            print("--------------------- user_input set to OllamaMessages dict 1 ---------------------")
            message = ollama_chat.chat(user_input=OllamaMessage(role="user", content="Hello, how are you?").to_dict())
            print(message.role)
            print(message.content)
            # user_input set to OllamaMessages dict 2
            print("--------------------- user_input set to OllamaMessages dict 2 ---------------------")
            message = ollama_chat.chat(
                user_input=OllamaMessage().create_message(role="user", content="Hello, how are you?"))
            print(message.role)
            print(message.content)

        except Exception():
            self.fail()

    def test_chat_history_with_messages(self):
        try:
            yaml_config = load_ollama_yaml_config(file_name=self.ollama_file_name, file_type=self.ollama_file_type)
            history_messages = [
                {
                    "role": "system",
                    "content": "You are a friendly bot."
                },
                {
                    "role": "user",
                    "content": "Hello, my name is chairc. How are you?"
                },
                {
                    "role": "assistant",
                    "content": "I am fine, thank you!"
                }
            ]
            user_input = {
                "role": "user",
                "content": "Do you know what my name is?"
            }
            # Test with history is True
            print("--------------------- Test with history is True ---------------------")
            ollama_chat = OllamaChat(messages=history_messages, history=True, configs=yaml_config)
            message = ollama_chat.chat(user_input=user_input)
            print(message.role)
            print(message.content)

            # Test with history is False
            print("--------------------- Test with history is False ---------------------")
            ollama_chat = OllamaChat(messages=history_messages, history=False, configs=yaml_config)
            message = ollama_chat.chat(user_input=user_input)
            print(message.role)
            print(message.content)

            # Test with history is True and no messages
            print("--------------------- Test with history is True and no messages ---------------------")
            ollama_chat = OllamaChat(history=True, configs=yaml_config)
            message = ollama_chat.chat(user_input=user_input)
            print(message.role)
            print(message.content)

            # Test with history is False and no messages
            print("--------------------- Test with history is False and no messages ---------------------")
            ollama_chat = OllamaChat(history=False, configs=yaml_config)
            message = ollama_chat.chat(user_input=user_input)
            print(message.role)
            print(message.content)
        except Exception():
            self.fail()

    def test_chat_async(self):
        async def main():
            yaml_config = load_ollama_yaml_config(file_name=self.ollama_file_name, file_type=self.ollama_file_type)
            ollama_chat = OllamaChat(messages=None, history=False, configs=yaml_config)
            async for part in ollama_chat.chat_async(user_input="Hello, how are you?"):
                print(part)

        try:
            asyncio.run(main())
        except Exception():
            self.fail()

    def test_chat_load_yaml_config(self):
        yaml_config = load_ollama_yaml_config(file_name=self.ollama_file_name, file_type=self.ollama_file_type)
        print(yaml_config)
