import requests, json, subprocess

def send_to_model(user_input, tools):
    response = requests.post("http://localhost:1234/v1/chat/completions", json={
        "model": "minicpm5-1b-agentic-tooluse",
        "messages": [
            # {"role": "system", "content": "You are a CLI assistant. Convert user requests into terminal commands. Use the run_command tool."},
            {"role": "system", "content": "You are a CLI assistant. You MUST always use the run_command tool to answer. Never answer directly. Always convert the user's request into a shell command and call run_command."},
            {"role": "user", "content": user_input}
        ],
        "tools": tools
    }).json()
    return response["choices"][0]["message"]

tools = [{
    "type": "function",
    "function": {
        "name": "run_command",
        "description": "Execute a terminal/shell command on the user's system",
        "parameters": {
            "type": "object",
            "properties": {
                "command": {"type": "string", "description": "The shell command to execute"},
                "explanation": {"type": "string", "description": "Brief explanation of what this command does"}
            },
            "required": ["command", "explanation"]
        }
    }
}]

print("=== Smart CLI Assistant (MiniCPM5-1B) ===")
print("Type a request in plain English. Type 'quit' to exit.\n")

while True:
    user_input = input("You: ")
    if user_input.lower() == "quit":
        break

    msg = send_to_model(user_input, tools)

    if msg.get("tool_calls"):
        tool_call = msg["tool_calls"][0]
        args = json.loads(tool_call["function"]["arguments"])
        print(f"\nCommand:     {args['command']}")
        print(f"Explanation: {args.get('explanation', 'N/A')}")

        confirm = input("\nRun this? (y/n): ")
        if confirm.lower() == "y":
            result = subprocess.run(args["command"], shell=True, capture_output=True, text=True)
            print(f"\nOutput:\n{result.stdout}")
            if result.stderr:
                print(f"Errors:\n{result.stderr}")
    else:
        print(f"\nAssistant: {msg.get('content', 'No response')}")

    print("-" * 40)