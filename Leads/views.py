from django.shortcuts import get_object_or_404, render, redirect
from .forms import new_lead_Form, new_agent_Form, lead_update_Form, agent_update_Form
from django.contrib import messages
from .models import Lead, Agent


def leads(request):
    data=Lead.objects.all()
    leads={"leads":data}
    
    return render(request, 'Leads/leads.html', leads)


def leads_detail(request, pk):
    lead= get_object_or_404(Lead,id=pk)
    if lead.agent:
        agent=Agent.objects.get(email=lead.agent)
        lead={'lead':lead,
            'agent':agent
        }
    else:
        lead={'lead':lead}

    return render(request, 'Leads/lead_detail.html', lead)


def leads_edit(request, pk):
    object= get_object_or_404(Lead,id=pk)
    lead=Lead.objects.get(id=pk)
    if request.method == 'POST':
        form= lead_update_Form(request.POST,instance=object)
        if form.is_valid():
            form.save()
            messages.success(request,f'Lead updated')
            return redirect('leads')
    else:
        form=lead_update_Form(instance=object)

    lead={'lead':lead,
        'form':form}    
    

    return render(request, 'Leads/lead_edit.html', lead)


def create_lead(request):
    if request.method == 'POST':
        form=new_lead_Form(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, f'Lead was successfully created')
            return redirect('Home_Page')
    else:
        form=new_lead_Form()

    return render(request, 'Leads/create_lead.html', {"form":form})



def agents(request):
    data=Agent.objects.all()
    agents={"agents":data}

    return render(request, 'Leads/agents.html', agents)


def agents_detail(request, pk):
    agent= get_object_or_404(Agent, id=pk)
    leads= Lead.objects.filter(agent=agent)
    nr_of_leads=leads.count()


    agent={'agent':agent,
        'leads':leads,
        'nr_of_leads':nr_of_leads,
        }
    return render(request, 'Leads/agent_detail.html', agent)


def agents_edit(request, pk):
    object= get_object_or_404(Agent,id=pk)
    agent= Agent.objects.get(id=pk)
    if request.method == 'POST':
        form= agent_update_Form(request.POST, request.FILES, instance=object)
        if form.is_valid():
            form.save()
            messages.success(request,f'Agent updated')
            return redirect('agents')
    else:
        form=agent_update_Form(instance=object)

    agent={'agent':agent,
        'form':form}    
    
    return render(request, 'Leads/agent_edit.html', agent)


def create_agent(request):
    if request.method == 'POST':
        form=new_agent_Form(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, f'Agent was successfully created')
            return redirect('Home_Page')
    else:
        form=new_agent_Form()

    return render(request, 'Leads/create_agent.html', {"form":form})