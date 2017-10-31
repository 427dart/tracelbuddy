# -*- coding: utf-8 -*-
from django.shortcuts import render, redirect
from .models import Trip, User
from django.contrib import messages
from django.conf.urls import url, include

def session_check(request):
    if 'user' in request.session:
        return True
    else:
        return False

def index(request):
    if session_check(request):
        context = {
            'user_trips': Trip.objects.filter(planner__id=request.session['user']['user_id']),
            'joined_trips': Trip.objects.filter(travelers__id=request.session['user']['user_id']),
            'all_trips': Trip.objects.all()
        }
        return render(request, 'travel_buddy/index.html', context)

    return redirect('login:index')

def planner(request):
    if session_check(request):
        return render(request, 'travel_buddy/plan.html')

    return redirect('login:index')

def add_trip(request):
    if session_check(request):

        errors = Trip.objects.add(request)

        if errors:
            print_errors(request, errors)
            return redirect('travel_buddy:plan')

        return redirect('travel_buddy:index')

    return redirect('login:index')

def show(request, id):
    if session_check(request):
        context = {
            'trip': Trip.objects.get(id=id),
            'attendees': User.objects.filter(trips__id=id)
        }
        return render(request, 'travel_buddy/show.html', context)

    return redirect('login:index')

def join_trip(request, id):
    if session_check(request):
        Trip.objects.join_trip(request, id)
        return redirect('travel_buddy:show', id)

    return redirect('login:index')

def errors(request, error_list):
    for error in error_list:
        messages.add_message(request, messages.INFO, error)

def logout(request):
    request.session.clear()

    return redirect('login:index')
