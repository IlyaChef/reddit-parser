import argparse
from reddit_parse import get_subreddit_posts, count_author_posts, count_author_comments, fetch_top_users
from reddit_api_client import create_reddit_api_client


def reddit_console_parser() -> None:
    parser = argparse.ArgumentParser(description="Reddit console parser")
    parser.add_argument("subreddit_name", help="input name of the subreddit to parse")
    parser.add_argument("--days", type=int, default=3, help="input number of days to parse (default: 3)")
    parser.add_argument("--post-authors", type=int, default=10,
                        help="input number of top post authors to print (default: 10)")
    parser.add_argument("--comment-authors", type=int, default=10,
                        help="input number of top comment authors to print (default: 10)")
    args = parser.parse_args()
    reddit = create_reddit_api_client()
    subreddit_name = args.subreddit_name
    days = args.days
    posts = get_subreddit_posts(subreddit_name, days, reddit)
    post_authors = args.post_authors
    comment_authors = args.comment_authors
    comments_count_by_user = count_author_posts(posts, subreddit_name, reddit)
    top_commenters = fetch_top_users(comments_count_by_user, comment_authors)
    posts_count_by_user = count_author_comments(posts, subreddit_name, reddit)
    top_posters = fetch_top_users(posts_count_by_user, post_authors)
    print(f"*****Top {args.post_authors} post authors******:")
    for user, count in top_posters:
        print(f"{user}: {count}")
    print(f"******Top {args.comment_authors} commenters in {subreddit_name}******:")
    for user, count in top_commenters:
        print(f"{user}: {count}")


if __name__ == '__main__':
    reddit_console_parser()
