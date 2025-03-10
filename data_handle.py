# Importing required modules

from os import path
from datetime import datetime
import AI.journalization as JZ
from md_to_html import Converter

content = JZ.journalize() 

# Defining resume and redefine

def resume(lastDate, lastTime):
    '''
    Writes the final journal in the same file as before.
    '''

    hour = int(lastTime[:2])
    minute = int(lastTime[2:4])
    second = int(lastTime[4:])

    timeFormat = f"{hour}:{minute}:{second}"

    file = rf"Diary\{lastDate}.md"

    with open(file, "a", encoding="utf-8") as f:
        f.write(f"\n\n## {timeFormat}\n\n{content}")
    
    Converter.writer(file)

def redefine(newDate, newTime):
    '''
    Writes the final journal in a new file.
    '''

    date = int(newDate[:2])
    month = int(newDate[2:4])
    year = int(newDate[4:])

    specific_date = datetime(year, month, date)
    day = specific_date.strftime("%A")
    
    dateFormat = specific_date.strftime("%d %B, %Y")

    hour = newTime[:2]
    minute = newTime[2:4]
    second = newTime[4:]

    timeFormat = f"{hour}:{minute}:{second}"

    file = rf"Diary\{newDate}.md"

    with open(file, "w", encoding="utf-8") as f:
        f.write(f"# {dateFormat}\n\n## {timeFormat}\n\n{content}")
    
    Converter.writer(file)

# Accessing the datetime from new_datetime

with open("Data/new_datetime.dat", 'r') as f:
    newDatetime = f.read()
        
newDatetimeList = newDatetime.split("-")
newDate = newDatetimeList[0]
newTime = newDatetimeList[1]

# Below is the code that decides whether to create a new file or continue in the previous file

if path.exists("Data/last_datetime.dat"):
    with open("Data/last_datetime.dat", "r") as f:
        lastDatetime = f.read()
    lastDatetime = lastDatetime.split("-")
    lastDate = lastDatetime[0]
    lastTime = lastDatetime[1]

    with open("Data/last_datetime.dat", "w") as f:
        f.write(newDatetime)

    if lastDate == newDate:
        resume(lastDate, lastTime)
        
    else:
        redefine(newDate, newTime)

else:
    with open("Data/last_datetime.dat", "w") as f:
        f.write(newDatetime)

    redefine(newDate, newTime)

with open("Data/record.dat", "w") as f:
    f.write("")