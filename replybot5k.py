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

# Variables, Constants
CONFIG_FILE = 'login.ini'
TARGET_SUB = "testingground4bots"
trigger_list = ['foo', 'bar']


def setup_new_config():
    ''' Sets up a new config file, sends user to edit it. '''
    prompt_text = 'The configuration file has not been generated. Taking you\
                   to your preferred editor to fill this out. Press Enter to\
                   continue...'
    input(prompt_text)
    os.system('cp blank-login.ini login.ini')
    os.system('$EDITOR login.ini')


def use_config():
    ''' Read config file. Return a Reddit object. '''
    config = configparser.ConfigParser()

    # If the config file doesn't exist, we want to set that up and have the
    # user fill it out.
    if not os.path.exists(CONFIG_FILE):
        setup_new_config()

    # Create an authorized Reddit instance from the config file info.
    config.read(CONFIG_FILE)
    instance = praw.Reddit(client_id=config['login']['client_id'],
                           client_secret=config['login']['client_secret'],
                           username=config['login']['username'],
                           password=config['login']['password'],
                           user_agent=config['login']['user_agent'])
    return instance


# Error handling loop
while True:
    try:
        reddit = use_config()

        # The subreddit to monitor.
        subreddit = reddit.subreddit(TARGET_SUB)

        # Let the user know you're up.
        print("Monitoring " + TARGET_SUB + "...")

        # Check every comment in the subreddit except the bot's.
        me = reddit.user.me()
        for comment in subreddit.stream.comments(skip_existing=True):

            # Check the trigger_phrase in each comment
            if [el for el in trigger_list if el in comment.body.lower()]\
                    and comment.author != me:

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
