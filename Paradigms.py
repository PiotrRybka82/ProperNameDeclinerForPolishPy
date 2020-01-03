# Lista paradygmatow
import Declinator.Auxiliary as Aux

Paradigms = []

# Paradygmat pusty - bez zakonczen
empty = ['', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '']

# 1 ndm (typ Dubois, Attenborough)
# Uwaga: nie dodawać ~u: wykluczy nazwiska typu Landau
en = ['NDM']
m = f = n = mf = af = empty
Paradigms.append([en, m, f, n, mf, af])

# 2 sm1_Ć (typ Jaś)
en = ['dź', 'ź', 'ć', 'ś', 'ń']
m = ['0', 'ia', 'iowi', '$', 'iem', 'iu', 'iu', 'iowie', 'ie', 'ie', 'iów', 'i', 'iom', '$', 'iami', 'iach']
f = n = mf = empty
Paradigms.append([en, m, f, n, mf, af])

# 3 sm1_Cy (typ Nagy, Barany, Kodaly)
en = ['ny/!ń!', 'gy/!dź!', 'ly/!j!']
m = ['0', 'a', 'owi', '$', 'em', 'u', 'u', 'owie', 'e', 'e', 'ów', '0', 'om', '$', 'ami', 'ach']
f = n = mf = empty
Paradigms.append([en, m, f, n, mf, af])

# 4 sm1_Cio (typ Bodzio, Badoglio, Fabio, Palladio)
en = Aux.Product(['dz', 'z', 'c', 's', 'n', 'l', 'b', 'p', 'd', 't'], ['io'])
m = ['io', 'ia', 'iowi', '$', 'iem', 'iu', 'iu', 'iowie', 'ie', 'ie', 'iów', 'i', 'iom', '$', 'iami', 'iach']
f = n = mf = empty
Paradigms.append([en, m, f, n, mf, af])

# 5 sm1_lj (typ Anatol, Bartłomiej, Stanley)
en = ['l', 'j']
m = ['0', 'a', 'owi', '$', 'em', 'u', 'u', 'owie', 'e', 'e', 'ów', 'i', 'om', '$', 'ami', 'ach']
f = n = mf = empty
Paradigms.append([en, m, f, n, mf, af])

# 6 sm1_lo (typ Paolo, Cereijo, Caio)
en = ['lo', 'jo', 'io']
m = ['o', 'a', 'owi', '$', 'em', 'u', 'u', 'owie', 'e', 'e', 'ów', 'i', 'om', '$', 'ami', 'ach']
mf = ['o', 'i', 'i', 'ę', 'ą', 'i', 'o', 'owie', 'e', 'e', 'ów', 'i', 'om', '$', 'ami', 'ach']
f = n = empty
Paradigms.append([en, m, f, n, mf, af])

# 7 sm2_C (typ Tadeusz)
en = ['c', 'dz', 'sz', 'ż', 'rz', 'cz', 'dż']
m = ['0', 'a', 'owi', '$', 'em', 'u', 'u', 'owie', 'e', 'e', 'ów', 'ów', 'om', '$', 'ami', 'ach']
f = n = mf = empty
Paradigms.append([en, m, f, n, mf, af])

# 8 sm2_Co (typ Vincenzo [vinczenco])
en = Aux.Product(['c', 'dz', 'sz', 'ż', 'rz', 'cz', 'dż'], ['o'])
m = ['o', 'a', 'owi', '$', 'em', 'u', 'u', 'owie', 'e', 'e', 'ów', 'ów', 'om', '$', 'ami', 'ach']
mf = ['o', 'y', 'y', 'ę', 'ą', 'y', 'o', 'owie', 'e', 'e', 'ów', 'ów', 'om', '$', 'ami', 'ach']
f = n = empty
Paradigms.append([en, m, f, n, mf, af])

# 9 sm3_K (typ Patryk, Roch, Georg)
en = ['k', 'g', 'ch', 'h']
m = ['0', 'a', 'owi', '$', '!em', 'u', 'u', 'owie', '!i', '!y', 'ów', 'ów', 'om', '$', 'ami', 'ach']
f = n = mf = empty
Paradigms.append([en, m, f, n, mf, af])

