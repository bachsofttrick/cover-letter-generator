# Cover letter generator
An AI-powered program that generates cover letter based on the job description.

Todo:
- [x] Implement REST API of llama.cpp to incorporate LLM in.
- [x] Make a prompt that ONLY releases result, then print out the result.txt
- [ ] Add some error handling to prevent 404, wrong url, fetching the wrong file...
- [ ] Implement llama-cpp-python to incorporate LLM in, since the lib is perfect for text prompt.
  - [ ] Implement an if case to check REST API first (/health).
- [ ] Use LangChain (if possible) to split the task to:
  - [ ] Get the keywords of the job
  - [ ] Make a perfect resume based on the job description (as a reference only)
  - [x] Make a cover letter based on your own resume
- [ ] Design a frontend for it.
- [ ] Implement a Tauri/Electron interface.