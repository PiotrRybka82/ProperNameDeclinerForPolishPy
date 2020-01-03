import Declinator.Auxiliary as Aux

# Reguły uzgodnienia zakończeń (ending adjustment rules)
Rules = []

# UWAGA: KAŻDA REGUŁA POWINNA WYKONYWAĆ TYLKO 1 ZMIANĘ, NIGDY DWIE LUB WIĘCEJ
# NP. ZMIANĘ Clark{e}|!em TRZEBA ROZPISAĆ NA 2 REGUŁY: 
# 1) USUNIĘCIE {e}: Clark{e}|!em > Clark|!em; 
# 2) ZMIĘKCZENIE k: Clark|!em >  Clarkiem

#######################################################
# KRZYŻYKAMI ZAZNACZONO REGUŁY, KTÓRE MUSZĄ SIĘ POJAWIĆ W PODANEJ KOLEJNOŚCI, 
# TZN. PIERWSZA PRZED DRUGĄ. 
# OZNACZA TO, ŻE MOŻNA JE PRZENOSIĆ Z ZACHOWANIEM PODANEJ KOLEJNOŚCI
#######################################################

# Inne oznaczenia: 
# {} = litera niema, np. Clark{e} [wym. klark]
# [] = litera wstawna, np. An[e]ka: Anka, Anki..., ale Anek
# ^ = litera miękcząca, np. Piotr + ^e > Piotrze, Dorota + ^e > Dorocie
# > = Zmiana po zastosowaniu 1 reguły
# >> = Zmiana po zastosowaniu n reguł
# | = granica między tematem a końcówką, a dokładniej granica zjawisk dopasowania zakończeń
# *) Granica | jest przesuwana przez niektóre reguły po to, by kolejne reguły mogły zostać wykonane
# 0 = końcówka zerowa
# ~ = dowolny ciąg liter


# EPENTEZY (PRZED INNYMI REGULAMI!!!)

#######################################################
# ^[e]C|0 > |^eC, C = ń, c, r - wstawienie [e] w formach na ~eń|0, np. Kwiet^[e]ń|0 >> Kwietnia, Lip^[e]c|0 > Lipiec (z przesunięciem granicy |)*
bef = Aux.Product(['^', ''], ['[e]'], ['ń', 'c', 'r'], ['|0'])
c = ['']
aft = Aux.Product(['|^', '|'], ['e'], ['ń', 'c', 'r'], ['|'])
Rules.append([bef, c, aft])
# ^[e]ń > tń - usunięcie [e] w formach na ~eń|~, np. Kwiecień > Kwietnia, Lip^[e]c|0 > Lipca
bef = Aux.Product(['^', ''], ['[e]'], ['ń', 'c', 'r'], ['|'])
aft = Aux.Product(['|^', '|'], [''], ['ń', 'c', 'r'], ['|'])
Rules.append([bef, c, aft])
#######################################################

#######################################################
# ![e]l|0 > |!el - wstawienie [e] w formach na ~el|0, np. Dek![e]l|0 >> Dekiel (z przesunięciem granicy |)*
bef = Aux.Product(['', '!'], ['[e]'], ['l', 'ł'], ['|0'])
aft = Aux.Product(['|', '|!'], ['e'], ['l', 'ł'], ['|'])
Rules.append([bef, c, aft])
# ![e]l > l - usunięcie [e] w formach na ~el|~, np. Dek![e]la > Dekla
bef = Aux.Product(['', '!'], ['[e]'], ['l', 'ł'])
aft = Aux.Product(['', ''], [''], ['l', 'ł'])
Rules.append([bef, c, aft])
#######################################################

######################################################
# [e]k|0 > ek - wstawienie [e] w formach na ~ek|0, np. Dud[e]k|0 > Dudek, Mnisz[e]ch > Mniszec
bef = Aux.Product(['[e]'], ['k', 'ch'], ['|0'])
aft = Aux.Product(['e'], ['k', 'ch'], ['|0'])
Rules.append([bef, c, aft])
# # [e]k > k - usunięcie [e] w formach na ~ek|~, np. Dud[e]k|a > Dudka
bef = Aux.Product(['[e]'], ['k', 'ch'])
aft = Aux.Product([''], ['k', 'ch'])
Rules.append([bef, c, aft])
#######################################################

