#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2023/3/28 17:20
# @Author  : HYG
from wtforms import Form, StringField, PasswordField
from wtforms.validators import Length, DataRequired, Email, ValidationError
from app.models.user import User


class LoginForm(Form):
    username = StringField(validators=[DataRequired(), Length(8, 64)])
    password = PasswordField(validators=[
        DataRequired(message='密码不可以为空，请输入你的密码'), Length(6, 32)])


class RegisterForm(Form):
    user_name = StringField(validators=[DataRequired(),
                                        Length(8, 64, message='姓名至少8个字符，最多64个字符')])
    phone_number = StringField(validators=[DataRequired(),
                                           Length(8, 64, message='姓名至少8个字符，最多64个字符')])
    email = StringField(validators=[DataRequired(), Length(8, 64),
                                    Email(message='电子邮箱不符合规范')])

    password = PasswordField(validators=[
        DataRequired(message='密码不可以为空，请输入你的密码'), Length(6, 32)])

    def validate_email(self, field):
        # db.session.
        if User.query.filter_by(email=field.data).first():
            raise ValidationError('电子邮件已被注册')
