from os import path
import pyperclip as pc

if path.exists('Data/geminiapi.dat'):
    pass
else:
    with open('Data/geminiapi.dat', 'w') as f:
        f.write(pc.paste())