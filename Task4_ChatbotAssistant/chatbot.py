"""
Datheon Python Programming Internship - Task 4
Rule-Based Interactive Terminal Assistant / Chatbot

Features:
- Multi-intent pattern matching using regular expressions and keyword scoring
- JSON-driven FAQ knowledge base ingestion from 'sample_faq.json'
- Conversational state management: greetings, FAQ inquiries, contextual fallbacks, exit
- Normalization (lowercasing, punctuation stripping, regex boundaries)
"""

import json
import os
import random
import re
import sys


class RuleBasedChatbot:
    def __init__(self, faq_file="sample_faq.json"):
        self.base_dir = os.path.dirname(os.path.abspath(__file__))
        self.faq_path = os.path.join(self.base_dir, faq_file)
        self.intents = []
        self.load_intents()

    def load_intents(self):
        """Loads intents, patterns, and responses from JSON dataset."""
        if os.path.exists(self.faq_path):
            try:
                with open(self.faq_path, "r", encoding="utf-8") as f:
                    data = json.load(f)
                    self.intents = data.get("intents", [])
            except Exception as e:
                print(f"[Warning] Failed loading FAQ JSON: {e}")
                self.intents = []
        else:
            print("[Warning] 'sample_faq.json' not found. Using internal fallback intents.")
            self.intents = []

    def normalize_input(self, text):
        """Cleans input text: lowercases and removes extraneous punctuation."""
        return re.sub(r"[^\w\s]", "", text.lower()).strip()

    def match_intent(self, user_input):
        """
        Calculates regex pattern match scores against all known intents.
        Returns the highest-scoring intent tag or None if no threshold is met.
        """
        normalized = self.normalize_input(user_input)
        if not normalized:
            return None

        best_tag = None
        best_score = 0

        for intent in self.intents:
            tag = intent["tag"]
            patterns = intent["patterns"]

            for pattern in patterns:
                # Regex match for word boundaries
                regex_pattern = r"\b" + re.escape(pattern.lower()) + r"\b"
                if re.search(regex_pattern, normalized):
                    # Direct phrase match has higher weight
                    score = len(pattern.split()) * 2
                    if score > best_score:
                        best_score = score
                        best_tag = tag

        return best_tag

    def get_response(self, tag):
        """Retrieves a random response matching the selected intent tag."""
        for intent in self.intents:
            if intent["tag"] == tag:
                return random.choice(intent["responses"])
        return self.get_fallback_response()

    def get_fallback_response(self):
        """Provides helpful fallback advice when user query confidence is low."""
        fallbacks = [
            "I'm not sure I understood that completely. You can ask me about our 'business hours', 'services', 'pricing', 'internship', or 'contact'.",
            "Could you please rephrase your question? Try asking about our 'services', 'internship requirements', or 'support email'.",
            "I didn't quite catch that. For direct human support, you can always reach out to hello@datheon.in."
        ]
        return random.choice(fallbacks)

    def run_conversation(self):
        """Runs the interactive conversational loop."""
        print("=================================================================")
        print("        DATHEON - INTERACTIVE TERMINAL AI ASSISTANT              ")
        print("=================================================================")
        print("Assistant: Hello! I am your Datheon Virtual Assistant.")
        print("           Ask me anything about Datheon services, hours, or internship.")
        print("           (Type 'quit', 'exit', or 'bye' to end the chat)\n")

        while True:
            try:
                user_msg = input("You: ").strip()
            except (EOFError, KeyboardInterrupt):
                print("\nAssistant: Goodbye! Session ended.")
                break

            if not user_msg:
                continue

            tag = self.match_intent(user_msg)

            if tag == "goodbye" or user_msg.lower() in ("exit", "quit", "bye"):
                print(f"Assistant: {self.get_response('goodbye')}")
                break

            if tag:
                reply = self.get_response(tag)
            else:
                reply = self.get_fallback_response()

            print(f"Assistant: {reply}\n")


def main():
    bot = RuleBasedChatbot()
    bot.run_conversation()


if __name__ == "__main__":
    main()
