#!/usr/bin/python3
"""
Replybot-5000: Reddit bot script that replies to comments submitted on
specified subreddits.

Author: jclocks @ github.com
Version: TBD
"""

# Modules
import datetime
import time
import configparser
import os
import praw
import prawcore

CONFIG_FILE = 'login.ini'

# Error handling loop
while True:
    try:

        # Read config file for credentials.
        config = configparser.ConfigParser()
        if not os.path.exists(CONFIG_FILE):
            input("""
The configuration file has not been generated. Taking you to your preferred
editor to fill this out. Press Enter to continue...
""")
            os.system("cp blank-login.ini login.ini ; $EDITOR login.ini")

        config.read(CONFIG_FILE)

        # Creating an authorized Reddit instance.
        reddit = praw.Reddit(client_id=config['login']['client_id'],
                             client_secret=config['login']['client_secret'],
                             username=config['login']['username'],
                             password=config['login']['password'],
                             user_agent=config['login']['user_agent'])

        # The subreddit to monitor.
        TARGET_SUB = "testingground4bots"
        subreddit = reddit.subreddit(TARGET_SUB)

        # Let the user know you're up.
        print("Monitoring " + TARGET_SUB + "...")

        # Phrases that trigger the bot.
        trigger_list = ['foo', 'bar']

        # Check every comment in the subreddit except the bot's.
        me = reddit.user.me()
        for comment in subreddit.stream.comments(skip_existing=True):

            # Check the trigger_phrase in each comment
            if [el for el in trigger_list if el in comment.body.lower()] and comment.author != me:

                # initialize the reply text
                REPLY_TEXT = 'Reply text goes here.'

                # Perform comment and log to stdout.
                comment.reply(REPLY_TEXT)
                print(str(datetime.datetime.now()) + ": Replied to comment "
                      + str(comment.id) + " by " + str(comment.author))

    # In the event an exception occurs, we want the application to reload.
    # See https://github.com/jclocks/replybot-5000/issues/1
    except prawcore.exceptions.ResponseException:
        time.sleep(10)
        continue
