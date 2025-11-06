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

def lisaa_varastoon(juoma: Varasto, maara):
    print(f"Lisätään {maara}")
    juoma.lisaa_varastoon(maara)
    tulosta_juoma(juoma)

def ota_varastosta(juoma: Varasto, maara):
    print(f"Otetaan {maara}")
    juoma.ota_varastosta(maara)
    tulosta_juoma(juoma)
    
def tulosta_juoma(juoma):
    print(print(f"{juoma.nimi}varasto: {juoma}"))

def main():
    mehua = Varasto(100.0)
    olutta = Varasto(100.0, 20.2)
    alusta_varasto(mehua, olutta)

#    mehua, olutta = alusta_varasto()
#    print("Luonnin jälkeen:")
#    print(f"Mehuvarasto: {saldo(olutta)}")
#    print(f"Olutvarasto: {olutta}")

    getterit(olutta)
#    print("Olut getterit:")
#    print(f"saldo = {olutta.saldo}")
#    print(f"tilavuus = {olutta.tilavuus}")
#    print(f"paljonko_mahtuu = {olutta.paljonko_mahtuu()}")
    print("Mehu setterit:")

    lisaa_varastoon(mehua, 50.7)
    
 #   print("Lisätään 50.7")
 #   mehua.lisaa_varastoon(50.7)
 #   print(f"Mehuvarasto: {mehua}")
    
    ota_varastosta(mehua, 3.14)

 #   print("Otetaan 3.14")
 #   mehua.ota_varastosta(3.14)
 #   print(f"Mehuvarasto: {mehua}")

    print("Virhetilanteita:")
    print("Varasto(-100.0);")
    huono = Varasto(-100.0)
    print(huono)

    print("Varasto(100.0, -50.7)")
    huono = Varasto(100.0, -50.7)
    print(huono)

    print(f"Olutvarasto: {olutta}")
    print("olutta.lisaa_varastoon(1000.0)")
    olutta.lisaa_varastoon(1000.0)
    print(f"Olutvarasto: {olutta}")

    print(f"Mehuvarasto: {mehua}")
    print("mehua.lisaa_varastoon(-666.0)")
    mehua.lisaa_varastoon(-666.0)
    print(f"Mehuvarasto: {mehua}")

    print(f"Olutvarasto: {olutta}")
    print("olutta.ota_varastosta(1000.0)")
    saatiin = olutta.ota_varastosta(1000.0)
    print(f"saatiin {saatiin}")
    print(f"Olutvarasto: {olutta}")

    print(f"Mehuvarasto: {mehua}")
    print("mehua.otaVarastosta(-32.9)")
    saatiin = mehua.ota_varastosta(-32.9)
    print(f"saatiin {saatiin}")
    print(f"Mehuvarasto: {mehua}")

if __name__ == "__main__":
    main()
