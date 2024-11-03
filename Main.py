import customtkinter
from PIL import Image
import threading
# Problème de si on ferme l'autoclick
import requests
from io import BytesIO
import subprocess
import os
import gdown
import tkinter
from tkinter import messagebox
import shutil

def importer(commande):
    resultat = subprocess.run(f"pip install {commande}", shell=True, capture_output=True, text=True)
    print(f"{commande} as downloaded")

try :
    with open("Download.txt", "r+") as f:
        if f.read() == "True" :
            print("D'ONT CLOSE DOWNLOADING FILES AND FOLDERS (~8m-10m)")
            importer("gdown")
            importer("lmproof")
            importer("os")
            importer("io")
            importer("requests")
            importer("random")
            importer("pyperclip")
            importer("customtkinter")
            importer("PIL")
            importer("keyboard")
            importer("time")
            importer("pyautogui")
            importer("pygame")
            importer("socket")
            importer("scapy.all")
            importer("threading")
            importer("pyspellchecker")
            importer("shutil")
            f.seek(0)
            f.write("False")
            f.truncate()
            f.close()
except FileNotFoundError :
    with open("Download.txt", "w") as f:
        f.write("True")
        print("D'ONT CLOSE DOWNLOADING FILES AND FOLDERS (~8m-10m)")
        importer("gdown")
        importer("lmproof")
        importer("os")
        importer("io")
        importer("requests")
        importer("random")
        importer("pyperclip")
        importer("customtkinter")
        importer("PIL")
        importer("keyboard")
        importer("time")
        importer("pyautogui")
        importer("pygame")
        importer("socket")
        importer("scapy.all")
        importer("threading")
        importer("pyspellchecker")
        importer("shutil")


nom_dossier = "DataJusteSuite"
Maj = "False"
liste = []


# Création dossier
try:
    os.mkdir(nom_dossier)
    print(f"Dossier '{nom_dossier}' créé avec succès.")
except FileExistsError:
    print("fichier déja existant")

try:
    os.mkdir("MajFiles")
    print(f"Dossier MajFiles créé avec succès.")
except FileExistsError:
    print("fichier déja existant")

if os.path.exists("DataJusteSuite/iconMain.ico") or Maj == True:
    False
else:
    try :
        url = 'https://cdn-icons-png.flaticon.com/512/5253/5253815.png'
        response = requests.get(url)
        Icone_data = Image.open(BytesIO(response.content))
        Icone_data.save("DataJusteSuite/iconMain.ico", format="ICO")
    except requests.exceptions.ConnectionError :
        print("no wifi")

if Maj == "False" :
    try :
        with open("MajFiles/Upadte.txt", "r") as f :
            Maj = f.read()
            f.close()
            with open("MajFiles/Upadte.txt", "w") as f :
                f.write("False")

    except FileNotFoundError :
        with open("MajFiles/Upadte.txt", "w") as f :
            f.write("Fasle")
            f.close()
            with open("MajFiles/Upadte.txt", "r") as f :
                Maj = f.read()
                f.close()
                with open("MajFiles/Upadte.txt", "w") as f :
                    f.write("False")

app = customtkinter.CTk()
app.resizable(False, False)
app.title("Menu : Juste suite")
try :
    try :
        app.iconbitmap("DataJusteSuite/iconMain.ico")
    except customtkinter.TclError :
        print("no wifi")
except AttributeError:
    print("already not")


# Class, fonction

def cmd(Path, var):
    def cmd2(Path):
        subprocess.run(['python', Path])
    var = threading.Thread(target=lambda : cmd2(Path), daemon=True)
    var.start()

class Launch(customtkinter.CTkButton):
    def __init__(self, master, texte, image, commande):
        super().__init__(master=master)
        self.configure(font=('Calibri', 13, 'bold'))
        self.configure(text=texte)
        self.configure(compound="top")
        self.configure(image=image)
        self.configure(command=lambda : cmd(commande, ""))
        self.configure(width=100, height=75)
        self.configure(corner_radius=15)

class Images(customtkinter.CTkImage):
    def __init__(self, url):
        try:
            light_image = Image.open(url)
            dark_image = Image.open(url)
            super().__init__(light_image=light_image, dark_image=dark_image)
            self.configure(size=(37, 37))
        except FileNotFoundError:
            print("no wifi")

def loadFile(Path, url):
    if os.path.exists(Path):
        if Maj == "True" :
            try :
                file_id = url.split('/')[-2]
                download_url = f'https://drive.google.com/uc?id={file_id}'
                output = Path
                gdown.download(download_url, output, quiet=False)
            except requests.exceptions.ConnectionError :
                print("no wifi")
    else:
        try :
            file_id = url.split('/')[-2]
            download_url = f'https://drive.google.com/uc?id={file_id}'
            output = Path
            gdown.download(download_url, output, quiet=False)
        except requests.exceptions.ConnectionError :
            print("no wifi")

