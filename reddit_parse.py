import collections
import datetime
import praw
from typing import List, Dict, Any, Tuple
from operator import itemgetter


def get_subreddit_posts(subreddit_name: str, days: int, reddit: praw.Reddit) -> List[Dict[str, Any]]:
    subreddit = reddit.subreddit(subreddit_name)
    date_from = datetime.datetime.utcnow() - datetime.timedelta(days=days)
    posts = []
    for post in subreddit.top(limit=40):
        if datetime.datetime.utcfromtimestamp(post.created_utc) >= date_from:
            posts.append({
                'id': post.id,
                'title': post.title,
                'author': post.author.name if post.author else "Unknown",
                'post_url': post.url,
                'num_comments': post.num_comments,
                'comments': post.comments,
                'comment_authors': extract_comment_authors(post.comments)
            })
    return posts


def extract_comment_authors(comments) -> List[str]:
    authors = []
    for comment in comments:
        author = comment.author
        if author:
            authors.append(author.name)
    return authors


def count_author_posts(posts: List[Dict[str, Any]], subreddit_name: str, reddit: praw.Reddit) -> Dict[str, int]:
    subreddit = reddit.subreddit(subreddit_name)
    user_post_count = collections.Counter(
        post.author.name for post in subreddit.top(limit=50) if post.author is not None
    )
    return user_post_count


def count_author_comments(posts: List[Dict[str, Any]], subreddit_name: str, reddit: praw.Reddit) -> Dict[str, int]:
    subreddit = reddit.subreddit(subreddit_name)
    comments_count = collections.Counter(comment.author for comment in subreddit.comments(limit=500))
    return comments_count


def fetch_top_users(user_data: Dict[str, int], count: int) -> List[Tuple[str, int]]:
    sorted_user_data = sorted(user_data.items(), key=itemgetter(1), reverse=True)
    return sorted_user_data[:count]
