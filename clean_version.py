# This is a version of the Reddit Extractor that will print clean text
# Headings and notations about user names, time posted, etc. are left out
# The purpose is that this can be fed directly into NLP

# Import libraries
import sys
import datetime
import praw

# Authentication
# This is my login info for registered Reddit API application - do not distribute
# Using no username or password ensures that I'm only getting public comments

reddit = praw.Reddit(
    client_id = "e5Kq4EYYJ8r6mw",
    client_secret = "CCo5ydLefQV3j6JFLLFTg9GNbgozSw",
    user_agent = "Testing_app",
)

# Main section of the code

# Prompt for submission URL
url = input('Enter URL here: ')
submission = reddit.submission(url=url)

# Prompt for file name, end with .txt manually
filename = input('What do you want to call this file? ')
sys.stdout = open(filename,'a')

# Expand "see more comments" buttons. Set lower limit to speed up processing time, trade-off thoroughness
submission.comments.replace_more(limit=5)

# FUNCTIONS
# Spacing function for printing
def twospaces():
    print()
    print()

# Recursive function for comment processing
# I got this recursive structure from a Reddit thread and still confused about recursion
def handle_comment(comment, depth = 2):
    for child_comment in comment.replies:
        print()
        print(depth * '  ')
        childcommenttext = child_comment.body
        print(childcommenttext)

        # Recursive element
        handle_comment(child_comment, depth+1)

# Printing the submission

print()

# Submission title
submissiontitle = submission.title
print(submissiontitle)

print()

# Submission body
submissionbody = submission.selftext
print(submissionbody)

twospaces()

# Printing the comments

for top_level_comment in submission.comments:
    twospaces()
    toplevelcommenttext = top_level_comment.body
    print(toplevelcommenttext)

    handle_comment(top_level_comment)

# Close the file
# Have had problems with this in the past - it seems to work in IDLE and PyCharm but not Jupyter Notebooks
sys.stdout.close()
