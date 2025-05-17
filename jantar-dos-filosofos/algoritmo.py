import threading
import time
import random
import tkinter as tk
from PIL import Image, ImageTk

root = tk.Tk()
root.title("Jantar das Cientistas da Computação")
root.geometry("1000x1100") 


imagens = [
    ImageTk.PhotoImage(Image.open("carol.jpeg").resize((140, 140))),   
    ImageTk.PhotoImage(Image.open("sthe.jpeg").resize((140, 140))),
    ImageTk.PhotoImage(Image.open("aretuza.jpeg").resize((140, 140))),
    ImageTk.PhotoImage(Image.open("clara.jpeg").resize((140, 140))),
    ImageTk.PhotoImage(Image.open("jessica.jpeg").resize((140, 140))),
]

cientistas = ["CAROL", "STHE", "ARETUZA", "CLARA", "JESSICA"]
garfos = [threading.Semaphore(1) for _ in range(5)] 
limite_cientistas_comendo = threading.Semaphore(4)  

estado_cientistas = ["Só sei que nada sei" for _ in range(5)]

labels = []

def atualizar_interface():
    
    for i in range(5):
        status = estado_cientistas[i]
        label = labels[i]
        label.config(text=f"{cientistas[i]}: {status}")


        if status == "Só sei que nada sei":
            label.config(bg="blue")
        elif status == "MDS FOME":
            label.config(bg="red")
        elif status == "Esperando a vez":
            label.config(bg="yellow")
        elif status == "Comendo":
            label.config(bg="lightgreen")

    root.after(1000, atualizar_interface) 

def jantar(filosofo_id):
    nome = cientistas[filosofo_id]
    garfo_esquerdo = garfos[filosofo_id]  
    garfo_direito = garfos[(filosofo_id + 1) % 5] 

    while True:
        estado_cientistas[filosofo_id] = "Só sei que nada sei"  
        time.sleep(random.uniform(1, 2))

        estado_cientistas[filosofo_id] = "MDS FOME"  
        limite_cientistas_comendo.acquire()  

        estado_cientistas[filosofo_id] = "Esperando a vez" 
        garfo_esquerdo.acquire()  
        garfo_direito.acquire()  

        estado_cientistas[filosofo_id] = "Comendo"  
        time.sleep(random.uniform(1, 2))

      
        garfo_esquerdo.release()
        garfo_direito.release()
        limite_cientistas_comendo.release()  

        estado_cientistas[filosofo_id] = "Só sei que nada sei"  
        time.sleep(random.uniform(0.5, 1.5))  


for i in range(5):
    frame = tk.Frame(root, bg="purple")
    frame.pack(pady=20, padx=20, fill="x") 

    icon = tk.Label(frame, image=imagens[i], bg="purple")
    icon.pack(side="left", padx=20)

    label = tk.Label(frame, text=f"{cientistas[i]}: Só sei que nada sei", width=100, height=4, bg="purple", font=("Arial", 14))
    label.pack(side="left")
    
    labels.append(label)


for i in range(5):
    t = threading.Thread(target=jantar, args=(i,))
    t.daemon = True  
    t.start()


root.after(1000, atualizar_interface)


root.mainloop()
