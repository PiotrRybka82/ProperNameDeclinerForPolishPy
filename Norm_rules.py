import Declinator.Auxiliary as Aux

# Reguly normalizacji form wejsciowych

Rules = []


# NAZWISKA NIEODMIENNE
# Typ Dubois, Attenborough
end = Aux.Product([ 'Noah', 'Hugo', 'Vigo', 'ough', 'ois', 'oit', 'oix', 'eu', 'oux', 'eau', 'ó', 'ois', 'drew', 'thew'], [''])
c = ['en', 'fr']
nrm = Aux.Product([ 'Noah', 'Hugo', 'Vigo', 'ough', 'ois', 'oit', 'oix', 'eu', 'oux', 'eau', 'ó', 'ois', 'drew', 'thew'], ['/NDM'])
Rules.append([end, c, nrm])


# JĘZYK WĘGIERSKI
# Typ Nagy [nodź], Barany [barań], Kodaly [kodaj], Zápolya [zapoja]
end = Aux.Product(['a', 'e', 'o', 'u', 'i'], ['gy', 'ny', 'ly', 'lya'])
c = ['hu']
nrm = Aux.Product(['a', 'e', 'o', 'u', 'i'], ['gy/!dź!', 'ny/!ń!', 'ly/!j!', 'lya/!ja!'])
Rules.append([end, c, nrm])

### Typ Balazs (tylko węgierski, więc nie jest potrzebny warunek)
end = ['zs']
c = ['']
nrm = ['zs/!ż']
Rules.append([end, c, nrm])

# Typ Horthy
end = Aux.Product(['th'], ['y'])
c = ['hu']
nrm = Aux.Product(['th'], ['y/!y'])
Rules.append([end, c, nrm])



# JĘZYK FRANCUSKI
# Typ Montaigne [monteń], Broglie [broj]
end = ['aigne', 'oigne', 'glie']
c = ['']
nrm = ['aign{e}/ń', 'oign{e}/ń' 'gli{e}/j']
Rules.append([end, c, nrm])




# JĘZYK ANGIELSKI
# Typ Hemingway, Berkeley
end = ['ay', 'ey', 'oy']
c = ['']
nrm = ['ay/j', 'ey/j', 'oy/j']
Rules.append([end, c, nrm])

# Typ Toynbee
end = ['ee']
c = ['en']
nrm = ['ee/i']
Rules.append([end, c, nrm])

# Typ Jamie, Christie, Barrie
end = Aux.Product(['m', 't', 'r', 'k', 'p', 'n', 'd', 'g', 'b', 'l'], ['ie'])
c = ['en']
nrm = Aux.Product(['m', 't', 'r', 'k', 'p', 'n', 'd', 'g', 'b', 'l'], ['i{e}/!i'])
Rules.append([end, c, nrm])


# Typ Fry
end = Aux.Product(['B', 'P', 'M', 'F', 'V', 'W', 'T', 'D', 'N', 'S', 'Z', 'C', 'L'], ['ry'])
c = ['en']
nrm = Aux.Product(['B', 'P', 'M', 'F', 'V', 'W', 'T', 'D', 'N', 'S', 'Z', 'C', 'L'], ['r{y}/j'])
Rules.append([end, c, nrm])

# Typ Kennedy, Connery, Anthony, Henry, Newby
end = Aux.Product(['a', 'e', 'o', 'u', 'i', 'w', 'n'], ['ck', 'll', 'l', 'rr', 'r', 'b', 'p', 't', 'd', 'f', 'w', 's', 'z', 'c', 'n', 'm'], ['y'])
c = ['en', 'fr', 'sp', 'po']
nrm = Aux.Product(['a', 'e', 'o', 'u', 'i', 'w', 'n'], ['ck', 'll', 'l', 'rr', 'r', 'b', 'p', 't', 'd', 'f', 'w', 's', 'z', 'c', 'n', 'm'], ['{y}/!y'])
Rules.append([end, c, nrm])

# Typ Galbraith
end = ['th']
c = ['']
nrm = ['th/t']
Rules.append([end, c, nrm])

# Typ Shaw, Longfellow, Landau
end = ['aw', 'ow', 'au']
c = ['en', 'fr']
nrm = ['aw/ow*', 'ow/ow*', 'au/ow*']
Rules.append([end, c, nrm])

# Typ Joe, Poe, Noe (wyjątkowo odmieniane przymiotnikowo i bez apostrofu) (koniecznie przed Monroe!!!)
end = Aux.Product(['Joe', 'Poe', 'Noe', 'Jozue'], [''])
c = ['']
nrm = Aux.Product(['Joe', 'Poe', 'Noe', 'Jozue'], ['/*'])
Rules.append([end, c, nrm])

# Typ Monroe, Marlowe
end = ['oe', 'owe']
c = ['en']
nrm = ['o{e}/oe*', 'ow{e}/owe*']
Rules.append([end, c, nrm])

# Typ Romeo
end = ['eo']
c = ['']
nrm = ['eo/eo*']
Rules.append([end, c, nrm])






