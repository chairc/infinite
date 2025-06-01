#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
    @Date   : 2025/6/1 17:07
    @Author : chairc
    @Site   : https://github.com/chairc
"""
from infinite.core.messages.base import BaseMessage


class OllamaMessage(BaseMessage):
    """
    Ollama class for messages
    This class is used to define the basic structure of messages
    """

    def __init__(self, role: str, content: str, **kwargs):
        """
        Initialize the ollama message with a role and content
        :param role: The role of the message sender (e.g., "user", "assistant")
        :param content: The content of the message
        """
        super().__init__(**kwargs)
        self.role = role
        self.content = content
        self.history_messages = []

    def create_message(self, role: str, content: str):
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
        return self.history_messages.append(current_message)

    def to_dict(self):
        """
        Convert the message to a dictionary format
        :return: A dictionary representation of the message
        """
        return {
            "role": self.role,
            "content": self.content
        }


if __name__ == "__main__":
    # Example usage
    # Creating an OllamaMessage instance and using its methods
    message = OllamaMessage(role="user", content="Hello, how are you?")
    # Output: {'role': 'user', 'content': 'Hello, how are you?'}
    print(message.to_dict())
    # Saving the message to history
    message.save_history_messages(message.to_dict())
    # Creating a new message
    new_message = message.create_message(role="assistant", content="I'm fine, thank you!")
    # Output: {'role': 'assistant', 'content': "I'm fine, thank you!"}
    print(new_message)
    # Saving the new message to history
    message.save_history_messages(new_message)
    # Output: [{'role': 'user', 'content': 'Hello, how are you?'}, {'role': 'assistant', 'content': "I'm fine, thank you!"}]
    print(message.history_messages)
