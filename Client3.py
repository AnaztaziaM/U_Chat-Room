import tkinter
import socket
from tkinter import *
from threading import Thread

def receive():
    while True:
        try:
            msg = s.recv(1024).decode("utf8")
            msg_list.insert(tkinter.END, msg)
        except:
            print("There is an error Receiving the Message.")

def send():
    msg = my_msg.get()
    my_msg.set("")
    s.send((bytes(msg, "utf8")))
    if msg == "#quit":
        s.close()
        window.close()


def on_closing():
    my_msg.set("#quit")
    send()


window = Tk()
window.title("Chat Room Application")
window.configure(bg="#A0522D")
window.bind('<Return>', send)

def enter(event):
    send()
window.bind('<Return>', enter)

message_frame = Frame(window, height=100, width=100, bg='white')
message_frame.pack()

my_msg = StringVar()
my_msg.set("")

scroll_bar = Scrollbar(message_frame)
msg_list = Listbox(message_frame, height=15, width=100, bg="#FFDAB9", font=("Aerial", 18), yscrollcommand=scroll_bar.set)
scroll_bar.pack(side=RIGHT, fill=Y)
msg_list.pack(side=LEFT, fill=BOTH)
msg_list.pack()

label = Label(window, text="Enter the Message", fg="black", font=("Aerial", 18, "bold"), bg="#FFDAB9")
label.pack()

entry_field = Entry(window, textvariable=my_msg, bg="#FFE4B5", fg='black', font=("Aerial", 14), width=100)
entry_field.pack()

send_Button = Button(window, text="Send", font=("Aerial", 18), bg="#ff9047", fg="black", command=send)
send_Button.pack()

quit_Button = Button(window, text="Quit", font=("Aerial", 15), bg="#ff9047", fg="black", command=on_closing)
quit_Button.pack()

Host = "127.0.0.1"
Port = 8080

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((Host, Port))

recieve_Tread = Thread(target=receive)
recieve_Tread.start()
mainloop()
