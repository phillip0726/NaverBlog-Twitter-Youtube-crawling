# NaverBlog-Twitter-Youtube-crawler


## Functions
- Menu 1 : Naver Blog crawling
- Menu 2 : Youtube comment crawling
- Menu 3 : Twitter posts crawling

### Menu 1 (Naver Blog)
- You have to enter the keyword.
- After enter the keywork, you have to enter the number of page to crawl.
- This program only crawls blog preview content.
- The data is stored in a csv file named 'naver_comment.csv'

### Menu 2 (Youtube comment)
- You have to enter the keyword.
- First step, crawls the URL of all videos for that keyword.
- The data is stored in a csv file named 'youtube_url_collection.csv'
- Second step, read 'youtube_url_collection.csv' file.
- Third step, access all URLs and crawl all comments, stored in a csv file named 'youtube_comment.csv'

### Menu 3 (Twitter posts)
- You have to enter the keyword.
- Search for that keyword on Twitter, and crawl all posts.
- The data is stored in a csv file named 'twitter_comment.csv'
