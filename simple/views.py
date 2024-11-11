from django.http import HttpResponse
from datetime import datetime

def hello(request):
    greeting = "Hello Again, World!"
    created_at = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    html = f"<h1>{greeting}</h1><p>Created at: {created_at}</p>"
    return HttpResponse(html)
