# Cover letter generator
An AI-powered program that generates cover letter based on the job description.

## Requirements
- Python 3 with `venv` module
- [llama.cpp](https://github.com/ggml-org/llama.cpp) running a LLM server
- A LLM model to run on llama.cpp. Currently I use `Qwen3-8B-Q4_K_M`
- [Tesseract-OCR](https://github.com/tesseract-ocr/tesseract) preinstalled

## Todo
- [x] Implement REST API of llama.cpp to incorporate LLM in.
- [x] Make a prompt that ONLY releases result, then print out the result.txt
- [x] Add some error handling to prevent 404, wrong url, fetching the wrong file...
- [ ] Integrate an OCR ability to read from images -> use LLM to piece together the job description ->
send to LLM to write a cover letter.
- [ ] Implement llama-cpp-python to incorporate LLM in, since the library is perfect for text prompt.
  - [x] Implement an if case to check REST API first (/health).
  - [ ] llama-cpp-python should be secondary if /health is okay.
- [ ] Use LangChain (if possible) to split the task to:
  - [ ] Get the keywords of the job
  - [ ] Make a perfect resume based on the job description (as a reference only)
  - [x] Make a cover letter based on your own resume
- [ ] Design a frontend for it.
- [ ] Implement a Tauri/Electron interface.
