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


TWITTER_URL = 'https://twitter.com/search?l=&q='


def crawling():
    data = []
    keyword = input('Keyword : ')

    driver = wd.Chrome('./tool/chromedriver.exe')
    driver.maximize_window()

    driver.get(TWITTER_URL + keyword)

    print('The scroll is starting to move bottom')

    # 페이지 스크롤을 끝날 때까지 계속 내림
    # 스크롤을 내리기 전의 화면 높이와 내렸을 때의 화면 높이가 같다면 더 이상 내려갈 곳이 없다는 의미이므로 무한 루프를 탈출함.
    last_height = driver.execute_script("return document.body.scrollHeight")
    while True:
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")
        time.sleep(1)
        new_height = driver.execute_script("return document.body.scrollHeight")
        
        if new_height == last_height:
            # Wait to load page
            time.sleep(1)
            new_height = driver.execute_script("return document.body.scrollHeight")
            
            if(new_height == last_height):
                break

        last_height = new_height
    print('Arrived at the end of the page')
    print('Start twitter crawling')
    soup = BeautifulSoup(driver.page_source, 'html.parser')

    # 트위터의 게시글에는 각각의 고유의 아이디가 있어서 트위터 사이트에서 모든 게시글 아이디를 리스트형으로 가져옴
    pattern = re.compile('stream-item-tweet-\d+')
    items = pattern.findall(str(soup))
    for item in items:
        # 위에서 가져온 고유 아이디를 이용하여 게시글 본문을 css selector를 이용하여 가져
        text = driver.find_element_by_css_selector('#'+ item +' > div > div.content > div.js-tweet-text-container > p').text

        # 특수기호를 없애는 작
        for idx in range(len(text)):
            if not ((0 <= ord(text[idx]) < 128) or (0xac00 <= ord(text[idx]) <= 0xd7af)):
                text = text.replace(text[idx], ' ')

        data.append(text)

    driver.close()
    
    print('Finish crawling')
    print('The data is being written to the csv file.')
    dataframe = pd.DataFrame(data, columns=["content"])
    dataframe.to_csv('../data/twitter_comment.csv', mode = 'a', encoding='cp949')
    print('Finish working')

    
