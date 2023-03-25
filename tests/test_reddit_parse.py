from unittest import mock
from reddit_parse import get_subreddit_posts, count_author_posts, count_author_comments, fetch_top_users, extract_comment_authors


def test_get_subreddit_posts_returns_correct_post_data(mock_subreddit, mock_posts):
    mock_top, mock_comments = mock_subreddit
    mock_top.return_value = [mock.MagicMock() for _ in range(len(mock_posts))]
    subreddit_name = "test_subreddit_name"
    days = 3
    reddit = mock.MagicMock()
    posts = get_subreddit_posts(subreddit_name, days, reddit)
    for i, post in enumerate(posts):
        assert post["id"] == mock_posts[i]["id"]
        assert post["title"] == mock_posts[i]["title"]
        assert post["author"] == mock_posts[i]["author"]
        assert post["post_url"] == mock_posts[i]["post_url"]
        assert post["num_comments"] == mock_posts[i]["num_comments"]
        assert post["comments"] == mock_posts[i]["comments"]
        assert post["comment_authors"] == mock_posts[i]["comment_authors"]


def test_count_author_comments(comments, mock_reddit):
    result = count_author_comments(comments, "test", mock_reddit)
    assert result == {"John Doe": 2, "Jane Doe": 1}


def test_fetch_top_users(user_data):
    top_users = fetch_top_users(user_data, 2)
    assert top_users == [("Jane Doe", 20), ("John Doe", 10)]


def test__fetch_top_users__returns_list(user_data):
    top_users = fetch_top_users(user_data, 2)
    assert isinstance(top_users, list)


def test__fetch_top_users__returns_expected_number_of_users(user_data):
    top_users = fetch_top_users(user_data, 3)
    assert len(top_users) == 3


def test__fetch_top_users__returns_correct_user_data(user_data):
    top_users = fetch_top_users(user_data, 2)
    assert top_users == [("Jane Doe", 20), ("John Doe", 10)]


def test_extract_comment_authors(comments):
    expected_result = ["John Doe", "Jane Doe"]
    result = extract_comment_authors(comments)
    assert result == expected_result
