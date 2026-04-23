#  AutoStream – Social-to-Lead Conversational AI Agent

#  Overview
AutoStream is a conversational AI agent designed to simulate a real-world SaaS sales assistant. The system interacts with users, answers product-related queries, detects high purchase intent, and converts conversations into qualified leads.

Unlike basic chatbots, this agent performs multi-step reasoning using intent detection, retrieval-based responses, and structured lead capture workflows.

#  Key Features

-  Intent Classification (Greeting, Inquiry, High-Intent)
-  RAG-based Knowledge Retrieval from a local JSON knowledge base
-  Multi-turn Conversation with Memory
-  Lead Qualification (Name, Email, Platform)
-  Controlled Tool Execution (Lead Capture)
-  End-to-End Workflow Testing with Pytest

# System Architecture

The system is modular and structured into multiple components:

- Agents Layer
  - Handles intent classification and response generation
- RAG Layer
  - Retrieves product information from a local knowledge base
- State Management
  - Maintains conversation memory across multiple turns
- Tool Layer
  - Executes lead capture only after all required details are collected
- Controller (Graph)
  - Orchestrates the flow between components

This design ensures separation of concerns and mimics real-world agentic workflows.

# Tech Stack

- Python 3.9+
- LangChain / Modular Agent Design
- OpenAI (GPT-4o-mini compatible setup)
- Pytest (Testing)
- JSON-based Knowledge Base

# Project Structure

autostream-agent/
│
├── app/
│   ├── main.py
│   ├── graph.py
│   ├── state.py
│   ├── config.py
│   ├── prompts.py
│   ├── agents/
│   │   ├── intent_classifier.py
│   │   ├── response_generator.py
│   │   └── lead_manager.py
│   ├── rag/
│   │   ├── loader.py
│   │   ├── retriever.py
│   │   └── knowledge_base.json
│   ├── tools/
│   │   └── lead_capture.py
│   └── utils/
│       └── validators.py
│
├── tests/
│   ├── test_intents.py
│   ├── test_rag.py
│   └── test_lead_capture.py
│
├── .env
├── .gitignore
├── requirements.txt
├── README.md
└── run.py 

# How to Run Locally

# 1. Clone the repository

git clone https://github.com/TistaM/Autostream_Response
cd autostream-agent

# 2. Create virtual environment

python -m venv venv
venv\Scripts\activate   

# 3. Install dependencies

pip install -r requirements.txt

# 4. Add environment variables

Create a .env file:
OPENAI_API_KEY=your_api_key_here

# 5. Run the chatbot

python run.py


# Running Tests

pytest -v

All tests validate:

Intent classification
Knowledge retrieval
Lead capture logic
Full conversation flow


# Conversation Workflow
User initiates conversation
Agent identifies intent
For product queries → retrieves data via RAG
For high-intent users → initiates lead capture
Collects:
Name
Email
Platform
Executes lead capture tool only after all inputs are received


# State Management

The system maintains conversation state using a structured AgentState object.

This includes:

Current intent
User details (name, email, platform)
Lead capture status
Conversation progress flags

This ensures the agent can handle multi-turn conversations reliably.


# Demo

Refer to:

demo/sample_chat.txt


# The demo showcases:

Pricing queries
Intent shift
Lead capture
Tool execution


# Evaluation Highlights
Clean modular architecture
Strong state management
Correct tool execution logic
Fully tested workflow
Real-world deployable design


# Conclusion

This project demonstrates how conversational AI can move beyond simple Q&A systems and function as an intelligent, goal-driven agent capable of driving business outcomes such as lead generation.
