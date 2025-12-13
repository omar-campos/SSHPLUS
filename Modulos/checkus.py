#!/usr/bin/env python3
import os
import subprocess
import time

# Colores
bl='\033[38;5;231m'
am='\033[38;5;228m'
az='\033[38;5;14m'
morado='\033[38;5;147m'
moL='\033[38;5;54m'
ro='\033[0;31m'
ve='\033[38;5;148m'
veR='\033[38;5;40m'
ye='\033[0;33m'
ros='\033[38;5;213m'
me='\033[38;5;208m'
gu='\033[38;5;161m'
azi="\033[38;5;18m"
ci='\033[0m'

PYTHON_SCRIPT = "/root/checkuser.py"


def start_server():
    print("Iniciando checkuser...")
    subprocess.run(["screen", "-dmS", "checkuser", "python3", PYTHON_SCRIPT])
    print("checkuser iniciado en sesión 'checkuser'.")


def stop_server():
    print("Deteniendo checkuser...")
    subprocess.run(["screen", "-S", "checkuser", "-X", "quit"])
    print("CheckUser detenido.")


def status_server():
    result = subprocess.run(["screen", "-list"], capture_output=True, text=True)
    if "checkuser" in result.stdout:
        print("CheckUser está corriendo.")
    else:
        print("CheckUser está detenido.")


def enter_screen():
    os.system("screen -r checkuser")


while True:
    os.system("clear")
    print(f"{veR}===== MENU CHECKUSER SERVER ====={ci}")

    print(f"{ros}1{ci}) {az}Iniciar checkuser{ci}")
    print(f"{ros}2{ci}) {az}Detener checkuser{ci}")
    print(f"{ros}3{ci}) {az}Estado del checkuser{ci}")
    print(f"{ros}4{ci}) {az}Entrar a la sesión screen{ci}")
    print(f"{ros}5{ci}) {ro}Salir{ci}")
    
    print(f"{veR}============================={ci}")

    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        start_server()
    elif opcion == "2":
        stop_server()
    elif opcion == "3":
        status_server()
    elif opcion == "4":
        enter_screen()
    elif opcion == "5":
        break
    else:
        print("Opción inválida")
        time.sleep(2)

    input("Presione Enter para continuar...")