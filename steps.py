import os
from pytesseract import image_to_string

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
