'''Moduł zawierający funkcje określające odmienność członów nazwy drużyny piłkarskiej.'''

class TeamDeclinator:
    
    @staticmethod
    def __checkRomanNumeral(text):
        '''Sprawdza, czy wprowadzony tekst jest liczbą rzymską.'''

        romanDigits = ['i', 'm', 'd', 'c', 'x', 'v', 'l']

        for letter in text:
            if letter.lower() not in romanDigits: 
                return False
        
        return True

    @staticmethod
    def __getType(text):
        '''Rozpoznaje typ ciągu znaków - zwraca "A", jeśli ciąg wejściowy to akronim (skrótowiec),
        albo "N", w przeciwnej sytuacji'''

        if TeamDeclinator.__checkRomanNumeral(text): 
            return '#'        
        elif text.upper() == text: 
            return 'A'
        else: return 'N'

    @staticmethod
    def __getTeamType(team_name):
        '''Rozpoznaje typ nazwy drużyny, zwracając ciąg liter składających się z symboli:
        "N" - człon nazwy niebędący skrótowcem (akronimem), 
        "A" - człon nazwy będący skrótowcem (akronimem),
        "#" - człon nazwy będący liczbą'''

        res = ''
        elements = team_name.split(' ')

        for e in elements:
            res += TeamDeclinator.__getType(e)
        
        return res

    @staticmethod    
    def __checkPolish(text):
        '''Funkcja sprawdza, czy podana nazwa drużyny jest w języku polskim.'''
        
        typical = ['ą', 'ę', 'gks', 'ł', 'azs', 'ks', 'mks', 'lzs', 'wks', 'mkp', 'cwks', 'ń', 'polska', 'ó', 'ś', 'ć', 'ź', 'ż', 'kks', 'jks', 'uks', 'ts', 'cks', 'aks', 'mlks', 'oks', 'glzs', 'tssr', 'hks', 'pwks', 'mlks', 'bks', 'tp', 'jks']

        for t in typical:
            if t in text.lower():
                return True
        return False

    @staticmethod
    def __getNameElement(name, number):
        '''Funkcja zwraca element nazwy "name" o indeksie "number".
        Jeśli indeks jest większy niż liczba elementów, funkcja zwraca nazwę wejściową.'''
        t = name.split(' ')
        if number < len(t):
            return t[number]
        else:
            return name

    @staticmethod
    def __getGender(name):
        '''Funkcja określa rodzaj gramatyczny na podstawie zakończenia nazwy.'''

        name = name.lower()
        name = name + '#'

        for x in ['a', 'szcz', 'ść']:
            if x + '#' in name: # rodzaj żeński
                return 'f'
        
        for x in ['e', 'o']:
            if x + '#' in name: # rodzaj nijaki
                return 'n'
        
        for x in ['b', 'p', 'm', 'f', 'w', 'v', 't', 'd', 'n', 's', 'z', 'c', 'r', 'l', 'ł', 'ś', 'ź', 'ć', 'ń', 'j', 'k', 'g', 'h']:
            if x + '#' in name: # rodzaj męski
                return 'm'
        
        return 'f' # domyślnie rodzaj żeński (ta drużyna)

    @staticmethod
    def GetTeamDeclination(team_name):
        '''Funkcja przypisująca sposób odmiany danej nazwie drużyny 
        (określa, które człony nazwy mają być odmieniane)
        oraz określająca rodzaj tej drużyny 
        (na podstawie zakończenia nadrzędnego elementu w nazwie).'''

        team_type = TeamDeclinator.__getTeamType(team_name)

        res = [team_type]

        if team_type == 'AN': # typ GSK Katowice, AS Roma
            if TeamDeclinator.__checkPolish(team_name):  
                g = TeamDeclinator.__getGender(TeamDeclinator.__getNameElement(team_name, 0))              
                res += ['ON', g] # GKS-em Katowice
            else: 
                g = TeamDeclinator.__getGender(TeamDeclinator.__getNameElement(team_name, 1))
                res += ['NO', g] # AS Romie
        elif team_type == 'NN': # Ruch Chorzów, Manchester United, Chelsea Londyn...
            g = TeamDeclinator.__getGender(TeamDeclinator.__getNameElement(team_name, 0))
            res += ['ON', g]
        elif team_type == 'ANN': # KS Ursus Warszawa, CA Boston River...
            g = TeamDeclinator.__getGender(TeamDeclinator.__getNameElement(team_name, 1))
            res += ['NNN', g]
        elif team_type == 'NNA' or team_type == 'NNN': 
            # San Francisco FC, Army United FC, Iraklis Saloniki FC, 
            # Los Angeles Galaxy, Unia Nowa Sarzyna 
            ex1 = ['san', 'los', 'la', 'east', 'west', 'north', 'south', 'santa']
            ex2 = ['town', 'city', 'united', 'hill']

            n = 0
            if TeamDeclinator.__getNameElement(team_name, 0) in ex1:
                n = 1 # San Francisco, Los Angeles -> nadrzędny jest element drugi
            elif TeamDeclinator.__getNameElement(team_name, 0) in ex2:
                n = 0 # Alton Town, Army United -> nadrzędny jest element pierwszy 
            else:
                n = 0 # Domyślnie nadrzędny jest element pierwszy (por. Iraklis Saloniki, Real Avilla)

            g = TeamDeclinator.__getGender(TeamDeclinator.__getNameElement(team_name, n))
            
            if TeamDeclinator.__checkPolish(team_name):
                res += ['ONN', g]
            else:
                res += ['NNN', g]
                
        elif team_type == 'NA': # Gretna FC, Crusaders FC
            g = TeamDeclinator.__getGender(TeamDeclinator.__getNameElement(team_name, 0))
            res += ['ON', g]
        elif team_type == 'N': # nazwy krajów
            g = TeamDeclinator.__getGender(TeamDeclinator.__getNameElement(team_name, 0))
            res += ['O', g]
        elif team_type == 'ANNN' or team_type == 'NNNA' or team_type == 'NNNN': 
            res += ['NNNN', 'n']
        elif team_type == 'AN#' or team_type == 'NAN' or team_type == 'NN#':
            res += ['NNN', 'n']
        elif team_type == 'NNNNN' or team_type == 'ANNNN': 
            res += ['NNNNN', 'n']
        else:
            res += ['N' * len(team_type), 'n']

        return res


