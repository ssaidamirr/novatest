import streamlit as st

st.set_page_config(page_title="Candidate Test", page_icon="✅", layout="centered")

TOTAL_QUESTIONS = 30


def score_to_code(score: int) -> str:
    if score >= 28:
        return "OIJVBN"
    if 25 <= score <= 27:
        return "OBRTB"
    if 20 <= score <= 24:
        return "IUYTH"
    if 18 <= score <= 19:
        return "GFTYU"
    return "UHGTY"


QUESTIONS = [
    {
        "id": 1,
        "text": "It is 2:10pm. A deliverable is due 6:00pm. You discover a critical missing input that only one person can provide, and they often reply late. Best move?",
        "A": "Keep working on other parts and message them later so you do not bother them",
        "B": "Message them now with a clear ask, deadline, and fallback assumptions, and start a parallel plan",
        "C": "Wait 30 minutes, then message if they still have not sent it",
    },
    {
        "id": 2,
        "text": "You realize you misunderstood a requirement yesterday and built the wrong version. Nobody noticed yet. Best move?",
        "A": "Quietly fix it and deliver the corrected version without mentioning the mistake",
        "B": "Inform your manager immediately with what happened, what you fixed, and how you will prevent repeats",
        "C": "Ask a coworker to review it first, then decide whether to tell your manager",
    },
    {
        "id": 3,
        "text": "You have two tasks. Task 1 affects a deadline tomorrow. Task 2 affects a long term improvement. You have 90 minutes. Best approach?",
        "A": "Start Task 2 because it prevents future problems",
        "B": "Finish the highest deadline risk item first, then spend remaining time on the long term item",
        "C": "Split time 45 and 45 so both advance",
    },
    {
        "id": 4,
        "text": "You are asked to \"make it look professional.\" No other details. Deadline is tight. Best move?",
        "A": "Ask for examples, audience, and format, then propose a quick structure and proceed if no reply",
        "B": "Wait until you get full clarity so you do not waste effort",
        "C": "Use your personal taste and deliver without asking questions",
    },
    {
        "id": 5,
        "text": "A teammate gives you data that seems inconsistent. If wrong, the output could mislead. Best move?",
        "A": "Assume it is correct because they own the data",
        "B": "Validate key totals and logic, flag inconsistencies with evidence, and ask for confirmation",
        "C": "Use it as is, but add a note that data quality is unknown",
    },
    {
        "id": 6,
        "text": "You notice a small error in a file name after sending it. It does not change content, but hurts organization. Best move?",
        "A": "Ignore it, it is too small",
        "B": "Correct it and notify the recipient with the updated link and a short reason",
        "C": "Rename only locally so your folders are clean",
    },
    {
        "id": 7,
        "text": "You have to send a status update to your manager. You made little progress because of blockers. Best update?",
        "A": "\"Blocked. Could not do much today.\"",
        "B": "\"Blocked by X. I tried Y and Z. Next action is W. If no reply by 3pm, I will do fallback plan.\"",
        "C": "\"Everything is fine, will be done soon.\"",
    },
    {
        "id": 8,
        "text": "Someone asks you for an answer you do not know. Deadline in 1 hour. Best move?",
        "A": "Give your best guess confidently so they can move fast",
        "B": "State what you know, what you do not know, and take a quick action to verify while proposing a safe interim choice",
        "C": "Tell them you do not know and stop there",
    },
    {
        "id": 9,
        "text": "You get 6 tasks at once. Your manager says \"handle it.\" Best first step?",
        "A": "Start executing the easiest tasks to build momentum",
        "B": "Ask one clarifying question: rank by urgency and impact, then propose your priority order and start",
        "C": "Pick the task you personally enjoy most and do it well",
    },
    {
        "id": 10,
        "text": "You are in charge of a recurring workflow. A mistake repeats twice in a month. Best response?",
        "A": "Remind everyone to be more careful",
        "B": "Add a simple system change: checklist, template, validation step, or automation, and document it",
        "C": "Accept that mistakes happen and move on",
    },
    {
        "id": 11,
        "text": "A task is 90 percent done. The last 10 percent requires polishing. Deadline is close. Best choice?",
        "A": "Keep polishing until it is perfect, even if late",
        "B": "Deliver on time with acceptable quality, and schedule a quick improvement pass if needed",
        "C": "Delay delivery until it meets your personal standard",
    },
    {
        "id": 12,
        "text": "You are asked to do something that feels unnecessary, but it is low effort and may help. Best move?",
        "A": "Refuse, it is not efficient",
        "B": "Do it quickly if it does not harm priorities, and mention a better alternative for next time",
        "C": "Do it, but complain about it to show you understand priorities",
    },
    {
        "id": 13,
        "text": "You realize a dependency is late and might cause a miss. Best escalation timing?",
        "A": "Escalate only after it actually becomes late",
        "B": "Escalate as soon as risk is clear, with evidence and options",
        "C": "Escalate immediately even without trying anything yourself",
    },
    {
        "id": 14,
        "text": "You are given a vague instruction that could be interpreted two ways. Wrong interpretation creates rework. Best move?",
        "A": "Choose one interpretation and proceed fast",
        "B": "Ask a targeted question, then proceed with a stated assumption if no reply within a set time",
        "C": "Pause all work until you get a response",
    },
    {
        "id": 15,
        "text": "You sent a message to a stakeholder. No reply for 24 hours. Deadline is 48 hours away. Best follow-up?",
        "A": "Send a second message that restates the question and deadline, plus a default option if no reply by a specific time",
        "B": "Wait, they are busy, do not seem annoying",
        "C": "Message their manager immediately",
    },
    {
        "id": 16,
        "text": "Someone asks you to \"handle it\" but you do not have permission for a key action. Best move?",
        "A": "Do it anyway to show ownership",
        "B": "Explain the permission gap and propose two paths: request approval or adjust scope",
        "C": "Drop the task",
    },
    {
        "id": 17,
        "text": "You notice two tasks conflict. Completing one will harm the other. Best move?",
        "A": "Do both and hope it works out",
        "B": "Flag the tradeoff, propose a recommendation, and ask for a decision if needed",
        "C": "Choose one without telling anyone",
    },
    {
        "id": 18,
        "text": "You are asked to produce a summary. You can either be fast or be accurate, not both, given time. Best move?",
        "A": "Be fast, accuracy can be fixed later",
        "B": "Be accurate on the most decision-critical parts, and clearly label what is approximate",
        "C": "Be accurate on everything even if late",
    },
    {
        "id": 19,
        "text": "You are working with a template. You see a better way to format it. Deadline is close. Best move?",
        "A": "Keep template unchanged and ship",
        "B": "Ship using template now, then propose improvement after deadline",
        "C": "Stop and redesign the template before shipping",
    },
    {
        "id": 20,
        "text": "You spot a risk that your manager missed. Mentioning it may cause tension. Best move?",
        "A": "Stay quiet to avoid conflict",
        "B": "Raise it calmly with specifics, impact, and a solution",
        "C": "Tell others instead of your manager",
    },
    {
        "id": 21,
        "text": "You are handed a messy folder with inconsistent naming and duplicates. Best first action?",
        "A": "Start renaming everything immediately",
        "B": "Create a structure, define naming rules, then batch organize with a quick audit",
        "C": "Delete duplicates and keep only the latest by guess",
    },
    {
        "id": 22,
        "text": "A stakeholder requests something outside scope and it would break your deadline. Best move?",
        "A": "Say yes and work overtime silently",
        "B": "Offer a trade: what can be delivered by deadline vs what must move later, and confirm",
        "C": "Refuse without explanation",
    },
    {
        "id": 23,
        "text": "You are asked to take notes for a meeting. Best practice?",
        "A": "Write everything verbatim",
        "B": "Capture decisions, owners, deadlines, and open questions, then send a short recap",
        "C": "Take no notes, meeting recordings exist",
    },
    {
        "id": 24,
        "text": "You receive a complaint that your output is confusing. Best response?",
        "A": "Defend your work, they should read more carefully",
        "B": "Ask what confused them, revise structure for clarity, and add a short guide for reuse",
        "C": "Ignore the complaint, it is subjective",
    },
    {
        "id": 25,
        "text": "You must choose between asking a question now vs making an assumption and moving. Best heuristic?",
        "A": "Assume whenever possible, questions slow things down",
        "B": "Ask if wrong assumption causes high rework or risk, otherwise assume and state it clearly",
        "C": "Always ask, assumptions are unprofessional",
    },
    {
        "id": 26,
        "text": "You are working on a process. You notice it has no clear \"done\" definition, causing endless work. Best move?",
        "A": "Keep working until told to stop",
        "B": "Define a \"done checklist\" and align it with your manager",
        "C": "Stop the process entirely",
    },
    {
        "id": 27,
        "text": "You deliver a draft and get vague feedback: \"Not it.\" Best next step?",
        "A": "Rewrite everything from scratch",
        "B": "Ask 2 to 3 pointed questions and propose 2 alternative directions quickly",
        "C": "Wait until they give clearer feedback",
    },
    {
        "id": 28,
        "text": "You see an opportunity to automate a repetitive task, but you are very busy this week. Best move?",
        "A": "Ignore automation forever, you are busy",
        "B": "Note it, and schedule a small time box later, like 30 minutes, to implement a minimal improvement",
        "C": "Pause urgent work to build a full automation now",
    },
    {
        "id": 29,
        "text": "You are asked for an ETA, but there is uncertainty. Best answer?",
        "A": "Give a confident time that sounds good",
        "B": "Give a range with assumptions, plus the next check-in point",
        "C": "Refuse to estimate",
    },
    {
        "id": 30,
        "text": "You made an error that impacted someone. Best approach?",
        "A": "Apologize and explain why it was not your fault",
        "B": "Own it, fix it fast, communicate the fix, and implement a prevention step",
        "C": "Fix it quietly and hope they do not notice",
    },
]

