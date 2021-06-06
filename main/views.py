from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import ToDoList, Item
from .forms import CreateNewList

# Create your views here.


def index(request, id):
    todolist = ToDoList.objects.get(id=id)
    print(f"Ying #{id}")

    if request.method == "POST":
        print(request.POST)
# <QueryDict:
        # {'csrfmiddlewaretoken': ['7efTaJwpGhiKwqnv9qasUFts4rSxNCv6av6rzIWNusVevTahKNDwinYLfeBe3KMo'], 'c2': ['clicked'], 'save': ['save'], 'new': ['']}>
# <QueryDict:
        # {'csrfmiddlewaretoken': ['zFlMNMM7YwHdvJv0uJ4gMrUDY3RlrWjECWckcLcvMHkHuciM56xka9pW9QA2H4AW'], 'c2': ['clicked'], 'new': ['Go to say hi'], 'newItem': ['newItem']}>
        if request.POST.get("save"):
            for item in todolist.item_set.all():
                if request.POST.get("c" + str(item.id)) == "clicked":
                    item.complete = True
                else:
                    item.complete = False

                item.save()

        elif request.POST.get("newItem"):
            txt = request.POST.get("new")
            if len(txt) > 2:
                todolist.item_set.create(text=txt, complete=False)
            else:
                print("invalid input")

    return render(request, "main/todo-list.html", {"todolist": todolist})


def home(request):
    return render(request, "main/home.html", {})
    # return HttpResponse('hi from home')


def create(request):
    if request.method == "POST":
        form = CreateNewList(request.POST)

        if form.is_valid():
            n = form.cleaned_data["name"]
            t = ToDoList(name=n)
            t.save()

        return HttpResponseRedirect(f"/{t.id}")

    form = CreateNewList()  # create a blank form
    return render(request, "main/create.html", {"form": form})
