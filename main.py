# Recursive Reddit Extractor
# Dependencies in requirements.txt
# Uses Python Reddit API Wrapper (PRAW)
# Contains sensitive information - Do not distribute
# For extracting Reddit posts and comments and transforming them into a .txt file that preserves tree structure
# This code should prompt for a Reddit post URL and then prompt for a file name (e.g. testerfile.txt), in the shell
# Result: a .txt file will be saved in the folder where this code is

# Import libraries
import sys
import textwrap
import datetime
import praw

# Authentication - CONFIDENTIAL
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
        print(depth * '  ', '__', 'Reply: Level', depth, '__') # This will show the comment level

        # Text-wrapping comment body
        childcommenttext = child_comment.body
        lines = textwrap.wrap(childcommenttext, width = 50)

        for line in lines:
            print(depth * '  ', line)

        # Comment data
        # If commenter is the original poster:
        if child_comment.is_submitter is True:
            print(depth * '  ', '///', 'By submitter.')
        # Author, comment and parent ID to be able to manually check
        print(depth * '  ', '///', 'Author:', child_comment.author)
        print(depth * '  ', '///', 'Comment ID:', child_comment.id)
        print(depth * '  ', '///', 'Parent ID:', child_comment.parent_id)

        # Time, converted from Unix to UTC
        timestamp = child_comment.created_utc
        value = datetime.datetime.fromtimestamp(timestamp)
        print(depth * '  ', '///', 'Time:', f"{value:%Y-%m-%d %H:%M:%S}")

        # Recursive element
        handle_comment(child_comment, depth+1)

# Printing the submission

print('___Submission___')
print()
print('-Submission title-')

# Textwrapping the submission title
submissiontitle = submission.title
lines = textwrap.wrap(submissiontitle, width = 60)
for line in lines:
    print(line)

print()

# Textwrapping the submission body
print('-Submission body-')
submissionbody = submission.selftext
lines = textwrap.wrap(submissionbody, width = 60)
for line in lines:
    print(line)

# Submission data
# This shows whether submission is text-only. If not, it includes this warning.
if submission.is_self is False:
    print('Note: This submission may include other media')
print()
print('-----')
# Prints submission author
print('Author:', submission.author)

# Time of submission, converted from Unix to UTC
timestamp = submission.created_utc
value = datetime.datetime.fromtimestamp(timestamp)
print('Time:', f"{value:%Y-%m-%d %H:%M:%S}")

# Submission ID, comments, other info
print('ID:', submission.id)
print('# of Comments:', submission.num_comments, '(Comments printed may be less)')
print('Permalink:', submission.permalink)
print('Other links in submission:', submission.url, '(Duplicate permalink if no other links)')
print('-----')
twospaces()

# Printing the comments
print('-----BEGINNING OF COMMENTS-----')

for top_level_comment in submission.comments:
    twospaces()
    print('___Comment___')

    # Textwrapping the comment body
    toplevelcommenttext = top_level_comment.body
    lines = textwrap.wrap(toplevelcommenttext, width = 60)

    for line in lines:
        print(line)

    print('-----')

    # Comment data
    if top_level_comment.is_submitter is True:
        print('///', 'By submitter.')
    print('///', 'Author:', top_level_comment.author)
    print('///', 'Parent ID (should be submission ID):', top_level_comment.parent_id)
    print('///', 'Comment ID:', top_level_comment.id)

    # Time of comment, converted from Unix to UTC
    timestamp = top_level_comment.created_utc
    value = datetime.datetime.fromtimestamp(timestamp)
    print('///', 'Time:', f"{value:%Y-%m-%d %H:%M:%S}")

    handle_comment(top_level_comment)

# Close the file
# Have had problems with this in the past - it seems to work in IDLE and PyCharm but not Jupyter Notebooks
sys.stdout.close()
