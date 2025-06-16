#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
    @Date   : 2025/6/16 08:57
    @Author : chairc
    @Site   : https://github.com/chairc
"""
import os

import yaml
import logging
import coloredlogs

logger = logging.getLogger(__name__)
coloredlogs.install(level="INFO")


def check_is_valid_yaml_file(file_path):
    """
    Check the file is valid yaml file
    :param file_path: The yaml file path
    :return: Boolean
    """
    # Check if the file exists
    if not os.path.exists(file_path):
        logger.error(msg=f"File does not exist: {file_path}")
        return False

    # Check the file extension
    _, ext = os.path.splitext(file_path)
    if ext.lower() not in (".yml", ".yaml"):
        logger.error(msg=f"File extension must be .yml or .yaml, current extension is {ext}")
        return False
    # Check successful
    return True
