# Funkcje deklinujace
import Declinator.Paradigms as P
import Declinator.EA_rules as EA
import Declinator.Auxiliary as Aux
import Declinator.Norm_rules as Norm
import Declinator.Language as Lang
import Declinator.FileManager as FM
import Declinator.Corrections as C

# Funkcja normalizujaca forme wejsciowa (base_form)
# Normalizacja polega na: 
# zaznaczeniu w formie wejsciowej liter epententycznych, np. Jarek -> Jar[e]k
# zaznaczeniu w formie wejsciowej liter niemych, np. Locke -> Lock{e}
# zaznaczeniu w formie wejsciowej wlasciwego sposobu wymowy zakonczenia, np. Laplace -> Laplace/s
def Normalize(base_form, full_name, delimiter = '#'):
    
    # Przegladam wszystkie reguly normalizacji
    for rule in Norm.Rules:
        # W kazdej regule przegladam liste zakonczen (pierwszy element reguly - lista napisow)
        for i in range(len(rule[0])):

            # Jesli i-te zakonczenie + delimiter (znacznik zakonczenia napisu) znajduje sie w formie wejsciowej + znacznik zakonczenia            
            if (rule[0][i] + delimiter) in (base_form + delimiter):

                # Sprawdzam warunki, jesli sa (tzn jesli pierwszy warunek jest rozny od '')                
                if (rule[1][0] != ''):

                    # Ustalam przyblizony jezyk pelnego nazwiska
                    lang = Lang.Language(full_name)

                    # Przegladam wszystkie warunki
                    for cond in rule[1]:

                        # Jesli warunek jest zgodny, podmieniam zakonczenia i-te zakonczenie i zwracam wynik
                        if cond == lang:
                            return (base_form + delimiter).replace(rule[0][i] + delimiter, rule[2][i])

                # Jesli regula nie ma warununkow, podmieniam i-te zakonczenie
                else:
                    return (base_form + delimiter).replace(rule[0][i] + delimiter, rule[2][i])
    
    # Jesli nie znajde reguly z pasujacym zakonczeniem, zwracam forme wejsciowa
    return base_form

# Funkcja dopasowujaca paradygmat do formy wejsciowej (base_form)
# Dopasowanie polega na sprawdzeniu, czy forma wejsciowa zawiera zakonczenie podane w zbiorze zakonczen paradygmatu
# Jesli tak jest, zwracany jest zestaw zakonczen paradygmatu odpowiadajacy podanemu rodzajowi gramatycznemu
# Dodatkowo brane jest pod uwage, czy forma wejsciowa to imie (name_no = 0), czy nazwisko (name_no = 1)
def MatchParadigm(base_form, gender, full_name, name_no, if_adj = False):   
    
    res = []

    # Tworze liste paradygmatow
    Paradigms = P.Paradigms

    # Przegladam paradygmaty
    for Para in Paradigms:

        # Sprawdzam, zakonczenia podane w paradygmacie (pierwszy element) znajduja sie w formie wejsciwej
        if Aux.IsAtEnd(base_form, Para[0]):

            # Sprawdzam rodzaj gramatyczny:

            # Jesli podano, ze forma wejsciowa jest rodzaju meskiego
            if gender == 'm':
                
                # Wynik to drugi element paradygmatu - zbior zakonczen meskich
                res = Para[1]

                # Pobieram ostatnia litere formy wejsciowej
                # last_letter = base_form.split('/')[0][-1] if r'/' in base_form else base_form[-1]
                last_letter = base_form[-1]
                

                # Probuje rozpoznac jezyk pelnego nazwiska
                language = Lang.Language((full_name))

                # Korekta nazwisk! na -o: 
                # jesli polskie (slowianskie) -> paradygmat żeński (Lato, Laty jak kobieta, kobiety), 
                # jesli niepolskie (nieslowianskie) -> paradygmat męski (Marco Polo, Marca Pola jak ojciec, ojca)
                if last_letter == 'o' and name_no == 1 and language == 'slav': # forma na -o i nazwisko i niesłowiańskie

                    # zwracam paradygmat zensko-meski (zenski w lp, meski w lm)
                    res = Para[4]

                # Korekta imion i nazwisk na -e:
                # jesli imię -> nieodmienne (Enrique), WYJĄTEK: Mojsze
                # jesli nazwisko -> odmienne (Dante, Dantego)                                
                elif (last_letter == 'e' or last_letter == 'é') and name_no == 0 and "Mojsze" not in base_form: # forma na -e i imię                    
                    res = Paradigms[0][1]                    
                    break

                else: # wszystkie inne przypadki: zwracam paradygmat meski                                                            
                    res = Para[1]                    
                    break
            
            # paradygmat zenski
            elif gender == 'f':
                if if_adj: 
                    # jeśli wprowadzono informację, że forma bazowa jest przymiotnikiem
                    res = Para[5] # wybieram paradygmat af (przymiotnikowy żeński)
                else:
                    # jeśli brak informacji, że forma bazowa jest przymiotnikiem
                    res = Para[2] # wybieram paradygmat f (rzeczownikowy żeski)
                break

            # paradygmat nijaki
            elif gender == 'n':
                res = Para[3]
                break

            # brak rodzaju - zwracam pierwszy paradygmat z list - paradygmat pusty (brak zakonczen)
            else:
                res = Paradigms[0][1]
                break    
    
    # Jeśli nie znaleziono żadnego paradygmatu, funkcja zwraca paradygmat pusty (bez zakończeń)
    if res == []:
        res = Paradigms[0][1]
    
    return res

