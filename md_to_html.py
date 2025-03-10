import markdown as md
import os

class Converter:
    pass

def convert(file):
    with open(file, 'r') as f:
        input = f.read()
    output = md.markdown(input)
    return output

def html_writer(file):
    output = Converter.convert(file)
    file = file.split('.')
    filename = file[0]
    with open(f'{filename}.html', 'w') as f:
        f.write(output)

def delete_md(f):
    os.system(f"del {f}")

Converter.convert = convert
Converter.writer = html_writer
Converter.delete_md = delete_md