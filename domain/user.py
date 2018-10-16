#!/usr/bin/env python
#-*-coding: utf-8 -*-
"""
@version: 0.1
@author:linyl
@file: user.py
@time: 2018/9/29 16:05
"""
import logging

from sqlalchemy import Column, BigInteger, String, Table, MetaData

from domain.base import Base, engine
from domain.base import Session

# 绑定元信息
metadata = MetaData(engine)

# 创建表格，初始化数据库
user = Table('user', metadata,
             Column('id', BigInteger, primary_key=True),
             Column('name', String(32), nullable=False),
             Column('password', String(128), nullable=False)
             )
if __name__ == '__main__':
    metadata.create_all(engine)


