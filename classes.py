import requests
from openai import OpenAI
import json

class LLM:
    def __init__(self, gptUrl: str):
        healthCheckUrl = gptUrl + "/health"
        with requests.get(healthCheckUrl) as res:
            if res.status_code != 200 or res.json()["status"] != "ok":
                raise Exception(res.json())
        self.client = OpenAI(
            base_url=gptUrl,
            api_key=''
        )
        self.messages = [
            {
                "role": "user",
                "content": ''
            }
        ]
    
    def edit_message(self, message: str):
        self.messages[0]["content"] = message

    def get_chat_response(self, message: str = '', progress: bool = False) -> str:
        if len(message) > 0: self.edit_message(message)
        completion = self.client.chat.completions.create(model='', messages=self.messages, stream=True)
        result = ""
        
        # Observe progress
        if progress:
            count = 0
            for chunk in completion:
                delta = chunk.choices[0].delta
                if delta and delta.content:
                    result += delta.content
                    count += 1
                    print(f"{count} tokens used.", end='\r')
            print(f"{count} tokens used.", end='\n')

        # Remove em dashes and shave off the newline
        result = result.lstrip('\n').replace("—", ",")

        return result

class Resume:
    def __init__(self, resumeUrl: str):
        with requests.get(resumeUrl) as res:
            if res.status_code != 200 or "---\ntitle" not in res.text:
                raise Exception('Wrong data')
        self.full_resume = res.text
        self.sections = self.__extract_sections()
        self.work_exp = self.sections[0]
        self.skills = self.sections[2]

    def __extract_sections(self) -> list[dict]:
        # Remove YAML metadata at the top
        text = self.full_resume.split("\n---")[1]
        
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

    def get_prompt(self) -> str:
        return f"#### {self.work_exp["header"]}\n{self.work_exp["content"]}\n\n" + f"#### {self.skills["header"]}\n{self.skills["content"]}\n"

class Config:
    def __init__(self):
        config = self.__load_config()
        self.resumeUrl = config["resumeUrl"]
        self.gptUrl = config["gptUrl"]
        self.resultFile = config["resultFile"]
        self.promptFile = config["promptFile"]
        self.jdPath = config["jdPath"]
        self.jdTextFile = config["jdTextFile"]

    def __load_config(self) -> dict:
        with open("config.json", 'r') as f:
            config = json.load(f)
        return config
    
