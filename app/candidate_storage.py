def candidate_storage(filename, analysis):
    with open(filename, "a", encoding="utf-8") as file:
        file.write(f"""
Summary:
{analysis.summary}

Score:
{analysis.score}

Role:
{analysis.recommended_role}

-------------------\n\n
""")