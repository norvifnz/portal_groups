from django.shortcuts import render, get_object_or_404
from .models import Event
import calendar
from datetime import date

def events_list(request):
    events = Event.objects.all()
    return render(request, 'events/events_list.html', {'events': events})

def calendar_view(request):
    today = date.today()
    year = today.year
    month = today.month

    cal = calendar.HTMLCalendar(firstweekday=0)
    html_calendar = cal.formatmonth(year, month)

    events = Event.objects.filter(date__year=year, date__month=month)
    return render(request, 'events/calendar.html', {
        'calendar': html_calendar,
        'events': events,
        'month': month,
        'year': year,
    })
