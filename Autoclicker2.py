import customtkinter
import tkinter
import mouse
import keyboard
import time
# pip install mouse
# pip install keyboard
# pip install customtkinter

cps = None

start_key = "x"
stop_key = "z"

start = False

def set_cps(x):
  global cps
  cps = x

customtkinter.set_appearance_mode("Light")

w = customtkinter.CTk()
w.geometry("700x650")
w.minsize(500, 650)
w.maxsize(720, 720)
w.title("Autoclicker")

label_title = customtkinter.CTkLabel(w, text="Select a CPS type :",text_font=("Arial", 20))
label_title.pack(pady=30, padx=10)

checkbox_1 = customtkinter.CTkCheckBox(w, text="10 CPS", text_font=("Arial", 15), command=lambda: set_cps(10))
checkbox_1.pack(pady=10, padx=10)

checkbox_2 = customtkinter.CTkCheckBox(w, text="20 CPS", text_font=("Arial", 15), command=lambda: set_cps(20))
checkbox_2.pack(pady=10, padx=10)

checkbox_3 = customtkinter.CTkCheckBox(w, text="30 CPS", text_font=("Arial", 15), command=lambda: set_cps(30))
checkbox_3.pack(pady=10, padx=10)

checkbox_4 = customtkinter.CTkCheckBox(w, text="45 CPS", text_font=("Arial", 15), command=lambda: set_cps(45))
checkbox_4.pack(pady=10, padx=10)

checkbox_5 = customtkinter.CTkCheckBox(w, text="65 CPS", text_font=("Arial", 15), command=lambda: set_cps(65))
checkbox_5.pack(pady=10, padx=10)


entry_1 = customtkinter.CTkEntry(w, text_font=(15), placeholder_text="Key to start :")
entry_1.pack(pady=12, padx=10)


def entry_1_event():
    global start_key
    start_key = entry_1.get()

start_button = customtkinter.CTkButton(w, text="Start Key select", text_font=("Arial", 15), command=entry_1_event)
start_button.pack(pady=12, padx=10)

entry_2 = customtkinter.CTkEntry(w, text_font=(15), placeholder_text="Key to stop :")
entry_2.pack(pady=12, padx=10)
stop_key = entry_2.get()

def entry_2_event():
    global stop_key
    stop_key = entry_2.get()

stop_button = customtkinter.CTkButton(w, text="Stop Key select", text_font=("Arial", 15), command=entry_2_event)
stop_button.pack(pady=12, padx=10)

label_title = customtkinter.CTkLabel(w, text="Close the page to use the Autoclicker !",text_font=("Arial", 20))
label_title.pack(pady=30, padx=10)

w.mainloop()

while True:
    while start == False:
        if keyboard.is_pressed(start_key):
            start = True
    while start == True:
        if keyboard.is_pressed(stop_key):
            start = False
        elif cps == 10:
            time.sleep(1/cps)
            mouse.click("left")
        elif cps == 20:
            time.sleep(1/cps)
            mouse.click("left")
        elif cps == 30:
            time.sleep(0.5/cps)
            mouse.click("left")
        elif cps == 45:
            time.sleep(0.65/cps)
            mouse.click("left")
        elif cps == 65:
            time.sleep(0.5/cps)
            mouse.click("left")