# 10 sm3_Ko (typ Jaśko, Domenico, Sinko)
# Uwaga: W lp imion: -u (Mieszku, Zbyszku), nazwisk: -o (Kościuszko, Moniuszko)
en = Aux.Product(['k', 'g', 'ch', 'h'], ['o'])
m = ['o', 'a', 'owi', '$', '!em', 'u', 'u', 'owie', '!i', '!y', 'ów', 'ów', 'om', '$', 'ami', 'ach']
mf = ['o', '!y', '^e', 'ę', 'ą', '^e', '^e', 'owie', '!i', '!y', 'ów', 'ów', 'om', '$', 'ami', 'ach']
n = f = empty
Paradigms.append([en, m, f, n, mf, af])

# 11 sm4_T (typ Jan)
en = ['b', 'p', 'd', 't', 'w', 'v', 'f', 'm', 'n', 'r', 's', 'z', 'ł']
m = ['0', 'a', 'owi', '$', 'em', '^e', '^e', 'owie', '^i', 'y', 'ów', 'ów', 'om', '$', 'ami', 'ach']
f = n = mf = empty
Paradigms.append([en, m, f, n, mf, af])

# 12 sm4_To (typ Benito)
en = Aux.Product(['b', 'p', 'd', 't', 'w', 'v', 'f', 'm', 'n', 'r', 's', 'z', 'ł'], ['o'])
m = ['o', 'a', 'owi', '$', 'em', '^e', '^e', 'owie', '^i', 'y', 'ów', 'ów', 'om', '$', 'ami', 'ach']
mf = ['o', '!y', '^e', 'ę', 'ą', '^e', '^e', 'owie', '^i', 'y', 'ów', 'ów', 'om', '$', 'ami', 'ach']
n = f = empty
Paradigms.append([en, m, f, n, mf, af])

# 13 sm4_aw (typ Shaw, Monroe, Longfellow, Landau, Marlowe)
en = ['ow*', 'owe*', 'oe*']
m = ['0', 'a', 'owi', '$', 'em', '0', '0', 'owie', '0', 'y', 'ów', 'ów', 'om', '$', 'ami', 'ach']
f = n = mf = empty
Paradigms.append([en, m, f, n, mf, af])

# 14 sm4_Vo (typ Romeo)
en = ['eo*']
m = ['o', 'a', 'owi', '$', 'em', 'o', 'o', 'owie', 'o', 'y', 'ów', 'ów', 'om', '$', 'ami', 'ach']
f = n = mf = empty
Paradigms.append([en, m, f, n, mf, af])

# 15 sf1_Cia_Ci (typ Kasia, Kościa [m])
en = Aux.Product(['s', 'z', 'c'], ['ia'])
f = ['ia', 'i', 'i', 'ię', 'ią', 'i', 'iu', 'ie', 'ie', 'ie', '^0', '^0', 'iom', 'ie', 'iami', 'iach']
m = ['ia', 'i', 'i', 'ię', 'ią', 'i', 'iu', 'iowie', 'ie', 'ie', 'iów', 'iów', 'iom', '$', 'iami', 'iach']
af = ['a', 'ej', 'ej', 'ą', 'ą', 'ej', 'a', 'e', 'e', 'e', 'ch', 'ch', 'm', 'e', 'mi', 'ch']
n = mf = empty
Paradigms.append([en, m, f, n, mf, af])


# 15 sf1_Cia_Ci (typ Ania) + (typ tania)
en = Aux.Product(['n'], ['ia'], ['/!nia!'])
f = ['ia', 'i', 'i', 'ię', 'ią', 'i', 'iu', 'ie', 'ie', 'ie', '^0', '^0', 'iom', 'ie', 'iami', 'iach']
m = ['ia', 'i', 'i', 'ię', 'ią', 'i', 'iu', 'iowie', 'ie', 'ie', 'iów', 'iów', 'iom', '$', 'iami', 'iach']
af = ['a', 'ej', 'ej', 'ą', 'ą', 'ej', 'a', 'e', 'e', 'e', 'ch', 'ch', 'm', 'e', 'mi', 'ch']
n = mf = empty
Paradigms.append([en, m, f, n, mf, af])


