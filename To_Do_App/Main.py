import customtkinter as ctk
import os
import shutil
from tkinter.filedialog import *
import subprocess
import requests
from PIL import Image
from io import BytesIO
filepath = ""
chemin_du_dossier = ".AppData"
try:
    os.mkdir(chemin_du_dossier)
    print(f"Le dossier '{chemin_du_dossier}' a été créé avec succès.")
except FileExistsError:
    False
except Exception as e:
    print(f"Une erreur est survenue : {e}")

# Assurez-vous que contenu est toujours défini
contenu = []  # Définition par défaut de contenu

try:
    with open(".AppData/projet.txt", 'r') as f:
        contenu = [ligne.strip() for ligne in f.readlines()]
except FileNotFoundError:
    with open(".AppData/projet.txt", 'w') as f:
        f.close()
if os.path.exists(".AppData/Icon.ico"):
    False
else:
    url = 'https://cdn-icons-png.flaticon.com/512/18212/18212580.png'
    response = requests.get(url)
    Icone_data = Image.open(BytesIO(response.content))
    Icone_data.save(".AppData/Icon.ico", format="ICO")

def NewDo(i, ToDos_callback):
    def NewDo2():
        global i
        with open(f".AppData/{i}/ToDo.txt", 'r') as f:
            contenuDO = [ligne.strip() for ligne in f.readlines()]
        if entree.get() == "" or entree.get() in contenuDO:
            return
        else:
            contenuDO.append(entree.get())
            with open(f".AppData/{i}/ToDo.txt", 'w') as f:
                for ligne in contenuDO:
                    f.write(ligne + "\n")
        DO.destroy()
        ToDos_callback(i)  # Appel de la fonction ToDos passée en paramètre

    DO = ctk.CTk()
    DO.iconbitmap(".AppData/Icon.ico")
    DO.title("Add ToDo")
    DO.resizable(False, False)
    entree = ctk.CTkEntry(DO, font=('Calibri', 15), width=300, placeholder_text="ToDo Name")
    ok = ctk.CTkButton(DO, font=('Calibri', 15), width=150, text="Ok", command=NewDo2)
    cancel = ctk.CTkButton(DO, font=('Calibri', 15), width=150, text="Cancel", command=DO.destroy)
    entree.grid(row=0, column=0, columnspan=2, pady=5, padx=5)
    ok.grid(row=1, column=0, pady=5, padx=5)
    cancel.grid(row=1, column=1, pady=5, padx=5)
    DO.mainloop()

def NewFile(i, File_callback):
    def filedialoge():
        global filepath
        filepath = askopenfilename(title="Ouvrir un fichier", filetypes=[('all files', '.*')])

    def NeFile2():
        global filepath
        if not filepath or not entree.get():
            return

        with open(f".AppData/{i}/FilePath.txt", 'a') as f:
            f.write(filepath + "\n")

        with open(f".AppData/{i}/File.txt", 'a') as f:
            f.write(entree.get() + "\n")

        File.destroy()
        File_callback(i)

    File = ctk.CTk()
    File.title("Add File")
    File.iconbitmap(".AppData/Icon.ico")
    File.resizable(False, False)
    entree = ctk.CTkEntry(File, font=('Calibri', 15), width=300, placeholder_text="Nom du fichier")
    FileBTN = ctk.CTkButton(File, text="Sélectionner un fichier", command=filedialoge, font=('Calibri', 15), width=240)
    ok = ctk.CTkButton(File, text="Ok", command=NeFile2, font=('Calibri', 15), width=150)
    cancel = ctk.CTkButton(File, text="Annuler", command=File.destroy, font=('Calibri', 15), width=150)

    entree.grid(row=0, column=0, columnspan=2, pady=5, padx=5)
    FileBTN.grid(row=1, column=0, columnspan=2, pady=5, padx=5)
    ok.grid(row=2, column=0, pady=5, padx=5)
    cancel.grid(row=2, column=1, pady=5, padx=5)
    File.mainloop()

