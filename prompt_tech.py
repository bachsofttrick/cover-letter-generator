import os

os.system('clear')
ogprompt = '''SKILLS:
- Language: C#, Python, HTML, CSS, Javascript, PHP, Bash
- Frontend: React, Vue
- Backend: .NET, NodeJS, NestJS, ExpressJS, Laravel
- Database: MySQL, MongoDB, SQLite, Redis
- Tools: Git, Docker, Rancher
- Virtualization: KVM, VPS
- Systems: Linux, Windows
Experience:
OSU COLLEGE OF AGRICULTURAL SCIENCES 9/2025
• Managed and maintained the OregonFlora codebase and infrastructure to ensure reliability and long-term usability  for researchers.
OSU EXTENSION SERVICE OUTDOOR SCHOOL 9/2024 – 10/2024
• Maintenance on the portal through which school districts and teachers can access the application, reporting systems, resources for developing outdoor school programs.
• Technology migration: From Umbraco 8 to Drupal 10 to improve stability, performance.
• Supported website content updates, maintaining consistency and clarity across pages.
ICC INNOVATIVE CONSULTING 11/2020 – 11/2022
- Maintained and optimized a B2B distribution management system,
focusing on promotions and deal calculation accuracy.
- Enhanced the activity generation algorithm, achieving a 96x speedup in runtime efficiency.
- Developed and deployed An Sinh, a large-scale social security relief application
supporting 9 million citizens during COVID-19 in Ho Chi Minh City.
Projects:
REVERSI: MINIMAX VS MONTE CARLO
• Designed and compared performance of two AI algorithms against several games of Reversi, varying in metrics using multithreading.
OBJECT DETECTION AND MONITORING THROUGH UAV
• Engineered a custom drone for searching, identifying, and following a designated subject while transmitting live video feeds to any RTSP-compatible device.
Summary of my resume:
Full stack web developer with experience in designing, deploying, and maintaining web applications. Skilled in .NET, JavaScript, React, MySQL, Docker, with a strong background in Linux systems and Agile development. Committed to building efficient, user-friendly tools and contributing to the growth of mission-driven projects.
'''
with open('prompt.txt', 'r', encoding='utf-8') as f:
    job = f.read()

prompt = ogprompt + 'Use the preceeding information to write me a cover letter so it aligns with this job:\n' + job
print(prompt)
if False:
	print('----- Press Enter -----')
	input()
	os.system('clear')
	prompt = ogprompt + 'Use the preceeding information to write me a cover letter for this job:' + job
	print(prompt)
