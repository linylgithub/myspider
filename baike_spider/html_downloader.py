#!/usr/bin/env python
#-*-coding: utf-8 -*-
"""
@version: 0.1
@author:linyl
@file: html_downloader.py
@time: 2018/9/20 21:55
"""
import urllib2


class HtmlDownLoader(object):
    def download(self, new_url):
        if new_url is None:
            return None
        response = urllib2.urlopen(new_url)

        if response.getcode() != 200:
            return None
        return response.read()