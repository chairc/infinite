#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
    @Date   : 2025/5/19 21:55
    @Author : chairc
    @Site   : https://github.com/chairc
"""
import os
import sys

import logging
import coloredlogs

from fastapi import APIRouter

sys.path.append(os.path.dirname(sys.path[0]))
logger = logging.getLogger(__name__)
coloredlogs.install(level="INFO")
router = APIRouter(tags=["chat_api"], responses={404: {"description": "Not found"}})


@router.get("/")
def index():
    return "Hello, Chat API!"


@router.get("/chat")
async def chat():
    return "Chat chat chat~"
