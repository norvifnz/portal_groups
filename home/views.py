from django.shortcuts import render
from .models import GroupInfo
from news.models import News
from events.models import Event
from diary.models import DiaryEntry


# або правильна назва
# якщо потрібно
# імпортуй інші моделі з інших додатків за потреби

def home_page(request):
    group_info = GroupInfo.objects.first()
    DiaryEntry.objects.order_by("-created_at")

    upcoming_events = Event.objects.order_by('date')[:3]
    # diary_entries = DiaryEntry.objects.order_by('-date')[:2]  # приклад

    context = {
        'group_info': group_info,
        'DiaryEntry': DiaryEntry,
        'upcoming_events': upcoming_events,
        # 'latest_diary': diary_entries,
    }
    return render(request, "home.html")

