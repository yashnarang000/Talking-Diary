import subprocess
from os import path
from os import makedirs
from sys import exit



# Setting up the defaults

if path.exists('Data'):
    pass
else:
    makedirs("Data")

# if path.exists('AI/Data'):
#     pass
# else:
#     makedirs("AI/Data")

if path.exists('Data/restart_handler.dat'):
    pass
else:
    with open('Data/restart_handler.dat', 'w') as f:
        f.write("0")

if path.exists('Data/voiceSelect.dat'):
    pass
else:
    with open('Data/voiceSelect.dat', 'w') as f:
        f.write('4')

if path.exists('Data/voice_status.dat'):
    pass
else:
    with open('Data/voice_status.dat', 'w') as f:
        f.write("1")

if path.exists('Diary'):
    pass
else:
    makedirs("Diary")

if path.exists("Data/history.dat"):
    pass
else:
    with open("Data/history.dat", "w") as f:
        f.write("")

# data_dir = f"{path.dirname(__file__)}\Data"

# with open('AI/Data/data_dir.dat', 'w') as f:
#     f.write(data_dir)

subprocess.run(['python', 'main_GUI.py'])

def restart():
    subprocess.run(['python', 'main_GUI.py'])

while True:
    with open('Data/restart_handler.dat', 'r') as f:
        signal = f.read()

    if signal == "1":
        restart()
    else:
        exit()
