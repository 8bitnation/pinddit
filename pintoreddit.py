import praw
from settings import REDDIT_ID, REDDIT_SECRET, REDDIT_USER_AGENT, REDDIT_USERNAME, REDDIT_PASSWORD, SUB_REDDIT

sub_reddit = SUB_REDDIT

reddit = praw.Reddit(
    client_id=REDDIT_ID,
    client_secret=REDDIT_SECRET,
    user_agent=REDDIT_USER_AGENT,
    username=REDDIT_USERNAME,
    password=REDDIT_PASSWORD)

print('Bot logged into Reddit as ', reddit.user.me())
# Create a post
#reddit.subreddit(sub_reddit).submit('Test post from Pinddit', 'Testing the ability for the pinddit bot to create a post in [/r/8bNDev](/r/8bNDev)')
#print('Created post')
# print(reddit.user.me()) # prints out the username logged in