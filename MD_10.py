import threading
import time

def pastaiga_ar_suni(vārds):
    time.sleep(4) # 4 sekundes
    print(f"Suns vārdā {vārds} izvests pastaigā.")

def pagatavot_pusdienas():
    time.sleep(2) # 2 sekundes
    print("Pusdienas ir gatavas.")

def pildit_pitonu():
    time.sleep(6) # 6 sekundes
    print("Pitona mājas darbs Nr.10 izpildīts.")

uzdevums1 = threading.Thread(target=pastaiga_ar_suni, args=("Elbatra",))
uzdevums1.start()

uzdevums2 = threading.Thread(target=pagatavot_pusdienas)
uzdevums2.start()

uzdevums3 = threading.Thread(target=pildit_pitonu)
uzdevums3.start()

uzdevums1.join() # Lai izpildītu šos uzdevumus un tikai tad noslēdzošo print tekstu, ir jāizmanto join() metode.
uzdevums2.join()
uzdevums3.join()

print("Šodienas uzdevumi ir paveikti!")
