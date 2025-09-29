import os

os.system('clear')
ogprompt = '''SKILLS:
• Frontend: React, Vue, PHP. Backend: .NET, NodeJS, NestJS, ExpressJS, PHP
• Database: MySQL, MongoDB, SQLite, Redis
• Scripting: Bash, Python. Version Control: Git, GitHub, GitLab
• Container & Orchestration: Docker, Rancher. Virtualization: KVM, VPS
• Proficient in Linux (Ubuntu, Debian, Fedora, Arch), Windows
• Experience in AWS, Azure
Experience:
OSU COLLEGE OF AGRICULTURAL SCIENCES 9/2025
• Managed and maintained the OregonFlora codebase and infrastructure to ensure reliability and long-term usability.
OSU EXTENSION SERVICE OUTDOOR SCHOOL 9/2024 – 10/2024
• Maintenance on the portal through which school districts and teachers can access the application, reporting systems, resources for developing outdoor school programs.
• Technology migration: From Umbraco 8 to Drupal 10 to improve stability, performance.
• Supported website content updates, maintaining consistency and clarity across pages.
ICC INNOVATIVE CONSULTING 11/2020 – 11/2022
• Maintained a distribution management system for Business-to-business sales. Specialized in promotion/deal calculation.
• Made improvements to the activity generation algorithm that sped up by 96x.
• Programmed a social security app offering relief packages during COVID-19 (An Sinh), utilized by about 9 million citizens in HCMC.
Summary of my resume:
Full stack web developer with experience in designing, deploying, and maintaining web applications across the full stack. Skilled in JavaScript, React, MySQL, CSS, and HTML, with a strong background in Linux systems and Agile development. Experienced in managing deadlines, collaborating with cross-functional teams, and delivering solutions that improve functionality and user experience. Adept at documentation, content management, and supporting site updates. Committed to building efficient, user-friendly tools and contributing to the growth of mission-driven projects.
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