#######################################################
# [n]|0 > |0 - usunięcie [n] w formach na ~[n]|0, np. Apollo, Bruno
bef = Aux.Product(['[n]'], ['|0'])
aft = Aux.Product([''], ['|0'])
Rules.append([bef, c, aft])
# [n]| > | - wstawienie [n] w formach na ~[n]|~, np. Apollona, Brunona
bef = Aux.Product(['[n]'], ['|'])
aft = Aux.Product(['n'], ['|'])
Rules.append([bef, c, aft])
#######################################################

#######################################################
# [e]k|0 > ek|0 - wstawienie [e] w formach na ~[e]k|0, np. An[e]ka > Anek, Baś[e]ka >> Basiek, Kasień[e]ka >> Kasieniek
bef = Aux.Product(['[e]'], ['k'], ['|0'])
aft = Aux.Product(['e'], ['k'], ['|0'])
Rules.append([bef, c, aft])
# # [e]k > k - usunięcie [e] w formach na ~[e]k|~, np. An[e]ka > Anka, Baś[e]ka > Baśka, Kasień[e]ka > Kasieńka
bef = Aux.Product(['[e]'], ['k'], ['|'])
aft = Aux.Product([''], ['k'], ['|'])
Rules.append([bef, c, aft])
#######################################################

#######################################################
# ów^[e]n|0 > ów|^en - wstawienie [e] w formach na ~ów^[e]|0, np. Marszałków^[e]n|0 > Marszałkówien
bef = Aux.Product(['ów'], ['^[e]'], ['n'], ['|0'])
aft = Aux.Product(['ów'], ['^[e]'], ['n'], ['|0'])
Rules.append([bef, c, aft])
# ów^[e]n > ówn - usunięcie [e] w formach na ~ów^[e]|~, np. Marszałków^[e]n|a > Marszałkówna
bef = Aux.Product(['ów'], ['^[e]'], ['n'], ['|'])
aft = Aux.Product(['ów'], [''], ['n'], ['|'])
Rules.append([bef, c, aft])
#######################################################



# LITERY NIEME

# {e}|0 > e|0
# - usunięcie oznaczenia litery niemej przed końcówką zerową |0
bef = Aux.Product(['}|0'])
aft = Aux.Product(['|0'])
Rules.append([bef, c, aft])

# C{e}|^V > C|^V, C = t, d, k, g, v, b, p, m, n, r, w, s, z, V = e, i 
# - usunięcie {e} przed ^i, ^e, np. Clark{e}|^i >> Clarcy, Cliv{e}|^e >> Clivie, Voltair{e}|^e >> Voltairze, Wild{e}|^e >> Wildzie, Descart{es}|^e >> Descarcie
bef = Aux.Product(['c', 'v', 't', 'd', 'k', 'g', 'v', 'b', 'p', 'm', 'n', 'r', 'w', 's', 'z'], ['{hes}', '{es}', '{e}'], ['|^'], ['e', 'i'])
aft = Aux.Product(['c', 'v', 't', 'd', 'k', 'g', 'v', 'b', 'p', 'm', 'n', 'r', 'w', 's', 'z'], ['', '', ''], ['|^'], ['e', 'i'])
Rules.append([bef, c, aft])

# C{e}|!E > C|!E, C = k, g, qu, gu, E = em, y
# - usunięcie {e} przed !em, !y, np. Lock{e}|!em >> Lockiem, Jacqu{es}|!em >> Jakiem, Clark{e}|!em >> Clarkiem
bef = Aux.Product(['k', 'g', 'qu', 'gu'], ['{e}', '{es}'],  ['|!', '|^'], ['em', 'y', 'i'])
aft = Aux.Product(['k', 'g', 'qu', 'gu'], ['', ''],  ['|!', '|^'], ['em', 'y', 'i'])
Rules.append([bef, c, aft])

# {y}|E > y|E, E = mi, m, ch - zamiana {y} w y przed mi, m, ch, np. Kenned{y}|m > Kennedym
bef = Aux.Product(['{y}'], ['|mi', '|m', '|ch'])
aft = Aux.Product(['y'], ['|mi', '|m', '|ch'])
Rules.append([bef, c, aft])

# {e}|iV > {e}|V - usunięcie i po {e}, np. Montaign{e}|iem >> Montaigne'em
bef = Aux.Product(["'i"], ['a', 'e', 'o', 'u', 'y', 'ę', 'ą'])
aft = Aux.Product(["'"], ['a', 'e', 'o', 'u', 'y', 'ę', 'ą'])
Rules.append([bef, c, aft])



