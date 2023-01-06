import openai
from io import StringIO

# Set your API key
openai.api_key = "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"

# Set the prompt you want to send to GPT-3
prompt = "Write an essay on Quantom Physics with 100000 words"

# Use the `Completion` endpoint to send the prompt to GPT-3 and receive a response
response = openai.Completion.create(
    engine="text-davinci-003", 
    prompt=prompt,
    max_tokens=2048,
    temperature=1)	

# Capture the output of the print function using StringIO
output = StringIO()

# Print the response
print(response["choices"][0]["text"], file=output)
# Write the captured output to a file
with open("E:\Output\output.html", "w") as f:
    f.write(output.getvalue())
