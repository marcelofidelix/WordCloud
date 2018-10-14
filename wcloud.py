import PyPDF2
from pathlib import Path
import os
from wordcloud import WordCloud, STOPWORDS
import matplotlib.pyplot as plt

dirpath = os.getcwd()

pathlist = Path(dirpath).glob('**/*.pdf')
for path in pathlist:
    #path não é uma string!
    path_in_str = str(path)
    print(path_in_str)
    pdfFileObj = open(path_in_str, 'rb')
    pdfReader = PyPDF2.PdfFileReader(pdfFileObj)

    texto = ''

    for i in range(pdfReader.numPages):
        pageObj = pdfReader.getPage(i)
        texto += pageObj.extractText()
    
    wordcloud = WordCloud(stopwords=STOPWORDS,
                              background_color='white', 
                          max_words=300,
                          width=2100, height=1200
                             ).generate(texto)
    plt.figure(figsize=(40,20))
    plt.clf()
    plt.imshow(wordcloud)
    plt.axis('off')
    plt.show()