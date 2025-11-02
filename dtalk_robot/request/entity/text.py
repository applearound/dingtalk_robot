from dataclasses import dataclass, field
from typing import Optional, Self


@dataclass
class TextBody:
    content: Optional[str] = field(default=None)

    def to_dict(self: Self) -> dict:
        return {"content": self.content}
