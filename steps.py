import os
from pytesseract import image_to_string

jd_file = "jd.txt"

def read_job_description(imagePath: str) -> str:
    job = ''
    if not os.path.exists(imagePath):
        os.makedirs(imagePath)
    files = os.listdir(imagePath)
    if len(files) == 0:
        raise Exception("No job description found.")
    
    if jd_file in files:
        with open(imagePath + jd_file, 'r', encoding="utf-8") as f:
            job = f.read()
            return job

    files = [f for f in files if f.endswith((".jpg", ".png"))]
    for image in files:
        job += image_to_string(imagePath + image)
        job += "---\n"

    return job
