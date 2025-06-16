#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
    @Date   : 2025/5/19 22:59
    @Author : chairc
    @Site   : https://github.com/chairc
"""
import os
import sys

import uvicorn
import logging
import coloredlogs

from fastapi import FastAPI

sys.path.append(os.path.dirname(sys.path[0]))
from infinite.controllers import chat_api

logger = logging.getLogger(__name__)
coloredlogs.install(level="INFO")
app = FastAPI()

# Router running
app.include_router(chat_api.router)

if __name__ == "__main__":
    uvicorn.run(app=app, host="0.0.0.0", port=12345)
