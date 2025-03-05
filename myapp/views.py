
from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.conf import settings
from openai import OpenAI
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


def github_models_api(heading):
    text = f"""Create an offering description for local exchange trading system 
        where I can offer activity or things like {heading}"""
    client = OpenAI(
        base_url="https://models.inference.ai.azure.com",
        api_key=settings.GITHUB_TOKEN,
    )
    system_msg = "You are a helpful assistant."
    response = client.chat.completions.create(
        messages=[
            {"role": "system", "content": system_msg},
            {"role": "user", "content": text},
        ],
        model="gpt-4o",
        temperature=1.0,
        max_tokens=1000,
        top_p=1.0,
    )
    return response.choices[0].message.content



def ajax_views(request, purpose):
    resp = ""
    if purpose == "stackcoinai":
        # ajax/ai/?details=
        resp = github_models_api(request.GET.get("details"))
    return HttpResponse(resp)