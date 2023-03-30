#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2023/3/30 10:32
# @Author  : HYG

from . import web
from flask import render_template
from flask_login import login_required


@web.route('/')
@login_required
def index():
    return render_template('index.html')