# LITERY O INNEJ WYMOWIE

# C|!E > K|!E, C = c, q, qu, gu, E = em, i
# - zamiana c, q, qu, gu na k przed !em, !i, np. Signac|!em >> Signakiem, Jacqu|!em > Jakiem
bef = Aux.Product(['c', 'q', 'cqu', 'qu', 'gu'], ['|!'], ['em', 'y', 'i'])
aft = Aux.Product(['k', 'k', 'k', 'k', 'k'], ['|!'], ['em', 'y', 'i'])
Rules.append([bef, c, aft])

# ck|^i > k|^i - zamiana ck na k przed ^i, np. Spock|^i > Spocy
bef = ['ck|^i']
aft = ['k|^i']
Rules.append([bef, c, aft])

# th|^e > t|^e - zamiana th na t przed ^e, np. Galbraith|^e >> Galbraicie
bef = Aux.Product(['th', 'dh', 'gh', 'kh'], ['|^e', '|!'])
aft = Aux.Product(['t', 'd', 'g', 'k'], ['|^e', '|!'])
Rules.append([bef, c, aft])

# c|^V > s|^V, V = e, i - zamiana c wymawianego jak s, np. Maurice, Lourenço
bef = Aux.Product(['c', 'ç'], ['|^'], ['i', 'e'])
aft = Aux.Product(['s', 's'], ['|^'], ['i', 'e'])
Rules.append([bef, c, aft])



# ALTERNACJE FONOLOGICZNE (ZMIANA FONEMU)

# oD|0 > óD|0, np. Jagoda > Jagód (KONIECZNIE PRZED INNYMI REGUŁAMI W TEJ GRUPIE!!!)
bef = Aux.Product(['o'], ['b', 'd', 'g', 'z', 'w', 'ł', 'dz', 'dź', 'dż'], ['|0'])
c = ['slav']
aft = Aux.Product(['ó'], ['b', 'd', 'g', 'z', 'w', 'ł', 'dz', 'dź', 'dż'], ['|0'])
Rules.append([bef, c, aft])

# óD|V > oD|V, np. Pieróg > Pieroga (KONIECZNIE PRZED INNYMI REGUŁAMI W TEJ GRUPIE!!!)
bef = Aux.Product(['ó'], ['b', 'd', 'g', 'z', 'w', 'ł', 'dz', 'dź', 'dż'], ['|'], ['^', '!', ''], ['a', 'e', 'o', 'ó', 'u', 'ę', 'ą', 'y'])
c = ['']
aft = Aux.Product(['o'], ['b', 'd', 'g', 'z', 'w', 'ł', 'dz', 'dź', 'dż'], ['|'], ['^', '!', ''], ['a', 'e', 'o', 'ó', 'u', 'ę', 'ą', 'y'])
Rules.append([bef, c, aft])

# Cn|^i > Ćni, C = s, dz, z, c, n, Ć = ś, ź, ć, ń, np. Żelazni > Żelaźni (KONIECZNIE PRZED INNYMI REGULAMI)
bef = Aux.Product(['s', 'dz', 'z', 'c'], ['n'], ['|'], ['!', '^'], ['i'])
aft = Aux.Product(['ś', 'dź', 'ź', 'ć'], ['n'], [''], ['', ''], ['i'])
Rules.append([bef, c, aft])

# cź > cz - korekta (poprzednia regula moze zamieniac cz w cź)
bef = Aux.Product(['s', 'c'], ['ź'])
aft = Aux.Product(['s', 'c'], ['z'])
Rules.append([bef, c, aft])

# K|!V > KiV, K = k, g, V = e, y 
# - zamiana k, g na ki, gi przed !e, !y, np. Patryk|!em > Patrykiem, Patryk|!y > Patryki
bef = Aux.Product(['k', 'g'], ['|!e', '|!y'])
c = ['']
aft = Aux.Product(['k', 'g'], ['ie', 'i'])
Rules.append([bef, c, aft])

# K|^V > CW, K = k, g, C = c, dz, V = i, e, W = y, e
# - zamiana k, g, ch, h, na odpowiednio c, dz, sz, ż przed ^i, ^e, ze zmianą tychże w odpowiednio ^y, ^e
# np. Ank|^e > Ance, prorok|^i > prorocy, Zoch|^e > Zosze, Tah|^e (nazw.) > Taże
bef = Aux.Product(['k', 'g'], ['|!i', '|^e'])
aft = Aux.Product(['c', 'dz'], ['y', 'e'])
Rules.append([bef, c, aft])

