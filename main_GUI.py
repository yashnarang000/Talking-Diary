import customtkinter as ctk
from AI.conversation import Voice
from AI.conversation import Misc
from AI.conversation import Chat
from AI.conversation import time
from PIL import Image
from os import path
from datetime import datetime
import subprocess as sbp
import sys

divider_text = "----------------------------------------------------------------------------------------------"

with open('Data/restart_handler.dat', 'w') as f:
    f.write("0")

def disable_main_buttons(list_of_buttons):
    for button in list_of_buttons:
        button.configure(state=ctk.DISABLED)
    exit_button.configure(state=ctk.NORMAL)

def enable_main_buttons(list_of_buttons):
    for button in list_of_buttons:
        button.configure(state=ctk.NORMAL)

def login_window():
    disable_main_buttons(list_of_buttons)

    login_frame = ctk.CTkFrame(root, fg_color="black")
    login_frame.place(x=275, y=0, relwidth=0.825, relheight=1)  

    fb_id = ctk.CTkEntry(login_frame, placeholder_text="Facebook Login ID", font=("Cascadia Mono", 20), fg_color="#083c3c")
    fb_id.place(anchor=ctk.CENTER, relx = 0.5, rely = 0.25, relwidth = 0.6, relheight = 0.1)

    fb_pass = ctk.CTkEntry(login_frame, placeholder_text="Facebook Password", font=("Cascadia Mono", 20), fg_color="#083c3c")
    fb_pass.place(anchor=ctk.CENTER, relx = 0.5, rely = 0.42, relwidth = 0.6, relheight = 0.1)

    login_button = ctk.CTkButton(login_frame, text="LOGIN", font=("Century Gothic", 40), command = lambda fb_id=fb_id, fb_pass=fb_pass, login_frame=login_frame: login(fb_id, fb_pass, login_frame))
    login_button.place(anchor=ctk.CENTER, relx=0.5, rely=0.62)


def reset_clicked_buttons(list_of_buttons):
    for item in list_of_buttons:
        item.configure(fg_color = "#1f538d", text_color = "#DCE4EE")


def clicked_button(button, list_of_buttons):
    reset_clicked_buttons(list_of_buttons)
    # button.configure(fg_color = "#15365e", text_color = "#231b11")
    button.configure(fg_color = "#000000")

def reset_chat():
    with open('Data/history.dat', 'w') as f:
        f.write("")
    
    with open("Data/record.dat", "w") as f:
        f.write("")


def write_to_diary(entry, chat_frame, frame):
    def reset_handler():

        Chat.input(entry)
        time.sleep(2)
        pi_says = Chat.output()

        me = ctk.CTkLabel(chat_frame, text=f"\nMe: {entry}", font=("Cascadia Mono", 14), wraplength=1000, justify = ctk.LEFT)
        me.pack(anchor=ctk.NW)

        pi = ctk.CTkLabel(chat_frame, text=f"\nPi: {pi_says}", font=("Cascadia Mono", 14), wraplength=1000, justify = ctk.LEFT)
        pi.pack(anchor = ctk.NW)

        reset_chat()
        with open('Data/restart_handler.dat', 'w') as f:
            f.write("1")

        time.sleep(3)
        
        exit()

    if entry == "!reset":
        confirmation(frame=frame, yes_command=reset_handler)
    else:
        Chat.input(entry)

        time.sleep(2)
        pi_says = Chat.output()
    
        with open("Data/record.dat", "a", encoding="utf-8") as f:
            f.write(f"{entry}\n")
        
        with open("Data/history.dat", "a", encoding="utf-8") as f:
            f.write(f"\n\nMe: {entry}\n\nPi: {pi_says}")

        me = ctk.CTkLabel(chat_frame, text=f"\nMe: {entry}", font=("Cascadia Mono", 14), wraplength=1000, justify = ctk.LEFT)
        me.pack(anchor=ctk.NW)

        pi = ctk.CTkLabel(chat_frame, text=f"\nPi: {pi_says}", font=("Cascadia Mono", 14), wraplength=1000, justify = ctk.LEFT)
        pi.pack(anchor = ctk.NW)

        


