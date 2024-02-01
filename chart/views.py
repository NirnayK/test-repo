import json
from django.shortcuts import render
from .models import School, Match
from . import csv_logic

def schools(request):
    data = {}
    schools = School.objects.all()

    district_counts = {}
    for school in schools:
        district_name = school.district_name
        if district_name in district_counts:
            district_counts[district_name] += 1
        else:
            district_counts[district_name] = 1

    labels = list(district_counts.keys())
    counts = list(district_counts.values())

    data['labels'] = labels
    data['counts'] = counts

    json_data = json.dumps(data)
    return render(request, "chart/schools.html", {'json_Data': json_data})

def matches(request):
    data = {}

    matches = Match.objects.all()

    season_counts = {}
    for match in matches:
        season = match.season
        if season in season_counts:
            season_counts[season] += 1
        else:
            season_counts[season] = 1

    counts = sorted(season_counts.items())
    season_counts = dict(counts)

    labels = list(season_counts.keys())
    counts = list(season_counts.values())

    data['labels'] = labels
    data['counts'] = counts
    json_data = json.dumps(data)
    return render(request, "chart/matches.html", {'json_Data': json_data})

def insert_model():
    schools = csv_logic.question1()
    for school in schools:
        School.objects.create(school_name=school['school_name'], district_name=school['district_name'], category=school['category'], language=school['language'])

    matches = csv_logic.question2()
    for match in matches:
        Match.objects.create(winner=match['winner'], season=match['season'], date=match['date'])

def index(request):
    links_list = ["View School graphs", "View Match graphs"]
    context = {"links_list": links_list}
    if School.objects.count() == 0:
        insert_model()
    else:
        print("Data already inserted")
    return render(request, "chart/index.html", context)
