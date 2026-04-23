from app.rag.loader import load_knowledge_base


def retrieve_relevant_info(user_query: str) -> str:
    kb = load_knowledge_base()
    query = user_query.lower()

    if any(word in query for word in ["price", "pricing", "plan", "cost", "feature"]):
        basic = kb["plans"]["basic"]
        pro = kb["plans"]["pro"]

        return (
            f"{basic['name']}: {basic['price']}, includes {', '.join(basic['features'])}.\n"
            f"{pro['name']}: {pro['price']}, includes {', '.join(pro['features'])}."
        )

    if "refund" in query:
        return kb["policies"]["refund_policy"]

    if "support" in query:
        return kb["policies"]["support_policy"]

    return "AutoStream offers Basic and Pro plans. Ask me about pricing, features, refunds, or support."