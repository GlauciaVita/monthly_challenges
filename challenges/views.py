from django.shortcuts import render
from django.http import HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse
from django.template.loader import render_to_string



challenges = {
    "january": "Walk a lot!",
    "february": "Drink more water!",
    "march": "Eat helthly!",
    "april": "Run when you can!",
    "may": "Learn something new!",
    "june": "Walk a lot!",
    "july": "Drink more water!",
    "august": "Eat helthly!",
    "september": "It's my birthday!",
    "october": "Learn something new!",
    "november": "Walk a lot!",
    "december": None
}

# Create your views here.

def index(request):
    # list_items = ""
    months = list(challenges.keys())

    return render(request, "challenges/index.html", {
        "months": months
    })


    # for month in months:
    #     capitalized_month = month.capitalize()
    #     month_path = reverse("month-challenge", args=[month])
    #     list_items += f"<button><a href=\"{month_path}\">{capitalized_month}</a></button>"

    # # "<li><a href=\"...\">January</a></li><li><a href=\"...\">February</a></li>"

    # response_data = f"<ul>{list_items}</ul>"
    # return HttpResponse(response_data)


def monthly_challenge_by_number(request, month):
    months = list(challenges.keys())
    if month > len(months):
        return HttpResponseNotFound("<h1>Invalid month!</h1>")
    redirect_month = months[month - 1]
    redirect_path = reverse("month-challenge", args=[redirect_month]) # /challenge/january
    return HttpResponseRedirect(redirect_path)

def monthly_challenge(request, month):
    try:
        challenge_text = challenges[month]
        return render(request,"challenges/challenge.html", {
            "title": "Changes of the year",
            "paragraph": month + " Challenge",
            "text": challenge_text
        })
    except:
        response_data = render_to_string("404.html")
        return HttpResponseNotFound(response_data)
    