# 16 sf1_Cia_Cii (typ Oliwia, Leokadia, Amelia, Maria, Ilia [m])
en = Aux.Product(['b', 'p', 't', 'd', 'f', 'w', 'v', 'k', 'g', 'l', 'r', 'n'], ['ia', 'ía'])
f = ['a', 'i', 'i', 'ę', 'ą', 'i', 'o', 'e', 'e', 'e', 'j', 'j', 'om', 'e', 'ami', 'ach']
m = ['a', 'i', 'i', 'ę', 'ą', 'i', 'o', 'owie', 'e', 'e', 'ów', 'ów', 'om', '$', 'ami', 'ach']
n = mf = empty
Paradigms.append([en, m, f, n, mf, af])

# 17 sf1_la (typ Ola, Kaligula)
en = ['la']
f = ['a', 'i', 'i', 'ę', 'ą', 'i', 'u', 'e', 'e', 'e', '0', '0', 'om', 'e', 'ami', 'ach']
m = ['a', 'i', 'i', 'ę', 'ą', 'i', 'o', 'owie', 'e', 'e', 'ów', 'ów', 'om', '$', 'ami', 'ach']
n = mf = empty
Paradigms.append([en, m, f, n, mf, af])

# 18 sf1_ja (typ Alicja, Azja [Tuchajbejowicz])
en = ['ja']
f = ['a', 'i', 'i', 'ę', 'ą', 'i', 'u', 'e', 'e', 'e', '0', '0', 'om', 'e', 'ami', 'ach']
m = ['a', 'i', 'i', 'ę', 'ą', 'i', 'o', 'owie', 'e', 'e', 'ów', 'ów', 'om', '$', 'ami', 'ach']
n = mf = empty
Paradigms.append([en, m, f, n, mf, af])

# 19 sf1_Va (typ Amadea, Amaltea, Andrea, Nauzykaa)
en = Aux.Product(['a', 'e'], ['a'])
# en = ['ea']
f = ['a', 'i', 'i', 'ę', 'ą', 'i', 'u', 'e', 'e', 'e', 'i', 'i', 'om', 'e', 'ami', 'ach']
m = ['a', 'i', 'i', 'ę', 'ą', 'i', 'o', 'owie', 'e', 'e', 'ów', 'ów', 'om', '$', 'ami', 'ach']
n = mf = empty
Paradigms.append([en, m, f, n, mf, af])


# 20 sf1_ja (typ Tuleya)
en = Aux.Product(['a', 'e', 'i', 'o', 'u'], ['ya'])
f = ['ya', 'i', 'i', 'yę', 'yą', 'i', 'yo', 'ye', 'ye', 'ye', 'i', 'i', 'yom', 'ye', 'yami', 'yach']
m = ['ya', 'i', 'i', 'yę', 'yą', 'i', 'yo', 'yowie', 'ye', 'ye', 'yów', 'yów', 'yom', '$', 'yami', 'yach']
mf = n = empty
Paradigms.append([en, m, f, n, mf, af])

# 21 sf2_Ca (typ Natasza, Sasza) + (typ grubsza)
en = Aux.Product(['c', 'cz', 'dz', 'dż', 'sz', 'ż', 'rz', 'zs', 'š'], ['a'])
f = ['a', 'y', 'y', 'ę', 'ą', 'y', 'o', 'e', 'e', 'e', '0', '0', 'om', 'e', 'ami', 'ach']
m = ['a', 'y', 'y', 'ę', 'ą', 'y', 'o', 'owie', 'e', 'e', 'ów', 'ów', 'om', '$', 'ami', 'ach']
af = ['a', 'ej', 'ej', 'ą', 'ą', 'ej', 'a', 'e', 'e', 'e', 'ych', 'ych', 'ym', 'e', 'ymi', 'ych']
n = mf = empty
Paradigms.append([en, m, f, n, mf, af])