def handle_text_submission(chatbox, chat_frame, frame):
    text = chatbox.get()
    write_to_diary(text, chat_frame, frame)
    chatbox.delete(0, ctk.END)

def toggle_voice_in_settings(toggler):
    with open("Data/voice_status.dat", "r") as f:
        initial_status = f.read()

    if initial_status == "0":
        final_status = "1"
    else:
        final_status = "0"
    
    with open("Data/voice_status.dat", "w") as f:
        f.write(final_status)

    if final_status == "0":
        voice_icon = ctk.CTkImage(dark_image=Image.open(r"Icons/voice_off.png"), size=(40, 40))
        hover_color = "#5e1414"
    else:
        voice_icon = ctk.CTkImage(dark_image=Image.open(r"Icons/voice_on.png"), size=(50, 50))
        hover_color = "#14375e"

    toggler.configure(image=voice_icon, hover_color=hover_color)    

def toggle_voice(toggler):
    with open("Data/voice_status.dat", "r") as f:
        initial_status = f.read()

    with open("Data/voiceSelect.dat", "r") as f:
        voice = f.read()

    if initial_status == "0":
        final_status = "1"
    else:
        final_status = "0"
    
    with open("Data/voice_status.dat", "w") as f:
        f.write(final_status)
    
    if final_status == "0":
        voice_icon = ctk.CTkImage(dark_image=Image.open(r"Icons/voice_off.png"), size=(40, 40))
        hover_color = "#5e1414"
    else:
        voice_icon = ctk.CTkImage(dark_image=Image.open(r"Icons/voice_on.png"), size=(50, 50))
        hover_color = "#14375e"

    toggler.configure(image=voice_icon, hover_color=hover_color)

    Voice.toggle(voice)
    

def voice_selector(voice):

    voice = voice.split(" ")
    voice = int(voice[1])
    Voice.select(voice)
    with open("Data/voiceSelect.dat", "w") as f:
        f.write(f"{voice}")

def login(fb_id, fb_pass, login_frame):
    login_id = fb_id.get()
    login_pass = fb_pass.get()

    try:
        Misc.login(login_id, login_pass)
    
    except:
        with open(r'Data\loginStatus.dat', 'w') as f:
            f.write("")

    time.sleep(3)

    with open('Data/restart_handler.dat', 'w') as f:
        f.write("1")

    time.sleep(3)
    
    exit()



def icon_grabber(icon):
    return Image.open(rf"Icons/{icon}.png")

def discard_function(chat_frame):
    with open("Data/record.dat", "w") as f:
        f.write("")
    
    divider = ctk.CTkLabel(chat_frame, text=f"\n{divider_text}\n", font=("Cascadia Mono", 18), text_color="red")
    divider.pack(anchor=ctk.CENTER)

def continue_function(chat_frame):
    sbp.run(['python', 'data_handle.py'])

    divider = ctk.CTkLabel(chat_frame, text=f"\n{divider_text}\n", font=("Cascadia Mono", 18), text_color="lime")
    divider.pack(anchor=ctk.CENTER)

def confirmation(frame, yes_command):

    def no_command():
        confirm_text.destroy()
        yes.destroy()
        no.destroy()
    
    def yes_command_handler():
        yes_command()
        confirm_text.destroy()
        yes.destroy()
        no.destroy()
    
    confirm_text = ctk.CTkLabel(frame, text="Are you sure?", font=("Century Gothic", 18, "bold"))
    confirm_text.place(relx = 0.888, rely = 0.35)

    yes_icon = ctk.CTkImage(dark_image=icon_grabber("confirm"), size=(50, 50))
    yes = ctk.CTkButton(frame, text="", image=yes_icon, fg_color="transparent", command=yes_command_handler)
    yes.place(relx=0.928, rely = 0.4, relwidth = 0.06)

    no_icon = ctk.CTkImage(dark_image=icon_grabber("discard"), size=(50, 50))
    no = ctk.CTkButton(frame, text="", image=no_icon, fg_color="transparent", command=no_command)
    no.place(relx=0.88, rely=0.4, relwidth=0.05)

