#!/usr/bin/env python
#-*-coding: utf-8 -*-
"""
@version: 0.1
@author:linyl
@file: db.py
@time: 2018/9/29 15:33
"""

from sqlalchemy import create_engine, MetaData
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

engine = create_engine('mysql+mysqldb://root:root123@localhost:3306/test?charset=utf8',
                       pool_size=1,
                       max_overflow=10,
                       echo=False,
                       encoding='utf-8',
                       pool_recycle=20000)
Session = sessionmaker(bind=engine)
