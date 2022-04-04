
import linecache
def update(filename, lineno, column, text):
    fro = open(filename, "r")
    print(linecache.getline(filename,lineno))

    current_line = 0
    while current_line < lineno - 1:
        fro.readline()
        current_line += 1

    seekpoint = fro.tell()
    frw = open(filename, "r+")
    frw.seek(seekpoint, 0)
  # read the line we want to update
    line = fro.readline()
    # column =   column if column > 0 else 1
    # chars = line[0: column-1] + text + line[column-1:]
    words = line.split(" ")
    words.insert(column,  text)
    chars = ' '.join(words)
    # print(line[0: column])
    print(words)
    print(chars)
    while chars:
        frw.writelines(chars)
        chars = fro.readline()

    fro.close()
    frw.truncate()
    frw.close()

if __name__ == "__main__":
    # strr = ['ENT']
    # strr.append('PRESENT')

    # strr = '[' + (', '.join(strr)) + ']'
    # print(strr)
    fro = open("ast/record-13.ast", "r")
    print(linecache.getline("ast/record-13.ast",27))
    # update("txt/record-13-test.txt", 115, 3, strr)