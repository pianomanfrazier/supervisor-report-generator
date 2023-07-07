#!./venv/bin/python

from subprocess import call
from time import strftime
from jinja2 import Environment, FileSystemLoader
import os

GIT_AUTHOR = "Mickey Mouse"
PROJECTS = [('PROJECT 1', '/home/username/project-1'), ('PROJECT 2', '/home/username/project-2')]

def file_get_contents(filename):
	with open(filename) as f:
		return f.read()

def get_git_report(repo):
    REPORT_CMD = f'git --no-pager log --branches --pretty=format:"%ad - %an: %s" --after=$(date +%Y-%m-%d -d "-14 day") --until=$(date +%Y-%m-%d) --author="{GIT_AUTHOR}"'
    CWD = os.getcwd() 
    tmp_file = f'{CWD}tmp-git-report.txt'
    call(f'cd {repo} && {REPORT_CMD} > {tmp_file}', shell=True)
    report = file_get_contents(tmp_file).split('\n')
    os.remove(tmp_file)

    return report

env = Environment(loader=FileSystemLoader(os.path.abspath('.')), trim_blocks=True, lstrip_blocks=True)
template = env.get_template('template.md')

git_reports = map(lambda x: (x[0], get_git_report(x[1])), PROJECTS)

output_file = strftime('%d-%m-%Y') + '.md'

with open(output_file, 'w') as fout:
	fout.write(template.render(reports=git_reports, date=strftime('%B %d, %Y')))

