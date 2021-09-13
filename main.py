import requests
import json

URL = 'https://www.googleapis.com/youtube/v3/'

# 自身のGoogle Cloud PlatformからAPIキーを取得
API_KEY = 'your key'


# video_idは"https://www.youtube.com/watch?v=eKw0X-aklqc&list=PLDKkKPYyoB3Aq1JRgay1kNNLvsdtayZlb"の?v=???&の???の部分
def print_video_comment(video_id, n=1, next_page_token=None):
    params = {
        'key': API_KEY,
        'part': 'snippet',
        'videoId': video_id,
        'order': 'relevance',
        'textFormat': 'plaintext',
        'maxResults': n,
        'pageToken': next_page_token,
    }
    response = requests.get(URL + 'commentThreads', params=params)
    return response.json()


pageToken = None

while True:
    resource = print_video_comment('eKw0X-aklqc', 100, pageToken)
    comments = resource["items"]
    for comment in comments:
        # コメント
        text = comment['snippet']['topLevelComment']['snippet']['textDisplay']
        # グッド数
        like_cnt = comment['snippet']['topLevelComment']['snippet']['likeCount']
        # 返信数
        reply_cnt = comment['snippet']['totalReplyCount']

        print('{}\nグッド数: {} 返信数: {}\n'.format(text, like_cnt, reply_cnt))

    print('総コメント数 : {}'.format(len(comments)))

    if "nextPageToken" in resource:
        pageToken = resource["nextPageToken"]
    else:
        break
