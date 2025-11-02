from dataclasses import dataclass, field
from typing import Optional, Self


@dataclass
class MarkdownBody:
    title: Optional[str] = field(default=None)
    text: Optional[str] = field(default=None)

    def to_dict(self: Self) -> dict:
        return {"title": self.title, "text": self.text}
