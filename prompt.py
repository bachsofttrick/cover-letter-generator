import os
import steps
from classes import LLM, Resume

# Global config
resumeUrl = "https://raw.githubusercontent.com/bachsofttrick/bachsofttrick.github.io/refs/heads/main/app/about/resume.md"
gptUrl = "http://localhost:8033/v1"
resultFile = "result.txt"
promptFile = "promptNote.txt"
imagePath = "./jd/"

def main():
    # llama.cpp health check
    try:
        llm = LLM(gptUrl)
    except Exception as e:
        print(f"Something is wrong with llama.cpp.\n{e}")
        return

    print("Getting resume from portfolio...")
    try:
        resume = Resume(resumeUrl)
    except Exception as e:
        print(f"Cannot read the resume:\n{e}")
        return

    print("Reading job description...")
    try:
        job = steps.read_job_description(imagePath)
    except Exception as e:
        print(f"Cannot read the job description:\n{e}")
        return

    print("Prompting...")
    try:
        with open(promptFile, 'r', encoding='utf-8') as f:
            prompt_note = "\n" + f.read()
    except Exception as e:
        print(f"Cannot read the resume:\n{e}")
        return
    prompt = "This is the job description:\n" + job + "This is my resume:\n" + resume.get_prompt() + prompt_note

    print("Writing cover letter...")
    try:
        result = llm.get_chat_response(prompt)
        with open(resultFile, 'w', encoding='utf-8') as f:
            f.write(result)

        print('Finished writing.')
    except Exception as e:
        print(f"Error while writing:\n{e}")
        return

if __name__ == "__main__":
    main()