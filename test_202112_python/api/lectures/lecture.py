from django.views import View
from django.http import HttpResponse
from test_202112_python.models import Lectures

class Lecture(View):
    
    # 특정 강의 내려주기 => 이름으로 조회?
    def get(self, request): 
                
        search_lecture = Lectures.objects.filter(name=request.GET['name']).first()
        
        
        return HttpResponse({
            'code' : 200,
            'message' : '특정 강의 내려주기',
            'data' : {
                'lecture' : search_lecture.get_data_object()
            }
        })