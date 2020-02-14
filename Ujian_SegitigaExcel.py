# Soal 2

import xlsxwriter
book = xlsxwriter.Workbook('soal2.xlsx')
sheet = book.add_worksheet('Sheet1')
polaKata = [0, 1, 3, 6, 10, 15, 21, 28, 36]
dataTulis = []

def segitigaKata2(x):
    zero = ''
    kata = x.replace(' ', '')
    pjgkata = len(kata)
    if pjgkata in polaKata:
        row1 = polaKata.index(pjgkata)
        i = 0
        for row in range(row1):
            baris = 0
            kolom = 0
            for col in range(row+1):
                zero += kata[i] + ' '
                i+=1
                sheet.write(baris, kolom, zero)
            baris +=1
            kolom +=1
            zero += '\n'
        book.close()
    else:
        return 'Mohon maaf, jumlah karakter tidak memenuhi syarat membentuk pola'

segitigaKata2('Purwadhika')
segitigaKata2('Purwadhika Startup and Coding School @BSD')
segitigaKata2('lintang')
segitigaKata2('kode')
segitigaKata2('kodeasdfgjklpoi345781')