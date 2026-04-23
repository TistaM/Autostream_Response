from app.state import AgentState
from app.graph import run_turn


def test_full_conversation_flow():
    state = AgentState()

    # Turn 1: Greeting
    state = run_turn(state, "Hi")
    assert "Hi!" in state.response or "help" in state.response
    assert state.intent == "greeting"

    # Turn 2: Pricing inquiry
    state = run_turn(state, "Tell me about your pricing")
    assert "Basic Plan" in state.response
    assert "Pro Plan" in state.response
    assert state.intent == "product_inquiry"

    # Turn 3: High-intent signal
    state = run_turn(state, "That sounds good, I want to try the Pro plan for my YouTube channel")
    assert "What's your name?" in state.response
    assert state.intent == "high_intent"
    assert state.lead_captured is False

    # Turn 4: Name provided
    state = run_turn(state, "John Doe")
    assert "email" in state.response.lower()
    assert state.name == "John Doe"
    assert state.lead_captured is False

    # Turn 5: Email provided
    state = run_turn(state, "john@example.com")
    assert "platform" in state.response.lower() or "youtube" in state.response.lower()
    assert state.email == "john@example.com"
    assert state.lead_captured is False

    # Turn 6: Platform provided
    state = run_turn(state, "YouTube")
    assert "captured successfully" in state.response.lower()
    assert state.platform == "YouTube"
    assert state.lead_captured is True