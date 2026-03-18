# data.py — Smart Student Support Chatbot (v3)
# Keywords are now split into TIERS for priority weighting:
#
#   TIER 1 (weight 3) — exact, unambiguous, highly specific terms
#   TIER 2 (weight 2) — strong indicators, topic-specific but slightly broader
#   TIER 3 (weight 1) — general/contextual words that support a topic
#
# Scoring formula in app.py:
#   final_score = Σ(tier1_hits × 3) + Σ(tier2_hits × 2) + Σ(tier3_hits × 1)

KEYWORDS = {

    # ── EXAMS ──────────────────────────────────────────────────────
    "exam": {
        1: [  # dead giveaways
            "exam", "exams", "midterm", "finals", "end sem", "end-sem",
            "semester exam", "hall ticket", "admit card", "question paper",
            "answer key", "viva", "oral exam", "practical exam",
        ],
        2: [  # strong signals
            "test", "quiz", "assessment", "paper", "revision", "revise",
            "study for", "preparation", "prepare for", "mock test",
            "study plan", "last minute", "all nighter", "all-nighter",
            "cram", "cramming", "cheat sheet",
        ],
        3: [  # supporting context
            "study", "studying", "concentrate", "focus", "distracted",
            "nervous", "tomorrow", "tonight", "week", "syllabus done",
        ],
    },

    # ── RESULTS & GRADES ───────────────────────────────────────────
    "result": {
        1: [
            "result", "results", "scorecard", "marksheet", "cgpa", "gpa",
            "sgpa", "re-evaluation", "revaluation", "recheck", "rechecking",
            "declared", "grade card", "transcript",
        ],
        2: [
            "marks", "grade", "grades", "percentage", "pass", "fail",
            "failed", "failing", "topped", "rank", "merit list",
            "distinction", "backlog", "arrear", "detained",
        ],
        3: [
            "score", "performance", "report", "poor", "low marks",
            "didn't pass", "not cleared",
        ],
    },

    # ── SYLLABUS & CURRICULUM ──────────────────────────────────────
    "syllabus": {
        1: [
            "syllabus", "curriculum", "course outline", "course content",
            "unit plan", "lesson plan", "elective", "core subject",
        ],
        2: [
            "subject", "subjects", "topics", "chapters", "units",
            "module", "modules", "what to study", "important topics",
            "course structure", "credit", "credits",
        ],
        3: [
            "course", "learn", "learning", "study material",
            "what chapters", "which topics",
        ],
    },

    # ── INTERNSHIP & PLACEMENT ─────────────────────────────────────
    "internship": {
        1: [
            "internship", "internships", "intern", "placement", "placements",
            "campus recruitment", "off-campus", "on-campus", "ppo",
            "pre-placement offer", "job offer", "offer letter",
            "internshala", "linkedin job", "naukri",
        ],
        2: [
            "resume", "cv", "cover letter", "job", "jobs", "hire",
            "hiring", "recruit", "recruiting", "apply", "application",
            "interview", "technical round", "hr round", "aptitude test",
            "coding round", "leetcode", "hackerrank", "portfolio",
        ],
        3: [
            "career", "company", "startup", "mnc", "work experience",
            "skill", "skills", "project", "github", "opportunity",
        ],
    },

    # ── STRESS & MENTAL HEALTH ─────────────────────────────────────
    "stress": {
        1: [
            "stress", "anxiety", "anxious", "panic attack", "mental health",
            "depression", "depressed", "burnout", "breaking down",
            "cant cope", "can't cope", "overwhelmed", "suicidal",
            "counselling", "therapist", "therapy", "mental breakdown",
        ],
        2: [
            "worried", "worry", "panic", "exhausted", "exhaustion",
            "pressure", "hopeless", "helpless", "alone", "lonely",
            "nobody", "unmotivated", "demotivated", "no motivation",
            "crying", "crying myself", "cant sleep", "can't sleep",
            "insomnia", "scared", "fear", "nervous wreck",
        ],
        3: [
            "tired", "sad", "difficult", "struggle", "struggling",
            "hard time", "lost", "confused", "frustrated", "stuck",
            "help me", "need help", "i give up",
        ],
    },

    # ── ATTENDANCE ─────────────────────────────────────────────────
    "attendance": {
        1: [
            "attendance", "attendence", "shortage", "attendance shortage",
            "detain", "detained", "debarred", "proxy", "attendance portal",
            "attendance percentage", "minimum attendance",
        ],
        2: [
            "absent", "absences", "missed class", "missed lecture",
            "bunked", "bunk", "skipped class", "medical leave",
            "leave application", "leave letter",
        ],
        3: [
            "class", "lecture", "present", "absent", "skip",
            "miss", "going to college",
        ],
    },

    # ── ASSIGNMENTS & PROJECTS ─────────────────────────────────────
    "assignment": {
        1: [
            "assignment", "homework", "submission", "submit",
            "deadline", "due date", "overdue", "late submission",
            "extension", "plagiarism", "turnitin",
        ],
        2: [
            "project", "lab work", "practical", "report writing",
            "case study", "dissertation", "thesis", "mini project",
            "major project", "group project", "team project",
        ],
        3: [
            "due", "pending", "complete", "finish", "write",
            "stuck on", "can't finish", "haven't started",
        ],
    },

    # ── LIBRARY ────────────────────────────────────────────────────
    "library": {
        1: [
            "library", "librarian", "library card", "digital library",
            "e-library", "nptel", "swayam", "jstor", "ieee xplore",
            "springer", "elsevier",
        ],
        2: [
            "book", "books", "borrow", "return book", "renew book",
            "journal", "research paper", "e-book", "textbook",
            "reference book", "due fine", "overdue book",
        ],
        3: [
            "read", "reading", "resource", "material", "pdf",
            "online book", "study room",
        ],
    },

    # ── FEES & FINANCE ─────────────────────────────────────────────
    "fees": {
        1: [
            "fees", "fee", "tuition fee", "hostel fee", "exam fee",
            "scholarship", "scholarships", "stipend", "financial aid",
            "nsp", "national scholarship", "fee waiver", "fee concession",
        ],
        2: [
            "payment", "pay fees", "online payment", "challan",
            "receipt", "refund", "fine", "penalty", "due amount",
            "installment", "emi",
        ],
        3: [
            "money", "cost", "expensive", "afford", "financial",
            "broke", "no money", "loan", "education loan",
        ],
    },

    # ── TIMETABLE & SCHEDULE ───────────────────────────────────────
    "timetable": {
        1: [
            "timetable", "time table", "class schedule", "lecture schedule",
            "exam schedule", "date sheet", "academic calendar",
        ],
        2: [
            "schedule", "routine", "class timing", "when is my class",
            "what time", "which day", "lab schedule", "free period",
        ],
        3: [
            "when", "timing", "today's class", "tomorrow's class",
            "week plan", "daily plan",
        ],
    },

    # ── FACULTY & STAFF ────────────────────────────────────────────
    "faculty": {
        1: [
            "faculty", "professor", "hod", "head of department",
            "principal", "dean", "class advisor", "mentor",
            "faculty advisor", "office hours",
        ],
        2: [
            "teacher", "lecturer", "instructor", "guide",
            "contact professor", "email professor", "meet teacher",
            "appointment", "feedback",
        ],
        3: [
            "sir", "madam", "staff", "department", "academic",
            "complain about", "report to",
        ],
    },

    # ── GREETINGS ──────────────────────────────────────────────────
    "hello": {
        1: [
            "hello", "hi", "hey", "howdy", "yo",
            "good morning", "good afternoon", "good evening", "good night",
        ],
        2: [
            "what's up", "whats up", "sup", "how are you",
            "how r u", "hru", "greetings",
        ],
        3: [
            "start", "begin", "help", "anyone there", "you there",
        ],
    },

    # ── THANKS ─────────────────────────────────────────────────────
    "thanks": {
        1: [
            "thank you", "thanks", "thank u", "many thanks",
            "much appreciated", "thx", "ty",
        ],
        2: [
            "appreciate", "grateful", "helpful", "helped me",
            "that helped", "got it", "understood",
        ],
        3: [
            "great", "awesome", "perfect", "nice", "good job",
            "well done", "brilliant",
        ],
    },

    # ── FAREWELL ───────────────────────────────────────────────────
    "bye": {
        1: [
            "bye", "goodbye", "good bye", "see you", "see ya",
            "cya", "farewell", "take care",
        ],
        2: [
            "later", "talk later", "catch you later", "ttyl",
            "signing off", "logging off",
        ],
        3: [
            "leaving", "done for today", "that's all", "nothing else",
        ],
    },
}


