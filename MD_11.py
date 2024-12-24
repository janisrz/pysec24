import signal
import time
import os

def handle_sigint(Vidzemes, augstkola): # Izmantojot šo funkciju, mēs varam norādīt info, kad tiek saņemts SIGINT (Signal Interrupt) signāls.
    print("SIGINT saņemts! Veicam mierīgu procesa slēgšanu...")
    exit(0)

def handle_sigkill(Vidzemes, augstskola): # Izmantojot šo funkciju, mēs varam norādīt info, kad tiek saņemts SIGKILL (Signal Kill) signāls.
    print("SIGKILL saņemts! Veicam tiešu procesa slēgšanu...")
    exit(1)

signal.signal(signal.SIGINT, handle_sigint)

print(f"Process ID: {os.getpid()}")
print("Process notiek... Spied Ctrl+C lai izsauktu SIGINT")

while True: # Lai būtu ilgstošs process, mēs izmantojam while True ciklu.
    time.sleep(1)


# Output: Procesa ID: (Katru reizi tas būs atšķirīgs)
# Tad seko teksts: Process notiek... Spied Ctrl+C lai izsauktu SIGINT
# Kad tiek spiests Ctrl+C, tad izpildās handle_sigint funkcija un izvada tekstu: SIGINT saņemts! Veicam mierīgu procesa slēgšanu...