import os
import requests
from openai import OpenAI

# Global config
resumeUrl = "https://raw.githubusercontent.com/bachsofttrick/bachsofttrick.github.io/refs/heads/main/app/about/resume.md"
gptUrl = "http://localhost:8033/v1"

# Get resume from portfolio
res = requests.get(resumeUrl)
resume = res.text

# Get prompt
with open('prompt.txt', 'r', encoding='utf-8') as f:
    job = f.read()
prompt = 'This is the job description:\n' + job + 'This is my resume:\n' + resume + '''
Only use the WORK EXPERIENCE (ignore the internship), SKILLS sections in my resume.
Write a concise, engaging, and professional cover letter with no bold style used.
Starting with "Dear".
'''

# Running to GPT to write
messages = [
    {
        "role": "user",
        "content": prompt
    }
]

print("Writing cover letter...")
client = OpenAI(
    base_url=gptUrl,
    api_key=''
)
result = client.chat.completions.create(model='', messages=messages)

# Get the result and shave off the newline
result = result.choices[0].message.content[2:]
with open('result.txt', 'w', encoding='utf-8') as f:
    f.write(result)

print('Finished writing.')
