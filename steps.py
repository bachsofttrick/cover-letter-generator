import os
from pytesseract import image_to_string

def read_job_description(path: str, jd_txt_file: str="jd.txt") -> str:
    job = ''
    if not os.path.exists(path):
        os.makedirs(path)
    files = os.listdir(path)
    if len(files) == 0:
        raise Exception("No job description found.")
    
    if jd_txt_file in files:
        with open(path + jd_txt_file, 'r', encoding="utf-8") as f:
            job = f.read()
            return job

    files = [f for f in files if f.endswith((".jpg", ".png"))]
    for image in files:
        job += image_to_string(path + image)
        job += "---\n"

    return job
