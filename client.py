from openai import OpenAI

client = OpenAI(
    api_key="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",
)

comletion = client.chat.completions.create(
    model= "gpt-3.5-turbo",
    messages=[
        {"role": "system","content": "You are virtual assistant named jarvis skilled in general tasks like Alexa and Google Cloud"},
        {"role": "user", "content": "what is coding"}
    ]
)

print(comletion.choices[0].message)
