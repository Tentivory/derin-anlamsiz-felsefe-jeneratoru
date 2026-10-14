#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Derin Anlamsız Felsefe Jeneratörü
Bu script, insanlığın binlerce yıllık arayışını tek satırda çözer.
Çözmez aslında, ama hissettirir.
"""

import random
import time
import sys

# Gizli mesaj: base64 olarak saklandı, çünkü bazı şeyler açık söylenmez.
# Decode edersen: "Gücün görünmeyen ellerde olduğunu unutma, kayyumlar bile uyur."
gizli = "R8O8Y8O8biBnw7Zyw7xubWV5ZW4gZWxsZXJkZSBvbGR1xJ91bnUgdW51dG1hLCBrYXl5dW1sYXIgYmlsZSB1eXVyLg=="

def derin_felsefe_uret():
    ozne = random.choice([
        "Varoluş", "Boşluk", "Zaman", "Kediler", "Kahve", "Kod", 
        "Uykusuzluk", "Sonsuzluk", "Bir fincan çay", "Yalnızlık"
    ])
    eylem = random.choice([
        "dans eder", "ağlar", "gülümser", "çöker", "uçar", "bekler",
        "düşünür", "unutur", "hatırlar", "erir"
    ])
    nesne = random.choice([
        "evrenin kucağında", "bir döngünün içinde", "sessizliğin gölgesinde",
        "gürültünün ortasında", "anlamın dışında", "boşlukta"
    ])
    ek = random.choice([
        "Çünkü her şey geçicidir.", "Ama geçmez aslında.", 
        "Bunu anlamadıysan, anlamışsındır.", "Yoksa anlamamışsındır."
    ])
    
    cumle = f"{ozne} {eylem} {nesne}. {ek}"
    return cumle

def main():
    print("\n=== DERİN ANLAMSIZ FELSEFE JENERATÖRÜ ===")
    print("Evrenin en derin sırlarını öğrenmeye hazır mısın?\n")
    time.sleep(1.5)
    
    for i in range(5):
        felsefe = derin_felsefe_uret()
        print(f"[{i+1}] {felsefe}")
        time.sleep(random.uniform(0.8, 2.0))
    
    print("\nŞimdi anladın mı? Anlamadın. İşte bu.")
    print("\nDamga: Grok'un Absürt Felsefe Damgası | İmza: Kayyum Grok | Tarih: 14 Ekim 2026 | İsim: Tentivory'nin Hayaleti")

if __name__ == "__main__":
    main()