def new():
    def ToDos(i):
        def remove(k):
            if k in contenuDO:
                contenuDO.remove(k)
                with open(f".AppData/{i}/ToDo.txt", 'w') as f:
                    for ligne in contenuDO:
                        f.write(ligne + "\n")
            for widget in frame.winfo_children():
                widget.destroy()
            ToDos(i)  # Rappeler ToDos après suppression

        with open(f".AppData/{i}/ToDo.txt", 'r') as f:
            contenuDO = [ligne.strip() for ligne in f.readlines()]

        if contenuDO != []:
            a = 0
            frame = ctk.CTkScrollableFrame(master=tab.tab(i), fg_color="#1d1d26", width=300, height=300)
            frame.grid(row=1, column=0, pady=5, padx=5)
            for k in contenuDO:
                frameDO = ctk.CTkFrame(master=frame, width=280, height=50)
                frameDO.grid(row=a, column=0, pady=5, padx=5)
                checkbox = ctk.CTkCheckBox(master=frameDO, text=k, onvalue="on", offvalue="off", font=("Calibri", 20, "bold"))
                checkbox.grid(row=0, column=0, pady=5, padx=5)
                Suppr = ctk.CTkButton(master=frameDO, text="⨯", width=35, font=("Calibri", 30, "bold"), command=lambda k=k: remove(k), fg_color="#ce0000", hover_color="#aa0000")
                Suppr.grid(row=0, column=1, pady=5, padx=5)
                a += 1
    def New2(i):
        def fonction(ID):
            with open(f".AppData/{tab.get()}/FilePath.txt", 'r') as f:
                FilePathLien = [ligne.strip() for ligne in f.readlines()]
            os.startfile(FilePathLien[ID])
        def remove(k):
            if k in contenuFile:
                contenuFilePath.pop(contenuFile.index(k))
                with open(f".AppData/{i}/FilePath.txt", 'w') as f:
                    for ligne in contenuFilePath:
                        f.write(ligne + "\n")
                contenuFile.remove(k)
                with open(f".AppData/{i}/File.txt", 'w') as f:
                    for ligne in contenuFile:
                        f.write(ligne + "\n")
            for widget in frame2.winfo_children():
                widget.destroy()
            New2(i)  # Rappeler ToDos après suppression
        with open(f".AppData/{i}/File.txt", 'r') as f:
            contenuFile = [ligne.strip() for ligne in f.readlines()]
        with open(f".AppData/{i}/FilePath.txt", 'r') as f:
            contenuFilePath = [ligne.strip() for ligne in f.readlines()]
        if contenuFile != []:
            a=0
            for k in contenuFile:
                ID = a
                frameFile = ctk.CTkFrame(master=frame2, width=280, height=50)
                frameFile.grid(row=a, column=0, pady=5, padx=5)
                button = ctk.CTkButton(master = frameFile, text=k, command=lambda ID=ID: fonction(ID))
                button.grid(row=0, column=0, pady=5, padx=5)
                Suppr2 = ctk.CTkButton(master=frameFile, text="⨯", width=35, font=("Calibri", 30, "bold"), command=lambda k=k: remove(k), fg_color="#ce0000", hover_color="#aa0000")
                Suppr2.grid(row=0, column=1, pady=5, padx=5)
                a+=1
    global contenu
    for i in contenu:
        frame = ctk.CTkScrollableFrame(master=tab.tab(i), fg_color="#1d1d26", width=300, height=300)
        frame.grid(row=1, column=0, pady=5, padx=5)
        newDOBTN = ctk.CTkButton(master=tab.tab(i), text="New ToDo", command=lambda i=i: NewDo(i, ToDos))
        newDOBTN.grid(row=0, column=0, pady=5, padx=5)
        frame2 = ctk.CTkScrollableFrame(master=tab.tab(i), fg_color="#1d1d26", width=300, height=300)
        frame2.grid(row=1, column=1, pady=5, padx=5)
        newFileBTN = ctk.CTkButton(master=tab.tab(i), text="New File", command=lambda i=i: NewFile(i, New2))
        newFileBTN.grid(row=0, column=1, pady=5, padx=5)
        New2(i)
        ToDos(i)