ANSWER_KEY = {
    1: "B", 2: "B", 3: "B", 4: "A", 5: "B", 6: "B", 7: "B", 8: "B", 9: "B", 10: "B",
    11: "B", 12: "B", 13: "B", 14: "B", 15: "A", 16: "B", 17: "B", 18: "B", 19: "B", 20: "B",
    21: "B", 22: "B", 23: "B", 24: "B", 25: "B", 26: "B", 27: "B", 28: "B", 29: "B", 30: "B",
}


def compute_score(answers: dict) -> int:
    score = 0
    for qid, correct in ANSWER_KEY.items():
        if answers.get(qid) == correct:
            score += 1
    return score


def reset_test() -> None:
    st.session_state.submitted = False
    st.session_state.result_code = None
    st.session_state.candidate_name = ""


def main() -> None:
    if "submitted" not in st.session_state:
        reset_test()

    st.title("Candidate Situational Test")

    if st.session_state.submitted:
        st.markdown("### Your result code")
        st.markdown(f"## **{st.session_state.result_code}**")
        st.caption("Send this code to the hiring manager.")
        if st.button("Start over"):
            reset_test()
            st.rerun()
        return

    name = st.text_input(
        "Candidate name",
        max_chars=80,
        placeholder="Type your full name",
        key="candidate_name",
    )

    st.divider()

    answers = {}

    with st.form("test_form", clear_on_submit=False):
        st.markdown("## Questions")

        for q in QUESTIONS:
            qid = q["id"]
            letters = ["A", "B", "C"]

            def fmt(letter: str, qq=q) -> str:
                return f"{letter}) {qq[letter]}"

            choice = st.radio(
                label=f"{qid}. {q['text']}",
                options=letters,
                index=None,
                format_func=fmt,
                key=f"q_{qid}",
            )
            answers[qid] = choice
            st.write("")

        submitted = st.form_submit_button("Submit")

    if submitted:
        if not name or not name.strip():
            st.error("Please enter your name before submitting.")
            return

        if not all(answers.get(i) in ("A", "B", "C") for i in range(1, TOTAL_QUESTIONS + 1)):
            st.error("Please answer all questions before submitting.")
            return

        score = compute_score(answers)
        code = score_to_code(score)

        st.session_state.submitted = True
        st.session_state.result_code = code
        st.rerun()


if __name__ == "__main__":
    main()
