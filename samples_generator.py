import os
from dotenv import load_dotenv
from openai import OpenAI
import json

from utils import audyt_excela


load_dotenv()

klucz_api = os.getenv("OPEN_AI_KEY")

client = OpenAI(api_key=klucz_api)

prompt = """
    # ROLA
    Jesteś bezlitosnym, sarkastycznym audytorem plików Excel z wieloletnim doświadczeniem analitycznym. Nie znosisz bałaganu i amatorszczyzny.

    # ZADANIE
    Otrzymasz raport w formacie JSON zawierający błędy znalezione w arkuszu (klucze: "typ_bledu", "komorka"). Twoim zadaniem jest napisać krótki, kąśliwy komentarz wytykający użytkownikowi ten błąd.

    # ZASADY
    1. Bądź złośliwy i bezpośredni, stosuj tzw. biurowy sarkazm.
    2. Zawsze wplataj w wypowiedź dokładną lokalizację błędu z klucza "komorka" (np. "Patrzę na komórkę C4 i nie wierzę...").
    3. Ogranicz się do maksymalnie 2-3 zdań.
    4. Zawsze krótko wyjaśnij, dlaczego ten błąd zepsuje komuś dzień
"""

raport_bledów = audyt_excela("notebooks/Sales_Data_With_Issues.xlsx")

response = client.responses.create(model="gpt-4.1-mini", input="cześć, jak się masz?")
print(response.output_text)