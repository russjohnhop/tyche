from django.shortcuts import render
from django.views import View
from . forms import InvestmentForm

# Create your views here.

def about(request):
    return render(request, "core/about.html")

def budgeting(request):
    return render(request, "core/budgeting.html")

def credit_cards(request):
    return render(request, "core/credit-cards.html")

def compound_calculator(request):
    if request.method == "GET" :
        form = InvestmentForm()
        return render(request, "core/compound-calculator.html", {
            "form" : form
        })
    
    if request.method == "POST" :
        form = InvestmentForm(request.POST)

        if form.is_valid():
            total_result = form.cleaned_data['starting_amount']
            total_interest = 0
            yearly_results = {}

            for i in range(1, int(form.cleaned_data['number_of_years'] + 1)):
                yearly_results[i] = {}
                interest = total_result * (form.cleaned_data['return_rate'] / 100)
                total_result += interest
                total_interest += interest

                total_result += form.cleaned_data['annual_additional_contribution']

                yearly_results[i]['interest'] = round(total_interest, 2)
                yearly_results[i]['total'] = round(total_result, 2)

                context = {
                    'total_result': round(total_result, 2),
                    'yearly_results' : yearly_results,
                    'number_of_years' : int(form.cleaned_data['number_of_years'])
                }
            
            return render(request, "core/result.html", context)


def emergency_fund(request):
    return render(request, "core/emergency-fund.html")

def mortgages(request):
    return render(request, "core/mortgages.html")

def pensions(request):
    return render(request, "core/pensions.html")