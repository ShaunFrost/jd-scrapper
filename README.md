# Linkedin Jobs Scrapper

This scrapper can be used to get details (jobId, role, company name, job description) from the linkedin guest jobs page without logging in.

## Steps

1. Create a virtual env
2. Run `requirements.txt` to install dependencies
3. (Optional) Change few parameters in the code like the `SCROLL_BREAK_ITERATION` to break iteration after certain number of scrolls
4. Run `python main.py` to generate the csv with details