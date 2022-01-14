#!/usr/bin/python3

# Modules
import praw, datetime, configparser

# WIP: Read config file for credentials.
config = configparser.ConfigParser()
config.read('login.ini')

# Prompt for credentials.
client_id = config['login']['client_id']
client_secret = config['login']['client_secret']
username = config['login']['username']
password = config['login']['password']
user_agent = config['login']['user_agent']
  
# Creating an authorized reddit instance.
reddit = praw.Reddit(client_id = client_id, client_secret = client_secret, username = username, password = password, user_agent = user_agent) 
  
# The subreddit to monitor.
target_sub = "testingground4bots"
subreddit = reddit.subreddit(target_sub)

# Let the user know you're up.
print("Monitoring " + target_sub + "...")
  
# Phrases that trigger the bot.
trigger_list = ['1660', 'on move 6', 'trapped queen', 'trapped the man\'s queen', 'trap the man\'s queen', 'like a potato']
  
# Check every comment in the subreddit except mine.
me = reddit.user.me()
for comment in subreddit.stream.comments(skip_existing=True):
  
    # Check the trigger_phrase in each comment
    if [ele for ele in trigger_list if(ele in comment.body.lower())] and comment.author != me:
  
        # initialize the reply text
        reply_text = """1660. 1660. You're telling me a 1600 hung a piece on move 6? **YOU ARE TELLING ME** THAT A _1600 RATED PLAYER HUNG A PIECE ON MOVE 6, 1600 RATED PLAYER HUNG A PIECE ON MOVE 6, THIS GUY IS 1660 AND HE HUNG A PIECE ON MOVE 6; 16, 16, 60 and he hung a piece on move 6!_

_Didn't see a trapped queen, could've trapped the man's queen. Didn't trap the man's queen, could've trapped the man's queen, this man had Rook a4 like 3 moves in a row, didn't even see it._
Like when I see the queen come here this is the first thing I think of.

_Damn. Damn. Damn damn damn. Well at least this dude has potato in his name because he_... played like a potato. He played like a potato.

^Beep boop. | [Source](https://github.com/jclocks/levy-rozbot) | [Issues? Suggestions?](https://github.com/jclocks/levy-rozbot/issues) | [Video](https://www.youtube.com/watch?v=7MRNWxCuIrI)"""
          
        # Shitpost.
        comment.reply(reply_text)
        print(str(datetime.datetime.now()) + ": Replied to comment " + str(comment.id) + " by " + str(comment.author))
