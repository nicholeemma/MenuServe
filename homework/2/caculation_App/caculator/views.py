from django.shortcuts import render
from django.http import HttpResponse


    
# Create your views here.
def caculate(request):
    '''
    content: a dictionary of information post back to the client side
    ['first_operator']: stores the first operator
    ['second_operator']: check whether second operater exists or not, calculation shoud occur
    ['first_number']: store the first number
    ['second_number']: store the second number
    content should be updated every POST

    request.POST.get : get the specific value of a key in content dictionary
    
    '''
    content = {}
    content['first_operator'] = ''
    content['second_operator'] = ''
    content['first_number'] = '0'
    content['second_number'] = ''
    # The result/ number show in the display section of calculator
    content['show'] = '0'
    if isValid(request):
        if "number" in request.POST:
            if request.POST.get('first_number')=='0' and request.POST.get('second_number') =='' and request.POST.get('first_operator') == '' and request.POST.get('second_operator') == '':
                content['first_number'] = request.POST.get('number')
                content['show'] = request.POST.get('number')
            elif request.POST.get('first_number')!='0' and request.POST.get('second_number') =='' and request.POST.get('first_operator') == '' and request.POST.get('second_operator') == '':
                content['first_number'] = str(request.POST.get('first_number'))+str(request.POST.get('number'))
                content['show'] = str(request.POST.get('first_number'))+str(request.POST.get('number'))
            elif request.POST.get('first_number')!='0' and request.POST.get('second_number') =='' and request.POST.get('first_operator') != '' and request.POST.get('second_operator') == '':
                content['first_number'] = request.POST.get('first_number')
                content['first_operator'] = request.POST.get('first_operator')
                content['second_number'] = request.POST.get('number')
                content['show'] = request.POST.get('number')
            elif request.POST.get('first_number')!='0' and request.POST.get('second_number') !='' and request.POST.get('first_operator') != '' and request.POST.get('second_operator') == '':
                content['second_number'] = str(request.POST.get('second_number'))+str(request.POST.get('number'))
                content['first_number'] = request.POST.get('first_number')
                content['first_operator'] = request.POST.get('first_operator')
                content['show'] = str(request.POST.get('second_number'))+str(request.POST.get('number'))
            
        elif "operator" in request.POST:
            if request.POST.get('first_number')=='0' and request.POST.get('second_number') =='' and request.POST.get('first_operator') == '' and request.POST.get('second_operator') == '':
                content['first_operator'] = request.POST.get('operator')
                content['show']=request.POST.get('first_number')
            elif request.POST.get('first_number')!='0' and request.POST.get('second_number') =='' and request.POST.get('first_operator') == '' and request.POST.get('second_operator') == '':
                if request.POST.get('operator').strip('\u200b')=='=':
                    content['first_number'] = request.POST.get('first_number')
                    content['show']=request.POST.get('first_number')
                else:
                    content['first_operator'] = request.POST.get('operator')
                    content['first_number'] = request.POST.get('first_number')
                    content['show']=request.POST.get('first_number')
            elif request.POST.get('first_number')!='0' and request.POST.get('second_number') =='' and request.POST.get('first_operator') != '' and request.POST.get('second_operator') == '':
                if request.POST.get('operator').strip('\u200b')=='=':
                    content['first_number'] = request.POST.get('first_number')
                    content['show']=request.POST.get('first_number')
                else:
                    content['first_operator'] = request.POST.get('operator')
                    content['first_number'] = request.POST.get('first_number')
                    content['show']=request.POST.get('first_number')
            elif request.POST.get('first_number')!='0' and request.POST.get('second_number') !='' and request.POST.get('first_operator') != '' and request.POST.get('second_operator') == '':
                content['first_operator'] = request.POST.get('first_operator')
                content['first_number'] = request.POST.get('first_number')
                content['second_number'] = request.POST.get('second_number')
                content['second_operator'] = request.POST.get('operator')
                if request.POST.get('operator').strip('\u200b')!='=':
                    if request.POST.get('first_operator').strip('\u200b') =='+': 
                        content['show']=str(int(request.POST.get('first_number'))+int(request.POST.get('second_number')))
                        content['first_number']=str(int(request.POST.get('first_number'))+int(request.POST.get('second_number')))
                        content['first_operator'] = request.POST.get('operator')
                        content['second_operator'] = ''
                        content['second_number'] = ''
                    elif request.POST.get('first_operator').strip('\u200b') =='−':
                        content['show']=str(int(request.POST.get('first_number'))-int(request.POST.get('second_number')))
                        content['first_number']=str(int(request.POST.get('first_number'))-int(request.POST.get('second_number')))
                        content['first_operator'] = request.POST.get('operator')
                        content['second_operator'] = ''
                        content['second_number'] = ''
                    elif request.POST.get('first_operator').strip('\u200b') =='×':
                        content['show']=str(int(request.POST.get('first_number'))*int(request.POST.get('second_number')))
                        content['first_number']=str(int(request.POST.get('first_number'))*int(request.POST.get('second_number')))
                        content['first_operator'] = request.POST.get('operator')
                        content['second_operator'] = ''
                        content['second_number'] = ''
                    elif request.POST.get('first_operator').strip('\u200b') =='÷':
                        content['show']=str((int)(int(request.POST.get('first_number'))/int(request.POST.get('second_number'))))
                        content['first_number']=str((int)(int(request.POST.get('first_number'))/int(request.POST.get('second_number'))))
                        content['first_operator'] = request.POST.get('operator')
                        content['second_operator'] = ''
                        content['second_number'] = ''
                else:
                    if request.POST.get('first_operator').strip('\u200b') =='+': 
                        
                        content['show']=str(int(request.POST.get('first_number'))+int(request.POST.get('second_number')))
                    elif request.POST.get('first_operator').strip('\u200b') =='−':
                       
                        content['show']=str(int(request.POST.get('first_number'))-int(request.POST.get('second_number')))
                    elif request.POST.get('first_operator').strip('\u200b') =='×':
                        
                        content['show']=str(int(request.POST.get('first_number'))*int(request.POST.get('second_number')))
                    elif request.POST.get('first_operator').strip('\u200b') =='÷':
                        
                        content['show']=str((int)(int(request.POST.get('first_number'))/int(request.POST.get('second_number'))))

                # clear        
                    content['first_operator'] = ''
                    content['second_operator'] = ''
                
                    content['first_number'] = '0'
                    content['second_number'] = ''
    else:
        content['show']='error'
            
    return render(request, "index.html", content)

# According the eighth requirement in the Additional Requirement, 
# users may send randome request, 
# that is why a validation needs to be implemented


def isValid(request):
    number_list = ['1','2','3','4','5','6','7','8','9','0']
    operator_list = ['+','−','×','÷']
    if request.POST=="":
        return True
    if ((not 'number' in request.POST) and (not 'operator' in request.POST)):
        return False
    if 'number' in request.POST and not request.POST.get('number') in number_list:
        return False
    if 'operator' in request.POST:
        if not request.POST.get('operator').strip('\u200b') in operator_list:
            return False
    
    return True



        

