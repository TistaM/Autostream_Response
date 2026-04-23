from app.agents.intent_classifier import classify_intent


def test_greeting_intent():
    assert classify_intent("Hi") == "greeting"
    assert classify_intent("Hello there") == "greeting"


def test_product_inquiry_intent():
    assert classify_intent("Tell me about your pricing") == "product_inquiry"
    assert classify_intent("What features are in the Pro plan?") == "product_inquiry"
    assert classify_intent("Do you offer support?") == "product_inquiry"


def test_high_intent():
    assert classify_intent("I want to try the Pro plan") == "high_intent"
    assert classify_intent("Sign me up") == "high_intent"
    assert classify_intent("I want to subscribe") == "high_intent"