# Funkcja dodajaca zakonczenia do formy wejsciowej (base_form) ze zbioru zakonczen podanego paradygmatu (paradigm)
def ApplyParadigm(base_form, paradigm):
    
    # usuniecie podpowiedzi (formy znormalizowane typu Locke/k, Laplace/s)
    if r'/' in base_form:
        base_form = base_form.split(r'/')[0]

    # utworzenie tematu (pseudotematu)
    stem = ''
    N_sg = paradigm[0]
    stem = Aux.GetStem(base_form, N_sg)

    res = []

    # przejrzenie wszystkich zakonczen w paradygmacie
    # uwaga: do funkcji trzeba wprowadzic liste zakonczen (koncowek), 
    # a nie element listy Paradigms, ktory zawiera 4 podlisty (spis zakonczen form wejciowych, koncowki meskie, zenskie, nijakie, zensko-meskie)
    for case in paradigm:
        res.append(stem + '|' + str(case))

    return res

# Dopasowanie zakonczen
def AdjustEndings(forms, full_name):

    # ustalam prawdopodobny jezyk, z ktorego pochodzi pelne nazwisko
    lang = Lang.Language(full_name)

    # przegladam formy (napisy typu: temat + | + zakonczenie)
    for i in range(len(forms)):
        
        # przegladam reguly uzgadniania
        for rule in EA.Rules:            

            # stosuje regule uzgadniania na i-tej formie
            forms[i] = Aux.ApplyRule(forms[i], rule, lang)

    return forms

# Poprawka synkretyzmow: 
# utworzenie wlasciwych biernikow rodzaju meskiego
def CorrectSincretism(forms, if_person, if_alive):
       
    # przegladam formy
    for i in range(len(forms)):        
        
        # szukam form zawierajacych znaczniki synkretyzmu - '$
        if '$' in forms[i]:
            
            # czy forma jest biernikiem lp
            if i == 3: # B lp

                # czy forma jest zywotna
                if if_alive: # rzeczownik męskożywotny lub męskoosobowy
                    # biernikiem jest dopelniacz lp
                    forms[i] = forms[1]
                else: # rzeczownik męskorzeczowy
                    # biernikiem jest mianownik lp
                    forms[i] = forms[0]

            # czy forma jest biernikiem lm
            elif i == 13: # B lm

                # czy forma jest osobowa
                if if_person: # rzeczownik męskoosobowy
                    # biernikiem jest dopelniacz lm
                    forms[i] = forms[10]
                # forma jest nieosobowa
                else: # rzeczownik męskorzeczowy lub męskożywotny
                    # biernikiem jest mianownik lm
                    forms[i] = forms[9]            
            
            # jesli to nie jest biernik lp lub lm, usun znaczniki '$
            else:
                forms[i] = forms[i].replace('$', '')   

    return forms

