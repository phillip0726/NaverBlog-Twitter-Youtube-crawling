import time
import pandas as pd
from selenium import webdriver as wd
from selenium.webdriver.common.keys import Keys

file_path = './video_text/'
comment_min = 0

def manual():
    print('+--------------------------------------------------------+')
    print('|                                                        |')
    print('| Youtube video -> Text                                  |')
    print('| 1. You must create the file youtube_url_collection.csv |')
    print('|    by running main.py in ../crawler.                   |')
    print('| 2. Simply convert videos without using STT API         |')
    print('| 3. Create a text file in                               |')
    print('|    [video num][title][views][comments] format|         |')
    print('|                                                        |')
    print('+--------------------------------------------------------+')

def commentNum(comment_arr):
    tmp = comment_arr[3:]
    tmp = tmp[:-1]
    tmp = tmp.replace(',','')

    return int(tmp)
    
def convertTEXT(driver, index, title, url):
    
    body = driver.find_element_by_tag_name("body")
    body.send_keys(Keys.PAGE_DOWN)
    time.sleep(2)

    views = driver.find_elements_by_css_selector('#count > yt-view-count-renderer > span.view-count.style-scope.yt-view-count-renderer')[0].text

    # 댓글을 달 수 없는 동영상입니다.
    try:
        comments = driver.find_elements_by_css_selector('#count > yt-formatted-string')[0].text
        comment_num = commentNum(comments)
    except Exception as e:
        comments = '댓글 0개'
        comment_num = 0


    if comment_num >= comment_min:

        title = title.replace('\\','').replace('/','').replace(':','').replace('*','').replace('?','').replace('"','').replace('<','').replace('>','').replace('|','')
        file_name = "(%03d) %s %s %s"%(index, title, views, comments)

        f = open(file_path + file_name + '.txt', 'a')
        
        pattern_tmp = '#body > ytd-transcript-body-renderer > div:nth-child({{idx}}) > div.cues.style-scope.ytd-transcript-body-renderer > div'
        idx = 1
        
        while True:
            try:
                pattern = pattern_tmp.replace('{{idx}}', str(idx))
                text = driver.find_elements_by_css_selector(pattern)[0].text
                if text == '[음악]' or text == '[Music]' or text == '[Applause]' or text == '[박수]' or text == '으' or text == '아':
                    idx += 1
                    continue
                f.write(text + '\n')
                idx += 1
            except Exception as e:
                break

        f.close()


    
if __name__ == '__main__':

    manual()

    print('Read url data...', end='')
    f = pd.read_csv('../data/youtube_url_collection.csv', encoding='cp949')
    print('Finish!')

    
    driver = wd.Chrome('../crawler/tool/chromedriver.exe')
    driver.maximize_window()


    for index, title, url in f.values[60:] :
        print('(video %03d) Start ...' %(index), end='')        
        driver.get(url)
        time.sleep(2)
        try:
            items = driver.find_elements_by_css_selector("#button")

            for item in items:
                if item.get_attribute('aria-label') == '추가 작업':
                    item.click()
                    break

            time.sleep(2)
            driver.find_elements_by_css_selector('#items > ytd-menu-service-item-renderer:nth-child(2) > paper-item')[0].click()        
            time.sleep(2)
            
            convertTEXT(driver, index, title, url)
            
        except Exception as e:
            pass
        print('End!')     
    
    driver.close()
    print('Finish Program!')
