import csv
import pandas as pd

def manual():
    print('********The order of execution of this program*******')
    print('1. Read data')
    print('2. Read spam keyword that needs to be removed')
    print('3. Read the data one line at a time and remove it if it contains spam keyword.')
    print('*****************************************************')

    
if __name__ == '__main__':
    
    manual()
    
    # 정제할 단어 목록을 읽음. 단어를 추가하고 싶으면 spam.txt파일 맨 아래에 추가
    filter_f  = open('./except_spam/spam.txt','r', encoding = 'cp949')
    naver_f   = pd.read_csv('./naver_comment.csv', encoding = 'cp949')
    twitter_f = pd.read_csv('./twitter_comment.csv', encoding = 'cp949')

    # 정제할 단어 목록을 리스트형으로 변환함.
    filtering_data = filter_f.read().split('\n')

    print('Start filtering NAVER BLOG')
    data = []
    flag = 1

    # 네이버 블로그 게시글 각각에 대하여 반복문 실행
    for content in naver_f['content'].dropna():
        flag = 1
        for keyword in filtering_data:

            # 어떤 spam keyword 중 하나라도 게시글에 포함되어 있으면 반복문 탈출
            if keyword in content:
                flag = 0
                break
        # 어떤 spam keyword라도 게시글에 포함되지 않았다면 해당 게시글을 따로 저장
        if flag:
            data.append(content)

            
    print('Finish filtering NAVER BLOG')
    print('Start filtering TWITTER POSTS')

    # 트위터 게시글 각각에 대하여 반복문 실행
    for content in twitter_f['content'].dropna():
        flag = 1

        # 어떤 spam keyword 중 하나라도 게시글에 포함되어 있으면 반복문 탈출
        for keyword in filtering_data:
            if keyword in content:
                flag = 0
                break
        # 어떤 spam keyword라도 게시글에 포함되지 않았다면 해당 게시글을 따로 저장
        if flag:
            data.append(content)

    # 네이버 블로그와 트위터를 하나로 합쳐서 한 파일에 저장함
    dataframe = pd.DataFrame(data, columns=['content'])
    dataframe.to_csv('./except_spam/naver_twitter_except_spam.csv', mode= 'w', encoding = 'cp949')


    print('Finish filtering TWITTER POSTS')

    youtube_f = pd.read_csv('./youtube_comment.csv', encoding = 'cp949')
    print('Start filtering YOUTUBE COMMENTS')
    youtube_data = []
    for content in youtube_f['content'].dropna():
        flag = 1
        # 유튜브 댓글 각각에 대하여 반복문 실행
        for keyword in filtering_data:
            # 어떤 spam keyword 중 하나라도 게시글에 포함되어 있으면 반복문 탈출
            if keyword in content:
                flag = 0
                break

        # 어떤 spam keyword라도 게시글에 포함되지 않았다면 해당 게시글을 따로 저장
        if flag:
            youtube_data.append(content)
            data.append(content)

    dataframe = pd.DataFrame(youtube_data, columns=['content'])
    dataframe.to_csv('./except_spam/youtube_except_spam.csv', mode= 'w', encoding = 'cp949')
    dataframe = pd.DataFrame(data, columns=['content'])
    dataframe.to_csv('./except_spam/total_except_spam.csv', mode= 'w', encoding = 'cp949')
            
    print('Finish filtering YOUTUBE COMMENTS')

            
    filter_f.close()
