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


YOUTUBE_URL = 'https://www.youtube.com/results?search_query='


def video_url_crawling():

        data = []
        keyword = input('Keyword : ')

        driver = wd.Chrome('./tool/chromedriver.exe')
        driver.maximize_window()

        driver.get(YOUTUBE_URL+keyword)


        print('The scrolling starts moving to the bottom of the main page.')
        body = driver.find_element_by_tag_name("body")

        while True:

            ### id = '#message' 에 해당하는 값을 가져옴.
            ### 유튜브에서는 id = '#message'는 scoll을 맨 끝까지 내렸을 때 나타나는 값임.
            items=driver.find_elements_by_css_selector('#message')

            ### scroll을 끝까지 내렸다면 반복문 탈출
            if(len(items)):
                break
            body.send_keys(Keys.PAGE_DOWN)

            ### 로딩 시간 기다림
            time.sleep(0.1)
            
        print('Arrived at the end of the main page')
        print('Start to get the url of the video')
        
        ### 동영상 제목, url을 가지고 있는 class를 가져옴.
        items = driver.find_elements_by_css_selector('#video-title')

        for idx in items:
            if(idx.get_attribute('href') is not None):
                ### 한글 깨짐 방지
                text = idx.text

                for i in range(len(text)):
                    if not ((0 <= ord(text[i]) < 128) or (0xac00 <= ord(text[i]) <= 0xd7af)):
                        text = text.replace(text[i], ' ')
                data.append([text, idx.get_attribute('href')])

        driver.close()

        print('Finish previous working')
        print('The data is being written to the csv file.')
        
        ### csv 파일에 저장 [동영상 제목, 동영상 url]
        dataframe = pd.DataFrame(data, columns=["title", "url"])
        dataframe.to_csv('../data/youtube_url_collection.csv', encoding='cp949')
        
        print('Finish working')        
        

def video_comment_crawling():
    data = []
    df = pd.read_csv('../data/youtube_url_collection.csv', encoding = 'cp949')

    driver = wd.Chrome('./tool/chromedriver.exe')
    driver.maximize_window()

    temporary_storage_num = 1
    for i in range(len(df.index)):
        title = df['title'][i]
        link = df['url'][i]

        print(f'Start comment crawling : title = {title}')
              
        driver.get(link)
        time.sleep(2)

        count = 0
        body = driver.find_element_by_tag_name("body")

        print('The scrolling starts moving to the bottom of the comment page.')
        
        ### 댓글 데이터를 가져옴
        last = driver.find_elements_by_css_selector('#content-text')

        while True:
            body.send_keys(Keys.PAGE_DOWN)
            time.sleep(0.4)
            new = driver.find_elements_by_css_selector('#content-text')

            if new == last:
                if count == 10:
                    break
                count += 1

            else:
                count = 0

            last = new
            
        print('Arrived at the end of the comment page')
        
        for idx in new:
            ### 한글 깨짐 방지
            text = idx.text

            for idx in range(len(text)):
                if not ((0 <= ord(text[idx]) < 128) or (0xac00 <= ord(text[idx]) <= 0xd7af)):
                    text = text.replace(text[idx], ' ')

            data.append([title, text])
            
        if temporary_storage_num % 100 == 0:
            dataframe = pd.DataFrame(data, columns=["title", "content"])
            dataframe.to_csv('../data/youtube_comment.csv', mode = 'a', encoding='cp949')
            data = []
            
        temporary_storage_num += 1

        
    driver.close()
    print('Finish comment crawling')
    print('The data is being written to the csv file.')
    
    ### 댓글 정보를 csv 파일에 저장
    dataframe = pd.DataFrame(data, columns=["title", "content"])
    dataframe.to_csv('../data/youtube_comment.csv', mode = 'a', encoding='cp949')

    print('Finish working')

