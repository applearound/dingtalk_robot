from dataclasses import dataclass, field
from typing import Optional, Self


@dataclass
class BtnBody:
    action_url: Optional[str] = field(default=None)
    title: Optional[str] = field(default=None)

    def to_dict(self: Self) -> dict:
        return {"actionURL": self.action_url, "title": self.title}
