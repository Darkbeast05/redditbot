import praw
import urllib.request
from praw.models import MoreComments

reddit = praw.Reddit(user_agent="Useless v0.1 by /u/PasswordPrevention",site_name="bot")
sub = reddit.subreddit("testingground4bots")
for submission in sub.new(limit=60):
    submission.comments.replace_more(limit=0)
    for comment in submission.comments.list():
        if isinstance(comment, MoreComments):
            continue
        if "!summonbot1" in comment.body:
            isme = False
            print("found")
            for reply in comment.replies:
                if reply.author == reddit.redditor("UselessBotFF"):
                    isme=True
            if not isme:             
                split = comment.body.split("-")
                if len(split) >= 3:
                    split.reverse()
                    split.pop()
                    if split.pop() =='toHex':
                        comment.reply((''.join(hex(ord(x))[2:] for x in split.pop()) + "/n/n/n Am a bot."))
            print(isme)
