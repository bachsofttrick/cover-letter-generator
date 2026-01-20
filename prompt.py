import os
import steps

# Global config
resumeUrl = "https://raw.githubusercontent.com/bachsofttrick/bachsofttrick.github.io/refs/heads/main/app/about/resume.md"
gptUrl = "http://localhost:8033/v1"
resultFile = "result.txt"
promptFile = "promptNote.txt"
imagePath = "./jd/"

def main():
    # llama.cpp health check
    try:
        client = steps.llama_health_check(gptUrl)
    except Exception as e:
        print(f"Something is wrong with llama.cpp.\n{e}")
        return

    messages = [
        {
            "role": "user",
            "content": ''
        }
    ]

    print("Getting resume from portfolio...")
    try:
        resume = steps.get_resume(resumeUrl)
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
    prompt = "This is the job description:\n" + job + "This is my resume:\n" + resume + prompt_note
    
    # Running to GPT to write
    messages[0]["content"] = prompt

    print("Writing cover letter...")
    try:
        result = steps.get_chat_response(client, messages)
        with open(resultFile, 'w', encoding='utf-8') as f:
            f.write(result)

        print('Finished writing.')
    except Exception as e:
        print(f"Error while writing:\n{e}")
        return

if __name__ == "__main__":
    main()