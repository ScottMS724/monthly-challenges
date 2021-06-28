from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse 

# Create your views here.

monthly_challenges = {
    "january": "The current month is January.",
    "february": "The current month is February.",
    "march": "The current month is March.",
    "april": "The current month is April.",
    "may": "The current month is May.",
    "june": "The current month is June.",
    "july": "The current month is July.",
    "august": "The current month is August.", 
    "september": "The current month is September.", 
    "october": "The current month is October.",
    "november": "The current month is November.",
    "december": "The current month is December."
}

def monthly_challenge_by_number(request, month_integer):
    months = list(monthly_challenges.keys())

    if month_integer > len(months):
        return HttpResponseNotFound("Please enter a valid month.")

    redirect_month = months[month_integer - 1]
    redirect_path = reverse("month-challenge", args=[redirect_month]) # /challenges/month 
    return HttpResponseRedirect(redirect_path)



def monthly_challenge(request, month):
    try:
        challenge_text = monthly_challenges[month]
    except: 
        return HttpResponseNotFound("Please enter a valid month.")
    return HttpResponse(challenge_text)