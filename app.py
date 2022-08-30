from decimal import Decimal
from numpy import mat
import pandas as pd


sandisk = pd.read_excel('sandisk.xls')


sandisk.rename(columns={'Kod towaru': 'KOD', 'Cena': 'WARTOŚĆ'}, inplace=True)
sandisk.insert(1, 'RODZAJ', int(3))
sandisk['WARTOŚĆ'] = round(sandisk['WARTOŚĆ'], 2)
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

# del sandisk['Kod u kontrahenta']
# del sandisk['Kontrahent']


sandisk.to_excel('sandisk_All.xls', index=False)

sandisk = pd.read_excel('sandisk.xls')


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

# del sandisk['Kod u kontrahenta']
# del sandisk['Kontrahent']


sandisk.to_excel('sandisk_1_procent.xls', index=False)

sandisk = pd.read_excel('sandisk.xls')


sandisk.rename(columns={'Kod towaru': 'KOD', 'Cena': 'WARTOŚĆ'}, inplace=True)
sandisk.insert(1, 'RODZAJ', int(3))
sandisk['WARTOŚĆ'] = round(sandisk['WARTOŚĆ']*0.98, 2)
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

# del sandisk['Kod u kontrahenta']
# del sandisk['Kontrahent']

sandisk.to_excel('sandisk_2_procent.xls', index=False)

sandisk = pd.read_excel('sandisk.xls')


sandisk.rename(columns={'Kod towaru': 'KOD', 'Cena': 'WARTOŚĆ'}, inplace=True)
sandisk.insert(1, 'RODZAJ', int(3))
sandisk['WARTOŚĆ'] = round(sandisk['WARTOŚĆ']*0.97, 2)
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

# del sandisk['Kod u kontrahenta']
# del sandisk['Kontrahent']

sandisk.to_excel('sandisk_3_procent.xls', index=False)