# Poprawka form typu Jessica (wym. Dżesika): 
# w algorytmie powstaje bledna forma C-Ms Jessisie wynikająca z reguly c|^e -> sie, ktora byla opracowana na wypadek form typu Maurice
# Nie jest możliwe na etapie tworzenia form i uzgadniania tematu i koncowki rozdzielenie obu typow, bo algorytm ma przed soba jedynie tematy Jessic, Mauric i już nie wie, że w pierwszym jest /k/, a w drugim /s/
def CorrectJessica(forms):
    
    # Ustal, czy mamy sytuację: zapis c, wymowa k
    base_form = forms[0]

    norm_form = Normalize(base_form, base_form)

    if r"/" in norm_form:        
        base_form = norm_form.split("/")[0].replace("a", "").replace("e", "") # base_form = Jessic, Mauric
        true_pron = norm_form.split("/")[1].replace("a", "") # true_pron = k, s

        base_form_last_letter = base_form[-1] # base_form_last_letter = c
        true_pron_last_letter = true_pron[-1] # true_pron_last_letter = k, s

        if base_form_last_letter == "c" and true_pron_last_letter == "k":
            forms[2] = forms[2].replace("sie", "ce")
            forms[5] = forms[5].replace("sie", "ce")

    return forms


# Ostatnie poprawki na podstawie listy
def Proofread(forms):   

    for i in range(len(forms)):
        for x in C.List:
            if forms[i] == x[0]:
                forms[i] = x[1]
    
    return forms
        

# Glowna funkcja odmieniajaca
def Decline(base_form, gender, if_person, if_alive, name_no, full_name, if_adj = False):

    if not Aux.CheckIfDeclinable(base_form, ''):        
        return [base_form]*16

    # zachowaj forme wejsciowa    
    raw_base_form = base_form

    res = []

    # Normalizacja formy wejściowej
    base_form = Normalize(base_form, full_name)
    
    # Dopasowanie paradygmatu (zestawu zakończeń)
    paradigm = MatchParadigm(base_form, gender, full_name, name_no, if_adj)
    
    # Dodanie zakończeń
    res = ApplyParadigm(base_form, paradigm)

    # Dopasowanie zakończeń
    res = AdjustEndings(res, full_name)

    # Korekta formy wejściowej (niektóre reguły mogą ją zmodyfikować)
    if (raw_base_form != res[0]):
        res[0] = raw_base_form
        # res[0] = base_form.split(r'/')[0] if r'/' in base_form else base_form

    # Korekta form synkretycznych (bierników)
    res = CorrectSincretism(res, if_person, if_alive)

    # Korekta form typu Jessica
    res = CorrectJessica(res)

    # Ostateczna korekta:
    res = Proofread(res)

    return res

# Glowna funkcja odmieniajca imiona i nazwiska
# Lepiej stosowac te, poniewaz rozbija ona nazwy dwuczlonowe poloczone lacznikiem i odmienia kazda z nich
# po czym laczy uzyskane formy w zlozona nazwe
def DeclineName(base_form, gender, name_no, full_name):
    
    res = []

    if '-' in base_form:
        temp = base_form.split('-')

        n1 = Decline(temp[0], gender, True, True, name_no, full_name)
        n2 = Decline(temp[1], gender, True, True, name_no, full_name)
        
        for i in range(len(n1)):
            res.append(n1[i] + '-' + n2[i])
    else:
        
        res = Decline(base_form, gender, True, True, name_no, full_name)

    return res




# fn = 'Andrea Crispino'
# n = 'Crispino'
# name_no = 1
# l = Lang.Language(fn)
# print(l)
# nrm = Normalize(n, fn)
# print(nrm)
# par = MatchParadigm(nrm, 'm', fn, name_no)
# print(par)
# frm = DeclineName(n, 'm', name_no, fn)
# print(frm)
# for f in frm: print(f.encode('utf-8').decode('ansi'), end=' ')


