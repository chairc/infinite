#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
    @Date   : 2025/5/23 22:07
    @Author : chairc
    @Site   : https://github.com/chairc
"""


class R:
    """
    Response class
    Use this class to return a response in the web api
    """

    def __init__(self, code=0, msg="", data=None):
        """
        Response class
        :param code: Response code
        :param msg: Response message
        :param data: Response data

        **Example**::

            >>> R(code=10000, msg="WOW", data={123, 234}).to_dict()
            >>> R().success(msg="111", data="111")
            >>> R().fail(code=400, msg="222")
        """
        self.code = code
        self.msg = msg
        self.data = data

    def success(self, msg="success", data=None):
        """
        Success response
        :param msg: Response message
        :param data: Response data
        :return: Response dictionary
        """
        self.code = 200
        self.msg = msg
        self.data = data
        return self.to_dict()

    def fail(self, code=400, msg="failure", data=None):
        """
        Failure response
        :param code: Response code
        :param msg: Response message
        :param data: Response data
        :return: Response dictionary
        """
        self.code = code
        self.msg = msg
        self.data = data
        return self.to_dict()

    def to_dict(self):
        """
        Convert response to dictionary
        :return: Response dictionary
        """
        return {
            "code": self.code,
            "msg": self.msg,
            "data": self.data
        }


if __name__ == "__main__":
    print(R(code=10000, msg="WOW", data={123, 234}).to_dict())
    print(R(code=10001, msg="DICT", data={"key_0": "value_0", "key_1": "value_1"}).to_dict())
    print(R().success(msg="111", data="111"))
    print(R().fail(code=400, msg="222"))
