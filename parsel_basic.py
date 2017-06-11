import webbrowser
import os

def show(selector_list, htmlsample):
    x = selector_list.extract()
    x = [i.rstrip().lstrip() for i in x]
    x = [i for i in x if i != '']
    y = ['<div style="background-color: yellow; font-weight:bold;">' + i + '</div>' for i in x]

    for i, j in zip(x, y):
        htmlsample = htmlsample.replace(i, j)

    newpath = os.path.realpath('./modified.html')
    
    with open(newpath, 'w') as f:
        f.write(htmlsample)
    
    webbrowser.open('file://' + newpath)