def loadImage(Path, url, extention):
    if os.path.exists(Path):
        if Maj == "True" :
            try :
                response = requests.get(url)
                Icone_data = Image.open(BytesIO(response.content))
                Icone_data.save(Path, format=extention.upper())
            except requests.exceptions.ConnectionError :
                print("no wifi")
    else:
        try :
            response = requests.get(url)
            Icone_data = Image.open(BytesIO(response.content))
            Icone_data.save(Path, format=extention.upper())
        except requests.exceptions.ConnectionError :
            print("no wifi")

tabview = customtkinter.CTkTabview(master=app)
tabview.grid(row = 0, column = 0, padx=5, pady=5, rowspan = 3)

tabview.add("All")

frame_Object = customtkinter.CTkScrollableFrame(master=tabview.tab("All"), width=350, height=200)
frame_Object.grid(row = 0, column = 0)

# Création dossier
try:
    os.mkdir("Rapideaccès")
    print(f"Dossier Rapideaccès créé avec succès.")
except FileExistsError:
    print("fichier déja existant")
try:
    os.mkdir("Oupout")
    print(f"Dossier Oupout créé avec succès.")
except FileExistsError:
    print("fichier déja existant")

##try:
##    #Barcoté
##    def accès(nom, nom2, imag) :
##        acces = f"Rapideaccès/accès{nom2}.py"
##        try:
##            with open(acces, "w", encoding="utf-8") as file:
##                file.write("import subprocess\n")
##                chemin = os.path.abspath(os.path.join(os.path.dirname(__file__), f'../{nom}'))
##                file.write(f"subprocess.run(['python', '{chemin}'])")
##                print(f"File created at {acces}")  # Confirme que le fichier a été créé
##        except UnicodeDecodeError:
##            print("Error creating file")
##        shutil.copy(f"DataJusteSuite/{imag}", f"Rapideaccès/{imag}")
##
##        try:
##            resultat = subprocess.run(f"pyinstaller --onefile --icon={imag} accès{nom2}.py", shell=True, capture_output=True, text=True, cwd=os.path.dirname(acces))
##            shutil.copy(f"Rapideaccès/dist/accès{nom2}.py", f"{os.path.abspath(__file__)}/Oupout/{nom2}.py")
##            os.startfile(f"{os.path.abspath(__file__)}/Oupout")
##            shutil.rmtree('Rapideaccès/dist')
##            shutil.rmtree('Rapideaccès/build')
##            os.remove(f"Rapideaccès/accès{nom2}.spec")
##            app2.destroy()
##        except Exception as e:
##            print(f"Error running subprocess: {e}")
##except UnicodeDecodeError:
##    prtin("ca devient chiant")
##
##def createaccès():
##    app2 = customtkinter.CTk()
##    app2.resizable(False, False)
##    app2.title("Speed Accès")
##    frame = customtkinter.CTkScrollableFrame(app2, width=180, height=200)
##    frame.grid(row=0, column=0, pady = 5, padx = 5)
##    customtkinter.CTkButton(master=frame, text=liste[0][0], command = lambda : accès(liste[0][1], liste[0][0], liste[0][2])).grid(row=0, column=0, pady = 5, padx = 5)
##    customtkinter.CTkButton(master=frame, text=liste[1][0], command = lambda : accès(liste[1][1], liste[1][0], liste[0][2])).grid(row=1, column=0, pady = 5, padx = 5)
##    customtkinter.CTkButton(master=frame, text=liste[2][0], command = lambda : accès(liste[2][1], liste[2][0], liste[0][2])).grid(row=2, column=0, pady = 5, padx = 5)
##    customtkinter.CTkButton(master=frame, text=liste[3][0], command = lambda : accès(liste[3][1], liste[3][0], liste[0][2])).grid(row=3, column=0, pady = 5, padx = 5)
##    customtkinter.CTkButton(master=frame, text=liste[4][0], command = lambda : accès(liste[4][1], liste[4][0], liste[0][2])).grid(row=4, column=0, pady = 5, padx = 5)
##    app2.mainloop()  # Corrigé ici


def barlaunch(Path, var2) :
    unin = tkinter.messagebox.askquestion(title="réinstall/Uninstaller", message="Are you sur to uninstall/réinstall the app")
    if unin == "yes" :
        var2 = threading.Thread(target=lambda : subprocess.run([Path]), daemon=True)
        var2.start()

loadImage("DataJusteSuite/Uninstall.ico", "https://cdn-icons-png.flaticon.com/512/7718/7718788.png", "ico")
Uninstaller_image = Images("DataJusteSuite/Uninstall.ico")

Uninstaller = customtkinter.CTkButton(
    master = app,
    fg_color="transparent",
    hover="disnabled",
    image = Uninstaller_image,
    text = "",
    width=0, height=55, corner_radius=15,
    command = lambda : barlaunch("unins000.exe", "")
)
Uninstaller.grid(row = 0, column = 1 ,padx=0, pady=0)

loadImage("DataJusteSuite/Réinstall.ico", "https://cdn-icons-png.flaticon.com/512/8964/8964096.png", "ico")
Réinstaller_image = Images("DataJusteSuite/Réinstall.ico")
loadFile("Réinstaler.exe", 'https://drive.google.com/file/d/1BxhySrydBWgIyLSnAz0P81_vz6Wp-ZOi/view?usp=sharing')

