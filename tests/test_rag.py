from app.rag.retriever import retrieve_relevant_info


def test_pricing_retrieval():
    response = retrieve_relevant_info("Tell me about your pricing")
    assert "Basic Plan" in response
    assert "$29/month" in response
    assert "Pro Plan" in response
    assert "$79/month" in response


def test_refund_policy_retrieval():
    response = retrieve_relevant_info("What is your refund policy?")
    assert "No refunds after 7 days" in response


def test_support_policy_retrieval():
    response = retrieve_relevant_info("Do you offer 24/7 support?")
    assert "24/7 support available only on Pro plan" in response