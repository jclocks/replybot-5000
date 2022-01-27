#!/usr/bin/python3

# Modules
import praw
import datetime
import configparser

# Read config file for credentials.
config = configparser.ConfigParser()
config.read('login.ini')

# Prompt for credentials.
client_id = config['login']['client_id']
client_secret = config['login']['client_secret']
username = config['login']['username']
password = config['login']['password']
user_agent = config['login']['user_agent']

# Creating an authorized Reddit instance.
reddit = praw.Reddit(client_id=client_id, client_secret=client_secret,
                     username=username, password=password,
                     user_agent=user_agent)

# The subreddit to monitor.
target_sub = "testingground4bots"
subreddit = reddit.subreddit(target_sub)

# Let the user know you're up.
print("Monitoring " + target_sub + "...")

# Phrases that trigger the bot.
trigger_list = ['foo', 'bar']

# Check every comment in the subreddit except the bot's.
me = reddit.user.me()
for comment in subreddit.stream.comments(skip_existing=True):

    # Check the trigger_phrase in each comment
    if ([ele for ele in trigger_list if(ele in comment.body.lower())]
            and comment.author != me):

        # initialize the reply text
        reply_text = ''

        # Shitpost.
        comment.reply(reply_text)
        print(str(datetime.datetime.now()) + ": Replied to comment "
              + str(comment.id) + " by " + str(comment.author))
