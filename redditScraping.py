#! python3
import praw
import pandas as pd
import datetime as dt

reddit = praw.Reddit(client_id = 'lCw4C-9qu8ok_A',
                    client_secret = 'M1xQOgCu1DBv8cp3RA7lrLKbmiQ',
                    user_agent = 'Scratching_beckRoadmap by /u/andrecodato',
                    username = 'andrecodato',
                    password = 'blackalien30.0')

subreddit = reddit.subreddit('programming')

top_subreddit = subreddit.top(limit=10) # subreddit.top(limit=999) | default = 100
topics_dict = { "title":[],
                "score":[],
                "id":[], "url":[],
                "comms_num":[],
                "created":[],
                "body":[]}

for submission in top_subreddit:
    topics_dict ["title"].append(submission.title)
    topics_dict ["score"].append(submission.score)
    topics_dict ["id"].append(submission.id)
    topics_dict ["url"].append(submission.url)
    topics_dict ["comms_num"].append(submission.num_comments)
    topics_dict ["created"].append(submission.created)
    topics_dict ["body"].append(submission.selftext)

topics_data = pd.DataFrame(topics_dict)

def get_date(created):
    return dt.datetime.fromtimestamp(created)

_timestamp = topics_data["created"].apply(get_date)
topics_data = topics_data.assign(timestamp = _timestamp)

topics_data.to_csv('TOP_10_subreddit_r_programming_posts.csv', index=False)