from openai import OpenAI

client = OpenAI(
  api_key="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"
)

completion = client.chat.completions.create(
  model="gpt-4o-mini",
  store=True,
  messages=[
    {"role": "user", "content": "who is ritik roshan"}
  ]
)

print(completion.choices[0].message);
