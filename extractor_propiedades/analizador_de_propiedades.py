paises = ['Afghanistan', 'Albania', 'Algeria', 'Angola', 'Andorra', 'Antigua and Barbuda', 'Argentina', 'Armenia', 'Australia', 'Austria', 'Azerbaijan', 'Bahamas', 'Bahrain', 'Bangladesh', 'Barbados', 'Belarus', 'Belgium', 'Benin', 'Bhutan', 'Bolivia', 'Bosnia and Herzegovina', 'Brazil', 'Brunei', 'Bulgaria', 'Burkina Faso', 'Cabo Verde', 'Cambodia', 'Cameroon', 'Canada', 'Central African Republic', 'Chad', 'Chile', 'China', 'Colombia', 'Congo (Brazzaville)', 'Congo (Kinshasa)', 'Costa Rica', "Cote d'Ivoire", 'Croatia', 'Cuba', 'Cyprus', 'Czechia', 'Denmark', 'Djibouti', 'Dominican Republic', 'Ecuador', 'Egypt', 'El Salvador', 'Equatorial Guinea', 'Eritrea', 'Estonia', 'Eswatini', 'Ethiopia', 'Fiji', 'Finland', 'France', 'Gabon', 'Gambia', 'Georgia', 'Germany', 'Ghana', 'Greece', 'Guatemala', 'Guinea', 'Guyana', 'Haiti', 'Honduras', 'Hungary', 'Iceland', 'India', 'Indonesia', 'Iran', 'Iraq', 'Ireland', 'Israel', 'Italy', 'Jamaica', 'Japan', 'Jordan', 'Kazakhstan', 'Kenya', 'Korea South', 'Kuwait', 'Kyrgyzstan', 'Latvia', 'Lebanon', 'Liberia', 'Lithuania', 'Luxembourg', 'Madagascar', 'Malaysia', 'Maldives', 'Malta', 'Mauritania', 'Mauritius', 'Mexico', 'Moldova', 'Monaco', 'Mongolia', 'Montenegro', 'Morocco', 'Namibia', 'Nepal', 'Netherlands', 'New Zealand', 'Nicaragua', 'Niger', 'Nigeria', 'North Macedonia', 'Norway', 'Oman', 'Pakistan', 'Panama', 'Papua New Guinea', 'Paraguay', 'Peru', 'Philippines', 'Poland', 'Portugal', 'Qatar', 'Romania', 'Russia', 'Rwanda', 'Saint Lucia', 'Saint Vincent and the Grenadines', 'San Marino', 'Saudi Arabia', 'Senegal', 'Serbia', 'Seychelles', 'Singapore', 'Slovakia', 'Slovenia', 'Somalia', 'South Africa', 'Spain', 'Sri Lanka', 'Sudan', 'Suriname', 'Sweden', 'Switzerland', 'Tanzania', 'Thailand', 'Togo', 'Trinidad and Tobago', 'Tunisia', 'Turkey', 'Uganda', 'Ukraine', 'United Arab Emirates', 'United Kingdom', 'Uruguay', 'US', 'Uzbekistan', 'Venezuela', 'Vietnam', 'Zambia', 'Zimbabwe', 'Dominica', 'Grenada', 'Mozambique', 'Syria', 'Timor-Leste', 'Belize', 'Laos', 'Libya', 'Guinea-Bissau', 'Mali', 'Saint Kitts and Nevis', 'Burma', 'Botswana', 'Burundi', 'Sierra Leone', 'Malawi']

database = open('propiedades_por_pais.csv','w')
print("Pais","Superficie","Poblacion","Namerica","Samerica","Europa","Asia","Oceania","Africa","PIB","Porcentaje de PIB en salud",file=database,sep=',')
for pais in paises:

    superficie = -1
    poblacion = -1
    continente = 'none'
    PIB = -1
    salud = -1

    found = False
    f = open('superficie.csv')
    for line in f:
        l = line.split(',')
        if l[0] == pais:
            if found:
                print("Alerta: Pais repetido",pais)
                exit()
            found = True
            superficie=float(l[1])
    f.close()

    found = False
    f = open('poblacion.csv')
    for line in f:
        l = line.split(',')
        if l[0] == pais:
            if found:
                print("Alerta: Pais repetido",pais)
                exit()
            found = True
            poblacion=float(l[1])
    f.close()

    found = False
    f = open('continente.csv')
    for line in f:
        l = line.replace('\n','').split(',')
        if l[0] == pais:
            if found:
                print("Alerta: Pais repetido",pais)
                exit()
            found = True
            if l[1]=='Namerica':
                continente='1, 0, 0, 0, 0, 0'
            if l[1]=='Samerica':
                continente='0, 1, 0, 0, 0, 0'
            if l[1]=='Europe':
                continente='0, 0, 1, 0, 0, 0'
            if l[1]=='Asia':
                continente='0, 0, 0, 1, 0, 0'
            if l[1]=='Oceania':
                continente='0, 0, 0, 0, 1, 0'
            if l[1]=='Africa':
                continente='0, 0, 0, 0, 0, 1'
    f.close()

    found = False
    f = open('PIB.csv')
    for line in f:
        l = line.split(',')
        if l[0] == pais:
            if found:
                print("Alerta: Pais repetido",pais)
                exit()
            found = True
            PIB=float(l[1])
    f.close()


    found = False
    f = open('salud_pib.csv')
    for line in f:
        l = line.split(',')
        if l[0] == pais:
            if found:
                print("Alerta: Pais repetido",pais)
                exit()
            found = True
            salud=float(l[1])
    f.close()

    print(pais,superficie,poblacion,continente,PIB,salud,file=database,sep=',')

