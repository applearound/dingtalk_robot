from dataclasses import dataclass, field
from typing import Optional


@dataclass
class ResponseBody:
    r"""DingTalk response body.

    see: https://open.dingtalk.com/document/orgapp/custom-robots-send-group-messages
    """

    errmsg: Optional[str] = field(default=None)
    errcode: Optional[int] = field(default=None)
