from openai import OpenAI

client = OpenAI(
    api_key="<YOUR API KEY>",
)

comletion = client.chat.completions.create(
    model= "gpt-3.5-turbo",
    messages=[
        {"role": "system","content": "You are virtual assistant named jarvis skilled in general tasks like Alexa and Google Cloud"},
        {"role": "user", "content": "what is coding"}
    ]
)

print(comletion.choices[0].message)
