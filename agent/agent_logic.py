import requests
import os
from agent.tools import read_file, write_file

GROQ_API_KEY = os.getenv("GROQ_API_KEY")

GROQ_URL = "https://api.groq.com/openai/v1/chat/completions"

def call_groq(prompt):
    models = ["llama-3.3-70b", "llama-3.1-8b-instant"]

    for model in models:
        try:
            response = requests.post(
                GROQ_URL,
                json={
                    "model": model,
                    "messages": [{"role": "user", "content": prompt}]
                },
                headers={
                    "Authorization": f"Bearer {GROQ_API_KEY}",
                    "Content-Type": "application/json"
                }
            )

            res_json = response.json()

            if "choices" in res_json:
                return res_json["choices"][0]["message"]["content"]

        except:
            continue

    return "All models failed"
def run_agent(task, file_path):
    steps = []

    code = read_file(file_path)

    # Step 1: Decide action
    decision_prompt = f"""
    You are an autonomous AI developer agent.

    Task: {task}

    Decide ONE action:
    - explain
    - debug
    - document
    - optimize

    Only return the action.
    """

    action = call_groq(decision_prompt).strip()
    steps.append({"step": "Decision", "output": action})

    # Step 2: Execute
    execution_prompt = f"""
    Perform this action: {action}

    Code:
    {code}

    Give detailed output.
    """

    result = call_groq(execution_prompt)
    steps.append({"step": "Execution", "output": result})

    # Step 3: Improvement loop (basic agent behavior)
    refine_prompt = f"""
    Improve the previous result if possible.

    Previous output:
    {result}
    """

    refined = call_groq(refine_prompt)
    steps.append({"step": "Refinement", "output": refined})

    return steps