#!/usr/bin/env python
#-*-coding: utf-8 -*-
"""
@version: 0.1
@author:linyl
@file: html_parser.py
@time: 2018/9/20 21:55
"""
import re
import urlparse

from bs4 import BeautifulSoup


class HtmlParser(object):
    def parse(self, page_url, html_cont):
        if page_url is None or html_cont is None:
            return
        soup =BeautifulSoup(html_cont, 'html.parser',from_encoding='utf-8')
        new_urls = self._get_new_urls(page_url,soup)
        new_data = self._get_new_data(page_url,soup)
        return new_urls,new_data

    def _get_new_urls(self, page_url, soup):
        new_urls = set()
        # /item/123.html
        links = soup.find_all('a',href=re.compile(r'/item/\d+\.html'))
        for link in links:
            new_url = link['href']
            new_full_url = urlparse.urljoin(page_url,new_url)
            print(new_full_url)
            new_urls.add(new_full_url)
        return new_urls

    def _get_new_data(self, page_url, soup):
        res_data = {}
        """<dd class="lemmaWgt-lemmaTitle-title">
                <h1>Python</h1>
                <h2>（计算机程序设计语言）</h2>
                <a href="javascript:;" class="edit-lemma cmn-btn-hover-blue cmn-btn-28 j-edit-link" style="display: inline-block;"><em class="cmn-icon wiki-lemma-icons wiki-lemma-icons_edit-lemma"></em>编辑</a>
                <a class="lock-lemma" nslog-type="10003105" target="_blank" href="/view/10812319.htm" title="锁定"><em class="cmn-icon wiki-lemma-icons wiki-lemma-icons_lock-lemma"></em>锁定</a>
            </dd>
        """
        title_node = soup.find('dd',class_="lemmaWgt-lemmaTitle-title").find('h1')
        res_data['title'] = title_node.get_text()

        """<div class="lemma-summary" label-module="lemmaSummary">
                <div class="para" label-module="para">Python 是一个有条理的和强大的面向对象的程序设计语言，类似于Perl, Ruby, Scheme, 或 Java.</div>
            </div>
        """
        summary_node = soup.find('div',class_='lemma-summary')
        res_data['summary'] = summary_node.get_text()
        res_data['url'] = page_url
        return res_data
