from app.state import AgentState
from app.graph import run_turn


def run_chat():
    state = AgentState()
    print("AutoStream Agent: Hi! How can I help you today?")

    while True:
        user_input = input("You: ").strip()

        if user_input.lower() in {"exit", "quit"}:
            print("AutoStream Agent: Goodbye!")
            break

        state = run_turn(state, user_input)
        print(f"AutoStream Agent: {state.response}")