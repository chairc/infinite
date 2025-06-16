#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
    @Date   : 2025/5/19 21:17
    @Author : chairc
    @Site   : https://github.com/chairc
"""
import os

from infinite.utils.check import check_is_valid_yaml_file
from infinite.utils.file_process import load_yaml


def load_ollama_yaml_config(file_name: str, file_type: str):
    """
    Load ollama yaml config file
    :param file_name: The yaml file name
    :param file_type: The yaml file type, such as chat, generate...
    :return: The yaml params
    """
    # Paths are matched based on name
    current_path = os.path.dirname(p=os.path.abspath(__file__))
    yml_path = os.path.join(current_path, file_type, file_name)
    # Check the current file path
    if check_is_valid_yaml_file(file_path=yml_path):
        # Gets the current file path
        ollama_yml = load_yaml(file_path=yml_path)
        return ollama_yml
    else:
        raise FileNotFoundError(f"File: {yml_path} is not found.")
