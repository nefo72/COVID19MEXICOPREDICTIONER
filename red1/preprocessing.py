import numpy as np

class Pais:
    def __init__(self,country):
        self.country = country
        self.lat = []
        self.long = []
        self.infected = []


f = open('time_series_covid19_confirmed_global.csv')

paises_names = ['Afghanistan', 'Albania', 'Algeria', 'Andorra', 'Angola', 'AntiguaandBarbuda', 'Argentina', 'Armenia', 'Australia', 'Austria', 'Azerbaijan', 'Bahamas', 'Bahrain', 'Bangladesh', 'Barbados', 'Belarus', 'Belgium', 'Benin', 'Bhutan', 'Bolivia', 'BosniaandHerzegovina', 'Brazil', 'Brunei', 'Bulgaria', 'BurkinaFaso', 'CaboVerde', 'Cambodia', 'Cameroon', 'Canada', 'CentralAfricanRepublic', 'Chad', 'Chile', 'China', 'Colombia', 'CostaRica', 'Croatia', 'DiamondPrincess', 'Cuba', 'Cyprus', 'Czechia', 'Denmark', 'Djibouti', 'DominicanRepublic', 'Ecuador', 'Egypt', 'ElSalvador', 'EquatorialGuinea', 'Eritrea', 'Estonia', 'Eswatini', 'Ethiopia', 'Fiji', 'Finland', 'France', 'Gabon', 'Gambia', 'Georgia', 'Germany', 'Ghana', 'Greece', 'Guatemala', 'Guinea', 'Guyana', 'Haiti', 'HolySee', 'Honduras', 'Hungary', 'Iceland', 'India', 'Indonesia', 'Iran', 'Iraq', 'Ireland', 'Israel', 'Italy', 'Jamaica', 'Japan', 'Jordan', 'Kazakhstan', 'Kenya', 'KoreaSouth', 'Kuwait', 'Kyrgyzstan', 'Latvia', 'Lebanon', 'Liberia', 'Liechtenstein', 'Lithuania', 'Luxembourg', 'Madagascar', 'Malaysia', 'Maldives', 'Malta', 'Mauritania', 'Mauritius', 'Mexico', 'Moldova', 'Monaco', 'Mongolia', 'Montenegro', 'Morocco', 'Namibia', 'Nepal', 'Netherlands', 'NewZealand', 'Nicaragua', 'Niger','Nigeria','NorthMacedonia', 'Norway', 'Oman', 'Pakistan', 'Panama', 'PapuaNewGuinea', 'Paraguay', 'Peru', 'Philippines', 'Poland', 'Portugal', 'Qatar', 'Romania', 'Russia', 'Rwanda', 'SaintLucia', 'SaintVincentandtheGrenadines', 'SanMarino', 'SaudiArabia', 'Senegal', 'Serbia', 'Seychelles', 'Singapore', 'Slovakia', 'Slovenia', 'Somalia', 'SouthAfrica', 'Spain', 'SriLanka', 'Sudan', 'Suriname', 'Sweden', 'Switzerland', 'Taiwan', 'Tanzania', 'Thailand', 'Togo', 'TrinidadandTobago', 'Tunisia', 'Turkey', 'Uganda', 'Ukraine', 'UnitedArabEmirates', 'UnitedKingdom', 'Uruguay', 'US', 'Uzbekistan', 'Venezuela', 'Vietnam', 'Zambia', 'Zimbabwe', 'Dominica', 'Grenada', 'Mozambique', 'Syria', 'Timor-Leste', 'Belize', 'Laos', 'Libya', 'WestBankandGaza', 'Guinea-Bissau', 'Mali', 'SaintKittsandNevis', 'Kosovo', 'Burma', 'MSZaandam']

paises = []

for pais in paises_names:
    paises.append(Pais(pais))

#Por razones de algoritmo tuve que quitar a Congo de la lista de paises
for line in f:
    data = line.replace('\n','').split(',')
    if(data[0] == 'Recovered'):
        continue
    for pais in paises:
        if(pais.country == data[1]):
            pais.lat.append(data[2])
            pais.long.append(data[3])
            pais.infected.append(data[4:])
            break

for pais in paises:
    pais.lat = np.mean(np.asarray(pais.lat,dtype=float))
    pais.long = np.mean(np.asarray(pais.long,dtype=float))
    pais.infected[0] = np.asarray(pais.infected[0],dtype=int)
    for i in range(1,len(pais.infected)):
        pais.infected[0] += np.asarray(pais.infected[i],dtype=int)

for pais in paises:
    print(","+pais.country+","+str(pais.lat)+","+str(pais.long),end=",")
    for i in range(len(pais.infected[0])):
        if(i<len(pais.infected[0])-1):
            print(str(pais.infected[0][i]),end=',')
        else:
            print(str(pais.infected[0][i]))

