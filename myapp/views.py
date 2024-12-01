
from django.shortcuts import redirect, render
from .pdf import GeneratePDF
import json
from django.views import View
# Create your views here.
from .models import PdfFile
from django.contrib import messages
class PDFView(View):
    def get_items(self, items):
        items_dict = json.loads(items)
        if items_dict[0][1]:
            return json.loads(items)
        return None

    def post(self, request, *args, **kwargs): 
        items = self.get_items(request.POST['items'])
        if not items:
            messages.warning(request, 'Please enter first description and quantity!')
            return redirect('/')
        name=request.POST['name']
        modelno=request.POST['model']
        plate=request.POST['plate']
        mobile=request.POST['mobile']
        iqama =request.POST['iqama']
        cfile = PdfFile.objects.create()
        pdf_gen = GeneratePDF(cfile, request.build_absolute_uri()[:-1])
        pdf_gen.generate(items, name,iqama, mobile, modelno,plate)
        messages.success(request, 'Challan generated successfully!')
        return redirect('/')
    
    def get(self, request):
        context = {
            'files':PdfFile.objects.order_by('-uploading_date')[:5],
        }
        return render(request,'home.html',context)

