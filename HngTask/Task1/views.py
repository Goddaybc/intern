from django.http import JsonResponse

# Create your views here.
def bio(request):
	return JsonResponse({"slackUsername": "Godday", "backend":True, "age": 30, "bio":"I love coding"})