# JĘZYK FRANCUSKI I ANGIELSKI
# Typ Gable, Voltaire, Clive, Laplace, Bruce, Savage, Monroe (nieme 'e' na koncu wyrazu)
end = Aux.Product(['ro', 'v', 'k', 'g', 'b', 'p', 't', 'd', 'm', 'n', 'l', 'r', 'f', 's', 'z', 'c'], ['e'])
c = ['en', 'fr']
nrm = Aux.Product(['ro{e}', 'v{e}/w', 'k{e}/k', 'g{e}/ż', 'b{e}/b', 'p{e}/p', 't{e}/t', 'd{e}/d', 'm{e}/m', 'n{e}/n', 'l{e}/l', 'r{e}/r', 'f{e}/f', 's{e}/s', 'z{e}/z', 'c{e}/s'], [''])
Rules.append([end, c, nrm])

# Typ Delaroche, Lelouch, Barthes, Descartes, Rabelais, Mackintosh, Coleridge, Georges, Jacques, Doumergue [dumerg], Lebesgue
end = ['ges', 'che', 'ch', 'thes', 'tes', 'lais', 'les', 'sh', 'dge', 'cques', 'rgue', 'sgue']
c = ['fr']
nrm = ['g{es}/ż', 'ch{e}/sz', 'ch/sz', 't{hes}/t', 't{es}/t', 'l{ais}/l', 'l{es}/l', 'sh/sz', 'dg{e}/dż', 'cqu{es}/k', 'rgu{e}/g', 'sgu{e}/k']
Rules.append([end, c, nrm])

# Typ Signac, Mouriac, Remarque, Lebesgue, Spock, Locke, Huq, 
end = ['que', 'gue', 'cke', 'ck', 'q']
c = ['fr', 'en', 'it', 'sp']
nrm = ['qu{e}/k', 'gu{e}/k', 'ck{e}/k', 'ck/k', 'q/k']
Rules.append([end, c, nrm])





# WŁOSKI
# Typ Lorenzo
end = Aux.Product(['n'], ['z'], ['o'], [''])
c = ['it']
nrm = Aux.Product(['n'], ['z'], ['o'], ['/co'])
Rules.append([end, c, nrm])

# Typ Goya
end = Aux.Product(['a', 'e', 'u', 'o', 'i'], ['ya'], [''])
c = ['']
nrm = Aux.Product(['a', 'e', 'u', 'o', 'i'], ['ya'], ['/ja'])
Rules.append([end, c, nrm])

# Typ Freschi [freski]
end = Aux.Product(['ch'], ['i'])
c = ['it']
nrm = Aux.Product(['ch'], ['i/ki'])
Rules.append([end, c, nrm])

# Typ Domenico, Luca, Marco
end = Aux.Product(['c'], ['o', 'a', ''], ['']) + ['Dominic']
c = ['fr', 'en', 'it', 'sp', 'po']
nrm = Aux.Product(['c'], ['o/ko', 'a/ka', '/k'], [''])  + ['Dominic/k']
Rules.append([end, c, nrm])

end = ['Dominic']
c = ['']
nrm = ['Dominic/k']
Rules.append([end, c, nrm])





# JĘZYK POLSKI - EPENTEZY
# Typ Kwiecień, Wróbel, Dekiel, Szczygieł
end = ['Wróbel', 'Kwiecień', 'Dekiel', 'Hegel', 'Wedel', 'Havel', 'Mendel', 'Szczygieł', 'Paweł', 'Karel', 'Bruegel', 'Haeckel', 'Haendel', 'Vogel', 'Weigel', 'Wenzel', 'Wrangel', 'Eiffel']
c = ['']
nrm = ['Wrób[e]l', 'Kwiet^[e]ń', 'Dek![e]l', 'Heg[e]l', 'Wed[e]l', 'Hav[e]l', 'Mend[e]l', 'Szczyg![e]ł', 'Paw[e]ł', 'Kar[e]l', 'Brueg[e]l', 'Haeck[e]l', 'Haend[e]l', 'Vog[e]l', 'Weig[e]l', 'Wenz[e]l', 'Wrang[e]l', 'Eiff[e]l']
Rules.append([end, c, nrm])

# Typ Lipiec, Janiec, Pawelec
end = Aux.Product(['i', 'a', 'e', 'o', 'u', 'y'], ['b', 'p', 't', 'd', 'f', 'w', 's', 'z', 'c', 'n', 'm', 'l'], ['iec', 'ec'])
c = ['slav']
nrm = Aux.Product(['i', 'a', 'e', 'o', 'u', 'y'], ['b', 'p', 'ć', 'dź', 'f', 'w', 'ś', 'ź', 'ć', 'ń', 'm', 'l'], ['^[e]c', '[e]c'])
Rules.append([end, c, nrm])

# Typ Dudek, ~ciek (Bociek)
end = ['Dudek', 'łek', 'szek', 'ciek', 'Szuster', 'Gustek', 'Leander', 'Kranjec', 'Mniszech', 'Sewer']
c = ['']
nrm = ['Dud[e]k', 'ł[e]k', 'sz[e]k', 'ć[e]k', 'Szust[e]r', 'Gust[e]k', 'Leand[e]r', 'Kranj[e]c', 'Mnisz[e]ch', 'Sew[e]r']
Rules.append([end, c, nrm])