# 22 sf3_Ka (typ Anka, Jadwiga) + (typ Kowalska)
en = Aux.Product(['k', 'g', 'ch', 'h'], ['a'])
f = ['a', '!y', '^e', 'ę', 'ą', '^e', 'o', '!y', '!y', '!y', '0', '0', 'om', '!y', 'ami', 'ach']
m = ['a', '!y', '^e', 'ę', 'ą', '^e', 'o', 'owie', '!i', '!y', 'ów', 'ów', 'om', '$', 'ami', 'ach']
af = ['a', 'iej', 'iej', 'ą', 'ą', 'iej', 'a', 'ie', 'ie', 'ie', 'ich', 'ich', 'im', 'ie', 'imi', 'ich']
n = mf = empty
Paradigms.append([en, m, f, n, mf, af])

# 23 sf4_Ta (typ Wanda, Eliza, Barnaba) + (typ gruba)
en = Aux.Product(['b', 'p', 'd', 't', 'w', 'v', 'f', 'z', 's', 'r', 'ł', 'm', 'n'], ['a', 'o'])
f = ['a', 'y', '^e', 'ę', 'ą', '^e', 'o', 'y', 'y', 'y', '0', '0', 'om', 'y', 'ami', 'ach']
m = ['a', 'y', '^e', 'ę', 'ą', '^e', 'o', 'owie', '^i', 'y', 'ów', 'ów', 'om', '$', 'ami', 'ach']
af = ['a', 'ej', 'ej', 'ą', 'ą', 'ej', 'a', 'e', 'e', 'e', 'ych', 'ych', 'ym', 'e', 'ymi', 'ych']
n = mf = empty
Paradigms.append([en, m, f, n, mf, af])

# 24 sf4_nha (typ Pessanha)
en = ['nha/na!']
m = ['ha', 'hy', 'ie', 'hę', 'hą', 'ie', 'ho', 'howie', 'i', 'hy', 'hów', 'hów', 'hom', '$', 'hami', 'hach']
f = n = mf = empty
Paradigms.append([en, m, f, n, mf, af])

# 24 sf4_nha (typ Sobrinho)
en = ['nho/no!']
m = ['ho', 'ha', 'howi', '$', 'hem', 'ie', 'ie', 'howie', 'i', 'hy', 'hów', 'hów', 'hom', '$', 'hami', 'hach']
f = n = mf = empty
Paradigms.append([en, m, f, n, mf, af])

# 24 sf4_nha (typ  Cehra)
en = ['rha/ra!']
m = ['ha', 'hy', '^e', 'hę', 'hą', '^e', 'ho', 'howie', '^i', 'hy', 'hów', 'hów', 'hom', '$', 'hami', 'hach']
f = n = mf = empty
Paradigms.append([en, m, f, n, mf, af])

# 25 sf4_To (typ Lato)
en = Aux.Product(['b', 'p', 'd', 't', 'w', 'f', 'z', 's', 'r', 'ł', 'm', 'n'], ['a', 'o'])
m = ['a', 'y', '^e', 'ę', 'ą', '^e', 'o', 'owie', '^i', 'y', 'ów', 'ów', 'om', '$', 'ami', 'ach']
f = n = m = empty
Paradigms.append([en, m, f, n, mf, af])

# 26 am1_Ci (typ Idzi, Antoni)
en = Aux.Product(['c', 'dz', 'z', 's', 'n'], ['i'])
m = ['i', 'iego', 'iemu', '$', 'im', 'im', 'i', 'iowie', 'i', 'ie', 'ich', 'ich', 'im', '$', 'imi', 'ich']
f = n = mf = empty
Paradigms.append([en, m, f, n, mf, af])

# 27 am1_li (typ Marceli, Torricelli)
en = ['li']
m = ['i', 'ego', 'emu', '$', 'im', 'im', 'i', 'owie', 'e', 'e', 'ich', 'ich', 'im', '$', 'imi', 'ich']
f = n = mf = empty
Paradigms.append([en, m, f, n, mf, af])

