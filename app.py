from decimal import Decimal
from numpy import mat
import pandas as pd

rabaty = [1, 0.99, 0.98, 0.97]
licznik = 0

for i in rabaty:
    sandisk = pd.read_excel('sandisk.xls')
    sandisk.rename(columns={'Kod towaru': 'KOD',
                   'Cena': 'WARTOŚĆ'}, inplace=True)
    sandisk.insert(1, 'RODZAJ', int(3))
    sandisk['WARTOŚĆ'] = round(sandisk['WARTOŚĆ']*i, 2)
    sandisk['PRÓG'] = 0
    sandisk['TYPNB'] = 'N'
    sandisk['WALUTA'] = 'PLN'
    sandisk['RODZAJ CENY'] = 'DETALICZNA'
    sandisk['GRATIS'] = 'NIE'
    sandisk['RODZAJ LIMITU'] = 0
    sandisk['TYP LIMITU'] = 0
    sandisk['LIMIT'] = 0
    sandisk['TYP PROGU TRANSAKCJI'] = 0
    sandisk['PRÓG TRANSAKCJI'] = 0
    if licznik == 0:
        sandisk.to_excel(f'sandisk_ALL.xls', index=False)
        licznik += 1
    else:
        sandisk.to_excel(f'sandisk_{licznik}_procent.xls', index=False)
        licznik += 1
