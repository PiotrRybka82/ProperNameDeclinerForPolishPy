'''Generator form fleksyjnych skrótowców.'''

vowels = ['a', 'e', 'o', 'i', 'u', 'y']

def IfNonInitialism(abbreviation):
    '''Funkcja sprawdza, czy podany skrótowiec jest głoskowcem, 
    tzn. czy zawiera przynajmniej jedną samogłoskę między pierwszą a ostatnią swoją literą.'''

    for v in vowels:
        if v in abbreviation[1:-1].lower():
            return True
    return False

def Decline(acronym):
    '''Wlaściwa funkcja odmieniająca skrotowce'''

    res = ''
    if IfNonInitialism(acronym):
        res = declineNoninitialism(acronym)
    else:
        res = declineInitialism(acronym)
    return res

def declineInitialism(acronym):
    '''Funkcja odmieniająca literowce - skrotowce typu PKP, WKO'''

    cons = ['f', 'j', 'l', 'm', 'n', 'r', 's', 'z', 'ź', 'ż']
    
    N = G = D = A = L = I = V = acronym.upper()

    last_letter = acronym[-1].lower()

    if last_letter in cons:
        if last_letter in ['f', 'm', 'n', 's']:
            # typ IPN
            G = G + '-u'
            D = D + '-owi'
            I = I + '-em'
            L = L + '-ie'
            V = L
        elif last_letter in ['j']:
            # typ UJ
            G = G + '-otu'
            D = D + '-otowi'
            I = I + '-otem'
            L = L + '-ocie'
            V = L
        elif last_letter in ['l']:
            # typ IBL
            G = G + '-u'
            D = D + '-owi'
            I = I + '-em'
            L = L + '-u'
            V = L
        elif last_letter in ['r']:
            # typ ONR
            G = G + '-u'
            D = D + '-owi'
            I = I + '-em'
            L = L + '-ze'
            V = L
        elif last_letter in ['z', 'ź', 'ż']:
            # typ ONZ
            G = G + '-etu'
            D = D + '-etowi'
            I = I + '-etem'
            L = L + '-ecie'
            V = L
        
    return [N, G, D, A, I, L, V]

def declineNoninitialism(acronym):
    '''Funkcja odmieniająca skrotowce gloskowe - skrotowce typu PAN, PIS'''

    last_letter = acronym[-1].lower()
    N = G = D = A = I = L = V = acronym

    lower = acronym.title()
    
    G = G + '-u'
    D = D + '-owi'
    I = I + '-em'
    
    if last_letter in ['b', 'p', 'm', 'f', 'v', 'w', 'n', 's', 'z', 'c']:
        # typ PAN'
        L = V = V + '-ie'
    elif last_letter in ['t']:
        # typ LOT
        L = V = lower[0:-1] + 'cie'
    elif last_letter in ['d']:
        L = V = lower[0:-1] + 'dzie'
    elif last_letter in ['r']:
        # typ KOR
        L = V = lower[0:-1] + 'rze'
    elif last_letter in ['l']:
        # typ PESEL
        L = V = V + '-lu'
    elif last_letter in ['ł']:
        # typ ???
        L = V = lower[0:-1] + 'le'
    elif last_letter in ['k', 'g']:
        # typ LOK 
        I = acronym + '-iem'
        L = V = G
    elif last_letter in ['h']:
        L = V = G
    else:
        G = D = A = I = L = V = N = acronym

    return [N, G, D, A, I, L, V]

