import csv
import pandas as pd

def manual():
    print('*****************************************')
    print('1. Input keyword until you enter 0')
    print('2. This program preform OR operation on the keywords')
    print('3. Create three csv files. (naver&&twitter, youtube, total)')
    print('*****************************************')
          
if __name__ == '__main__':

    manual()
    
    keyword = []
    
    # 사용자가 0을 입력하기 전까지 keyword를 계속 입력받는다.
    while True:
        tmp = input('keyword : ')
        if tmp == '0':
            break
        keyword.append(tmp)
        
    print('Read data')

    naver_twitter_f = pd.read_csv('./except_spam/naver_twitter_except_spam.csv', encoding = 'cp949')
    youtube_f = pd.read_csv('./except_spam/youtube_except_spam.csv', encoding = 'cp949')


    print('Finish read data')


    print('Start filtering NAVER BLOG && TWITTER POSTS')
    data = []
   
    for content in naver_twitter_f['content']:

        for i in keyword:
            # 네이버 블로그&&트위터 게시글에 keyword가 하나라도 포함되면 해당 게시글을 따로 저장하고 반복문 탈출
            if i in content:
                data.append(content)
                break
    dataframe = pd.DataFrame(data, columns=['content'])
    dataframe.to_csv('./include_keyword/naver_twitter_include_or_' + keyword[0] + '.csv', mode= 'w', encoding = 'cp949')


    print('Finish filtering NAVER BLOG && TWITTER POSTS')
    print('Start filtering YOUTUBE COMMENTS')

    youtube_data = []
    
    for content in youtube_f['content']:

        for i in keyword:
            if i in content:
                # 유튜브 댓글에 keyword가 하나라도 포함되면 해당 게시글을 따로 저장하고 반복문 탈출                
                youtube_data.append(content)
                data.append(content)
                break
    dataframe = pd.DataFrame(youtube_data, columns=['content'])
    dataframe.to_csv('./include_keyword/youtube_include_or_' + keyword[0] + '.csv', mode= 'w', encoding = 'cp949')
    dataframe = pd.DataFrame(data, columns=['content'])
    dataframe.to_csv('./include_keyword/total_include_or_' + keyword[0] + '.csv', mode= 'w', encoding = 'cp949')
    
    print('Finish filtering YOUTUBE COMMENTS')


