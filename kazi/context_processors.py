# myapp/context_processors.py

def kazi_context_processor(request):
    return {
        'user': request.user,
    }