def start():

    clicked_button(start_button, list_of_buttons)

    with open("Data/history.dat", "r", encoding="utf-8") as f:
        chat_history = f.read()


    Misc.wait()

    # Creating new_datetime file

    x = datetime.now()
    y = x.strftime("%d%m%Y-%H%M%S")


    with open("Data/new_datetime.dat", "w") as f:
        f.write(y)

    conversation = ctk.CTkFrame(root, fg_color = "black")
    conversation.place(x=275, y=0, relwidth = 0.825, relheight = 1)

    with open("Data/voiceSelect.dat", "r") as f:
        voice = f.read()
    with open("Data/voice_status.dat", "r") as f:
        voice_status = f.read()
    
    if voice_status == "0":
        voice_icon = ctk.CTkImage(dark_image=Image.open(r"Icons/voice_off.png"), size=(40, 40))
        hover_color = "#5e1414"
    else:
        voice_icon = ctk.CTkImage(dark_image=Image.open(r"Icons/voice_on.png"), size=(50, 50))
        hover_color = "#14375e"
        Voice.toggle(voice)

    voice_toggler = ctk.CTkButton(conversation, image=voice_icon, text="", fg_color="transparent", hover_color=hover_color)
    voice_toggler.configure(command=lambda voice_toggler=voice_toggler: toggle_voice(voice_toggler))
    voice_toggler.place(relx = 0.9, rely = 0.73, relwidth = 0.05)

    chatbox = ctk.CTkEntry(conversation, font=("Cascadia Mono", 14), bg_color="black", fg_color="black", placeholder_text="Let's chat...")
    chatbox.place(relx=0.01, rely=0.85, relwidth = 0.85, relheight=0.1)

    chat_frame = ctk.CTkScrollableFrame(conversation, fg_color="black")
    chat_frame.place(relx = 0.025, rely = 0.05, relheight = 0.77, relwidth = 0.85)

    history =  ctk.CTkLabel(chat_frame, text=chat_history, font=("Cascadia Mono", 14), wraplength=1000, justify=ctk.LEFT)
    history.pack(anchor=ctk.NW)

    chatbox.bind("<Return>", lambda event, chatbox=chatbox, chat_frame=chat_frame, frame=conversation: handle_text_submission(chatbox=chatbox, chat_frame=chat_frame, frame=frame))
    
    send_icon = ctk.CTkImage(dark_image=icon_grabber('send'), size=(50, 50))
    send_button = ctk.CTkButton(conversation, text="", image=send_icon, font=("Arial", 70), command=lambda chatbox=chatbox, chat_frame=chat_frame, frame=conversation: handle_text_submission(chatbox=chatbox, chat_frame=chat_frame, frame=frame))
    send_button.place(relx = 0.87, rely = 0.85, relheight = 0.1, relwidth = 0.1)

    with open("Data/history.dat", "r") as f:
        c_history = f.read()

    if c_history == "":
        if Misc.username == "Profile":
            initial = ctk.CTkLabel(chat_frame, text=f"Hey there, great to meet you. I'm Pi, your personal AI.\nMy goal is to be useful, friendly and fun. Ask me for advice, for answers, or let's talk about whatever's on your mind.\nHow's your day going?", font=("Cascadia Mono", 14), wraplength=1000, justify = ctk.LEFT)
        else:
            initial = ctk.CTkLabel(chat_frame, text=f"Hey {Misc.username}, great to meet you. I'm Pi, your personal AI.\nMy goal is to be useful, friendly and fun. Ask me for advice, for answers, or let's talk about whatever's on your mind.\nHow's your day going?", font=("Cascadia Mono", 14), wraplength=1000, justify = ctk.LEFT)
        
        initial.pack(anchor = ctk.NW)

    else:
        pass

    def continue_function_handler():
        continue_function(chat_frame=chat_frame)

    continue_icon = ctk.CTkImage(dark_image=icon_grabber('continue'), size=(53, 53))

    continue_button = ctk.CTkButton(conversation, text="", fg_color="transparent", image=continue_icon)
    continue_button.configure(command=lambda frame=conversation, command=continue_function_handler: confirmation(frame, command))
    continue_button.place(relx = 0.928, rely = 0.049, relwidth = 0.06)

    discard_icon = ctk.CTkImage(dark_image=icon_grabber('discard'), size=(50, 50))
    def discard_function_handler():
        discard_function(chat_frame=chat_frame)

    
    discard_button = ctk.CTkButton(conversation, text="", fg_color="transparent", image=discard_icon)
    discard_button.configure(command=lambda frame=conversation, command=discard_function_handler: confirmation(frame, command))
    discard_button.place(relx = 0.88, rely = 0.051, relwidth = 0.05)


