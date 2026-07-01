# how do we talk to the API?
def build_resume_prompt(resume_text):
    return f"""
You are an experienced technical recruiter looking for a new mid-level Java Software Engineer.

Analyze the following resume.

Return ONLY valid JSON.

Also score the candidate from 0-100.

Use this format:

{{
    "summary": "",
    "skills": [],
    "years_experience": "",
    "recommended_role": "",
    "score": 0
}}

Resume:

{resume_text}
"""