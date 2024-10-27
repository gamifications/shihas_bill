
from django.shortcuts import redirect, render
from .pdf import GeneratePDF
import json
from django.views import View
# Create your views here.
from .models import PdfFile

class PDFView(View):

    def post(self, request, *args, **kwargs): 
        items = json.loads(request.POST['items'])
        mobile=request.POST['mobile']
        iqama =request.POST['iqama']
        cfile = PdfFile.objects.create()
        pdf_gen = GeneratePDF(cfile, request.build_absolute_uri()[:-1])
        pdf_gen.generate(items, mobile, iqama)
        # messages.success(request, 'Challan generated successfully!')
        return redirect('/')
    
    def get(self, request):
        context = {
            'files':PdfFile.objects.order_by('-uploading_date')[:5],
        }
        return render(request,'home.html',context)

