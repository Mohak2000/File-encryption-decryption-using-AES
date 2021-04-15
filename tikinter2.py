# import tkinter module
from tkinter import *

import self as self
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad
from base64 import b64encode
import os
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
from base64 import b64decode
import getpass
# import other necessery modules
import random
import time
import datetime
from tkinter import filedialog

# creating root object
root = Tk()

# defining size of window
root.geometry("1200x6000")

# setting up the title of window
root.title("File Encryption and Decryption")

Tops = Frame(root, width=1100, relief=SUNKEN)
Tops.pack(side=TOP)

f1 = Frame(root, width=1100, height=1000,
           relief=SUNKEN)
f1.pack(side=LEFT)

# ==============================================
#				 TIME
# ==============================================
localtime = time.asctime(time.localtime(time.time()))

lblInfo = Label(Tops, font=('helvetica', 50, 'bold'),
                text="CNS project",
                fg="Black", bd=10, anchor='w')

lblInfo.grid(row=0, column=0)

lblInfo = Label(Tops, font=('arial', 20, 'bold'),
                text=localtime, fg="Steel Blue",
                bd=10, anchor='w')

lblInfo.grid(row=1, column=0)

rand = StringVar()

key = StringVar()
mode = StringVar()

upload = StringVar()
self.fileupload_name = StringVar()


# exit function
def qExit():
    root.destroy()


# Function to reset the window
def Reset():
    rand.set("")

    key.set("")
    mode.set("")

    upload.set("")



def browseFiles():
    filename = filedialog.askopenfilename(initialdir="",
                                          title="Select a File",
                                          filetypes=(('all files', '.*'), ('text files', '.txt')
                                                     ))

    fileupload_name = filename

    upload.set(fileupload_name)

    # Change label contents


btnUpload = Button(f1, padx=10, pady=8, bd=10,
                   fg="black", font=('arial', 16, 'bold'),
                   width=10, text="Upload file", bg="yellow", anchor="w",
                   command=browseFiles).grid(row=0, column=0)

txtFile = Entry(f1, font=('arial', 16, 'bold'),
                textvariable=upload, bd=10, insertwidth=4,
                bg="powder blue", justify='right')

txtFile.grid(row=0, column=1)

lblkey = Label(f1, font=('arial', 16, 'bold'),
               text="KEY", bd=16, anchor="w")

lblkey.grid(row=2, column=0)

txtkey = Entry(f1, font=('arial', 16, 'bold'),
               textvariable=key, bd=10, insertwidth=4,
               bg="powder blue", justify='right')

txtkey.grid(row=2, column=1)

lblmode = Label(f1, font=('arial', 16, 'bold'),
                text="MODE(e for encrypt, d for decrypt)",
                bd=16, anchor="w")

lblmode.grid(row=3, column=0)

txtmode = Entry(f1, font=('arial', 16, 'bold'),
                textvariable=mode, bd=10, insertwidth=4,
                bg="powder blue", justify='right')

txtmode.grid(row=3, column=1)

import base64


# Function to encode
def encode(my_key,file_encode):

    print(file_encode)

    my_key = my_key.encode('UTF-8')
    my_key = pad(my_key, AES.block_size)
    with open(file_encode, 'rb') as entry:
        data = entry.read()
        cipher = AES.new(my_key, AES.MODE_CFB)
        ciphertext = cipher.encrypt(pad(data, AES.block_size))

        iv = b64encode(cipher.iv).decode('UTF-8')
        ciphertext = b64encode(ciphertext).decode('UTF-8')
        to_write = iv + ciphertext

    entry.close()

    with open(file_encode + 'encrypted'+'.enc', 'w') as data:
        data.write(to_write)
    data.close()


# Function to decode
def decode(my_key,filedecode_name):

    my_key = my_key.encode('UTF-8')
    my_key = pad(my_key, AES.block_size)

    with open(filedecode_name, 'r') as entry:
        try:
            data = entry.read()
            length = len(data)
            iv = data[:24]
            iv = b64decode(iv)
            ciphertext = data[24:length]
            ciphertext = b64decode(ciphertext)
            cipher = AES.new(my_key, AES.MODE_CFB, iv)
            decrypted = cipher.decrypt(ciphertext)
            decrypted = unpad(decrypted, AES.block_size)
            x=filedecode_name
            y=x[:len(x)-17]
            x=x[len(x)-17:len(x)-13]

            with open(y+"decrypted"+x, 'wb') as data:
                data.write(decrypted)
            data.close()

        except(ValueError, KeyError):
            print("Wrong password")


def Ref():
    k = key.get()

    m = mode.get()

    file_name=upload.get()

    if m == 'e':
        encode(k,file_name)
    else:
        decode(k,file_name)


# Show message button
btnTotal = Button(f1, padx=16, pady=8, bd=16, fg="black",
                  font=('arial', 16, 'bold'), width=10,
                  text="Execute", bg="green",
                  command=Ref).grid(row=9, column=0)

# Reset button
btnReset = Button(f1, padx=16, pady=8, bd=16,
                  fg="black", font=('arial', 16, 'bold'),
                  width=10, text="Reset", bg="red",
                  command=Reset).grid(row=9, column=1)

# Exit button


# keeps window alive
root.mainloop()
