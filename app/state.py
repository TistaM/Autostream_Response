from typing import Optional
from pydantic import BaseModel


class AgentState(BaseModel):
    user_input: str = ""
    intent: Optional[str] = None
    response: str = ""

    name: Optional[str] = None
    email: Optional[str] = None
    platform: Optional[str] = None

    awaiting_name: bool = False
    awaiting_email: bool = False
    awaiting_platform: bool = False
    lead_captured: bool = False