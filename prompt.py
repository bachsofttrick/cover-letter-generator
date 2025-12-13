import os

os.system('clear')
resume = '''
WORK EXPERIENCE
Software Developer	10/2025 - present
OregonFlora - Corvallis, Oregon
• Improved reliability and performance of a statewide research system serving thousands of daily users.
• Optimized ingestion pipeline, reducing processing time from 2 hours to 2 minutes through optimized database update and caching strategies.
Web Assistant	8/2024 - 9/2024
OSU Extension Service - Outdoor School - Corvallis, Oregon
• Maintained the portal for educators and school districts, ensuring seamless access to outdoor education resources and reporting systems.
• Supported platform migration, contributing to improved platform stability and performance.
Software Developer	9/2020 - 11/2022
ICC Innovative Consulting - Ho Chi Minh City, Vietnam
• Maintained a business-to-business distribution management system,  ensuring accurate calculation for high-volume operations.
• Enhanced the activity generation algorithm, reducing runtime from 1 hour to 1 minute.
• Developed and deployed An Sinh, a large-scale mission-critical social security application supporting 9 million citizens during COVID-19 in Ho Chi Minh City.
PROJECTS
Reversi: Minimax VS Monte Carlo - Paper
• Designed a benchmark of two AI algorithms against several games of Reversi, using multithreading to improve efficiency.
Object Detection and Monitoring through UAV - Paper | Video 1 | Video 2
• Engineered a custom drone for capable of identifying, following targets, and transmitting live video to RTSP-compatible devices.
SKILLS
• Language: C, C++, C#, Python, Go, Javascript, TypeScript, SQL, NoSQL, Bash
• Frontend: React, Vue, Svelte, NextJS, Tailwind, Bootstrap, SCSS
• Backend: .NET, NodeJS, NestJS, ExpressJS, FastAPI, Django, Laravel
• Database: MySQL, Postgres, MongoDB, Redis, RabbitMQ, Solr
• CI/CD Tools: Git, Github Actions, Docker, Kubernetes, Ansible
• AI Deployments: llama.cpp, ollama, Hugging Face
• AI Developer Tools: Copilot, Cursor, Claude Code, ChatGPT
• Cloud Platforms: AWS

'''
with open('prompt.txt', 'r', encoding='utf-8') as f:
    job = f.read()

prompt = 'Act like a hiring manager for this role in this description:\n' + job + '\What would be a perfect resume that fits the company\'s misson, culture, technical requirements:\n' + resume
print(prompt)
if False:
	print('----- Press Enter -----')
	input()
	os.system('clear')
	prompt = ogprompt + 'Use the preceeding information to write me a cover letter for this job:' + job
	print(prompt)
