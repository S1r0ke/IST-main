with open("subcode/normy_database.txt", "r+", encoding="utf8") as f:
    normy = str(f.read())

def create_list(inp):
    def norm_list(str):
        str = str.split("ČSN")
        final = []
        for var in str:
            var = "ČSN" + var
            final.append(var)
        return final
    normy = norm_list(inp)
    final = []
    for norm in normy:
        hl = (norm.split("\n"))[0]
        čsn =  "\n" + ((norm[norm.find('(')+1:norm.find(')')]).replace("(", "")).replace(")", "")
        name = ((norm.split("Vydána:"))[0]).split("\n")
        vydána = (norm[norm.find('Vydána: ')+1:norm.find('\nCena: ')]).replace("ydána: ", "Vydána: ")
        name = "\n" + "\n".join(name)
        sub_final = [hl, čsn, name, vydána]
        final.append(sub_final)
    del final[0]
    return final


def find_num(num):
    list = create_list(normy)
    output = []
    for norm in list:
        if norm[1] == "\n" + num:
            output.append(norm)
        else:
            pass
    return output


def norm_print(n_list):
    output = ""
    for n in n_list:
        n.pop(0)
        n.pop(0)
        for name in n:
            output = output + name
        output = output + "\n"
    return output
