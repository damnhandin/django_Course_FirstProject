from django.http import HttpResponse
from django.shortcuts import render


def index(request, name):
    return render(request, "blog/index.html", context={
        "name": name
    })


def about(request, name):
    # return HttpResponse(f"""
    #     <h2>О пользователе</h2>
    #     <p>Имя: {name}</p>
    #     <p>Возраст: {age}</p>
    # """)
    return render(request, "blog/about.html",
                  context={"name": name})


def contact(request):
    return HttpResponse("<h2>Контакты</h2>")


def user(request, name="undefined", age=0):
    return HttpResponse(f"<h2>Имя: {name}, возраст: {age}</h2>")