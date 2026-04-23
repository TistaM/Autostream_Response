from app.rag.retriever import retrieve_relevant_info
from app.agents.lead_manager import handle_lead_collection
from app.utils.validators import is_valid_email


def generate_response(state):
    user_input = state.user_input.strip()

    if state.awaiting_name and not state.name:
        state.name = user_input
        state.awaiting_name = False
        return handle_lead_collection(state)

    if state.awaiting_email and not state.email:
        if not is_valid_email(user_input):
            state.response = "That email doesn't look valid. Please enter a valid email address."
            return state
        state.email = user_input
        state.awaiting_email = False
        return handle_lead_collection(state)

    if state.awaiting_platform and not state.platform:
        state.platform = user_input
        state.awaiting_platform = False
        return handle_lead_collection(state)

    if state.intent == "greeting":
        state.response = "Hi! I can help with AutoStream pricing, features, and plans."
        return state

    if state.intent == "product_inquiry":
        state.response = retrieve_relevant_info(user_input)
        return state

    if state.intent == "high_intent":
        return handle_lead_collection(state)

    state.response = "I can help with pricing, features, support, or getting started with AutoStream."
    return state