from openai_client import get_client

client = get_client()

completion = client.chat.completions.create(
  model="ft:gpt-4o-mini-2024-07-18:subspace-labs::9sGLPEy9",
  messages=[
    {"role": "system", "content": "You are a helpful assistant."},
    {"role": "user", "content": "Tell me about the Autonomys Network"}
  ]
)
print(completion.choices[0].message)