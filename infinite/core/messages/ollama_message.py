#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
    @Date   : 2025/6/1 17:07
    @Author : chairc
    @Site   : https://github.com/chairc
"""
import json

from infinite.core.messages.base import BaseMessage


class OllamaMessage(BaseMessage):
    """
    Ollama class for messages
    This class is used to define the basic structure of messages
    """

    def __init__(self, role: str = None, content: str = None, thinking: bool = None, images: list = None,
                 tool_calls: list = None, **kwargs):
        """
        Initialize the ollama message with a role and content
        Detail information please visit https://github.com/ollama/ollama/blob/main/docs/api.md
        Ollama messages format, used to initialize as a standard template
        :param role: The role of the message sender (e.g., "user", "assistant")
        :param content: The content of the message
        :param thinking: The model's thinking process, if the model is thinking model
        :param images: A list of images to include in the message
        :param tool_calls: A list of tools in JSON that the model wants to use
        """
        super().__init__(**kwargs)
        self.role = role
        self.content = content
        self.thinking = thinking
        self.images = images
        self.tool_calls = tool_calls
        self.history_messages = []

    def create_message(self, role: str, content: str, thinking: bool = None, images: list = None,
                       tool_calls: list = None):
        """
        Create a message dictionary
        :return: A dictionary representation of the message
        """
        if not isinstance(role, str) or not isinstance(content, str):
            raise ValueError("Role and content must be strings")
        if not role or not content:
            raise ValueError("Role and content cannot be empty")
        self.role = role
        self.content = content
        self.thinking = thinking
        self.images = images
        self.tool_calls = tool_calls
        return self.to_dict()

    def save_history_messages(self, current_message: dict):
        """
        Save a history message from a dictionary format
        :param current_message: A dictionary containing the message details
        :return: History messages list
        """
        if not isinstance(current_message, dict):
            raise ValueError("Message must be a dictionary")
        if "role" not in current_message or "content" not in current_message:
            raise ValueError("Message must contain 'role' and 'content'")
        self.history_messages.append(current_message)
        return self.history_messages

    def to_dict(self):
        """
        Convert the message to a dictionary format
        :return: A dictionary representation of the message
        """
        # New dictionary
        dict_params = {}
        # The params must be set
        dict_params.update({"role": self.role, "content": self.content})
        # The optional params
        if self.thinking is not None:
            dict_params.update({"thinking": self.thinking})
        if self.images is not None:
            dict_params.update({"images": self.images})
        if self.tool_calls is not None:
            dict_params.update({"tool_calls": self.tool_calls})
        return dict_params


if __name__ == "__main__":
    # Example usage
    print("============================ Example 1 ============================")
    # Init a new OllamaMessage
    init_message = OllamaMessage()
    # Output: {'role': None, 'content': None}
    print(init_message.to_dict())
    init_user_message = init_message.create_message(role="system", content="This is init message.")
    print(init_user_message)
    init_message.save_history_messages(init_user_message)
    print(init_message.history_messages)

    # System call
    print("============================ Example 2 ============================")
    # Creating an OllamaMessage instance and using its methods
    message = OllamaMessage(role="system", content="You are a friendly bot.")
    # Output: {'role': 'system', 'content': 'You are a friendly bot.'}
    print(message.to_dict())
    # Saving the message to history
    message.save_history_messages(message.to_dict())

    # User call
    # Creating a user message
    user_message = message.create_message(role="user", content="Hello, how are you?", images=["image1"])
    # Output: {'role': 'user', 'content': 'Hello, how are you?', image: ['image1']}
    print(user_message)
    # Saving the message to history
    message.save_history_messages(user_message)

    # Assistant call
    # Creating a new message
    assistant_message = message.create_message(role="assistant", content="I am fine, thank you!")
    # Output: {'role': 'assistant', 'content': 'I am fine, thank you!'}
    print(assistant_message)
    # Saving the new message to history
    message.save_history_messages(assistant_message)
    # Output: [{'role': 'system', 'content': 'You are a friendly bot.'}, {'role': 'user', 'content': 'Hello, how are you?', 'images': ['image1']}, {'role': 'assistant', 'content': 'I am fine, thank you!'}]
    print(message.history_messages)
