#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
    @Date   : 2025/5/22 14:55
    @Author : chairc
    @Site   : https://github.com/chairc
"""
import yaml


def load_yaml(file_path):
    """
    Load YAML file
    :param file_path: Path to the YAML file
    :return: Loaded data
    """
    with open(file=file_path, mode="r", encoding="utf-8") as file:
        yaml_config = yaml.safe_load(file)
    return yaml_config
