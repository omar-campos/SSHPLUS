#!/usr/bin/env python3
import os
import subprocess
import time

# --- COLORES BASADOS EN TU SCRIPT MENU.SH (ANSI Codes) ---
R='\033[1;31m'  # Rojo (Para las líneas de borde)
G='\033[1;32m'  # Verde
Y='\033[1;33m'  # Amarillo
B='\033[1;36m'  # Cyan/Azul Claro
W='\033[1;37m'  # Blanco
C='\033[0m'     # Reset

# --- CÓDIGO DE FORMATO PARA EL TÍTULO ---
# Definición explícita para evitar errores de \E
FUNDO_ROJO_TEXTO_BRANCO = '\033[41;1;37m' 

PYTHON_SCRIPT = "/root/checkuser.py"

# --- FUNCIONES DE CONTROL ---

def start_server():
    print(f"{G}Iniciando checkuser...{C}")
    # Uso compatible con Python 3.6
    subprocess.run(["screen", "-S", "checkuser", "-X", "quit"], stdout=subprocess.PIPE, stderr=subprocess.PIPE, universal_newlines=True)
    subprocess.run(["screen", "-dmS", "checkuser", "python3", PYTHON_SCRIPT])
    print(f"{G}CheckUser iniciado en sesión 'checkuser'.{C}")

def stop_server():
    print(f"{G}Deteniendo checkuser...{C}")
    subprocess.run(["screen", "-S", "checkuser", "-X", "quit"])
    print(f"{R}CheckUser detenido.{C}")

def status_server():
    # Compatibilidad con Python 3.6
    result = subprocess.run(["screen", "-list"], stdout=subprocess.PIPE, stderr=subprocess.PIPE, universal_newlines=True)
    if "checkuser" in result.stdout:
        print(f"{G}CheckUser está corriendo (Activo).{C}")
    else:
        print(f"{R}CheckUser está detenido (Inactivo).{C}")

def enter_screen():
    print(f"{B}Entrando a la sesión 'checkuser'. Presiona CTRL+A, luego D para salir de la sesión.{C}")
    os.system("screen -r checkuser")

def print_menu():
    os.system("clear")
    
    # --- Lógica de Alineación y Colores del Título ---
    TITULO_CENTRAL = "⇱ MENU CHECKUSER SHUMELO ⇲"
    LINEA_BORDE = "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
    ANCHO_TOTAL = len(LINEA_BORDE) # 50 caracteres

    print(f"{R}{LINEA_BORDE}{C}")

    # AQUI ESTÁ LA CORRECCIÓN CLAVE: Uso de FUNDO_ROJO_TEXTO_BRANCO
    TITULO_FORMATEADO = f"{FUNDO_ROJO_TEXTO_BRANCO}{TITULO_CENTRAL:^{ANCHO_TOTAL}}{C}"
    print(f"{R}{TITULO_FORMATEADO}{C}") 

    print(f"{R}{LINEA_BORDE}{C}")
    # ----------------------------------------

    # Compatibilidad con Python 3.6 para chequear el estado del servicio
    status_result = subprocess.run(["screen", "-list"], stdout=subprocess.PIPE, stderr=subprocess.PIPE, universal_newlines=True)
    is_running = "checkuser" in status_result.stdout

    status_indicator = f"{G}◉{C}" if is_running else f"{R}○{C}"
    
    # Opciones
    print(f"{R}[\033[1;36m1\033[1;31m] {W}• {Y}Iniciar checkuser{C}")
    print(f"{R}[\033[1;36m2\033[1;31m] {W}• {Y}Detener checkuser{C}")
    print(f"{R}[\033[1;36m3\033[1;31m] {W}• {Y}Estado del checkuser {status_indicator}{C}")
    print(f"{R}[\033[1;36m4\033[1;31m] {W}• {Y}Entrar a la sesión screen{C}")
    
    # Opción de salir
    print(f"{R}[\033[1;36m0\033[1;31m] {W}• {Y}SAIR {R}>\033[1;33m>\033[1;32m>{C}")
    
    print(f"{R}{LINEA_BORDE}{C}")
    print("")

def exit_menu():
    print(f"{R}Saindo...{C}")
    time.sleep(1)
    
# --- BUCLE PRINCIPAL ---

while True:
    print_menu()
    
    opcion = input(f"{G}OQUE DESEJA FAZER {Y}??{W} : {C}")

    if opcion == "1":
        start_server()
    elif opcion == "2":
        stop_server()
    elif opcion == "3":
        status_server()
    elif opcion == "4":
        enter_screen()
    elif opcion == "0" or opcion == "5":
        exit_menu()
        break
    else:
        print(f"{R}\nOpcao invalida !{C}")
        time.sleep(1)

    if opcion != "0" and opcion != "5":
        input(f"{R}ENTER {Y}para retornar ao {G}MENU!{C}")
