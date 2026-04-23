def classify_intent(user_input: str) -> str:
    text = user_input.lower()

    if any(word in text for word in ["hi", "hello", "hey"]):
        return "greeting"

    if any(phrase in text for phrase in ["i want to try", "sign me up", "i want the pro plan", "i want to subscribe", "get started"]):
        return "high_intent"

    if any(word in text for word in ["price", "pricing", "cost", "plan", "feature", "refund", "support"]):
        return "product_inquiry"

    return "product_inquiry"