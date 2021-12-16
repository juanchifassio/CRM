from django.shortcuts import render, redirect

from Leads.models import Lead, Agent, User

def Home_Page(request):
    leads=Lead.objects.all()
    agents=Agent.objects.all()

    if not request.user.is_authenticated:
        return redirect('login')
    else:
        nr_leads=leads.count()
        nr_agents=agents.count()
        nr_assigned=leads.filter(agent__isnull=False).count()
        nr_unassigned=leads.filter(agent__isnull=True).count()
        nr_open=leads.filter(status='Open').count()
        nr_working=leads.filter(status='Working').count()
        nr_customers=leads.filter(status='Customer').count()
        nr_nurture=leads.filter(status='Nurture').count()
        nr_inactive=leads.filter(status='Inactive').count()
    


        data={  'nr_leads':nr_leads,
        'nr_agents':nr_agents,
        'nr_assigned':nr_assigned,
        'nr_unassigned':nr_unassigned,
        'nr_open':nr_open,
        'nr_working':nr_working,
        'nr_customers':nr_customers,
        'nr_nurture':nr_nurture,
        'nr_inactive': nr_inactive,
        }


    return render(request, 'CRM_Main/home.html', data)

def Landing_Page(request):
    if not request.user.is_authenticated:
        return redirect('login')
    else:
        return redirect('home')


def handler404(request, exception):
    return render(request,'CRM_Main/404.html')


def handler500(request, exception):
    return render(request,'CRM_Main/500.html')


