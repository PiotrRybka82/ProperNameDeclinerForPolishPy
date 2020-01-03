# Funkcje pomocncze

# Wycinanie tematu (pseudotematu) 
# przed odcięcie od formy podstawowej + znacznika zakonczenia 
# koncowki mianownika lp + znacznika zakonczenia
# W przypadku koncowki zerowej oznaczonej '0' forma wejsciowa jest tematem (pseudotematem)
def GetStem(base_form, N_sg, end_marker = '#'):
           
    return (base_form + end_marker).replace(N_sg + end_marker, '').replace(end_marker, '')    

# Sprawdzanie, czy dana forma zawiera ktorekolwiek zakonczenie ze zbioru
def IsAtEnd(form, input_set, end_marker = '#'):

    # posortowanie zbioru zakonczen pod wzgledem dlugosci (od najdluzszego)    
    input_set = SortByLength(input_set)

    # dodanie do formy wejsciowej znacznika zakonczenia
    form = form + end_marker
    
    # przejrzenie zbioru zakonczen
    for el in input_set:
        # sprawdzenie, czy w formie wejsciowej ze znacznikiem zakonczenia wystepuje zakonczenie ze zbioru
        if form.replace(el + end_marker, '') != form:
            return True

    return False

# Funkcja zwracajaca iloczyn kartezjanski dowolnej liczby list napisow
def Product(*sets):
    res = []
    for subset in sets:
        res = product(res, subset)
    return res      

# Funkcja zwracajaca iloczyn kartezjanski 2 list napisow
def product(setA, setB):
    res = []

    if len(setA) == 0:
        return setB

    for elA in setA:
        for elB in setB:
            res.append(elA + elB)
    return res 

# Funkcja sortujaca listy napisow w kolejnosci od najdluzszych 
def SortByLength(Set):
    
    Set.sort(key = lambda x: len(x), reverse = True)

    return Set

# Funkcja stosujaca wskazana regule dopasowywania tematu (pseudetematu) do zakonczenia
def ApplyRule(form, rule, lang):
    
    # przegladam lewe strony regul (przed zmiana) - pierwszy element reguly (lista napisow)
    for i in range(len(rule[0])):
        # sprawdzam, czy regula zawiera warunek dot. jezyka - drugi element reguly (lista napisow)
        if rule[1][0] != '':
            # przegladam warunki dot. jezyka
            for l in rule[1]:
                if l == lang:
                    # jesli jezyk jest zgodny, stosuje regule
                    # - zamieniam napis z lewej strony reguly na napis z prawej strony (trzeci element reguly)
                    form = form.replace(rule[0][i], rule[2][i])
        # jesli regula nie zawiera warunkow dot jezyka, stosuje regule
        else:
            form = form.replace(rule[0][i], rule[2][i])
        
    return form

# Funkcja konwertująca symbol przypadka na liczbę wg schematu: 
# N = 0, G = 1, D = 2, A = 3, I = 4, L = 5, V = 6
def CaseToNumber(case):

    case = str(case).upper()
    cases = ['N', 'G', 'D', 'A', 'I', 'L', 'V']

    return cases.index(case)

def CaseToLetter(case):
    
    cases = ['N', 'G', 'D', 'A', 'I', 'L', 'V']

    return cases[case]


def CheckIfDeclinable(name, prefix):
    
    not_declinable_current = ['do', 'da', 'de', 'la', 'los', 'del', 'dos', 'di', 'von', 'bin', 'la', 'den', 'al', 'el']
    not_declinable_next = ['do', 'da', 'de', 'la', 'dos', 'los', 'del']

    if name.lower() in not_declinable_current:
        return False
    elif prefix.lower() in not_declinable_next:
        return False
    else:
        return True