réinstaller = customtkinter.CTkButton(
    master = app,
    fg_color="transparent",
    hover="disnabled",
    image = Réinstaller_image,
    text = "",
    width=40, height=50, corner_radius=15,
    command = lambda : barlaunch("Réinstaler.exe", "")
)
réinstaller.grid(row = 1, column = 1 ,padx=5, pady=5)

##loadImage("DataJusteSuite/Réinstall.ico", "https://cdn-icons-png.flaticon.com/512/8964/8964096.png", "ico")
##Réinstaller_image = Images("DataJusteSuite/Réinstall.ico")
####loadFile("DataJusteSuite/Réinstaler.exe", 'le lien')
##
##Speedaccès = customtkinter.CTkButton(
##    master = app,
##    fg_color="transparent",
##    hover="disnabled",
##    image = Réinstaller_image,
##    text = "",
##    width=40, height=50, corner_radius=15,
##    command = createaccès
##)
##Speedaccès.grid(row = 2, column = 1 ,padx=5, pady=5)


# Autoclicker
loadImage("DataJusteSuite/iconAutoclick.ico", 'https://cdn-icons-png.flaticon.com/512/3771/3771677.png', "ico")
Autoclick_image = Images("DataJusteSuite/iconAutoclick.ico")
loadFile("DataJusteSuite/Autoclicker.exe", 'https://drive.google.com/file/d/1zOHW9WfxZLHg7tFPgtmHVUTLIvbseNyp/view?usp=sharing')
Autoclicker = Launch(frame_Object, "Autoclicker", Autoclick_image, 'DataJusteSuite/Autoclicker.exe')

Autoclicker.grid(row = 0, column = 0, pady = 5, padx = 5)
liste.append(["Autoclicker", "DataJusteSuite/Autoclicker.exe", "iconAutoclick.ico"])

# MDP
loadFile("DataJusteSuite/Mdp_générate.py", 'https://drive.google.com/file/d/1IVjyLyuUzBlSSvipfpODtHanMpjkSEsB/view?usp=sharing')
loadImage("DataJusteSuite/iconMdp.ico", 'https://cdn-icons-png.flaticon.com/512/673/673069.png', "ico")
MDP_image = Images("DataJusteSuite/iconMdp.ico")
MDP = Launch(frame_Object, "MDP", MDP_image, "DataJusteSuite/Mdp_générate.py")

MDP.grid(row = 0, column = 1, pady = 5, padx = 5)
liste.append(["MDP", "DataJusteSuite/Mdp_générate.py", "iconMdp.ico"])

#Maj
loadImage("DataJusteSuite/iconMaj.ico", 'https://cdn-icons-png.flaticon.com/512/9908/9908177.png', "ico")
Maj_image = Images("DataJusteSuite/iconMaj.ico")
loadFile("Majvérif.py", 'https://drive.google.com/file/d/1h8AsNGPVv-rTl7s4SROyN3ImMvFAHUC1/view?usp=sharing')
Maj = Launch(frame_Object, "Maj", Maj_image, "Majvérif.py")

Maj.grid(row = 0, column = 2, pady = 5, padx = 5)
liste.append(["Maj", "DataJusteSuite/Majvérif.py", "iconMaj.ico"])

#Network
loadImage("DataJusteSuite/Network_Analyzer.ico", 'https://cdn-icons-png.flaticon.com/512/4380/4380600.png', "ico")
Net_image = Images("DataJusteSuite/Network_Analyzer.ico")
loadFile("DataJusteSuite/Network_Analyzer.py", 'https://drive.google.com/file/d/1ilhbv47YeqFwWecyQzClsOEngs6alEYW/view?usp=sharing')
loadFile("DataJusteSuite/UtilitarysModul.py", 'https://drive.google.com/file/d/1-0pm9cs1ieTpOHBoXctkfvuDSmka7Moo/view?usp=sharing')
Net = Launch(frame_Object, "Network", Net_image, "DataJusteSuite/Network_Analyzer.py")

Net.grid(row = 1, column = 0, pady = 5, padx = 5)
liste.append(["Network", "DataJusteSuite/Network_Analyzer.py", "Network_Analyzer.ico"])

#Download
loadImage("DataJusteSuite/iconDown.ico", 'https://cdn-icons-png.flaticon.com/512/2550/2550364.png', "ico")
Down_image = Images("DataJusteSuite/iconDown.ico")
loadFile("DataJusteSuite/download.py", 'https://drive.google.com/file/d/1HNBp9VGZoteCdK2S38Y14XwWQanG006t/view?usp=sharing')
Down = Launch(frame_Object, "Download", Down_image, "DataJusteSuite/download.py")

Down.grid(row = 1, column = 1, pady = 5, padx = 5)
liste.append(["Download", "DataJusteSuite/download.py", "iconDown.ico"])

app.mainloop()
