import requests
from openai import OpenAI

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

    def get_chat_response(self, message: str = '') -> str:
        if (len(message) > 0): self.edit_message(message)
        result = self.client.chat.completions.create(model='', messages=self.messages)
        # Get the result and shave off the newline
        result = result.choices[0].message.content[2:]

        return result

class Resume:
    def __init__(self, resumeUrl: str):
        with requests.get(resumeUrl) as res:
            if res.status_code != 200 or "---\ntitle" not in res.text:
                raise Exception('Wrong data')
        self.full_resume = res.text
        self.sections = self.extract_sections()
        self.work_exp = self.sections[0]
        self.skills = self.sections[2]

    def extract_sections(self) -> list[dict]:
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