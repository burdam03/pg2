def cislo_text(cislo):
    if int(cislo)<=100:
        desitky = ["","","dvacet","třicet","čtyřicet","padesát","šedesát", "sedmdesát","osmdesát","devadesát"]
        jednotky = ["", "jedna", "dva", "tři", "čtyři", "pět", "šest", "sedm", "osm", "děvět"]

        if len(cislo)==3:
            if (cislo[0]=="1" and cislo[1]=="0" and cislo[2]=="0"):
                cislo_cislo = "sto"

        if len(cislo)==2:
            if cislo[0] == "1":
                teens = ["deset", "jedenáct","dvanáct","třináct","čtrnáct", "patnáct", "šestnáct","sedmnáct", "osmnáct","devatenáct"]
                cislo_cislo = teens[int(cislo[1])]
            else:
                cislo_cislo = desitky[int(cislo[0])]+ " " + jednotky[int(cislo[1])]
        if len(cislo)==1:
            jednotky[0] = "nula"
            cislo_cislo = jednotky[int(cislo[0])]
    else:
        cislo_cislo = "Větší než sto"
    return cislo_cislo


if __name__ == "__main__":
    cislo = input("Zadej číslo: ")
    text = cislo_text(cislo)
    print(text)
