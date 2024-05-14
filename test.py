import openai
import os

# openai.api_key = 'my first test key'

# response = openai.Completion.create(
#   engine="text-davinci-002",
#   prompt="Translate the following English text to French: '{}'",
#   max_tokens=60
# )

# print(response.choices[0].text.strip())


openai.api_key = 'sk-proj-kXrCHKZNiTYj5jVQwtpVT3BlbkFJhQuCBku11ekcpnYEU89y'

response = openai.ChatCompletion.create(
  model="gpt-3.5-turbo",
  messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "Translate the following English text to French: '{}'"}
    ]
)

print(response['choices'][0]['message']['content'])

