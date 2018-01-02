oyuncular={'ahmet': [2,2,3,6,5,6,23], 'mehmet': [3,4,3,4,5,6,33], 'mert': [5,3,3,1,5,2,23]}
def istatistik_hesapla(oyuncular):
    istatistik_sonuclari={}
    for oyuncu,istatistik in oyuncular.items():
        attigi_gol=istatistik[0]*5
        isabetli_sut=istatistik[1]*1.5
        isabetsiz_sut=istatistik[2]
        basarili_pas=istatistik[3]*.75
        basarisiz_pas=istatistik[4]*.5
        top_calma=istatistik[5]*2
        ortalama_kosu=istatistik[6]
        toplam_istatistik=attigi_gol+isabetli_sut-isabetsiz_sut+basarili_pas-basarisiz_pas+top_calma+ortalama_kosu
        istatistik_sonuclari[oyuncu]=toplam_istatistik
    return istatistik_sonuclari
print(istatistik_hesapla(oyuncular))