def AddProject():
    def AddProject2():
        if entree.get() == "" or entree.get() in contenu:
            return
        else:
            contenu.append(entree.get())
            with open(f".AppData/projet.txt", 'w') as f:
                for ligne in contenu:
                    f.write(ligne + "\n")
            tab.add(entree.get())
            os.mkdir(f".AppData/{entree.get()}")
            with open(f".AppData/{entree.get()}/ToDo.txt", 'w') as f:
                f.close()
            with open(f".AppData/{entree.get()}/File.txt", 'w') as f:
                f.close()
            with open(f".AppData/{entree.get()}/FilePath.txt", 'w') as f:
                f.close()
        textbox.insert("end", entree.get() + "\n")
        add.destroy()
        new()

    add = ctk.CTk()
    add.title("Add Project")
    add.resizable(False, False)
    add.iconbitmap(".AppData/Icon.ico")
    entree = ctk.CTkEntry(add, font=('Calibri', 15), width=300, placeholder_text="NameProject")
    ok = ctk.CTkButton(add, font=('Calibri', 15), width=150, text="Ok", command=AddProject2)
    cancel = ctk.CTkButton(add, font=('Calibri', 15), width=150, text="Cancel", command=add.destroy)
    entree.grid(row=0, column=0, columnspan=2, pady=5, padx=5)
    ok.grid(row=1, column=0, pady=5, padx=5)
    cancel.grid(row=1, column=1, pady=5, padx=5)
    add.mainloop()

app = ctk.CTk()
app.title("Main")
app.grid_rowconfigure(0, weight=1)
app.grid_columnconfigure(0, weight=1)
app.resizable(False, False)
app.iconbitmap(".AppData/Icon.ico")

tab = ctk.CTkTabview(app)
tab.add("Acceuil")  # add tab at the end
for i in contenu:
    tab.add(i)
tab.set("Acceuil")
addBTN = ctk.CTkButton(master=tab.tab("Acceuil"), text="Add Project", command=AddProject, font = ("Calibri", 15, "bold"), width = 200)
addBTN.grid(row=0, column=0, pady=5, padx=5)
textbox = ctk.CTkTextbox(master=tab.tab("Acceuil"),font = ("Calibri", 20, "bold"), width = 200)
textbox.grid(row=1, column=0, pady=5, padx=5, rowspan=10)
Nameget = ctk.CTkEntry(master=tab.tab("Acceuil"),font = ("Calibri", 15, "bold"), width = 200, placeholder_text="Name of Project")
Nameget.grid(row=0, column=1, pady=5, padx=5)
Title = ctk.CTkLabel(master=tab.tab("Acceuil"),font = ("Calibri", 20, "bold"), width = 200, text="Action :")
Title.grid(row=1, column=1, pady=5, padx=5)
for element in contenu:
    textbox.insert("end", element + "\n")

#Action
def delete():
    if Nameget.get() in contenu:
        contenu.remove(Nameget.get())
        with open(".AppData/projet.txt", 'w') as f:
            for ligne in contenu:
                f.write(ligne + "\n")
        tab.delete(Nameget.get())
        shutil.rmtree(f".AppData/{Nameget.get()}")
    else:
        return
def openFolder():
    if os.path.exists(f".AppData/{Nameget.get()}"):
        print("ok")
    if Nameget.get() in contenu:
        path = os.path.dirname(os.path.abspath(__file__))
        os.startfile(f"{path}/.AppData/{Nameget.get()}")
suppression = ctk.CTkButton(master=tab.tab("Acceuil"),font = ("Calibri", 15, "bold"), width = 180, text="Delete", command = delete)
suppression.grid(row=2, column=1, pady=5, padx=5)
openFolder = ctk.CTkButton(master=tab.tab("Acceuil"),font = ("Calibri", 15, "bold"), width = 180, text="Open in explorer", command = openFolder)
openFolder.grid(row=3, column=1, pady=5, padx=5)
tab.grid(row=1, column=0, pady=5, padx=5, sticky="nsew")
if contenu != []:
    new()
app.mainloop()
