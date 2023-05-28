import mysql.connector
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def login(request):
    email = request.GET.get('email')
    password = request.GET.get('password')
    test = mysql.connector.connect(host="localhost",
                                   user="root", password="sumit0828",
                                   database="mobilesWorld")
    crs = test.cursor()
    query = "Select password from users where email = '" + email + "'"
    crs.execute(query)
    data = crs.fetchone()
    str = ""
    if data is None:
        str = "You are not registered user"
    else:
        if data[0] == password:
            str = "You are valid user"
        else:
            str = "Your password is not correct"
    return HttpResponse(str)

from django.shortcuts import render
from datetime import date
#
# def daily_health_routine(request):
#     # Get current date
#     today = date.today()
#
#     # Sample data for demonstration
#     # Replace this with actual data from your database or any other source
#     health_data = {
#         'exercise': True,
#         'medication': True,
#         'nutrition': False,
#         'sleep': True,
#         'hygiene': True,
#     }
#
#     # Render the template with the health data
#     return render(request, 'daily_health_routine.html', {'health_data': health_data, 'today': today})

from django.http import HttpResponse
from datetime import date

def daily_health_routine(request):
    # Get current date
    today = date.today()

    # Sample data for demonstration
    # Replace this with actual data from your database or any other source
    health_data = {
        'exercise': True,
        'medication': True,
        'nutrition': False,
        'sleep': True,
        'hygiene': True,
    }

    # Create response content
    response_content = f"Today's date: {today}\n"
    response_content += "Health data:\n"
    for key, value in health_data.items():
        response_content += f"{key}: {'Done' if value else 'Pending'}\n"

    # Create HTTP response with the content
    return HttpResponse(response_content, content_type='text/plain')
from django.http import JsonResponse

def get_meditation_sessions(request):
    sessions = [
        {
            'title': 'Morning Meditation',
            'description': 'Start your day with a peaceful meditation session.',
            'duration_minutes': 15,
        },
        {
            'title': 'Evening Relaxation',
            'description': 'Relax your mind and body before bedtime.',
            'duration_minutes': 10,
        },
        # Add more meditation sessions as needed
    ]
    return JsonResponse(sessions, safe=False)
