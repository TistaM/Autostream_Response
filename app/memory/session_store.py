from typing import Dict
from app.state import AgentState


class SessionStore:
    def __init__(self):
        # Stores session_id -> AgentState
        self.sessions: Dict[str, AgentState] = {}

    def get_session(self, session_id: str) -> AgentState:
        """Retrieve existing session or create a new one"""
        if session_id not in self.sessions:
            self.sessions[session_id] = AgentState()
        return self.sessions[session_id]

    def update_session(self, session_id: str, state: AgentState):
        """Update session state"""
        self.sessions[session_id] = state

    def reset_session(self, session_id: str):
        """Reset session"""
        if session_id in self.sessions:
            self.sessions[session_id] = AgentState()