# ── ANSWERS ────────────────────────────────────────────────────────
ANSWERS = {
    "exam": (
        "📚 Exams can feel daunting, but you've got this! Here are some tips:\n"
        "• Review past papers — they're your best predictor of what's coming.\n"
        "• Use the Pomodoro method: 45 min study → 10 min break.\n"
        "• Focus on understanding concepts, not just memorising.\n"
        "• Prioritise topics by marks weightage in the syllabus.\n"
        "• Get 7–8 hours of sleep before the exam — rest beats last-minute cramming.\n"
        "• Check your hall ticket / admit card well in advance!\n"
        "Need help with a specific subject or topic?"
    ),
    "result": (
        "📊 Checking results? Here's the deal:\n"
        "• Results are published on the official university/college portal — check there first.\n"
        "• If unsatisfied, apply for re-evaluation or re-checking within the deadline.\n"
        "• Got a backlog/arrear? Don't panic — plan your supplementary exam immediately.\n"
        "• One bad grade doesn't define your journey — focus on consistent improvement.\n"
        "• Talk to your faculty about weak areas and how to recover.\n"
        "• Your CGPA matters, but skills, projects, and attitude matter equally to employers!"
    ),
    "syllabus": (
        "📋 Looking for syllabus info? Here's how to get it:\n"
        "• Check your institution's website, LMS, or student portal.\n"
        "• Ask your faculty or class representative — they're the fastest sources.\n"
        "• Senior students often share important topics and previous years' papers.\n"
        "• Identify high-weightage units early and plan study time accordingly.\n"
        "• For electives, compare syllabi before choosing — pick what excites you!"
    ),
    "internship": (
        "💼 Smart move thinking about internships! Here's your roadmap:\n"
        "• Keep your resume/CV to one page — achievement-focused, not task-focused.\n"
        "• Start with Internshala, LinkedIn, AngelList, and your campus placement cell.\n"
        "• Apply 2–3 months before the term you want to intern — companies open early.\n"
        "• Practice DSA on LeetCode / HackerRank for technical interviews.\n"
        "• Prepare a 2-minute self-introduction and common HR questions.\n"
        "• Build a GitHub portfolio — even 2–3 good projects make a huge difference.\n"
        "• A PPO (Pre-Placement Offer) is possible — treat every internship like a job interview!\n"
        "Want tips on a specific field or company type?"
    ),
    "stress": (
        "💙 Hey, I hear you — and it's completely okay to feel this way.\n"
        "Student life is genuinely hard sometimes, and your feelings are valid.\n\n"
        "Here are some things that can help right now:\n"
        "• Take one slow, deep breath. In for 4 counts, out for 6. Seriously — try it.\n"
        "• Talk to someone you trust — a friend, family member, or counsellor.\n"
        "• Break the overwhelming thing into the smallest possible next step.\n"
        "• Step away for 10 minutes — walk, stretch, get water. Your brain needs it.\n"
        "• Your institution's counselling cell is there for exactly this. Please reach out.\n\n"
        "You don't have to figure everything out today. One step at a time. 🌱\n"
        "You matter more than any grade or deadline."
    ),
    "attendance": (
        "🗓️ Attendance worries? Here's what you can do:\n"
        "• Check your exact attendance percentage on the student portal right now.\n"
        "• If below the required threshold (usually 75%), speak to your faculty/advisor ASAP.\n"
        "• Submit a medical certificate or valid reason — many colleges consider it.\n"
        "• Write a formal leave letter addressed to the HOD if needed.\n"
        "• Going forward: even 1–2 classes per day adds up — don't let it snowball.\n"
        "• Ask your CR to mark you present if you're participating remotely (where allowed)."
    ),
    "assignment": (
        "📝 Deadline creeping up? Let's handle this:\n"
        "• List all pending submissions and sort them by due date — tackle shortest first.\n"
        "• If you're stuck, ask classmates or post in your college group — collaborate.\n"
        "• Email your professor politely for an extension — most appreciate communication.\n"
        "• Avoid plagiarism — paraphrase, cite properly, and use your own words.\n"
        "• Tools: Google Docs for collaboration, Notion for task tracking, Grammarly for polish.\n"
        "• Submit even an incomplete version — partial marks beat zero every time."
    ),
    "library": (
        "📖 Library queries — happy to help!\n"
        "• Your library likely has both physical books and digital subscriptions (IEEE, Springer, etc.).\n"
        "• Ask the librarian about interlibrary loans if a specific book isn't in stock.\n"
        "• Free alternatives: NPTEL, SWAYAM, MIT OpenCourseWare, Google Scholar.\n"
        "• Track your due dates — overdue fines add up quickly!\n"
        "• Use quiet study rooms in the library for focused, distraction-free sessions.\n"
        "• Download papers via Sci-Hub or ResearchGate when institutional access isn't available."
    ),
    "fees": (
        "💰 Fee-related concerns — here's where to start:\n"
        "• Visit the accounts / finance office for official dues and payment procedures.\n"
        "• Check eligibility for scholarships: government (NSP), merit-based, or need-based.\n"
        "• NSP (National Scholarship Portal) lists dozens of central and state schemes.\n"
        "• Education loans are available via nationalised banks at subsidised interest rates.\n"
        "• If facing hardship, speak to the Student Welfare Office — many colleges have emergency funds.\n"
        "• Always keep digital + physical copies of every payment receipt."
    ),
    "timetable": (
        "🕐 Looking for your timetable?\n"
        "• Check your institution's student portal or LMS — it's usually posted there.\n"
        "• Your CR (class representative) shares updates on WhatsApp / Telegram groups.\n"
        "• The department notice board is a reliable offline source.\n"
        "• For exam date sheets, check the official university website.\n"
        "• If there are clashes or errors, report them to your faculty advisor immediately."
    ),
    "faculty": (
        "👩‍🏫 Want to connect with a faculty member?\n"
        "• Find contact details and office hours on your institution's official website.\n"
        "• Email is the most professional approach — subject line: [Name | Class | Query].\n"
        "• Be specific and polite — mention your name, roll number, and exact question.\n"
        "• For academic complaints, escalate to the HOD only after trying the faculty first.\n"
        "• Faculty are generally more responsive during working hours (10 AM – 4 PM)."
    ),
    "hello": (
        "👋 Hey there! I'm StudyBot — your Smart Student Support Chatbot.\n"
        "I can help you with exams, assignments, internships, attendance, stress, fees, and more.\n"
        "What's on your mind today?"
    ),
    "thanks": (
        "😊 You're very welcome! Really glad I could help.\n"
        "Come back any time you have questions — good luck out there! 🍀"
    ),
    "bye": (
        "👋 Take care! Remember — every day is a fresh start.\n"
        "Come back anytime you need help. You've got this! 💪"
    ),
}

FALLBACK = (
    "🤔 Hmm, I'm not quite sure about that one.\n"
    "I can help with topics like:\n"
    "• Exams, results & syllabus\n"
    "• Internships & placements\n"
    "• Stress & mental wellness\n"
    "• Attendance, assignments, fees, library & faculty\n"
    "• Timetable & scheduling\n\n"
    "Could you rephrase your question? I'll do my best to help!"
)
