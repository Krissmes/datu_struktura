#iegūt daudz mašīnu datus no ss.lv
import requests
import os
from bs4 import BeautifulSoup as bs
import csv
import time

URL = "https://www.ss.lv/lv/transport/cars/today-5/sell/"
DATI = "dati/"
LAPAS = "lapas/"

#kkadas funkcijas
def vai_ir_k(subject):
    if isinstance(subject, ):
        for item in subject:
            if isinstance(item, str) and "kst" in item.lower():
                print(1)
            else:
                if isinstance(item, list) and "kst" in item.lower():
                    print(12345)
                else:
                    print("afngsebkbgksgbsk;gbgba")









#kkadas funkcijas beigas




def saglaba_lapu(url, nosaukums):
    iegutais = requests.get(url)
    print(iegutais.status_code)
    if iegutais.status_code == 200:
        with open(nosaukums, "w", encoding="utf-8") as f:
            f.write(iegutais.text)
    return

# saglaba_lapu(URL, LAPAS+"pirma.html")




def saglaba_visas_lapas(skaits):
    for i in range(1,skaits+1):
        saglaba_lapu(f"{URL}page{i}.html", f"{LAPAS}lapa{i}.html")
        time.sleep(0.5)
    return

# saglaba_visas_lapas(5)

def dabut_info(lapa):
    dati = []
    with open(lapa, "r", encoding="utf-8") as f:
        html = f.read()
    zupa = bs(html, "html.parser")
    galvenais = zupa.find(id="page_main")
    tabulas = galvenais.find_all('table')
    rindas = tabulas[2].find_all('tr')
    for rinda in rindas[1:]:
        lauki = rinda.find_all('td')
        if len(lauki)<8:
            print("Dīvaina rinda")
            continue
        auto = {}
        auto['sludinajuma_saite'] = lauki[1].find('a')['href']
        auto['bilde'] = lauki[1].find('img')['src']

        saraksts = lauki[3].contents
        if len(saraksts)==3:
            auto['marka'] = saraksts[0]
            auto['modelis'] = saraksts[2]
        else:
            try:
                auto['marka'] = list(saraksts[0].children)[0]
                auto['modelis'] = list(saraksts[0].children)[2]
            except:
                auto['marka'] = saraksts[0]
                auto['modelis'] = '-'

        try:
            saraksts_gads_tag =  lauki[4].contents
            saraksts_gads_str = [str(item_tag) for item_tag in saraksts_gads_tag]
            auto['gads'] = int(saraksts_gads_str[0])
            
        except:
            saraksts_gads_tag =  lauki[4].contents
            saraksts_gads_str = [str(item_tag) for item_tag in saraksts_gads_tag]
            auto['gads'] = int(str(saraksts_gads_str[0][3:-4]))
        
        
        saraksts_braukums = lauki[6].contents
            
    
        
        print(saraksts_braukums)
        vai_ir_k(saraksts_braukums)




        dati.append(auto)
    return dati

def saglaba_datus(dati):
    with open(DATI+"sslv.csv", "w", encoding = "utf-8") as f:
        lauku_nosaukumi = ['sludinajuma_saite', 'bilde', 'marka', 'modelis', 'gads', 'nobraukums']
        w = csv.DictWriter(f, fieldnames=lauku_nosaukumi)
        w.writeheader()
        for auto in dati:
            w.writerow(auto)
    return

# saglaba_datus(dabut_info(LAPAS+"pirma.html"))

def dabut_info_daudz(skaits):
    visi_dati = []
    for i in range(1,skaits+1):
        dati = dabut_info(f"{LAPAS}lapa{i}.html")
        visi_dati += dati
    return visi_dati

# saglaba_visas_lapas(20)
info = dabut_info_daudz(20)
saglaba_datus(info)
    