from django.shortcuts import render

first_number=null
second_number=null
character=null

def update(i):
    if i.isdigit() and first_number==null and character==null:
        first_number=i
    if i.isdigit() and first_number!=null and character==null:
        first_number=first_number*10+i
    if character!=null and second_number==null:
        second_number=i
    
# Create your views here.
def caculate(request):
    content = {}
    content['show'] = '0'
	content['first_operator'] = ''
    content['second_operator'] = ''
	content['current_status'] = 'idle'
	content['first_number'] = '0'
    content['second_number'] = null
    
    if request.method == "POST":
        if "button1" in request.POST:
            if content['first_number'] == '0':
                content['first_number']=1
            if content['first_number'] != '0' and content['operator'] == '':
                content['first_number']=str(10*content['first_number']+1)
            if content['operator'] != '' and content['second_number'] == null:
                content['second_number']=1
            if content['operator'] != '' and content['second_number'] != null:
                content['second_number']=str(10*content['second_number']+1)

    
    return render(request, 'index.html', content)
        

