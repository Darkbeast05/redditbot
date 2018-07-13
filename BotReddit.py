import praw, os, time
from praw.models import MoreComments
from boto.s3.connection import S3Connection

s3 = S3Connection(os.environ['PASS'], os.environ['SECRET'])

reddit = praw.Reddit(user_agent="Useless v0.1 by /u/PasswordPrevention", client_id='tsfUXGBvO_3ASw', client_secret=os.environ['SECRET'], username='UselessBotFF', password=os.environ['PASS'])
sub = reddit.subreddit("testingground4bots")
while True:
    for submission in sub.new(limit=60):
        submission.comments.replace_more(limit=0)
        for comment in submission.comments.list():
            if isinstance(comment, MoreComments):
                continue
            if "!summonbot1" in comment.body:
                isme = False
                sys.stdout.write("found")
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
                sys.stdout.write(isme)
                time.sleep(20)
