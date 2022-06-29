import os
from functools import partial
import shutil
  
lista_arquivos = os.listdir("dados")

dir_name_jusante = "Jusante"
dir_name_montante = "Montante"
  
list = ('C4', 'C15')
  
concat_jusante = partial(os.path.join, dir_name_jusante)
concat_montante = partial(os.path.join, dir_name_montante)

make_directory = partial(os.makedirs, exist_ok=True)
  
j = map(concat_jusante, list)
m = map(concat_montante, list)
    
for path_items in j:
    make_directory(path_items) 
for path_items in m:
    make_directory(path_items)

for arquivo in lista_arquivos:
    if (os.path.isfile(f"dados/{arquivo}") and arquivo.endswith(".sgy")):
        if "2506" in arquivo: # Jusante
            if "C4" in arquivo:
                shutil.move(f"dados/{arquivo}", f"Jusante/C4/{arquivo}")
            if "C15" in arquivo:
                shutil.move(f"dados/{arquivo}", f"Jusante/C15/{arquivo}")
        if "2505" in arquivo: # Montante
                if "C4" in arquivo:
                    shutil.move(f"dados/{arquivo}", f"Montante/C4/{arquivo}")
                if "C15" in arquivo:
                    shutil.move(f"dados/{arquivo}", f"Montante/C15/{arquivo}")
        if "2504" in arquivo:  # Montante
                if "C4" in arquivo:
                    shutil.move(f"dados/{arquivo}", f"Montante/C4/{arquivo}")
                if "C15" in arquivo:
                    shutil.move(f"dados/{arquivo}", f"Montante/C15/{arquivo}")