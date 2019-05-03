#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
import urllib
import time
import pandas as pd
import re
from pandas import DataFrame, Series
from urllib.request import urlopen
from bs4 import BeautifulSoup
from selenium import webdriver as wd
from selenium.webdriver.common.keys import Keys


NAVER_URL = 'https://section.blog.naver.com/Search/Post.nhn?pageNo=%%PAGE_NUM%%&rangeType=ALL&orderBy=sim&keyword='


def crawling():
    data = []
    BLOG_COUNT_PER_PAGE = 7
    keyword = input('Keyword : ')
    try:
        page_num = int(input('Page Num : '))
    except:
        print('Please press valid page number (int)')
        sys.exit(1)

    driver = wd.Chrome('./tool/chromedriver.exe')
    driver.maximize_window()

    _const_title_selector = '#content > section > div.area_list_search > div:nth-child(%%BLOG_NUM%%) > div > div.info_post > div > a.desc_inner > strong > span.title'
    _const_content_selector = '#content > section > div.area_list_search > div:nth-child(%%BLOG_NUM%%) > div > div.info_post > div > a.text'

    temporary_storage_num = 1
    for PAGE_NUM in range(page_num + 1):
        print(f'Start crawling page {PAGE_NUM}')
        link = NAVER_URL.replace('%%PAGE_NUM%%', str(PAGE_NUM)) + keyword
        driver.get(link)
        time.sleep(2)
        for BLOG_NUM in range(1, BLOG_COUNT_PER_PAGE + 1):
            title_selector = _const_title_selector.replace('%%BLOG_NUM%%',str(BLOG_NUM))
            content_selector = _const_content_selector.replace('%%BLOG_NUM%%', str(BLOG_NUM))
            
            title  = driver.find_element_by_css_selector(title_selector).text
            content = driver.find_element_by_css_selector(content_selector).text

            for idx in range(len(title)):
                if not ((0 <= ord(title[idx]) < 128) or (0xac00 <= ord(title[idx]) <= 0xd7af)):
                    title = title.replace(title[idx], ' ')
                    
            for idx in range(len(content)):
                if not ((0 <= ord(content[idx]) < 128) or (0xac00 <= ord(content[idx]) <= 0xd7af)):
                    content = content.replace(content[idx], ' ')

            data.append([title, content])

        if temporary_storage_num % 100 == 0:
            dataframe = pd.DataFrame(data, columns=["title", "url"])
            dataframe.to_csv('./naver_comment.csv', mode='a', encoding='cp949')
            data = []
            
        temporary_storage_num += 1
  
    driver.close()
        
    print('Finish crawling')
    print('The data is being written to the csv file.')
    dataframe = pd.DataFrame(data, columns=["title", "url"])
    dataframe.to_csv('./naver_comment.csv', mode='a', encoding='cp949')       
    print('Finish working')

    
