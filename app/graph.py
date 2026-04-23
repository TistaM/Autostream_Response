from app.agents.intent_classifier import classify_intent
from app.agents.response_generator import generate_response


def run_turn(state, user_input: str):
    state.user_input = user_input

    if not (state.awaiting_name or state.awaiting_email or state.awaiting_platform):
        state.intent = classify_intent(user_input)

    state = generate_response(state)
    return state