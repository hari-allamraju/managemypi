import os
from jinja2 import Environment, FileSystemLoader
import subprocess
 
PATH = os.path.dirname(os.path.abspath(__file__))
TEMPLATE_ENVIRONMENT = Environment(
    autoescape=False,
    loader=FileSystemLoader(os.path.join(PATH, 'templates')),
    trim_blocks=False)
 

def sorted_ls(path):
    mtime = lambda f: os.stat(os.path.join(path, f)).st_mtime
    return list(sorted(os.listdir(path), key=mtime))

def render_template(template_filename, context):
    return TEMPLATE_ENVIRONMENT.get_template(template_filename).render(context)
 
 
def create_index_html():
    hall = os.path.expanduser("~/FTP/Hall/index.html")
    hariroom = os.path.expanduser("~/FTP/HariRoom/index.html")
    files=[]
    items = sorted_ls(os.path.expanduser("~/FTP/Hall"))
    for names in items:
        if names.endswith(".mp4"):
            files.append(names)
    context = {
        'files': files
    }
    with open(hall, 'w') as f:
        html = render_template('index_html.j2', context)
        f.write(html)
    files=[]
    items = sorted_ls(os.path.expanduser("~/FTP/HariRoom"))
    for names in items:
        if names.endswith(".mp4"):
            files.append(names)
    context = {
        'files': files
    }
    with open(hariroom, 'w') as f:
        html = render_template('index_html.j2', context)
        f.write(html)
 
def main():
    create_index_html()
 
if __name__ == "__main__":
    main()