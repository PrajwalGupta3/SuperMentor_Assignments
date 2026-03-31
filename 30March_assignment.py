# Assignment Name : Prompt Engineer
# Description : Write prompts for resume, business idea, study plan and compare weak vs strong prompts.

"""
This assignment compares weak (vague) prompts vs strong (well-engineered) prompts
for three tasks: Resume Writing, Business Idea Generation, and Study Plan Creation.
Each section shows both prompts, their expected outputs, and explains why the
strong prompt produces better results.
"""

prompt_comparisons = [
    {
        "task": "1. RESUME WRITING",
        "weak_prompt": "Write me a resume.",
        "strong_prompt": (
            "Act as a professional resume writer with 10 years of experience. "
            "Write a one-page resume for a Computer Science fresh graduate applying "
            "for a Junior Software Developer role at a tech startup. Include sections: "
            "Professional Summary (3 lines), Education (B.Tech in CS from XYZ University, "
            "GPA 8.5), Skills (Python, JavaScript, React, SQL, Git), 2 academic projects "
            "(an e-commerce website and a chatbot using NLP), and certifications (AWS Cloud "
            "Practitioner). Use action verbs and quantify achievements where possible. "
            "Format it in a clean, ATS-friendly style."
        ),
        "weak_output": (
            "The AI generates a generic resume template with placeholder text like "
            "'[Your Name]', '[Your Experience]'. It has no specific skills, no tailored "
            "summary, and the format may not be ATS-friendly. The result requires significant "
            "manual editing to be usable."
        ),
        "strong_output": (
            "The AI generates a complete, ready-to-use resume with a tailored professional "
            "summary, specific skills listed, detailed project descriptions with quantified "
            "achievements (e.g., 'Built an e-commerce platform handling 500+ products with "
            "React and Node.js'), proper ATS formatting, and a professional tone throughout."
        ),
        "why_better": (
            "The strong prompt provides: (1) a specific role/persona for the AI, (2) concrete "
            "details to include, (3) specific formatting requirements, (4) measurable criteria "
            "like 'action verbs' and 'quantify achievements'. This eliminates guesswork and "
            "produces a targeted, high-quality output."
        ),
    },
    {
        "task": "2. BUSINESS IDEA GENERATION",
        "weak_prompt": "Give me a business idea.",
        "strong_prompt": (
            "I have a budget of $5,000 and 3 months of free time. I am a computer science "
            "student skilled in Python, web development, and machine learning. I live in a "
            "Tier-2 city in India. Suggest 3 realistic online business ideas that: (1) can be "
            "started solo, (2) have low overhead costs, (3) can generate $500-$1000/month "
            "within 3 months, (4) leverage my tech skills. For each idea, provide: a one-line "
            "description, startup steps, estimated costs, revenue model, and potential risks."
        ),
        "weak_output": (
            "The AI responds with vague, generic suggestions like 'Start a restaurant', "
            "'Open an online store', or 'Become a freelancer' — with no details about "
            "budget, skills, location, or timeline. The ideas are not actionable."
        ),
        "strong_output": (
            "The AI provides 3 specific, actionable ideas like: (1) SaaS micro-tool for "
            "local businesses — detailed steps, $500 hosting costs, subscription revenue model; "
            "(2) AI-powered content writing service — using GPT APIs, freelance marketplace "
            "strategy; (3) Online coding bootcamp for beginners — curriculum outline, pricing "
            "strategy. Each includes startup costs, timeline, and risk assessment."
        ),
        "why_better": (
            "The strong prompt constrains the problem with specific parameters (budget, skills, "
            "location, timeline, revenue target). It also specifies the OUTPUT FORMAT (description, "
            "steps, costs, revenue, risks) so the AI knows exactly what structure to follow. "
            "Constraints lead to creativity within boundaries, producing practical ideas."
        ),
    },
    {
        "task": "3. STUDY PLAN CREATION",
        "weak_prompt": "Help me study for exams.",
        "strong_prompt": (
            "Create a 2-week study plan for a 3rd-year Computer Science student preparing for "
            "end-semester exams in 4 subjects: Data Structures & Algorithms, Database Management "
            "Systems, Operating Systems, and Computer Networks. I can study 6 hours per day. "
            "My weak subjects are OS and CN. My exams start on April 15, with one exam every "
            "2 days. Use the Pomodoro technique (25 min study + 5 min break). Include: daily "
            "schedule with time slots, which topics to cover each day, revision days before "
            "each exam, and one practice test per subject. Prioritize weak subjects but don't "
            "neglect strong ones."
        ),
        "weak_output": (
            "The AI gives a generic response like 'Study a few hours each day, take breaks, "
            "review your notes, and do practice questions.' No specific schedule, no subject "
            "allocation, no consideration of weak areas or exam dates."
        ),
        "strong_output": (
            "The AI creates a detailed day-by-day plan: Day 1-3 focused on OS (weak subject) "
            "covering process scheduling, memory management, file systems; Day 4-5 on CN "
            "(weak) covering OSI model, TCP/IP, subnetting; Day 6-7 mixed DSA and DBMS; "
            "Day 8-13 cycling through subjects with revision; Day 14 light review. Each day "
            "has 6 hours broken into Pomodoro slots with specific topics per slot. Includes "
            "practice test dates aligned with exam schedule."
        ),
        "why_better": (
            "The strong prompt provides: (1) specific subjects and their difficulty levels, "
            "(2) available study hours, (3) exam schedule for proper planning, (4) a specific "
            "study technique (Pomodoro), (5) desired output structure. The AI can now create "
            "a plan that accounts for all constraints, rather than giving generic study advice."
        ),
    },
]