def settings():
    clicked_button(settings_button, list_of_buttons)

    setting = ctk.CTkFrame(root, fg_color="black")
    setting.place(x=275, y=0, relwidth=0.825, relheight = 1)

    settings_text = ctk.CTkLabel(setting, text="SETTINGS", font=("Century Gothic", 70, "underline"))
    settings_text.pack(anchor=ctk.N, padx = 30, pady=10)

    with open("Data/voiceSelect.dat", "r") as f:
        voice = f.read()
    with open("Data/voice_status.dat", "r") as f:
        voice_status = f.read()
    
    if voice_status == "0":
        voice_icon = ctk.CTkImage(dark_image=Image.open(r"Icons/voice_off.png"), size=(40, 40))
        hover_color = "#5e1414"
    else:
        voice_icon = ctk.CTkImage(dark_image=Image.open(r"Icons/voice_on.png"), size=(50, 50))
        hover_color = "#14375e"

    voice_toggler = ctk.CTkButton(setting, image=voice_icon, text="", fg_color="transparent", hover_color=hover_color)
    voice_toggler.configure(command=lambda voice_toggler=voice_toggler: toggle_voice_in_settings(voice_toggler))
    voice_toggler.place(relx = 0.88, rely = 0.051, relwidth = 0.05)    

    # toggle_voice = ctk.CTkButton(setting, text="Toggle Voice", font=("Tw Cen MT", 75))
    # toggle_voice.place(relx=0.25, rely=0.2, relwidth = 0.5, relheight = 0.25)

    # change_voice = ctk.CTkButton(setting, text="Change Voice", font=("Tw Cen MT", 75))
    # change_voice.place(relx=0.25, rely=0.2, relwidth = 0.5, relheight = 0.25)

    change_voice = ctk.CTkLabel(setting, text="Select voice for your diary ------------------------------------------------------------------------------------------" , font=("Tw Cen MT", 25))
    change_voice.place(relx = 0.05, rely = 0.5)
    
    voice_list = []
    for n in range(8):
        voice_list.append(f"Voice {n+1}")
        n = n+1
    
    with open("Data/voiceSelect.dat", "r") as f:
        initial_voice = f.read()
    
    initial_value = ctk.StringVar(value=f'Voice {initial_voice}')
    available_voices = ctk.CTkComboBox(setting, values=voice_list, command=voice_selector, variable=initial_value)
    available_voices.place(relx = 0.85, rely = 0.505)


def exit():
    clicked_button(exit_button, list_of_buttons)
    Misc.quit()
    sys.exit()

root = ctk.CTk()

root.title("Talking Diary")

root.iconbitmap(r"Icons\app_icon.ico")

root._state_before_windows_set_titlebar_color = 'zoomed'

ctk.set_default_color_theme("dark-blue")
ctk.set_appearance_mode('dark')


menu = ctk.CTkFrame(root)
menu.pack(fill=ctk.Y, anchor=ctk.W, expand=True)

title = ctk.CTkLabel(menu, text="Talking\nDiary", font=('Century Gothic', 40), text_color="white")
title.pack(pady=50, padx=70)

start_button = ctk.CTkButton(menu, text="Chat", font=("Tw Cen MT", 37), command=start)
start_button.pack(pady=15)

settings_button = ctk.CTkButton(menu, text="Settings", font=("Tw Cen MT", 37), command=settings)
settings_button.pack(pady=15)

exit_button = ctk.CTkButton(menu, text="Exit", font=("Tw Cen MT", 37), command=exit)
exit_button.pack(pady=15)

credit = ctk.CTkLabel(menu, text="PROGRAMMED BY ALPHACOMET", font=('Cascadia Mono', 14))
credit.place(relx=0.095, rely=0.95)