# H|^i > Si, H = ch, h, S = s, z - zamiana ch, h na s, z, 
# np. mnich > mnisi, druh > druhowie, Zocha > Zosze, wataha > wataże
bef = ['ch|!i', 'ch|^e', 'h|!i', 'h|^e']
aft = ['si', 'sze', 'howie', 'że']
Rules.append([bef, c, aft])

# T|^e > Tie, T|^i > Ti, T = p, b, t, d, w, f, m, n, s, z
bef = Aux.Product(['p', 'b', 'v', 'w', 'f', 'm', 'n', 's', 'z'], ['|^e', '|^i'])
aft = Aux.Product(['p', 'b', 'v', 'w', 'f', 'm', 'n', 's', 'z'], ['ie', 'i'])
Rules.append([bef, c, aft])

# C|^e > Ćie, C|^i > Ći, C = t, d, Ć = c, dz
bef = Aux.Product(['s', 'z', ''],  ['t', 'd'], ['|^e', '|^i'])
aft = Aux.Product(['ś', 'ź', ''], ['c', 'dz'], ['ie', 'i'])
Rules.append([bef, c, aft])

# C|^e > Ćie, C|^i > Ći, C = ł, Ć = l
bef = Aux.Product(['ł'], ['|^e', '|^i'])
aft = Aux.Product(['l'], ['e', 'i'])
Rules.append([bef, c, aft])

# C|^e > Ćie, C|^i > Ći, C = r, Ć = rz
bef = Aux.Product(['r'], ['|^e', '|^i'])
aft = Aux.Product(['rz'], ['e', 'y'])
Rules.append([bef, c, aft])

# C|^0 > Ć, C = n, s, z, c, Ć = ń, ś, ź, ć
bef = Aux.Product(['n', 's', 'z', 'c'], ['|^0'])
aft = Aux.Product(['ń', 'ś', 'ź', 'ć'], [''])
Rules.append([bef, c, aft])

# C|ij > Cyj, C = t, d, r, s, z, c
bef = Aux.Product(['t', 'd', 'r', 's', 'z', 'c'], ['i|j', 'j|0'])
aft = Aux.Product(['t', 'd', 'r', 's', 'z', 'c'], ['yj', 'yj'])
Rules.append([bef, c, aft])

# CĆe > ĆĆe, C = s, z, n, Će = cie, dzie, nie
bef = Aux.Product(['s', 'z', 'n'], ['c', 'dz', 'n'], ['ie'])
aft = Aux.Product(['ś', 'ź', 'ń'], ['c', 'dz', 'n'], ['ie'])
Rules.append([bef, c, aft])





# ALTERNACJE GRAFICZNE (ZMIANA SPOSOBU ZAPISU TEGO SAMEGO FONEMU)

# Ć|V > CiV, Ć = ś, ć, ź, ń, C = s, c, z, n, V = a, e, o, u, ę, ą
bef = Aux.Product(['ś', 'ć', 'ź', 'ń'], ['|!', '|^', '|', ''], ['a', 'e', 'o', 'u', 'ę', 'ą'])
aft = Aux.Product(['s', 'c', 'z', 'n'], ['i', 'i', 'i', 'i'], ['a', 'e', 'o', 'u', 'ę', 'ą'])
Rules.append([bef, c, aft])

# Ć|i > Ci, Ć = ś, ć, ź, ń, C = s, c, z, n
bef = Aux.Product(['ś', 'ć', 'ź', 'ń'], ['|'], ['i'])
aft = Aux.Product(['s', 'c', 'z', 'n'], [''], ['i'])
Rules.append([bef, c, aft])

# Vj|i > Vi, V = a, e, i, o, u, y
bef = Aux.Product(['a', 'e', 'i', 'o', 'u', 'y'], ['j', 'y', 'i'], ['|i'])
aft = Aux.Product(['a', 'e', 'i', 'o', 'u', 'y'], ['', '', ''], ['i'])
Rules.append([bef, c, aft])

# KOŃCOWE REGUŁY (USUNIĘCIE ZNAKÓW SPECJALNYCH)
bef = ['|', '0', '{', '}', '^', '#', '!']
aft = ['', '', '', "'", '', '', '']
Rules.append([bef, c, aft])


