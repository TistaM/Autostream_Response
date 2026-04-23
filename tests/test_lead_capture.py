from app.state import AgentState
from app.agents.lead_manager import handle_lead_collection


def test_asks_for_name_first():
    state = AgentState()
    updated_state = handle_lead_collection(state)

    assert updated_state.response == "Great — I can help with that. What's your name?"
    assert updated_state.lead_captured is False


def test_asks_for_email_after_name():
    state = AgentState(name="John Doe")
    updated_state = handle_lead_collection(state)

    assert updated_state.response == "Thanks! What's your email address?"
    assert updated_state.lead_captured is False


def test_asks_for_platform_after_email():
    state = AgentState(name="John Doe", email="john@example.com")
    updated_state = handle_lead_collection(state)

    assert updated_state.response == "Got it. Which creator platform do you use, like YouTube or Instagram?"
    assert updated_state.lead_captured is False


def test_captures_lead_only_when_all_fields_present():
    state = AgentState(
        name="John Doe",
        email="john@example.com",
        platform="YouTube"
    )
    updated_state = handle_lead_collection(state)

    assert updated_state.lead_captured is True
    assert updated_state.response == "Perfect — your details have been captured successfully."