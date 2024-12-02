from enum import Enum


class MsgType(Enum):
    TEXT = "text"
    LINK = "link"
    MARKDOWN = "markdown"
    ACTION_CARD = "actionCard"
    FEED_CARD = "feedCard"
