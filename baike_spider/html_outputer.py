#!/usr/bin/env python
#-*-coding: utf-8 -*-
"""
@version: 0.1
@author:linyl
@file: html_outputer.py
@time: 2018/9/20 21:56
"""


class HtmlOutputer(object):
    def __init__(self):
        self.datas = []

    def collect_data(self, data):
        if data is None:
            return
        self.datas.append(data)

    def output_html(self):
        fout = open('output.html','w')
        fout.write('<html>')
        fout.write('<body>')
        fout.write('<table>')

        #ascii
        for data in self.datas:
            fout.write('<tr>')
            fout.write('<td>%s</td>'%data['url'])
            fout.write('<td>%s</td>'%data['title'].encode('utf-8'))
            fout.write('<td>%s</td>'%data['summary'].encode('utf-8'))
            fout.write('</tr>')
        fout.write('</table>')
        fout.write('</body>')
        fout.write('</html>')

        fout.close()