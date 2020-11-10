import PySimpleGUI as pg

layout = [
          [pg.Text('Scraping from wikipedia')],
          [pg.Text('Paste the URL'), pg.InputText()],
          [pg.Button('OK')]
          ]
window = pg.Window('Scrap Data').Layout(layout)

button, values = window.Read()

if button == 'OK':
    print(values)
    from urllib.request import urlopen
    from bs4 import BeautifulSoup
    import re
    import sys

    url = values[0]
    try:

        html = urlopen(url)
    except:
        print(sys.exit('Url Not Correct'))
    html2 = html.read()
    soup = BeautifulSoup(html2, 'lxml')
    fr = soup.title
    print(fr)
    gr = soup.find(class_="infobox")
    head = []
    cont = []
    for hu in gr:
        co = hu.find_all('th')
        for df in co:
            head.append(df.text)
        fr = hu.find_all('td')
        for vc in fr:
            cont.append(vc.text)
    a=zip(head,cont)
    print(a)
    for c,b in a:
        print(c+":"+b)

print('Hi')






