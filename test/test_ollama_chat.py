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


class TestOllamaChat(TestCase):
    def test_chat(self):
        try:
            yaml_config = load_ollama_yaml_config(file_name="ollama_chat_qwen3_1.7b.yml", file_type="chat")
            ollama_chat = OllamaChat(messages=None, history=False, configs=yaml_config)
            message = ollama_chat.chat(user_input="Hello, how are you?")
            print(message.role)
            print(message.content)
        except Exception():
            self.fail()

    def test_chat_async(self):
        async def main():
            yaml_config = load_ollama_yaml_config(file_name="ollama_chat_qwen3_1.7b.yml", file_type="chat")
            ollama_chat = OllamaChat(messages=None, history=False, configs=yaml_config)
            async for part in ollama_chat.chat_async(user_input="Hello, how are you?"):
                print(part)

        try:
            asyncio.run(main())
        except Exception():
            self.fail()

    def test_chat_load_yaml_config(self):
        yaml_config = load_ollama_yaml_config(file_name="ollama_chat_qwen3_1.7b.yml", file_type="chat")
        print(yaml_config)
