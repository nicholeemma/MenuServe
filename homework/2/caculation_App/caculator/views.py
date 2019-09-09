from django.shortcuts import render
from django.http import HttpResponse
import datetime
# first_number=null
# second_number=null
# character=null

content = {}
content['first_operator'] = ''
content['second_operator'] = ''
content['error'] = ''
content['first_number'] = '0'
content['second_number'] = ''
    
# Create your views here.
def caculate(request):
    '''
    content: a dictionary of information post back to the client side
    ['first_operator'] stores the number
    ['second_operator']
    ['first_number']
    ['second_number']
    '''
    content = {}
    content['first_operator'] = ''
    content['second_operator'] = ''
    content['error'] = ''
    content['first_number'] = '0'
    content['second_number'] = ''
    
    content['show'] = '0'
    if True:
        if "number" in request.POST:
            if request.POST.get('first_number')=='0' and request.POST.get('second_number') =='' and request.POST.get('first_operator') == '' and request.POST.get('second_operator') == '':
                content['first_number'] = request.POST.get('number')
                content['show'] = request.POST.get('number')
            elif request.POST.get('first_number')!='0' and request.POST.get('second_number') =='' and request.POST.get('first_operator') == '' and request.POST.get('second_operator') == '':
                content['first_number'] = str(request.POST.get('first_number'))+str(request.POST.get('number'))
                content['show'] = str(request.POST.get('first_number'))+str(request.POST.get('number'))
            elif request.POST.get('first_number')!='0' and request.POST.get('second_number') =='' and request.POST.get('first_operator') != '' and request.POST.get('second_operator') == '':
            
                content['second_number'] = request.POST.get('number')
                content['show'] = request.POST.get('number')
            elif request.POST.get('first_number')!='0' and request.POST.get('second_number') !='' and request.POST.get('first_operator') != '' and request.POST.get('second_operator') == '':
                content['second_number'] = str(request.POST.get('second_number'))+str(request.POST.get('number'))
                
                content['show'] = str(request.POST.get('second_number'))+str(request.POST.get('number'))
            
        elif "operator" in request.POST:
            if request.POST.get('first_number')=='0' and request.POST.get('second_number') =='' and request.POST.get('first_operator') == '' and request.POST.get('second_operator') == '':
                content['first_operator'] = request.POST.get('operator')
                content['show']=request.POST.get('first_number')
            elif request.POST.get('first_number')!='0' and request.POST.get('second_number') =='' and request.POST.get('first_operator') == '' and request.POST.get('second_operator') == '':
            
                content['first_operator'] = request.POST.get('operator')
                content['first_number'] = request.POST.get('first_number')
                content['show']=request.POST.get('first_number')
            elif request.POST.get('first_number')!='0' and request.POST.get('second_number') =='' and request.POST.get('first_operator') != '' and request.POST.get('second_operator') == '':
            
                content['first_operator'] = request.POST.get('operator')
                content['first_number'] = request.POST.get('first_number')
                content['show']=request.POST.get('first_number')
            elif request.POST.get('first_number')!='0' and request.POST.get('second_number') !='' and request.POST.get('first_operator') != '' and request.POST.get('second_operator') == '':
                content['first_operator'] = request.POST.get('first_operator')
                content['first_number'] = request.POST.get('first_number')
                content['second_operator'] = request.POST.get('operator')
                if request.POST.get('operator')!='=':
                    if request.POST.get('first_operator').strip('\u200b') =='+': 
                        content['show']=str(request.POST.get('first_number')+request.POST.get('second_operator'))
                        content['first_number']=request.POST.get('first_number')+request.POST.get('second_operator')
                        content['first_operator'] = request.POST.get('operator')
                        content['second_operator'] = ''
                        content['second_number'] = ''
                    elif request.POST.get('first_operator').strip('\u200b') =='-':
                        content['show']=str(request.POST.get('first_number')-request.POST.get('second_operator'))
                        content['first_number']=request.POST.get('first_number')-request.POST.get('second_operator')
                        content['second_operator'] = ''
                        content['second_number'] = ''
                    elif request.POST.get('first_operator').strip('\u200b') =='*':
                        content['show']=str(request.POST.get('first_number')*request.POST.get('second_operator'))
                        content['first_number']=request.POST.get('first_number')*request.POST.get('second_operator')
                        content['second_operator'] = ''
                        content['second_number'] = ''
                    elif request.POST.get('first_operator').strip('\u200b') =='÷':
                        content['show']=str((int)(request.POST.get('first_number')/request.POST.get('second_operator')))
                        content['first_number']=(int)(request.POST.get('first_number')/request.POST.get('second_operator'))
                        content['second_operator'] = ''
                        content['second_number'] = ''
                else:
                    if request.POST.get('first_operator').strip('\u200b') =='+': 
                        
                        content['show']=request.POST.get('first_number')+request.POST.get('second_operator')
                    elif request.POST.get('first_operator').strip('\u200b') =='-':
                       
                        content['show']=request.POST.get('first_number')-request.POST.get('second_operator')
                    elif request.POST.get('first_operator').strip('\u200b') =='*':
                        
                        content['show']=request.POST.get('first_number')*request.POST.get('second_operator')
                    elif request.POST.get('first_operator').strip('\u200b') =='÷':
                        
                        content['show']=(int)(request.POST.get('first_number')+request.POST.get('second_operator'))

                # clear        
                    content['first_operator'] = ''
                    content['second_operator'] = ''
                
                    content['first_number'] = '0'
                    content['second_number'] = ''
            
    return render(request, "index.html", content)

# According the eighth requirement in the Additional Requirement, 
# users may send randome request, 
# that is why a validation needs to be implemented


def isValid(request):
    number_list = ['1','2','3','4','5','6','7','8','9','0']
    operator_list = ['+','-','*','÷']
    if ((not 'number' in request.POST) and (not 'operator' in request.POST)):
        return False
    if 'number' in request.POST and not request.POST.get('number') in number_list:
        return False
    if 'operator' in request.POST:
        if not request.POST.get('operator').strip('\u200b') in operator_list:
            return False



        

