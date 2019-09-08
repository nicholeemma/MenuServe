from django.shortcuts import render

first_number=null
second_number=null
character=null


    
# Create your views here.
def caculate(request):
    content = {}
    content['show'] = '0'
    # content['first_operator'] = ''
    # content['second_operator'] = ''
	# content['current_status'] = 'idle'
	# content['first_number'] = '0'
    # content['second_number'] = null
    if (isValid(request)):

    
# The GET information is a dictionary
        if "number" in request.GET:
            if content['show'] == request.GET.number:
            #     content['first_number']=1
            # if content['first_number'] != '0' and content['operator'] == '':
            #     content['first_number']=str(10*content['first_number']+1)
            # if content['operator'] != '' and content['second_number'] == null:
            #     content['second_number']=1
            # if content['operator'] != '' and content['second_number'] != null:
            #     content['second_number']=str(10*content['second_number']+1)

    
    return render(request, 'index.html', content)

# According the eighth requirement in the Additional Requirement, 
# users may send randome request, 
# that is why a validation needs to be implemented
def isValid(request):
    number_list = ['1','2','3','4','5','6','7','8','9','0']
    operator_list = ['+','-','*','÷']
    if ((not 'number' in request.GET) and (not 'operator' in request.GET)):
		return False
    if 'number' in request.GET and not request.GET.get('number') in number_list:
		return False
	if 'operator' in request.GET:
		if not request.GET.get('operator').strip('\u200b') in operator_list:
			return False



        

