from django import forms
from django.shortcuts import render
from django.template import RequestContext

from . import util


class NewEntryForm(forms.Form):
    title = forms.CharField(label="Enter Title")
    text = forms.CharField(widget=forms.Textarea, label="Enter Text")

def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def entry(request, title):
    file = util.get_entry(title)

    if file == None:
        return render(request, "encyclopedia/error.html", {
            "file": file,
            "title": title
        })

    else:
        return render(request, f"encyclopedia/{title}.html", {
            "file": file,
            "title": title
        })

def random(request):
    return render(request, "encyclopedia/randompage.html", {
        "head": "Random Page"
    })

def new_entry(request):
    if request.method == "POST":
        form = NewEntryForm(request.POST)
        if form.is_valid():
            title = form.cleaned_data["title"]
            text = form.cleaned_data["text"]

            if title in util.list_entries():
                return render(request, "encyclopedia/already_exists_error.html", {
                    "title": title
                })

            util.save_entry(title, text)
            new_html(title, text)

            file = util.get_entry(title)
            return render(request, f"encyclopedia/{title}.html", {
                "file": file,
                "title": title
            })

    return render(request, "encyclopedia/newentry.html", {
        "form": NewEntryForm()
    })

def search(request):
    query = None
    if request.method == "GET":
        query = request.GET.get('q')
        if query in util.list_entries():
            file = util.get_entry(query)
            return render(request, f"encyclopedia/{query}.html", {
                "file": file,
                "title": query
            })
        else:
            entries = util.list_entries()
            list = []
            for entry in entries:
                if query in entry:
                    list.append(entry)

            return render(request, "encyclopedia/search_results.html", {
                "entries": list
            })

def new_html(title, text):
        f = open(f'encyclopedia/templates/encyclopedia/{title}.html', 'w')

        # html template code for file
        html_template = """
        {% extends "encyclopedia/layout.html" %}

        {% block title %}
            {{ title }}
        {% endblock %}

        {% block body %}
            <h1>{{ title }}</h1>

            <a>{{ file }}</a>

        {% endblock %}
        """

        # writing code into the file
        f.write(html_template)

        # close the file
        f.close()
