import os
import requests
from openai import OpenAI

# Global config
resumeUrl = "https://raw.githubusercontent.com/bachsofttrick/bachsofttrick.github.io/refs/heads/main/app/about/resume.md"
gptUrl = "http://localhost:8033/v1"
healthCheckUrl = gptUrl + "/health"
jobFile = "job.txt"
resultFile = "result.txt"

def main():
    # llama.cpp health check
    try:
        with requests.get(healthCheckUrl) as res:
            if res.status_code != 200 or res.json()["status"] != "ok":
                raise Exception(res.json())
    except Exception as e:
        print(f"Something is wrong with llama.cpp.\n{e}")
        return

    print("Getting resume from portfolio...")
    try:
        with requests.get(resumeUrl) as res:
            if res.status_code != 200 or "---\ntitle" not in res.text:
                raise Exception('Wrong data')
            resume = res.text
    except Exception as e:
        print(f'Resume Not Found:\n{e}')
        return

    print("Reading job description...")
    try:
        with open(jobFile, 'r', encoding='utf-8') as f:
            job = f.read()
    except Exception as e:
        print(f"Error while reading prompt:\n{e}")
        return
    
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

    try:
        result = client.chat.completions.create(model='', messages=messages)

        # Get the result and shave off the newline
        result = result.choices[0].message.content[2:]
        with open(resultFile, 'w', encoding='utf-8') as f:
            f.write(result)

        print('Finished writing.')
    except Exception as e:
        print(f"Error while writing:\n{e}")
        return

if __name__ == "__main__":
    main()