#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2023/3/30 8:40
# @Author  : HYG
from werkzeug.security import generate_password_hash

key = generate_password_hash('123DSG123123')
print(key)