list_of_buttons = [start_button, settings_button, exit_button]


guide = ctk.CTkScrollableFrame(root, fg_color="transparent")
guide.place(x=275, y=0, relwidth=0.825, relheight = 1)

invisible_frame = ctk.CTkFrame(guide, fg_color="transparent", height = 200, width = 300)
invisible_frame.grid(row = 0, column = 0)

try:
    if Misc.username == "Profile":
        welcome = ctk.CTkLabel(guide, text=f"Welcome back!", font=('Century Gothic', 70), text_color="white")
    else:
        welcome = ctk.CTkLabel(guide, text=f"Welcome back, {Misc.username}!", font=('Century Gothic', 70), text_color="white")

except:
    welcome = ctk.CTkLabel(guide, text=f"Welcome back!", font=('Century Gothic', 70), text_color="white")

welcome.place(anchor=ctk.N, relx=0.5, rely=0.01)

text1 = ctk.CTkLabel(guide, text="I am PI - The Talking Diary. If you ever feel journaling the traditional way boring, try me.\nChat with me, share your experiences, and you'll end up with personalized journal entries in your hands.", font=('Century Gothic', 18, 'bold'), justify = ctk.CENTER)
text1.place(relx=0.148, rely=0.06)

frame1 = ctk.CTkFrame(guide, corner_radius=20, border_color="#14375e", border_width=5, fg_color="gray10")
frame1.grid(row = 1, column = 0, padx = 5, pady = 30, ipady=10)

text2 = ctk.CTkLabel(frame1, text="Quick Guide", font=("Century Gothic", 50, 'underline'), justify=ctk.LEFT, text_color='white')
text2.pack(pady = 10, padx = 20)

text3 = ctk.CTkLabel(frame1, text="Chat > Greet me here\n\nSettings > Change my voice here\n\nExit > Sayonara!", font=("Cascadia Mono", 25, 'bold'), justify=ctk.CENTER, width = 1195)
text3.pack(padx = 20, pady = 90)

text4 = ctk.CTkLabel(frame1, text="\n\n\nScroll down for more", font=("Cascadia Mono", 18, 'bold'), justify=ctk.LEFT, width = 1195)
text4.pack()

frame2 = ctk.CTkFrame(guide, corner_radius=20, border_color="#14375e", border_width=5, fg_color="gray10")
frame2.grid(row = 2, column = 0, padx = 10, pady = 20)

screenshot = ctk.CTkImage(dark_image=icon_grabber('guide_screenshot'), size=(1195, 635))
screenshot_label = ctk.CTkLabel(frame2, image=screenshot, text="", height=635, width=1195)
screenshot_label.pack()

frame3 = ctk.CTkFrame(guide, corner_radius=20, border_color="#14375e", border_width=5, fg_color="gray10")
frame3.grid(row = 3, column = 0, padx = 5, pady = 30, ipady=30)

text5 = ctk.CTkLabel(frame3, text="Discard, Continue & Reset Functions", font=("Century Gothic", 50, 'underline'), justify=ctk.LEFT, text_color='white', width=1195)
text5.pack(anchor=ctk.W, pady = 15, padx = 20)

text6 = ctk.CTkLabel(frame3, text="Discard:\n\n    > You will see this button at the top of the right pane.\n\n    Suppose you've talked your heart out about your crush in the night — and in the day, clarity strikes you. You want that past conversation to not be the part of your final journal entry. What do you do? You click on Discard button.\n\n\nContinue:\n\n    > This button is located at the right of Discard button.\n\n    You click this button when the conversation is over and now you want to make a diary entry based on the conversation.\n\n\nReset:\n\n    > You can used Reset feature by typing '!reset' in the chatbox.\n\n    This is an emotional feature 🥹 You've had long chats with me, but for some reason, you want to start again with a fresh slate — you use Reset function and I will have not a little memory of what we talked about. Use it carefully 🙂")
text6.configure(font=("Cascadia Mono", 18, "bold"), justify=ctk.LEFT, width = 1195, wraplength = 1000)
text6.pack(padx = 20, pady = 15)

if path.exists("Data/loginStatus.dat"):
    pass
else:
    login_window()

root.mainloop()