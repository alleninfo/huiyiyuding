from django.http import JsonResponse
import json


def listmeeting(request):
    if request.method == 'GET':
        request.params =request.GET
    # POST/PUT/DELETE 请求 参数 从 request 对象的 body 属性中获取
    elif request.method in ['POST', 'PUT', 'DELETE']:
        # 根据接口，POST/PUT/DELETE 请求的消息体都是 json格式
        request.params = json.loads(request.body)

    # 根据不同的action分派给不同的函数进行处理
    action = request.params['action']
    if action == 'list_meetings':
        return listmeetings(request)
    elif action == 'add_meetings':
        return addmeeting(request)
    elif action == 'modify_meetings':
        return modifymeeting(request)
    elif action == 'del_meetings':
        return deletemeeting(request)

    else:
        return JsonResponse({'ret':1, 'msg':'不支持该类型http请求'})

def addmeeting(request):
    info = request.params['name']