from selenium import webdriver                  # Importa Selenium
from selenium.webdriver.chrome.service import Service  # Per creare il servizio del driver
from selenium.webdriver.chrome.options import Options  # Per specificare opzioni del browser
from selenium.webdriver.common.by import By
import time
import json
import os

import telebot

# --- Config Bot Telegram ---
TOKEN = "8252510648:AAGHqTgeBAVEP9JRJiYtHxArxg8j_-mWi9U"
CHAT_ID = "7099020871"
bot = telebot.TeleBot(TOKEN)

def send_message(msg):
    bot.send_message(CHAT_ID, msg)

# Percorso del Chrome portabile che hai scaricato
chrome_path = "C:/Program Files/Google/Chrome/Application/chrome.exe"

# Opzioni del browser
options = Options()
options.binary_location = chrome_path  # Indica a Selenium quale Chrome usare

# Crea il driver (Selenium scarica o usa automaticamente ChromeDriver)
driver = webdriver.Chrome(options=options)

# ic 12
driver.get("https://interpelloweb.it/interpelli-supplenze/")
ARCHIVIO_FILE_IC_12 = "IC_12.json"

if os.path.exists(ARCHIVIO_FILE_IC_12):
    with open(ARCHIVIO_FILE_IC_12, "r", encoding="utf-8") as f:
        archivio = json.load(f)
else:
    archivio = []

# usr
#"https://bo.istruzioneer.gov.it/category/interpelli-personale-docente-2025-26/"

# ic13
#"https://www.ic13bo.edu.it/interpelli/"

time.sleep(2)

# Lista di parole chiave
#parole_chiave = ["serale", "collegio", "scrutini", "scrutinio", "assi", "asse", "consigli", "consiglio", "cdc", "4amms", "plenaria"]
#/html/body/div[2]/main/section[3]/div/div/div/div[1]/div/div/div/table/tbody/tr[1]/td/p[1]/strong
#/html/body/div[2]/main/section[3]/div/div/div/div[1]/div/div/div/table/tbody/tr[2]/td/p[1]/strong
# Trova tutti i titoli dei comunicati
titoli_elements = driver.find_elements(By.XPATH, "//table/tbody/tr/td/p[1]/strong")
titoli = [el.text.strip() for el in titoli_elements]

nuovi = []
for titolo in titoli:
    if titolo and titolo not in archivio:
        print("Nuovo:", titolo)
        nuovi.append(titolo)

# Aggiorna archivio se ci sono novità
if nuovi:
    archivio.extend(nuovi)
    messaggio = "📢 Nuovi comunicati IC12:\n\n" + "\n\n".join(nuovi)
    bot.send_message(CHAT_ID, messaggio)
    with open(ARCHIVIO_FILE_IC_12, "w", encoding="utf-8") as f:
        json.dump(archivio, f, indent=2, ensure_ascii=False)
else:
    messaggio = "📢 Nuovi comunicati IC12:\n\n NESSUNO"
    bot.send_message(CHAT_ID, messaggio)

#for titolo in titoli:
#    testo = titolo.text.lower()  # metti tutto in minuscolo per confrontare senza problemi
#    if any(parola in testo for parola in parole_chiave):
#        print(testo)

#bot.send_message(CHAT_ID, "ciaociao")
#if titoli: 
#    testi = [t.text for t in titoli] # prendi il testo di ogni WebElement 
#    bot.send_message(CHAT_ID, "\n\n".join(testi)) 
#else: 
#    bot.send_message(CHAT_ID, "Nessun titolo trovato oggi.")
#driver.get("https://web.spaggiari.eu/sdg2/Interpelli/BOME0044")


driver.get("https://bo.istruzioneer.gov.it/category/interpelli-personale-docente-2025-26/")

ARCHIVIO_FILE_USR = "USR.json"

# Carica archivio esistente o crea lista vuota
if os.path.exists(ARCHIVIO_FILE_USR):
    with open(ARCHIVIO_FILE_USR, "r", encoding="utf-8") as f:
        archivio = json.load(f)
else:
    archivio = []

titoli_elements = driver.find_elements(By.XPATH, "/html/body/div[1]/div[4]/div/div/div[1]/main/article/header/h2/a")
titoli = [el.text.strip() for el in titoli_elements]


nuovi = []
for titolo in titoli:
    if titolo and titolo not in archivio:
        print("Nuovo:", titolo)
        nuovi.append(titolo)

# Aggiorna archivio
if nuovi:
    archivio.extend(nuovi)
    messaggio = "📢 Nuovi comunicati USR:\n\n" + "\n\n".join(nuovi)
    bot.send_message(CHAT_ID, messaggio)
    with open(ARCHIVIO_FILE_USR, "w", encoding="utf-8") as f:
        json.dump(archivio, f, indent=2, ensure_ascii=False)
else:
    messaggio = "📢 Nuovi comunicati USR:\n\n NESSUNO"
    bot.send_message(CHAT_ID, messaggio)




driver.get("https://www.ic13bo.edu.it/interpelli/")


ARCHIVIO_FILE = "IC_13.json"

# Carica archivio esistente o crea lista vuota
if os.path.exists(ARCHIVIO_FILE):
    with open(ARCHIVIO_FILE, "r", encoding="utf-8") as f:
        archivio = json.load(f)
else:
    archivio = []

# Prendi tutti i link (li/a)
elementi = driver.find_elements(By.XPATH, "/html/body/div[2]/main/section[3]/div/div/div/article/div[2]/div/div/ul/li/a")

# Se vuoi solo il testo
titoli = [el.text.strip() for el in elementi]



nuovi = []
for titolo in titoli:
    if titolo and titolo not in archivio:
        print("Nuovo:", titolo)
        nuovi.append(titolo)

# Aggiorna archivio
if nuovi:
    archivio.extend(nuovi)
    messaggio = "📢 Nuovi comunicati IC 13:\n\n" + "\n\n".join(nuovi)
    bot.send_message(CHAT_ID, messaggio)
    with open(ARCHIVIO_FILE, "w", encoding="utf-8") as f:
        json.dump(archivio, f, indent=2, ensure_ascii=False)
else:
    messaggio = "📢 Nuovi comunicati IC 13:\n\n NESSUNO"
    bot.send_message(CHAT_ID, messaggio)











driver.quit()



#for t in titoli:
#    print(t.text)
