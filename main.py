#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
import naver_crawler
import youtube_crawler
import twitter_crawler

MAX_MENU = 3
NAVER_CRAWLING = 1
YOUTUBE_CRAWLING = 2
TWITTER_CRAWLING = 3

def menu():
    print('Crawling Program >> Please select menu')
    print('=======================================')
    print('1. Naver Blog Crawling')
    print('2. Youtube Comment Crawling')
    print('3. Twitter Crawling')
    print('=======================================')
    
if __name__ == "__main__":

    menu()
    try:
        menu_num = int(input('Menu : '))

    except :
        print('Please press valid menu number')
        sys.exit(1)
    if(not( 1 <= menu_num <= MAX_MENU)):
        print('Please press valid menu number (1~3)')
        sys.exit(1)


    if(menu_num == NAVER_CRAWLING):
        naver_crawler.crawling()

        
    elif(menu_num == YOUTUBE_CRAWLING):
        #youtube_crawler.video_url_crawling()          # 유튜브에 있는 동영상 제목, url 전부 가져옴
        youtube_crawler.video_comment_crawling()     # 유튜브 각 동영상에 있는 댓글 전부 가져옴
    
    elif(menu_num == TWITTER_CRAWLING):
        twitter_crawler.crawling()
       
