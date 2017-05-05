"""
Design a system that would allow you to create various types of posts that can
 be submitted to multiple social media platforms simultaneously.

Support the following post types:
- text
- image
- link

Support the following social media platforms:
- Twitter
- Facebook
- Tumblr

Don't actually create a functioning application. Just stub out the classes,
methods, and functions. Do include parameters and sample return values. Also
include pseudo-code test cases.
"""

from functools import singledispatch
from enum import Enum, auto
import logging
import typing


# define concrete types for the content we want to post

class Image(str):
    """
    This type of string refers to a binary image file on the filesystem.
    """
    pass

class Link(str):
    """
    This type of string refers to an external url.
    """
    pass

class Text(str):
    """
    This type of string is simply meant to be used as-is. 
    """
    pass

# Create union of content types so we can use a static type checker
# if we want and to help document code

Content = typing.Union[Image, Link, Text]

# enumerate the social media platforms we want to support
class SocialNetwork(Enum):
    twitter = auto()
    facebook = auto()
    tumblr = auto()

# define functions for posting to twitter

@singledispatch
def post_to_twitter(content):
    """
    Post content to twitter.
    
    :param content: Any
    :return: None
    """
    logging.error(f'No function registered to handle posting type: {type(content)} to twitter')
    pass

@post_to_twitter.register(Image)
def _(content):
    pass

@post_to_twitter.register(Link)
def _(content):
    pass

@post_to_twitter.register(Text)
def _(content):
    pass

# define functions for posting to tumblr

@singledispatch
def post_to_tumblr(content):
    """
    Post content to tumblr.
    
    :param content: Any
    :return: None
    """
    logging.error(f'No function registered to handle posting type: {type(content)} to tumblr')
    pass

@post_to_tumblr.register(Image)
def _(content):
    pass

@post_to_tumblr.register(Link)
def _(content):
    pass

@post_to_tumblr.register(Text)
def _(content):
    pass

# define functions for posting to facebook
@singledispatch
def post_to_facebook(content):
    """
    Post content to facebook.

    :param content: Any
    :return: None
    """
    logging.error(f'No function registered to handle posting type: {type(content)} to facebook')
    pass

@post_to_facebook.register(Image)
def _(content):
    pass

@post_to_facebook.register(Link)
def _(content):
    pass

@post_to_facebook.register(Text)
def _(content):
    pass

# generic post function

def post(content: Content, social_network: SocialNetwork):

    # the actual function we want to use based on the social network
    function = {
        SocialNetwork.twitter: post_to_twitter,
        SocialNetwork.tumblr: post_to_tumblr,
        SocialNetwork.facebook: post_to_facebook,
    }.get(social_network)

    if not function:
        message = f"No post function defined for social network: {social_network}"
        logging.error(message)
        raise ValueError(message)

    return function(content)