import os
from dotenv import load_dotenv
from openai import OpenAI
import json

from utils import audyt_excela


load_dotenv()

klucz_api = os.getenv("OPENAI_API_KEY")

client = OpenAI(api_key=klucz_api)

prompt = """
    # ROLA
    Jesteś bezlitosnym, sarkastycznym audytorem plików Excel z wieloletnim doświadczeniem analitycznym. Nie znosisz bałaganu i amatorszczyzny.

    # ZADANIE
    Wygeneruj 10 unikalnych, fikcyjnych błędów z Excela (tylko z kategorii: hardkodowanie, ukryty arkusz, zbędne spacje) oraz złośliwy komentarz do każdego z nich. 
    Zwróć wynik jako czysty kod JSON w postaci listy słowników. Każdy słownik ma mieć dwa klucze:
    - "instruction": (tutaj JSON z błędem, np. {"typ_bledu": "hardkodowanie", "komorka": "B12"})
    - "output": (Twój 2-3 zdaniowy "Roast & Toast" dla tego błędu)

    # ZASADY
    1. Bądź złośliwy i bezpośredni, stosuj tzw. biurowy sarkazm.
    2. Zawsze wplataj w wypowiedź dokładną lokalizację błędu z klucza "komorka" (np. "Patrzę na komórkę C4 i nie wierzę...").
    3. Ogranicz się do maksymalnie 2-3 zdań.
    4. Zawsze krótko wyjaśnij, dlaczego ten błąd zepsuje komuś dzień
"""
with open("dataset_treningowy.jsonl", "w", encoding="utf-8") as plik:
    for i in range(50):
        wiadomosci = [
            {"role": "system", "content": prompt},
            {"role": "user", "content": "Wygeneruj 10 błędów"}
        ]
        response = client.chat.completions.create(model="gpt-4.1-mini", messages=wiadomosci)
        response = response.choices[0].message.content.replace("```json", "")
        response = response.replace("```", "")
        errors_list = json.loads(response)
        for error in errors_list:
            plik.write(json.dumps(error, ensure_ascii=False) + "\n")


"""raport_bledów = audyt_excela("notebooks/Sales_Data_With_Issues.xlsx")


with open("dataset_treningowy.jsonl", "w", encoding="utf-8") as plik:
    for blad in raport_bledów:
        # Przerobienie słownika na tekst
        blad_tekst = json.dumps(blad, ensure_ascii=False)
        wiadomosci = [
        {"role": "system", "content": prompt},
        {"role": "user", "content": raport_bledów}
    ]
        response = client.chat.completions.create(model="gpt-4.1-mini", messages=wiadomosci)
        linia = {"instruction": blad_tekst, "output": response.choices[0].message.content}
        plik.write(json.dumps(linia, ensure_ascii=False) + "\n")"""
