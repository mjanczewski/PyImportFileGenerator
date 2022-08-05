from decimal import Decimal
from numpy import mat
import pandas as pd
import math

sandisk = pd.read_excel('test.xls')


sandisk.rename(columns={'Kod towaru': 'KOD', 'Cena': 'WARTOŚĆ'}, inplace=True)
sandisk.insert(1, 'RODZAJ', int(3))
sandisk['WARTOŚĆ'] = round(sandisk['WARTOŚĆ']*0.99, 2)
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

del sandisk['Kod u kontrahenta']
del sandisk['Kontrahent']


# sandisk.drop(['Kod u kontrahenta', 'Kontrahent'],
#              index=False, axis=1, inplace=True)


sandisk.to_excel('sandisk_mod.xls', index=False)
