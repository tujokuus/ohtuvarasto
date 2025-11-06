from varasto import Varasto

def alusta_varasto(mehua: Varasto, olutta: Varasto):
    mehua.nimi = "Mehu"
    olutta.nimi = "Olut"
    print("Luonnin jälkeen:")
    print(f"Mehuvarasto: {saldo(mehua)}")
    print(f"Olutavarasto: {saldo(olutta)}")
    return

def saldo(juoma: Varasto):
    return juoma.saldo

def getterit(juoma: Varasto):
    print(f"{juoma.nimi} getterit:")
    print(f"saldo = {juoma.saldo}")
    print(f"tilavuus = {juoma.saldo}")
    print(f"paljonko_mahtuu = {juoma.paljonko_mahtuu()}")

def lisaa(juoma: Varasto, maara):
    print(f"Lisätään {maara}")
    juoma.lisaa_varastoon(maara)
    tulosta_juoma(juoma)

def ota(juoma: Varasto, maara):
    print(f"Otetaan {maara}")
    juoma.ota_varastosta(maara)
    tulosta_juoma(juoma)

def juoma1(juoma: Varasto, maara):
    print(f"{juoma.nimi}varasto {juoma}")
    if juoma.nimi == "Olut":
        print("olutta.lisaa_varastoon(1000.0)")
    else:
        print("mehua_lisaa_varastoon(-666.0)")

    lisaa(juoma, maara)

def saatiin_olutta(juoma: Varasto, maara):
    tulosta_juoma(juoma)
    print("olutta.ota_varastosta(1000.0)")
    saatiin = juoma.ota_varastosta(maara)
    print(f"saatiin {saatiin}")
    tulosta_juoma(juoma)

def saatiin_mehua(juoma: Varasto, maara):
    tulosta_juoma(juoma)
    print(f"mehua.ota_varastosta({maara})")
    saatiin = juoma.ota_varastosta(maara)
    print(f"saatiin {saatiin}")
    tulosta_juoma(juoma)

def tulosta_virhetilanne():
    print("Virhetilanteita:")
    print("Varasto(-100.0);")

def tee_huono():
    huono = Varasto(-100.0)
    print(huono)

    print("Varasto(100.0, -50.7)")
    huono = Varasto(100.0, -50.7)
    print(huono)
    
def tulosta_juoma(juoma: Varasto):
    print(f"{juoma.nimi}varasto: {juoma}")

def main():
    mehua = Varasto(100.0)
    olutta = Varasto(100.0, 20.2)
    alusta_varasto(mehua, olutta)
    getterit(olutta)
    print("Mehu setterit:")
    lisaa(mehua, 50.7)
    ota(mehua, 3.14)
    tulosta_virhetilanne()
    tee_huono()
    juoma1(olutta, 1000.0)
    juoma1(mehua, -666.0)
    saatiin_olutta(olutta, 1000.0)
    saatiin_mehua(mehua, -32.9)

if __name__ == "__main__":
    main()
