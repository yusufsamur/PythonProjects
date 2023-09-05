with open("ornek_metin.txt", encoding='utf-8') as f:
    with open("gecenler.txt", "w", encoding='utf-8') as g:
        with open("kalanlar.txt", "w", encoding='utf-8') as k:
            g.write(
                "İSİM" + " " * 21 + "SOYAD" + " " * 20 + "BÖLÜM" + " " * 20 + "ORTALAMA" + " " * 16 + "DURUM" + "\n\n")
            k.write(
                "İSİM" + " " * 21 + "SOYAD" + " " * 20 + "BÖLÜM" + " " * 20 + "ORTALAMA" + " " * 16 + "DURUM" + "\n\n")
            icerik = f.readlines()
            m = 0

            for satir in icerik:
                if m == 0:
                    m += 1
                    continue

                satir = satir.replace("\n", "")
                bosluk_sayisi = 0
                bosluk_indexleri = []
                index = 0
                for karakter in satir:
                    if karakter == " ":
                        bosluk_sayisi += 1
                        bosluk_indexleri.append(index)
                    index += 1
                ad_soyad = satir[:bosluk_indexleri[0]]
                soyad = ad_soyad.split("-")[-1]
                ad = ad_soyad[:ad_soyad.index(soyad) - 1].replace("-", " ")
                notlar = satir.split(" ")[-1].split("/")
                birinciVize = int(notlar[0])
                ikinciVize = int(notlar[1])
                final = int(notlar[2])
                ortalama = birinciVize * 0.3 + ikinciVize * 0.3 + final * 0.4
                if bosluk_sayisi == 2:
                    bolum = satir[bosluk_indexleri[0] + 1:bosluk_indexleri[1]]
                elif bosluk_sayisi == 3:
                    bolum = satir[bosluk_indexleri[0] + 1:bosluk_indexleri[2]]
                if ortalama >= 70 and final >= 70:
                    g.write(ad)
                    g.write(" " * (25 - len(ad)))
                    g.write(soyad)
                    g.write(" " * (25 - len(soyad)))
                    g.write(bolum)
                    g.write(" " * (25 - len(bolum)))
                    g.write(str(round(ortalama, 2)))
                    g.write(" " * 20)
                    g.write("GEÇTİ")
                    g.write("\n")
                else:
                    k.write(ad)
                    k.write(" " * (25 - len(ad)))
                    k.write(soyad)
                    k.write(" " * (25 - len(soyad)))
                    k.write(bolum)
                    k.write(" " * (25 - len(bolum)))
                    k.write(str(round(ortalama, 2)))
                    k.write(" " * 20)
                    k.write("KALDI")
                    k.write("\n")
