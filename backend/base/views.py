from django.shortcuts import render,redirect
from django.views import View
from .models import EMP
from .forms import EmpForm
from django.http import HttpResponseRedirect
from django.contrib.auth.views import LoginView 
from .forms import FeedbackForm



class Home(View):
    def get(self,request):
        return render(request,'home.html',{})
    
class ListEMP(View):
    def get(self, request):
        emps = EMP.objects.all()
        return render(request, 'listEmp.html', {'emps': emps})

name = 'list_emp'

class EMPDetails(View):
    def get(self, request, idEMP):
        emp = EMP.objects.get(id=idEMP)
        return render(request, 'empDetail.html', {'emp': emp})
    
class EmpCreate(View):
    def get(self,request):
        form=EmpForm()
        return render(request,'newEMP.html',{'form':form})
    
    def post(self,request):
        form=EmpForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/emp/')
        return render(request,'newEMP.html',{'form':form})
    

    
class updateEmp(View):
    def get(self,request,idEMP):
        emp=EMP.objects.get(id=idEMP)
        form=EmpForm(instance=emp)
        return render(request, 'editEMP.html', {'form': form})

    def post(self,request,idEMP):
          emp=EMP.objects.get(id=idEMP)
          form=EmpForm(request.POST,instance=emp)
          if form.is_valid():
                 form.save()
                 return HttpResponseRedirect('/emp/')
              
          return render(request, 'editEMP.html', {'form': form})


class deleteEmp (View) :
      def get(self,request,idEMP):
          emp=EMP.objects.get(id=idEMP)
          emp.delete()
          return HttpResponseRedirect('/emp/')
      
class CustomLoginView(LoginView):
    template_name = 'login.html'
    success_url = '/' # the URL to redirect to upon successful login




class FindEMP(View):
    def get(self, request, idEMP):
        try:
            employee = EMP.objects.get(id=idEMP)
        except EMP.DoesNotExist:
            employee = None

        context = {'employee': employee}
        return render(request, 'Search.html', context)

class SearchEMP(View):
    def get(self, request):
        return render(request, 'Search.html')

    def post(self, request):
        idEMP = request.POST.get('idEMP')
        return redirect('search_results', idEMP=idEMP)

class FeedbackEMP(View):
    def get(self, request):
        form = FeedbackForm()
        return render(request, 'feedback.html', {'form': form})
    
    def post(self, request):
        form = FeedbackForm(request.POST)
        if form.is_valid():
            # traitez les données du formulaire ici
            email= form.cleaned_data['email']
            name = form.cleaned_data['name']
            feedback = form.cleaned_data['feedback']
            # enregistrer le feedback dans la base de données
            return render(request, 'feedbackSuccess.html')
        else:
            return render(request, 'feedback.html', {'form': form})
        