# Typ Arek, Goncarek, Piotrek
end = Aux.Product(['a', 'e', 'i', 'o', 'u', 'y', 'ę', 'ą', 't', 'd'], ['b', 'p', 'm', 'f', 'w', 't', 'd', 'c', 'z', 's', 'r', 'l'], ['ek'])
c = ['']
nrm = Aux.Product(['a', 'e', 'i', 'o', 'u', 'y', 'ę', 'ą', 't', 'd'], ['b', 'p', 'm', 'f', 'w', 't', 'd', 'c', 'z', 's', 'r', 'l'], ['[e]k'])
Rules.append([end, c, nrm])

# Typ Apollo, Bruno
end = Aux.Product(['Apollo', 'Bruno', 'Gwido', 'Iwo', 'Zeno', 'Cycero', 'Hugo'], [''])
c = ['']
nrm = Aux.Product(['Apollo', 'Bruno', 'Gwido', 'Iwo', 'Zeno', 'Cycero', 'Hugo'], ['[n]/n'])
Rules.append([end, c, nrm])

# Typ Anka, Baśka, Kasieńka
end = Aux.Product(['n', 'ś', 'ń', 'sz'], ['k'], ['a'])
c = ['']
nrm = Aux.Product(['n', 'ś', 'ń', 'sz'], ['[e]k'], ['a'])
Rules.append([end, c, nrm])

# Typ Marszałkówna
end = ['ówna']
c = ['']
nrm = ['ów^[e]na']
Rules.append([end, c, nrm])

# Typ Aleksander, Luter
end = ['Aleksander', 'Alexander', 'Luter', 'Holender', 'Kacper', 'Kasper', 'Koper', 'Skamander', 'Sylwester', 'Świder', 'Tyber', 'Wawer', 'Węgier', 'Wicher']
c = ['']
nrm = ['Aleksand[e]r', 'Alexand[e]r', 'Lut[e]r', 'Holend[e]r', 'Kacp[e]r', 'Kasp[e]r', 'Kop[e]r', 'Skamand[e]r', 'Sylwest[e]r', 'Świd[e]r', 'Tyb[e]r', 'Waw[e]r', 'Węg![e]r', 'Wich[e]r']
Rules.append([end, c, nrm])

# POLSKI - BRAK ALTERNACJI 
end = ['Józio', 'Rózio']
c = ['']
nrm = ['Jó!zio', 'Rózio']
Rules.append([end, c, nrm])





# JĘZYK NIEMIECKI
# Typ Leibniz, Toeplitz
end = Aux.Product(['i'], ['z', 'tz'], [''])
c = ['ge']
nrm = Aux.Product(['i'], ['z', 'tz'], ['/c'])
Rules.append([end, c, nrm])






# JĘZYKI SŁOWIAŃSKIE
# Typ Bogorodckij
end = Aux.Product(['s', 'z', 'c'], ['k'], ['oj'], [''])
c = ['']
nrm = Aux.Product(['s', 'z', 'c'], ['k'], ['oj'], ['/oj*'])
Rules.append([end, c, nrm])

# Typ Bogorodckij
end = Aux.Product(['s', 'z', 'c'], ['k'], ['ij'], [''])
c = ['']
nrm = Aux.Product(['s', 'z', 'c'], ['k'], ['ij'], ['/ij*'])
Rules.append([end, c, nrm])

# Typ Andrei, Yevgeniy, Dmitriy 
end = Aux.Product(['Andrei', 'Yevgeniy', 'Dmitriy'], [''])
c = ['']
nrm = Aux.Product(['Andrei', 'Yevgeniy', 'Dmitriy'], ['/j'])
Rules.append([end, c, nrm])

# Typ Miloš
end = Aux.Product(['š'])
c = ['']
nrm = Aux.Product(['š/sz'])
Rules.append([end, c, nrm])

# Typ Ania, Mania, Gdynia, Kcynia
end = Aux.Product(['nia'])
c = ['slav']
nrm = Aux.Product(['nia/!nia!'])
Rules.append([end, c, nrm])





# JĘZYK TURECKI
end = Aux.Product(['ş', 'ç'])
c = ['tu']
nrm = Aux.Product(['ş/sz', 'ç/cz'])
Rules.append([end, c, nrm])





# JĘZYK PORTUGALSKI
# Typ Pessanha, Cerha, Badolho
end = ['nha', 'nho', 'rha', 'rho', 'lho', 'lha']
c = ['']
nrm = ['nha/na!', 'nho/no!', 'rha/ra!', 'rho/ro!', 'lho/lo', 'lha/la']
Rules.append([end, c, nrm])

end = Aux.Product(['nço'])
c = ['']
nrm = Aux.Product(['nço/so'])
Rules.append([end, c, nrm])





# JĘZYKI GERMAŃSKIE
# Typ Lundegårdh
end = Aux.Product(['th', 'dh'])
c = ['']
nrm = Aux.Product(['th/t', 'dh/d'])
Rules.append([end, c, nrm])






