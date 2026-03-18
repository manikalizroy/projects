# 🎓 StudyBot — Smart Student Support Chatbot

A lightweight, beginner-friendly Flask chatbot that answers common student queries using keyword matching — no ML, no external APIs.

---

## 📁 Project Structure

```
chatbot/
├── app.py              ← Flask backend (routes + matching logic)
├── data.py             ← Keywords + responses dictionary
├── requirements.txt    ← Python dependencies
└── templates/
    └── index.html      ← Complete frontend (HTML + CSS + JS)
```

---

## 🚀 How to Run

### 1. Install dependencies
```bash
pip install -r requirements.txt
```

### 2. Start the server
```bash
python app.py
```

### 3. Open in your browser
```
http://127.0.0.1:5000
```

---

## 💬 Supported Topics

| Topic       | Example Query                            |
|-------------|------------------------------------------|
| Exams       | "How do I prepare for my finals?"        |
| Internship  | "How do I apply for internships?"        |
| Stress      | "I'm feeling overwhelmed and anxious"    |
| Attendance  | "My attendance is low, what do I do?"    |
| Assignment  | "I have a deadline tomorrow"             |
| Syllabus    | "Where can I find the syllabus?"         |
| Result      | "How do I check my CGPA?"               |
| Library     | "Can I borrow books from the library?"   |
| Fees        | "Is there a scholarship I can apply for?"|
| Timetable   | "When are my classes this week?"         |
| Faculty     | "How do I contact my professor?"         |

---

## 🛠️ How It Works

1. User types a message in the browser
2. JavaScript sends it to `/chat` via `fetch` (POST)
3. Flask calls `get_response()` which:
   - Lowercases the input
   - Checks for keyword matches against `RESPONSES` dict in `data.py`
   - Returns the matched answer or a friendly fallback
4. Response is displayed as a chat bubble

---

## ➕ Extending the Bot

To add a new topic (e.g., "hostel"):

**In `data.py`:**
```python
RESPONSES["hostel"] = ["hostel", "dorm", "room", "accommodation", "warden"]
ANSWERS["hostel"]   = "🏠 For hostel queries, contact the warden's office..."
```

That's it — no other changes needed!
