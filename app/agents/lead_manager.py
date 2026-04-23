from app.tools.lead_capture import mock_lead_capture


def handle_lead_collection(state):
    if not state.name:
        state.awaiting_name = True
        state.response = "Great — I can help with that. What's your name?"
        return state

    if not state.email:
        state.awaiting_email = True
        state.response = "Thanks! What's your email address?"
        return state

    if not state.platform:
        state.awaiting_platform = True
        state.response = "Got it. Which creator platform do you use, like YouTube or Instagram?"
        return state

    if not state.lead_captured:
        mock_lead_capture(state.name, state.email, state.platform)
        state.lead_captured = True
        state.awaiting_name = False
        state.awaiting_email = False
        state.awaiting_platform = False
        state.response = "Perfect — your details have been captured successfully."
        return state

    state.response = "Your lead has already been captured."
    return state