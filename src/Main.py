from Element import Element
from TableRow import TableRow
from Table import Table
from TableWriter import TableWriter

def main():
    t = Table()
    for r in range(100):
        if r == 0:
            r = TableRow(isHeader = True)
        else:
            r = TableRow()
        for e in range(10):
            e = Element()
            e.addTxt('hello')
            r.addElement(e)
        t.addRow(r)
    tw = TableWriter(t, 'out')
    tw.write()

if __name__ == '__main__':
    main()

