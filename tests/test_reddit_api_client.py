import praw
from reddit_api_client import create_reddit_api_client


def test_reddit_api_client_creation():
    client = create_reddit_api_client()
    assert isinstance(client, praw.Reddit)
