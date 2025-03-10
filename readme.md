# Introduction

Bored of writing your diary/journal the old traditional way?

Introducing, **Talking Diary!**

    > Chat with it.

    > Share your experiences and thoughts.

    > Let it automatically generate diary entry for you based on your conversation.


# What is Talking Diary made of?

Talking Diary is an AI-powered diary writer program and it is made by integrating two very popular AI language models:

## 1. Pi AI

**Pi AI** is an AI chatbot, created by **Inflection AI**, and is built to provide helpful, engaging, and fun conversation for anyone who interacts with Pi. This is the main frontend AI that you interact with.

### Why Pi?
The conversation holder - one of the special reasons I chose Pi for this project. Seriously dude, just try having a conversation with Pi and you'll get to know it better.

**CAUTION : IT WILL MAKE YOUR GOSSIPS NEVERENDING!**

## 2. Gemini AI (From Google)

**Gemini**, formerly known as Bard, is a generative artificial intelligence chatbot developed by **Google**. This AI is the mastermind of all your magical diary entries. It operates in the backend and transforms your conversations with Pi into a creative page of your personal diary. 

### Why Gemini?

First, the level of creativity of Gemini AI transcends the requirement for this project. Second, its API availability ensures stable backend processing. Third...

**why not?**

# How to use Talking Diary?

For first timers, do not panic and just follow the instructions. Installing and using Talking Diary is easy.

## Installation

### Step 1: Install Python

Install Python if not already installed. There are many tutorials available for how to do it correctly, but the most basic way to do it is to go to https://www.python.org/downloads/ and download the latest version.

Once you have downloaded the setup file, install it in your system with default options.

### Step 2: Download Talking Diary

Follow this link to the github repository (if you are not already there): https://github.com/Alpha-Comet/talkingdiary

Click on 'Code' dropdown and download ZIP from there.

### Step 3: Extract ZIP

Extract the ZIP file that you have now installed to your desired folder.

### Step 4: Install required libraries

There should be a file in the talkingdiary folder named 'requirements_installer.py'. Open that file using Python that you just installed on your machine. 

This will take some time to install the dependencies. But once the download is complete, you'll have no problem continuing with the upcoming steps. 

### Step 5: Gemini API Setup

As mentioned, Talking Diary uses Gemini AI's API as its backend. So, you'll have to set it up to get it to work properly. 

    1. Go to https://aistudio.google.com/app/

    2. Login if you haven't.
   
    3. Click on 'Get API key'.
   
    4. Click on 'Create API key'

    5. Select Generative Language Cliet in the dropdown and create it. 

    6. You will not have your API key available. Just copy it. 

Make sure that you do not copy anything else in the process except your API key.

Open 'gemini-configure.py' file in your talkingdiary folder and let the magic happen. 

Your API key is now set as an environment variable of your machine and can easily be accessed by the Talking Diary program.

### Step 6: Launch and login with your Facebook account.

You'll have to create a Facebook account first if you do not have one. 

Open launcher.py and enter your Facebook ID and Password (you do not have to do it everytime you launch the program, it's just a one time process).

Wait a little and BOOM, your Talking Diary is now unlocked and should work smooth as a butter. 

**Still confused? The quick tutorial at the startup is just for you. Scroll through it to know its fascinating features.**

**Finally, all your diary files with be available in the Diary folder in both .md and .html extensions.**