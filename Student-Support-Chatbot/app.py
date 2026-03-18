# app.py — Smart Student Support Chatbot (v3)
# Fixed: unified scoring engine, tiered weights, logging, category tag

import re
import datetime
from flask import Flask, render_template, request, jsonify
from data import KEYWORDS, ANSWERS, FALLBACK

app = Flask(__name__)

# ─────────────────────────────────────────────────────────────────
# TIER WEIGHTS
#   Tier 1 — highly specific, unambiguous keywords  → 3 points each
#   Tier 2 — strong topic signals                   → 2 points each
#   Tier 3 — supporting / contextual words          → 1 point each
# ─────────────────────────────────────────────────────────────────
TIER_WEIGHTS = {1: 3, 2: 2, 3: 1}


def score_category(text: str, tier_keywords: dict) -> int:
    """
    Score a single category against the user's text using tier weights.

    - Tier 1 hit = 3 pts  (e.g. "cgpa", "panic attack", "internshala")
    - Tier 2 hit = 2 pts  (e.g. "resume", "grade", "missed class")
    - Tier 3 hit = 1 pt   (e.g. "study", "tired", "company")

    Uses left-boundary regex (\b prefix) so:
      "stress" matches "stressed", "stressful"
      "exam"   matches "exams", "examination"
      "hi"     does NOT false-match inside "this" or "white"
    """
    total = 0
    for tier, weight in TIER_WEIGHTS.items():
        for kw in tier_keywords.get(tier, []):
            if " " in kw:                           # multi-word phrase
                if kw in text:
                    total += weight
            else:                                   # single word
                if re.search(r"\b" + re.escape(kw), text):
                    total += weight
    return total


def get_response(user_input: str) -> dict:
    """
    Score every category with weighted keyword matching and return
    the best match together with its score and full scoreboard.

    Flow:
      1. Lowercase + strip input
      2. Score all categories using score_category()
      3. Pick the highest-scoring category
      4. Return response, category name, score, and full scoreboard
    """
    text = user_input.lower().strip()

    best_category = None
    best_score    = 0
    all_scores    = {}          # full scoreboard — used in terminal log

    for category, tier_keywords in KEYWORDS.items():
        score = score_category(text, tier_keywords)
        all_scores[category] = score
        if score > best_score:
            best_score    = score
            best_category = category

    if best_category and best_score > 0:
        response = ANSWERS[best_category]
        category = best_category
    else:
        response = FALLBACK
        category = "unknown"

    return {
        "response":   response,
        "category":   category,
        "score":      best_score,
        "scoreboard": all_scores,
    }


# ─────────────────────────────────────────────────────────────────
# INTERACTION LOGGING
# Prints timestamp, user input, matched category, weighted score,
# and top-3 competing categories to the terminal on every message.
# ─────────────────────────────────────────────────────────────────

def log_interaction(user_input: str, result: dict) -> None:
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    top3 = sorted(result["scoreboard"].items(), key=lambda x: x[1], reverse=True)[:3]
    top3_str = "  |  ".join(f"{cat}: {sc}" for cat, sc in top3 if sc > 0)

    print()
    print(f"[{timestamp}]")
    print(f"  User      : {user_input}")
    print(f"  Matched   : {result['category']}  (weighted score: {result['score']})")
    print(f"  Top scores: {top3_str or 'none — fallback triggered'}")
    print(f"  Bot       : {result['response'][:75].strip()}...")
    print("-" * 65)


# ─────────────────────────────────────────────────────────────────
# Routes
# ─────────────────────────────────────────────────────────────────

@app.route("/")
def index():
    return render_template("index.html")


@app.route("/chat", methods=["POST"])
def chat():
    data         = request.get_json()
    user_message = data.get("message", "").strip()

    if not user_message:
        return jsonify({
            "response": "Please type something so I can help you! 😊",
            "category": "empty",
            "score":    0,
        })

    result = get_response(user_message)
    log_interaction(user_message, result)

    # Send response + category + score to frontend (not the full scoreboard)
    return jsonify({
        "response": result["response"],
        "category": result["category"],
        "score":    result["score"],
    })


if __name__ == "__main__":
    total_keywords = sum(
        len(kws) for cat in KEYWORDS.values() for kws in cat.values()
    )
    print("=" * 65)
    print(f"  StudyBot v3 — Tiered Priority Weighting ACTIVE")
    print(f"  {total_keywords} keywords across {len(KEYWORDS)} categories")
    print(f"  Weights  : Tier1 = x3  |  Tier2 = x2  |  Tier3 = x1")
    print(f"  Logging  : ON  |  Port: 55000")
    print("=" * 65)
    app.run(debug=True, port=55000)

