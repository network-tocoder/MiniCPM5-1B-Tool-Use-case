import requests, json

def calculator(expression):
    return str(eval(expression))

tools = [{
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
}]

question = "What is 347 x 892?"

response = requests.post("http://localhost:1234/v1/chat/completions", json={
    "model": "minicpm5-1b-agentic-tooluse",
    "messages": [{"role": "user", "content": question}],
    "tools": tools
}).json()

msg = response["choices"][0]["message"]
tool_call = msg["tool_calls"][0]
func_name = tool_call["function"]["name"]
args = json.loads(tool_call["function"]["arguments"])

print(f"Model wants to call: {func_name}({args})")
result = calculator(args["expression"])
print(f"Result: {result}")