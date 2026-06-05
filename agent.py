import yaml
 
# Load skill function
def load_skill(skill_file, prompt_file):
    with open(skill_file, "r") as f:
        skill = yaml.safe_load(f)
 
    with open(prompt_file, "r") as f:
        prompt = f.read()
 
    return skill, prompt
 
 
# Simple agent decision logic
def choose_skill(user_input):
    user_input = user_input.lower()
 
    if "email" in user_input:
        return "skill.yaml", "prompt.txt"
    elif "resume" in user_input:
        return "resume_skill.yaml", "resume_prompt.txt"
    elif "meeting" in user_input:
        return "meeting_skill.yaml", "meeting_prompt.txt"
    elif "bug" in user_input or "error" in user_input:
        return "bug_skill.yaml", "bug_prompt.txt"
    else:
        return None, None
 
 
# Replace variables manually
def fill_prompt(prompt):
    # Example inputs
    inputs = {
        "client_name": "Arun",
        "meeting_summary": "Discussed onboarding",
        "action_items": "Send documents",
        "resume_text": "Ravi, Python developer with 3 years experience",
        "meeting_notes": "Project delayed, deadline extended",
        "bug_description": "App crashes on login"
    }
 
    for key, value in inputs.items():
        prompt = prompt.replace(f"{{{{{key}}}}}", value)
 
    return prompt
 
 
# MAIN AGENT
print("🔥 AI Agent Started")
user_input = input("Enter your request: ")
 
skill_file, prompt_file = choose_skill(user_input)
 
if skill_file:
    skill, prompt = load_skill(skill_file, prompt_file)
 
    final_prompt = fill_prompt(prompt)
 
    print("\n✅ Selected Skill:", skill["name"])
    print("\n--- GENERATED PROMPT ---\n")
    print(final_prompt)
 
    print("\n--- OUTPUT ---")
    print("👉 Copy this prompt into ChatGPT for real response")
 
else:
    print("❌ No matching skill found")
