#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2023/3/28 15:48
# @Author  : HYG
from app import create_app

app = create_app()

if __name__ == '__main__':
    app.run(host='127.0.0.1', debug=True)
