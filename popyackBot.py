#!/usr/bin/python
import praw
import re

reddit = praw.Reddit('bot1')

subreddit = reddit.subreddit("Justletmetest")

for comment in subreddit.stream.comments():
	print(comment.body)
	if re.search("popyack", comment.body, re.IGNORECASE):
		comment.reply('You hear a whisper from the distance. It says, "Getting a degree in Computer Science is like getting a degree in Refrigerator Science"')
		print("Got em")


