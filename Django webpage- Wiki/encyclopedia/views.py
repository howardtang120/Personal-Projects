from django.shortcuts import render, redirect
from django.http import HttpResponse
from django import forms

from . import util
from markdown2 import markdown

import random


def index(request):
    print("index")
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def entry(request, entry):
    print(f"entry {entry}")
    content = util.get_entry(entry)
    if content == None:
        return HttpResponse("*This page does not exist*")

    return render (request, "encyclopedia/entry.html", 
        {"entry": entry, "content": markdown(content)},
    )

def search(request):
    query = request.GET["q"].lower()
    print(query)

    entries = util.list_entries()
    matches = []
    message = f"Search results for \"{query}\":"

    for entry in entries:
        if query == entry.lower():
            return redirect("entry", entry=entry)

        if query in entry.lower():
            matches.append(entry)

    if not matches:
        message = f'There are no matches for \"{query}\"'

    print(entries)
    print("matchs: ", matches)

    return render(request, "encyclopedia/search.html", {
        "message": message, "matches": matches},
)


class entry_form(forms.Form):
    entry = forms.CharField(label="entry title", max_length="32")
    content = forms.CharField(
        label="content",
        widget=forms.Textarea
    )

def new_page(request):
    print("new_page")

    if request.method == "POST":
        form = entry_form(request.POST)
        if form.is_valid():
            entry = form.cleaned_data["entry"].title()
            content = form.cleaned_data["content"]

            print("entry=", entry, "\ncontent=", content)
            if entry.lower() in [title.lower() for title in util.list_entries()]:
                return HttpResponse("This page already exists")

            f = open(f"entries/{entry}.md", "x")
            f.write(f"# {entry} \n{content}")
            f.close()

            return redirect("entry", entry=entry)

    return render(request, "encyclopedia/new_page.html", 
                  {"entry_form": entry_form()})

def edit_page(request, entry):
    print(f"edit page {entry}")

    content = util.get_entry(entry)
    if content is None:
        return HttpResponse("The requested page does not exist")

    if request.method == "POST":
        form = entry_form(request.POST)
        if form.is_valid():
            entry = form.cleaned_data["entry"].title()
            content = form.cleaned_data["content"]

            f = open(f"entries/{entry}.md", "w")
            f.write(f"{content}")
            f.close()

            return redirect("entry", entry=entry)


    form = entry_form(initial={"content": content})
    return render(request, "encyclopedia/edit_page.html", 
                  {"entry_form": form, "entry": entry}
    )


def random_page(request):
    entries = util.list_entries()
    entry = entries[random.randrange(1, len(entries))]
    print(f"random: {entry}")

    return redirect("entry", entry=entry)
