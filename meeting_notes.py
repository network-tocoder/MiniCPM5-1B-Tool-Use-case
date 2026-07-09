import requests, json

tools = [
    {
        "type": "function",
        "function": {
            "name": "create_action_item",
            "description": "Create a task with assignee, deadline and priority",
            "parameters": {
                "type": "object",
                "properties": {
                    "task": {"type": "string", "description": "The task description"},
                    "assignee": {"type": "string", "description": "Person responsible"},
                    "deadline": {"type": "string", "description": "Due date"},
                    "priority": {"type": "string", "description": "high, medium, or low"}
                },
                "required": ["task", "assignee", "deadline", "priority"]
            }
        }
    },
    {
        "type": "function",
        "function": {
            "name": "calculator",
            "description": "Perform a math calculation",
            "parameters": {
                "type": "object",
                "properties": {
                    "expression": {"type": "string", "description": "Math expression"}
                },
                "required": ["expression"]
            }
        }
    }
]

meeting_notes = """
Team standup July 8: John said the API migration is behind schedule, 
needs to finish by Friday July 11. Maria will review the Q3 budget, 
we're over by 15 percent on a 50000 dollar budget so need to find 
cuts. Raj is handling the client demo on Monday July 14, high priority. 
Sarah needs to update the documentation by end of week, low priority.
"""

print("=== Meeting Notes → Action Items (MiniCPM5-1B) ===\n")
print(f"Input:\n{meeting_notes}")
print("Processing...\n")

response = requests.post("http://localhost:1234/v1/chat/completions", json={
    "model": "minicpm5-1b-agentic-tooluse",
    "messages": [
        {"role": "system", "content": "You are a meeting assistant. Extract ALL action items from the notes. Use create_action_item for each task. Use calculator for any math needed."},
        {"role": "user", "content": f"Extract action items from these meeting notes:\n{meeting_notes}"}
    ],
    "tools": tools
}).json()

msg = response["choices"][0]["message"]

if msg.get("tool_calls"):
    print(f"Found {len(msg['tool_calls'])} action items:\n")
    for i, tc in enumerate(msg["tool_calls"], 1):
        args = json.loads(tc["function"]["arguments"])
        func = tc["function"]["name"]
        if func == "create_action_item":
            print(f"  [{i}] {args.get('task', 'N/A')}")
            print(f"      Assignee: {args.get('assignee', 'N/A')}")
            print(f"      Deadline: {args.get('deadline', 'N/A')}")
            print(f"      Priority: {args.get('priority', 'N/A')}\n")
        elif func == "calculator":
            result = eval(args["expression"])
            print(f"  [CALC] {args['expression']} = {result}\n")
else:
    print(f"Response: {msg.get('content', 'No response')}")