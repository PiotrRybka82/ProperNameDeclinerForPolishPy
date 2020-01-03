def LoadData(path, delimiter=';', encoding='utf-8'):
    with open(file=path, encoding=encoding) as fin:
        res = []       
        line = ''
        while True:
            line = fin.readline().strip()
            if not line:
                break
            
            res.append(line.replace('"', '').split(delimiter))
    return res

def SafeData(path, data, append=False, delimiter=";", encoding='utf-8'):
    with open(file=path, mode='a' if append else 'w', encoding=encoding) as fout:
        
        for i in range(len(data)):
            input_line = ''
            for j in range(len(data[i])):
                if j == len(data[i]) - 1: 
                    input_line = input_line + data[i][j] + '\n'
                else:
                    input_line = input_line + data[i][j] + delimiter
            fout.write(input_line)

            
