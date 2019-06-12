# NaverBlog-Twitter-Youtube-crawling

## 0. Installing
- How to install

```
- git clone https://github.com/phillip0726/NaverBlog-Twitter-Youtube-crawling.git
- cd NaverBlog-Twitter-Youtube-crawling/
- pip install -r requestments.txt
```

## 1. Functions
> Crawling </br>
> Data Cleaning, extraction </br>
> Youtube video extraction & Convert to mp3 files. </br>

## 2. Crawling
### 2.1 Naver Blog Crawling
```
- You have to enter the keyword.
- After enter the keyword, you have to enter the number of page to crawl.
- This program only crawls blog preview content.
- The data is stored in a csv file named '/data/naver_comment.csv'
```

### 2.2 Youtube Comment Crawling
```
- You have to enter the keyword.
- First step, crawls the URL of all videos for that keyword.
- The data is stored in a csv file named 'youtube_url_collection.csv'.
- Second step, read 'youtube_url_collection.csv' file.
- Third step, access all URLs and crawl all comments, and stored in '/data/youtube_comment.csv'.
```

### 2.3 Twitter Posts Crawling
```
- You have to enter the keyword.
- Search for that keyword on Twitter, and crawl all posts.
- The data is stored in a csv file named '/data/twitter_comment.csv'.
```

## 3. Data Cleaning, extraction
### 3.1 Cleaning
```
- '/data/except_spam.py' perform filtering for the spam keyword.
- The words to be filtered are stored in '/data/except_spam/spam.txt'.
- When '/data/except_spam.py' is executed, refined data is stored in '/data/except_spam/'.
```
### 3.2 Extraction
```
- '/data/filtering_keyword_or.py' perform an OR operation on the input keywords.
- '/data/filtering_keyword_and.py' perform an AND operation on the input keywords.
- When these files are executed, extracted dataes are stored in '/data/include_keyword/'.
```
## 4. Youtube video processing
### 4.1 video -> mp3 file
```
- '/youtube_to_mp3/main.py' perform downloading youtube videos and convert to mp3 files.
- The video url to be downloaded is stored in '/data/youtube_url_collection.csv'.
- If you want to download another videos, add to the list of video URLs in '/data/youtube_url_collection.csv'.
- video/mp3 format : [video/mp3 num] [video/mp3 title]
```

### 4.2 video -> text
```
- '/youtube_to_text/main.py' perform operations similar to the Google STT.
- The video is converted to TEXT and stored in 'video_text'.
```