# Print all comparisons
print("=" * 70)
print("        PROMPT ENGINEERING — WEAK vs STRONG PROMPTS")
print("=" * 70)

def print_wrapped(text, indent=4, width=66):
    """Helper to print text wrapped at a given width."""
    words = text.split()
    line = " " * indent
    for word in words:
        if len(line) + len(word) + 1 > width:
            print(line)
            line = " " * indent + word
        else:
            line += " " + word if line.strip() else " " * indent + word
    if line.strip():
        print(line)

for comp in prompt_comparisons:
    print(f"\n{'━' * 70}")
    print(f"  {comp['task']}")
    print(f"{'━' * 70}")

    print(f"\n  ❌ WEAK PROMPT:")
    print(f"    \"{comp['weak_prompt']}\"")

    print(f"\n  ✅ STRONG PROMPT:")
    print_wrapped(f"\"{comp['strong_prompt']}\"")

    print(f"\n  ❌ WEAK PROMPT OUTPUT:")
    print_wrapped(comp['weak_output'])

    print(f"\n  ✅ STRONG PROMPT OUTPUT:")
    print_wrapped(comp['strong_output'])

    print(f"\n  💡 WHY THE STRONG PROMPT IS BETTER:")
    print_wrapped(comp['why_better'])

# Key Principles
print(f"\n{'━' * 70}")
print(f"\n{'=' * 70}")
print("  KEY PROMPT ENGINEERING PRINCIPLES")
print("=" * 70)
print("""
  1. BE SPECIFIC — Instead of 'write a resume', specify the role, skills,
     experience level, and desired format.

  2. PROVIDE CONTEXT — Tell the AI who you are, what you need, and why.
     Context reduces ambiguity and improves relevance.

  3. ASSIGN A ROLE — 'Act as a professional resume writer' gives the AI
     a persona to emulate, improving tone and expertise.

  4. DEFINE OUTPUT FORMAT — Specify structure (bullet points, sections,
     tables) so the AI knows exactly what to produce.

  5. SET CONSTRAINTS — Budget, timeline, word count, difficulty level.
     Constraints paradoxically improve creativity within boundaries.

  6. USE EXAMPLES — When possible, show the AI what good output looks
     like (few-shot prompting) for even better results.

  7. ITERATE — Strong prompts often require 2-3 refinements. Start with
     a good prompt, evaluate the output, and refine further.

  Formula for a strong prompt:
  ┌─────────────────────────────────────────────────────────────┐
  │ Role + Context + Task + Format + Constraints = Great Output │
  └─────────────────────────────────────────────────────────────┘
""")