# 28 am1_Ki (typ Kowalski)
en = Aux.Product(['k', 'g'], ['i'])
m = ['i', 'iego', 'iemu', '$', 'im', 'im', 'i', '!i', '!i', '!e', 'ich', 'ich', 'im', '$', 'imi', 'ich']
f = n = mf = empty
Paradigms.append([en, m, f, n, mf, af])

# 29 am1_Koj (typ Trubieckoj)
en = Aux.Product(['s', 'c', 'z'], ['koj/oj*'])
m = ['oj', 'iego', 'iemu', '$', 'im', 'im', 'oj', '!i', '!i', '!e', 'ich', 'ich', 'im', '$', 'imi', 'ich']
f = n = mf = empty
Paradigms.append([en, m, f, n, mf, af])

# 30 am1_Kij (typ Bogorodckij)
en = Aux.Product(['s', 'c', 'z'], ['kij/ij*'])
m = ['ij', 'iego', 'iemu', '$', 'im', 'im', 'ij', '!i', '!i', '!e', 'ich', 'ich', 'im', '$', 'imi', 'ich']
f = n = mf = empty
Paradigms.append([en, m, f, n, mf, af])

# 31 am1_Ky (typ Chomsky)
en = Aux.Product(['s', 'c', 'z'], ['ky'])
m = ['y', 'iego', 'iemu', '$', 'im', 'im', 'y', '!i', '!i', '!e', 'ich', 'ich', 'im', '$', 'imi', 'ich']
f = n = mf = empty
Paradigms.append([en, m, f, n, mf, af])

# 32 am1_Ký (typ Komenský, Kopečný)
# en = Aux.Product(['s', 'c', 'z'], ['ký'])
en = ['ý']
m = ['ý', '!ego', '!emu', '$', '!ym', '!ym', 'ý', '!i', '!y', '!e', '!ych', '!ych', '!ym', '$', '!ymi', '!ych']
f = n = mf = empty
Paradigms.append([en, m, f, n, mf, af])

# 33 am1_Kyi (typ Stsepinskyi)
en = Aux.Product(['s', 'c', 'z'], ['kyi'])
m = ['yi', 'iego', 'iemu', '$', 'im', 'im', 'yi', '!i', '!i', '!e', 'ich', 'ich', 'im', '$', 'imi', 'ich']
f = n = mf = empty
Paradigms.append([en, m, f, n, mf, af])


# 34 am1_Ti (typ Luigi, Vivaldi)
en = Aux.Product(['b', 'p', 'd', 't', 'w', 'v', 'f', 'z', 's', 'r', 'm', 'n', 'g'], ['i'])
m = ['i', 'iego', 'iemu', '$', 'im', 'im', 'i', 'iowie', 'i', 'ie', 'ich', 'ich', 'im', '$', 'imi', 'ich']
f = n = mf = empty
Paradigms.append([en, m, f, n, mf, af])

# 35 am1_Ti (typ Martí)
en = Aux.Product(['b', 'p', 'd', 't', 'w', 'f', 'z', 's', 'r', 'm', 'n', 'g'], ['í'])
m = ['í', 'íego', 'íemu', '$', 'ím', 'ím', 'í', 'íowie', 'í', 'íe', 'ích', 'ích', 'ím', '$', 'ími', 'ích']
f = n = mf = empty
Paradigms.append([en, m, f, n, mf, af])

# 36 am1_Vi (typ Yahiaoui)
en = Aux.Product(['a', 'e', 'o', 'u', 'y'], ['i'])
m = ['i', 'iego', 'iemu', '$', 'im', 'im', 'i', 'iowie', 'i', 'ie', 'ich', 'ich', 'im', '$', 'imi', 'ich']
f = n = mf = empty
Paradigms.append([en, m, f, n, mf, af])

# 37 am2_Cy (typ Ambroży, Rakoczy)
en = Aux.Product(['c', 'dz', 'cz', 'dż', 'sz', 'ż', 'rz'], ['y'])
m = ['y', 'ego', 'emu', '$', 'ym', 'ym', 'y', 'owie', 'y', 'e', 'ych', 'ych', 'ym', '$', 'ymi', 'ych']
f = n = mf = empty
Paradigms.append([en, m, f, n, mf, af])

