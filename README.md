# Cover letter generator
An AI-powered program that generates cover letter based on the job description.

Todo:
- [ ] Implement llama-cpp-python to incorporate LLM in, since the lib is perfect for text prompt.
- [ ] Make a prompt that ONLY releases result, then print out the result.txt
- [ ] Use LangChain (if possible) to split the task to:
  - [ ] get the keywords of the job
  - [ ] make a perfect resume based on the job description (as a reference only)
  - [ ] make a cover letter based on your own resume
- [ ] Design a frontend for it.
- [ ] Implement a Tauri/Electron interface.