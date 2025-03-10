from weasyprint import HTML
from django.template.loader import render_to_string
from django.conf import settings

from django.core.files import File

class GeneratePDF:
    def __init__(self, cfile,url):
        self.url = url 
        self.cfile = cfile

    def generate(self,items, name, iqama, mobile, modelno, plate):
        print(items)
        context = {
            'totalqty': sum([i[2] for i in items if i[2]]),
            'file': self.cfile,            
            'url':  self.url, # strip last /
            'items': items, 
            'name':name,
            'modelno':modelno,
            'plate':plate,
            'mobile': mobile,
            'iqama': iqama,
            'date': self.cfile.uploading_date, # timezone.now(),
        }
        
        html = HTML(string=render_to_string('pdf/index.html', context))
        html.write_pdf(f'{settings.MEDIA_ROOT}/output/challan.pdf')

        self.cfile.billfile.save(f'{self.cfile.id}.pdf', File(open(f'{settings.MEDIA_ROOT}/output/challan.pdf','rb')))
