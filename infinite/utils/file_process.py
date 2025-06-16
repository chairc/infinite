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
    try:
        with open(file=file_path, mode="r", encoding="utf-8") as file:
            yaml_config = yaml.safe_load(file)
        return yaml_config
    except yaml.YAMLError as e:
        if hasattr(e, "problem_mark"):
            mark = e.problem_mark
            error_msg = f"YAML format error (line {mark.line + 1}, column {mark.column + 1}): {e}"
        else:
            error_msg = f"YAML format error: {str(e)}"
        raise yaml.YAMLError(error_msg)
    except Exception as e:
        raise Exception(f"Error occurred while reading the file: {str(e)}")
