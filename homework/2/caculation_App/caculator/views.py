from django.shortcuts import render
from django.http import HttpResponse
import datetime
# first_number=null
# second_number=null
# character=null


    
# Create your views here.
def caculate(request):


    content = {}
    content['show'] = '0'
    if "number" in request.POST:
        content['show'] = request.POST.get('number')
        #request.GET.get('textbox') = request.GET.get('number')
    # content['first_operator'] = ''
    # content['second_operator'] = ''
	# content['current_status'] = 'idle'
	# content['first_number'] = '0'
    # content['second_number'] = null
    if (isValid(request)):
        
        print('valid')

    
# The GET information is a dictionary
        # if "number" in request.GET:
        #     content['show'] == request.GET.number
        #     request.GET.textbox = request.GET.number
            #     content['first_number']=1
            # if content['first_number'] != '0' and content['operator'] == '':
            #     content['first_number']=str(10*content['first_number']+1)
            # if content['operator'] != '' and content['second_number'] == null:
            #     content['second_number']=1
            # if content['operator'] != '' and content['second_number'] != null:
            #     content['second_number']=str(10*content['second_number']+1)
            # print(context['current_status'])

    return render(request, "index.html", content)

# According the eighth requirement in the Additional Requirement, 
# users may send randome request, 
# that is why a validation needs to be implemented


def isValid(request):
    number_list = ['1','2','3','4','5','6','7','8','9','0']
    operator_list = ['+','-','*','÷']
    if ((not 'number' in request.POST) and (not 'operator' in request.POST)):
        return False
    if 'number' in request.POST and not request.GET.get('number') in number_list:
        return False
    if 'operator' in request.POST:
        if not request.POST.get('operator').strip('\u200b') in operator_list:
            return False



        

