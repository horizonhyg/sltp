#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2023/3/29 14:14
# @Author  : HYG
from flask import Blueprint
from flask import render_template

web = Blueprint('web', __name__)


@web.app_errorhandler(404)
def not_found(e):
    # AOP 思想
    return render_template('404.html'), 404


from app.web import auth
from app.web import main
