

tableData = [['apples', 'oranges', 'cherries', 'banana'],
 ['Alice', 'Bob', 'Carol', 'David'],
 ['dogs', 'cats', 'moose', 'goose']]

def printTable(data: list[list[str]]) -> str:
    new_row = []
    column_widths = []
    output= ""
    for col in data:
        column_widths.append(max([len(element) for element in col]) +1 )

    for col in enumerate(data[0]):
        for row in enumerate(data):
            output += '{}'.format(data[row[0]][col[0]].rjust(column_widths[row[0]]))
        output = output + "\n"

    return output

print(printTable(tableData))