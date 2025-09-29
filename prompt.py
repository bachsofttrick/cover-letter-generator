import os

os.system('clear')
ogprompt = '''SKILLS:
• Comfortable managing deadlines and timelines across concurrent projects.
• Capable of working independently and with teams on long- and short-term tasks.
• Proficient in Microsoft Office Suite (Word, Excel, PowerPoint)
• Experience with data entry and maintaining databases.
• Effective verbal and written communicator with attention to detail.
• Multilingual: English, Vietnamese
• Experience with digitization of files and information management systems.
Experience:
OSU CARLSON COLLEGE OF VETERINARY MEDICINE 7/2025 – 8/2025
• Led and supervised a group of academically driven high school students during OSU's Summer Veterinary Experience, ensuring their safety, engagement, and successful participation in a smooth, incident-free program.
• Promoted a supportive, inclusive environment by building rapport with students from diverse backgrounds, contributing to a positive group and increased interest in veterinary careers.
OSU EXTENSION SERVICE OUTDOOR SCHOOL 9/2024 – 10/2024
• Supported website content updates, maintaining consistency and clarity across pages.
• Collaborated with team members to process content and image submissions.
• Organized files and contributed to documentation efforts for site management.
ICC INNOVATIVE CONSULTING 11/2020 – 11/2022
• Collaborated on development teams to design and deploy full-stack web applications.
• Managed timelines, deadlines, and client deliverables using Agile methodologies.
• Produced documentation, reports, and spreadsheets to support team operations.
Summary of my resume:
Detail-oriented and adaptable student with strong organizational, communication, and computer skills. Experienced in supporting office operations, managing files and databases, and assisting with content creation and digitization projects. Proficient in Microsoft Office Suite and comfortable with email, phone, and in-person communication. Skilled at working independently or with teams to complete tasks efficiently, troubleshoot technical issues, and provide excellent support for faculty, staff, and students.
'''
with open('prompt.txt', 'r', encoding='utf-8') as f:
    job = f.read()

prompt = ogprompt + 'Use the preceeding information to change summary of my resume so it aligns with this job:\n' + job
print(prompt)
if False:
	print('----- Press Enter -----')
	input()
	os.system('clear')
	prompt = ogprompt + 'Use the preceeding information to write me a cover letter for this job:' + job
	print(prompt)
