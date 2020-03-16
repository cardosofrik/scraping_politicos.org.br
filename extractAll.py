import requests
import re
from reportlab.pdfgen import canvas

class Info:

    def connector(self,i):
        user_agent = {'User-agent': 'Mozilla/5.0'}
        url = requests.get(i, headers=user_agent)
        print("[ 1 ] - Starting")

        def filter():
            info = [ ]

            details={"name":'<h3 class="labelCandidate" id="NameParlamentar">(.*?)</h3>',
                     "candidate":'<h5 class="labelCandidate" id="PositionParlamentar">(.*?)</h5>',
                     "broken":'<h5 class="labelCandidate" id="PrefixParlamentar">(.*?)</h5>',
                     }
            for i in details:
                rex = re.compile(details[i])
                results= ",".join(rex.findall(url.text))
                print(i,"  ", results)
                info = info +[results]


            def creadPDF():
                nome_pdf = "{}.pdf".format(info[1])
                pdf = canvas.Canvas(str(nome_pdf).format(" ",''))
                info.sort()
                pdf.drawString(247, 720, info[0])
                pdf.drawString(247, 700, info[1])
                pdf.drawString(247, 681, info[2])
                pdf.setTitle(nome_pdf)
                pdf.setFont("Helvetica-Oblique", 14)
                pdf.drawString(245, 750, 'https://www.politicos.org.br/')
                pdf.setFont("Helvetica-Bold", 12)
                pdf.save()
                print("[ 2 ] - PDF created")
            creadPDF()
        filter()

if __name__ == '__main__':
    person= "????name???"
    Info().connector("https://www.politicos.org.br/"+person)