# 38 am2_Ty (typ Metody, Batory, Newerly)
en = Aux.Product(['b', 'p', 'd', 't', 'w', 'f', 'z', 's', 'r', 'm', 'n', 'ł', 'l'], ['y'])
m = ['y', 'ego', 'emu', '$', 'ym', 'ym', 'y', 'owie', '^i', 'e', 'ych', 'ych', 'ym', '$', 'ymi', 'ych']
f = n = mf = empty
Paradigms.append([en, m, f, n, mf, af])

# 39 am1_Hi (typ Eustachy)
en = Aux.Product(['ch', 'h'], ['y'])
m = ['y', 'ego', 'emu', '$', 'ym', 'ym', 'y', 'owie', '!i', '!e', 'ych', 'ych', 'ym', '$', 'ymi', 'ych']
f = n = mf = empty
Paradigms.append([en, m, f, n, mf, af])

# 40 am1_y (typ Joe, Poe)
en = Aux.Product(['Joe', 'Poe'], ['/*'])
m = ['e', 'ego', 'emu', '$', 'em', 'em', 'e', 'owie', 'e', 'e', 'ów', 'ów', 'om', '$', 'ami', 'ach']
f = n = mf = empty
Paradigms.append([en, m, f, n, mf, af])

# 41 am2_e (typ Dante)
en = Aux.Product(['k', 'g', 'b', 'p', 'd', 't', 'w', 'f', 'z', 's', 'r', 'm', 'n', 'ł', 'ch', 'h', 'l', 'j', 'y'], ['e', 'ie'])
m = ['e', 'ego', 'emu', '$', 'em', 'em', 'e', 'owie', 'e', 'e', 'ów', 'ów', 'om', '$', 'ami', 'ach']
f = n = mf = empty
Paradigms.append([en, m, f, n, mf, af])

# 42 am2_é (typ Malarmé)
en = Aux.Product(['b', 'p', 'd', 't', 'w', 'f', 'z', 's', 'r', 'm', 'n', 'ł', 'ch', 'h'], ['é'])
m = ['é' , 'ego', 'emu', '$', 'em', 'em', 'é', 'owie', 'é', 'é', 'ów', 'ów', 'om', '$', 'ami', 'ach']
f = n = mf = empty
Paradigms.append([en, m, f, n, mf, af])

# 43 am2_oe (typ Joe, Poe, Noe, Jozue)
en = ['oe/*', 'ue/*']
m = ['e', 'ego', 'emu', '$', 'em', 'em', 'e', 'owie', 'e', 'e', 'ów', 'ów', 'om', '$', 'ami', 'ach']
f = n = mf = empty
Paradigms.append([en, m, f, n, mf, af])

# 44 am2_y (typ Henry, Kennedy, Larry, Horthy)
en = ['!y']
m = ['0', "ego", "emu", '$', 'm', 'm', '0', 'owie', '0', 'e', 'ch', 'ch', 'm', '$', 'mi', 'ch']
f = n = mf = empty
Paradigms.append([en, m, f, n, mf, af])

# 45 am2_ie (typ Jamie, Christie)
en = ['!i']
m = ['e', "ego", "emu", '$', 'em', 'em', 'e', 'e', 'e', 'e', 'ech', 'ech', 'em', '$', 'emi', 'ech']
f = n = mf = empty
Paradigms.append([en, m, f, n, mf, af])




# Sortowanie zakonczen:
def SortPara(paradigms):
    unsorted = paradigms

    paradigms = []

    # Nowa lista paradygmatow
    # Kazdy pardygmat to lista skladajaca sie z 4 elementow: 
    # 0: zakonczenie, 1: zestaw 16 zakonczen w rodzaju meskim, 2: 16 zakonczen zenskich, 3: 16 zakonczen nijakich
    for para in unsorted:
        for end in para[0]:
            paradigms.append([[end], para[1], para[2], para[3]])

    # Wlasciwe sortowanie
    paradigms.sort(key=lambda x: len(x[0]), reverse=True)

    return paradigms