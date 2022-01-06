#!/usr/bin/python3

# import the modules
import praw
import datetime

# initialize with appropriate values
print("Client ID: ", end="")
client_id = input()
print("Client Secret: ", end="")
client_secret = input()
print("Username: ", end="")
username = input()
print("Password: ", end="")
password = input()
print("User Agent: ", end="")
user_agent = input()
  
# creating an authorized reddit instance
reddit = praw.Reddit(client_id = client_id, client_secret = client_secret, username = username, password = password, user_agent = user_agent) 
  
# the subreddit where the bot is to be live on
target_sub = "anarchychess"
subreddit = reddit.subreddit(target_sub)
  
# phrase to trigger the bot
#trigger_phrase = "1660"
  
# check every comment in the subreddit except mine
me = reddit.user.me()
for comment in subreddit.stream.comments():
  
    # check the trigger_phrase in each comment
    if (("1660" in comment.body) or ("like a potato" in comment.body)) and comment.author != me:
  
        # initialize the reply text
        reply_text = """ 1660. 1660. You are telling me a 1600 hung a piece on move 6? YOU ARE TELLING ME THAT A _1600 RATED PLAYER HUNG A PIECE ON MOVE 6, 1600 RATED PLAYER HUNG A PIECE ON MOVE 6, THIS GUY IS 1660 AND HE HUNG A PIECE ON MOVE 6; 16, 16, 60 and he hung a piece on move 6!_

_Didn't see a trapped queen, could've trapped the man's queen. Didn't trap the man's queen, could've trapped the man's queen, this man had Rook a4 like 3 moves in a row, didn't even see it._
Like when I see the queen come here this is the first thing I think of.

_Damn. Damn. Damn damn damn. Well at least this dude has potato in his name because... he_ played like a potato. He played like a potato.

^(Beep boop. Made using Debian and PRAW)"""
          
        # Shitpost.
        comment.reply(reply_text)
        print(str(datetime.datetime.now()) + ": Replied to comment " + comment.id)