#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2023/3/28 17:26
# @Author  : HYG

from flask_login import UserMixin
from app.models.base import Base
from sqlalchemy import Column, Integer, String
from werkzeug.security import generate_password_hash, check_password_hash
from authlib.jose import jwt
from datetime import datetime, timedelta
from flask import current_app
from app import login_manager


class User(UserMixin, Base):
    __tablename__ = 't_user'
    id = Column(Integer, primary_key=True)
    user_name = Column(String(24), nullable=False)
    phone_number = Column(String(18), unique=True)
    _password = Column('password', String(128), nullable=False)
    email = Column(String(50), unique=True, nullable=False)
    dpmt = Column(String(50))
    wx_open_id = Column(String(50))
    wx_name = Column(String(32))

    @property
    def password(self):
        return self._password

    @password.setter
    def password(self, raw):
        self._password = generate_password_hash(raw)

    def check_password(self, raw):
        return check_password_hash(self._password, raw)

    def generate_token(self):
        now = datetime.utcnow()
        payload = {
            'sub': self.id,
            'iat': now,
            'exp': now + timedelta(minutes=30)
        }
        secret_key = current_app.config['SECRET_KEY']
        token = jwt.encode({'alg': 'HS256', 'typ': 'JWT'}, payload, secret_key)
        return token.decode('utf-8')

    @staticmethod
    def verify_token(token):
        try:
            secret_key = current_app.config['SECRET_KEY']
            header = {'alg': 'HS256', 'typ': 'JWT'}
            payload = jwt.decode(token, secret_key, header_fields=['alg', 'typ'])
            user_id = payload['sub']
            user = User.query.get(user_id)
            return user
        except Exception as e:
            return None

    @property
    def summary(self):
        return dict(
            nickname=self.nickname,
            beans=self.beans,
            email=self.email,
            send_receive=str(self.send_counter) + '/' + str(self.receive_counter)
        )


@login_manager.user_loader
def get_user(uid):
    return User.query.get(int(uid))
