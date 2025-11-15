import os

os.system('clear')
resume = '''WORK EXPERIENCE
Software Developer	9/2025 - present
OregonFlora - Corvallis, Oregon
• Maintained and enhanced a research platform supporting thousands of daily users in Oregon.
• Improved the uploading process, reducing runtime from 2 hour to 2 minute.
Web Assistant	9/2024 - 10/2024
OSU Extension Service - Outdoor School - Corvallis, Oregon
• Maintained the portal through which school districts and teachers can access the application, reporting systems, resources for developing outdoor school programs.
• Supported platform migration, contributing to improved stability and performance.
Software Developer	9/2020 - 11/2022
ICC Innovative Consulting - Ho Chi Minh City, Vietnam
• Maintained and optimized a business-to-business distribution management system, focusing on promotions and deal calculation accuracy.
• Enhanced the activity generation algorithm, reducing runtime from 1 hour to 1 minute.
• Developed and deployed An Sinh, a large-scale social security relief application supporting 9 million citizens during COVID-19 in Ho Chi Minh City.
PROJECTS
Reversi: Minimax VS Monte Carlo - Paper
• Designed and compared performance of two AI algorithms against several games of Reversi, varying in configurations using multithreading.
Object Detection and Monitoring through UAV - Paper | Video 1 | Video 2
• Engineered a custom drone for searching, identifying, and following a designated subject while transmitting live video feeds to any RTSP-compatible device.
SKILLS
• Language: C, C++, C#, Python, Go, Javascript, TypeScript, SQL, NoSQL, Bash
• Frontend: React, Vue, Svelte, NextJS, Tailwind, Bootstrap, SCSS
• Backend: .NET, NodeJS, NestJS, ExpressJS, FastAPI, Django, Laravel, Ruby on Rails
• Database: MySQL, Postgres, MongoDB, Redis, Kafka, Solr, ElasticSearch
• CI/CD Tools: Git, Github Actions, Docker, Kubernetes, Ansible
• AI Developer Tools: Copilot, Cursor, Claude Code, ChatGPT
• Cloud Platforms: AWS
'''
with open('prompt.txt', 'r', encoding='utf-8') as f:
    job = f.read()

prompt = 'Act like a hiring manager for this role in this description:\n' + job + '\nNow I got this job. Use points in my old resume before this job, craft a resume to fit in company\'s misson, culture that got me this job:\n' + resume
print(prompt)
if False:
	print('----- Press Enter -----')
	input()
	os.system('clear')
	prompt = ogprompt + 'Use the preceeding information to write me a cover letter for this job:' + job
	print(prompt)
