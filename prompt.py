import os
import requests
import json

# Get resume from portfolio
resumeUrl = "https://raw.githubusercontent.com/bachsofttrick/bachsofttrick.github.io/refs/heads/main/app/about/resume.md"
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
gptUrl = "http://localhost:8033/v1/chat/completions"
post = {
    "messages": [
        {
            "role": "user",
            "content": prompt
        }
    ]
}

print("Writing cover letter...")
postReturn = requests.post(gptUrl, json=post)
result = postReturn.json()

# Get the result and shave off the newline
result = result["choices"][0]["message"]["content"][2:]
with open('result.txt', 'w', encoding='utf-8') as f:
    f.write(result)

print('Finished writing.')
