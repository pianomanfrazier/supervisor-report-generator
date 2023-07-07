# Weekly Report Generator

## To Run

```bash
virtualenv -p python3 venv
source ./venv/bin/activate
pip install -r requirements.txt
./generate.py
```

Edit the template in `template.md` to change the output. It currently goes into my projects directories and generates a git commit report and populates a markdown file. 

You can then generate the html to paste into your email with

```bash
pandoc <date>.md -o output.html && xclip -sel clip < output.html
```

On Windows the easiest way is to generate the html, open that html file in your browser and copy the output.

```bash
pandoc <date>.md -o output.html # then open output.html in browser <ctrl-a> <ctrl-v> and paste into Outlook
```
