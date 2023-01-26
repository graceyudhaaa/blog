import sys
import os

BLOG_PATH = os.path.join(os.path.dirname(os.getcwd()), 'blog')
sys.path.append(BLOG_PATH)

from app import create_app

def test_api():
    response = create_app().test_client().get('/api/test')
    print()

test_api()