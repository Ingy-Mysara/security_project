import os.path

import customtkinter as ctk
from ftplib import FTP
from customtkinter import filedialog

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("dark-blue")

root = ctk.CTk()
root.title("Login")
root.geometry("500x500")
frame1 = ctk.CTkFrame(master=root)
frame1.pack(pady=20, padx=60, fill="both", expand=True)
label= ctk.CTkLabel(master=frame1, text="Login to FTP")
label.pack(pady=12, padx=10)

username_entry = ctk.CTkEntry(master=frame1, placeholder_text="Enter Username")
username_entry.pack(pady=12, padx=10)

password_entry = ctk.CTkEntry(master=frame1, placeholder_text="Enter Password", show="*")
password_entry.pack(pady=12, padx=10)





host = "127.0.0.1"
port = 6060








def uploadeditems():
    ctk.set_appearance_mode("dark")
    ctk.set_default_color_theme("dark-blue")
    root = ctk.CTk()
    root.title("Uploaded items")
    root.geometry("500x500")

    frame3 = ctk.CTkFrame(master=root)
    frame3.place(height=250, width=500)
    frame3.pack(pady=20, padx=60, fill="both", expand=True)
    label3 = ctk.CTkLabel(master=frame3, text="Uploaded files")
    label3.pack(pady=12, padx=10)

    with FTP(host) as ftp:
        ftp.connect(host=host, port=port)
        ftp.login(user=username_entry.get(), passwd=password_entry.get())
        fileitems = ftp.nlst()
        for i in fileitems:
            print(i)
            itemlabel = ctk.CTkLabel(master=frame3, text=i, width=480, height=30, corner_radius=10, fg_color="#1f538d")
            itemlabel.place(relx=0.5, rely=0.5, anchor=ctk.W)
            itemlabel.pack(pady=5, padx=10)

    root.mainloop()


def chooseGUI():
    ctk.set_appearance_mode("dark")
    ctk.set_default_color_theme("dark-blue")
    root = ctk.CTk()
    root.title("Upload or Download")
    root.geometry("500x500")
    frame = ctk.CTkFrame(master=root)
    frame.pack(pady=20, padx=60, fill="both", expand=True)
    label = ctk.CTkLabel(master=frame, text="upload or download")
    label.pack(pady=12, padx=10)
    download_button = ctk.CTkButton(master=frame, text="Download", command=lambda: filedownloadGUI())
    download_button.pack(pady=12, padx=10)

    upload_button = ctk.CTkButton(master=frame, text="Upload", command=lambda: fileuploadGUI())
    upload_button.pack(pady=12, padx=10)


    root.mainloop()

def download(combox):
    val = combox.get()
    print(val)
    with FTP(host) as ftp:
        ftp.connect(host=host, port=port)
        ftp.login(user=username_entry.get(), passwd=password_entry.get())
        with open(val, "wb") as file:

            ftp.retrbinary(f"RETR {val}", file.write)
            # quit and close the connection
        ftp.quit()





def filedownloadGUI():
    ctk.set_appearance_mode("dark")
    ctk.set_default_color_theme("dark-blue")
    root = ctk.CTk()
    root.title("Download items")
    root.geometry("500x500")
    frame4 = ctk.CTkFrame(master=root)

    label4 = ctk.CTkLabel(master=frame4, text="Download")
    frame4.place(height=250, width=500)
    frame4.pack(pady=20, padx=60, fill="both", expand=True)
    label4.pack(pady=12, padx=10)

    with FTP(host) as ftp:
        ftp.connect(host=host, port=port)
        ftp.login(user=username_entry.get(), passwd=password_entry.get())
        fileitems = ftp.nlst()

    combobox = ctk.CTkOptionMenu(master=frame4, values=fileitems)
    combobox.pack(padx=20, pady=10)





    download_button = ctk.CTkButton(master=frame4, text="Download", command=lambda: download(combobox))
    download_button.pack(pady=12, padx=10)

    root.mainloop()


def upload():

    with FTP(host) as ftp:
        ftp.connect(host=host, port=port)
        ftp.login(user=username_entry.get(), passwd=password_entry.get())

        file = filedialog.askopenfilename(initialdir="D:\\semester9\\security_project\\security_project") #u can change this to your own default directory or remove it at all
        fileobj=open(file, "rb")

        filename = os.path.basename(file)
        ftp.storbinary("STOR " + filename, fileobj)

        uploadeditems()
        ftp.quit()
    root.mainloop()




def fileuploadGUI():
   upload()



def accessFTP():
    with FTP(host) as ftp:
        user = username_entry.get()
        password = password_entry.get()
        ftp.connect(host=host, port=port)
        ftp.login(user=user, passwd=password)
        login_response = ftp.login(user, password)
        print(login_response)
        print(ftp.getwelcome())
        print(username_entry.get())

        chooseGUI()

        return user, password





login_button = ctk.CTkButton(master=frame1, text="Join ftp server", command=accessFTP)
login_button.pack(pady=12, padx=10)


root.mainloop()
