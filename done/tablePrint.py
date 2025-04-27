
tableData = [['apples', 'oranges', 'cherries', 'banana'], 
            ['Alice', 'Bob', 'Carol', 'David'], 
            ['dogs', 'cats', 'moose', 'goose']]


def printTable(listen: list) -> str:
    spalte_weite = []
    output = ""
    for liste in listen:
        spalte_weite.append(max([len(element) for element in liste]) + 1)
        
    for spalten_index in enumerate(listen[0]):
        for reihen_index in enumerate(listen):
            output =output +  '{}'.format(listen[reihen_index[0]][spalten_index[0]].rjust(spalte_weite[reihen_index[0]]))  
        output = output + '\n'
    return output


print(printTable(tableData))