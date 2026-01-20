import os
import requests
from openai import OpenAI
from pytesseract import image_to_string

def llama_health_check(gptUrl: str) -> OpenAI:
    healthCheckUrl = gptUrl + "/health"
    with requests.get(healthCheckUrl) as res:
        if res.status_code != 200 or res.json()["status"] != "ok":
            raise Exception(res.json())
    client = OpenAI(
        base_url=gptUrl,
        api_key=''
    )
    return client

def extract_resume_sections(text: str) -> list[dict]:
    # Remove YAML metadata at the top
    text = text.split("\n---")[1]
    
    # Split by #### heading
    sections = text.split("#### ")
    
    # Process each section
    result = []
    for section in sections[1:]:  # Skip first empty string
        if section:
            section = section.strip()
            if section:
                if "\n" in section:
                    header, content = section.split("\n", 1)
                    result.append({
                        "header": header.strip(),
                        "content": content.strip()
                    })
                else:
                    result.append({
                        "header": section,
                        "content": ""
                    })
    
    return result

def get_resume(resumeUrl: str) -> str:
    with requests.get(resumeUrl) as res:
        if res.status_code != 200 or "---\ntitle" not in res.text:
            raise Exception('Wrong data')
        resume = res.text

    # Extract only Work Experience and Skills sections
    extracted = extract_resume_sections(resume)
    work_exp = extracted[0]
    skills = extracted[2]
    return f"#### {work_exp["header"]}\n{work_exp["content"]}\n\n" + f"#### {skills["header"]}\n{skills["content"]}\n"

def read_job_description(imagePath: str) -> str:
    job = ''
    if not os.path.exists(imagePath):
        os.makedirs(imagePath)
    files = os.listdir(imagePath)
    if len(files) == 0:
        raise Exception("No job description image found.")
    for image in os.listdir(imagePath):
        job += image_to_string(imagePath + image)
        job += "---\n"

    return job

def get_chat_response(client: OpenAI, messages: list[dict]) -> str:
    result = client.chat.completions.create(model='', messages=messages)
    # Get the result and shave off the newline
    result = result.choices[0].message.content[2:]

    return result