from dataclasses import dataclass, field
from typing import Self

from dingtalk_robot.request.constants import MsgType
from dingtalk_robot.request.entity import (
    ActionCardBody,
    AtBody,
    FeedCardBody,
    LinkBody,
    MarkdownBody,
    TextBody,
)


@dataclass
class RequestBody:
    msgtype: MsgType
    text: TextBody = field(default=None)
    at: AtBody = field(default=None)
    link: LinkBody = field(default=None)
    markdown: MarkdownBody = field(default=None)
    action_card: ActionCardBody = field(default=None)
    feed_card: FeedCardBody = field(default=None)

    @classmethod
    def text_body(cls, msgtype: MsgType, text: TextBody, at: AtBody = None) -> Self:
        return cls(msgtype=msgtype, text=text, at=at)

    @classmethod
    def link_body(cls, msgtype: MsgType, link: LinkBody) -> Self:
        return cls(msgtype=msgtype, link=link)

    @classmethod
    def markdown_body(
        cls, msgtype: MsgType, markdown: MarkdownBody, at: AtBody = None
    ) -> Self:
        return cls(msgtype=msgtype, markdown=markdown, at=at)

    @classmethod
    def action_card_body(cls, msgtype: MsgType, action_card: ActionCardBody) -> Self:
        return cls(msgtype=msgtype, action_card=action_card)

    @classmethod
    def feed_card_body(cls, msgtype: MsgType, feed_card: FeedCardBody) -> Self:
        return cls(msgtype=msgtype, feed_card=feed_card)

    def to_dict(self: Self) -> dict:
        return {
            "msgtype": self.msgtype.value,
            "text": self.text.to_dict(),
            "at": self.at.to_dict(),
            "link": self.link.to_dict(),
            "markdown": self.markdown.to_dict(),
            "actionCard": self.action_card.to_dict(),
            "feedCard": self.feed_card.to_dict(),
        }
