import pytest
from unittest import mock
from unittest.mock import MagicMock


@pytest.fixture
def mock_reddit():
    with mock.patch("praw.Reddit") as mock_client:
        yield mock_client.return_value


@pytest.fixture
def mock_subreddit(mock_reddit):
    subreddit = mock_reddit.subreddit.return_value
    with mock.patch.object(subreddit, "top") as mock_top:
        with mock.patch.object(subreddit, "comments") as mock_comments:
            yield mock_top, mock_comments


@pytest.fixture
def mock_posts():
    post1 = MagicMock()
    post1.id = "post1"
    post1.title = "Title 1"
    post1.author.name = "John Doe"
    post1.url = "https://www.reddit.com/r/subreddit/post1"
    post1.num_comments = 7

    post2 = MagicMock()
    post2.id = "post2"
    post2.title = "Title 2"
    post2.author.name = "Jane Doe"
    post2.url = "https://www.reddit.com/u/subreddit/post2"
    post2.num_comments = 24

    post3 = MagicMock()
    post3.id = "post3"
    post3.title = "Title 3"
    post3.author.name = "John Doe"
    post3.url = "https://www.reddit.com/u/subreddit/post3"
    post3.num_comments = 12

    return [post1, post2, post3]


@pytest.fixture
def mock_reddit_posts():
    reddit = MagicMock()
    subreddit = MagicMock()
    subreddit.display_name = 'test'
    reddit.subreddit.return_value = subreddit
    subreddit.top.return_value = [
        MagicMock(title='Title 1', author='John Doe'),
        MagicMock(title='Title 2', author='John Doe'),
        MagicMock(title='Title 3', author='Jane Doe')
    ]
    subreddit.comments.return_value = [
        MagicMock(author='John Doe'),
        MagicMock(author='Jane Doe'),
        MagicMock(author='John Doe')
    ]
    return reddit


@pytest.fixture
def user_data():
    return {"John Doe": 10, "Jane Doe": 20, "Judy Doe": 5, "James Doe": 2}


@pytest.fixture
def comments():
    comment1 = MagicMock()
    comment1.author.name = "John Doe"

    comment2 = MagicMock()
    comment2.author.name = "Jane Doe"

    comment3 = MagicMock()
    comment3.author = None

    return [comment1, comment2, comment3]
