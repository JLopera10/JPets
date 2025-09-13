from django.shortcuts import render
from django.views.generic import TemplateView
from .models import Producto

class ProductPageView(TemplateView):
    template_name='index.html'
    
    def get(self, request):
        viewData = {}
        viewData["title"] = "Products - Jpets"
        viewData["subtitle"] = "List of products"
        viewData["products"] = Producto.objects.all()

        return render(request, self.template_name, viewData)    
