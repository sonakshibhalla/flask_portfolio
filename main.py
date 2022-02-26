# import "packages" from flask

from pathlib import Path

from flask import Flask, render_template, request
import requests
import http.client

# create a Flask instance
app = Flask(__name__)


from crud3.app_crud import app_crud
import http.client

# create a Flask instance

app.register_blueprint(app_crud)


# connects default URL to render index.html
@app.route('/')
def home():
    return render_template("home.html")


@app.route('/dark')
def dark():
    return render_template("dark.html")


@app.route('/study')
def study():
    return render_template("study.html")


@app.route('/stress')
def stress():
    return render_template("stress.html")


@app.route('/volunteer')
def volunteer():
    return render_template("volunteer.html")

@app.route('/createtask')
def createtask():
    return render_template("createtask.html")


@app.route('/crud/search')
def search():
    return render_template("search.html")


@app.route('/crud')
def crud():
    return render_template("crud.html")

@app.route('/fibonacci')
def fibonacci():
    return render_template("fibonacci.html")

@app.route('/sonakshi', methods=['GET', 'POST'])
def sonakshi():
    # submit button has been pushed
    if request.form:
        name = request.form.get("name")
        if len(name) != 0:  # input field has content
            return render_template("sonakshi.html", name=name)
    # starting and empty input default
    return render_template("sonakshi.html", name="World")


@app.route('/forum', methods=['GET', 'POST'])
def forum():
    # submit button has been pushed
    if request.form:
        name = request.form.get("name")
        if len(name) != 0:  # input field has content
            return render_template("forum.html", name=name)
    # starting and empty input default
    return render_template("forum.html", name="Advice Here")


@app.route('/shreya', methods=['GET', 'POST'])
def shreya():
    # submit button has been pushed
    if request.form:
        name = request.form.get("name")
        if len(name) != 0:  # input field has content
            return render_template("shreya.html", name=name)
    # starting and empty input default
    return render_template("shreya.html", name="World")


@app.route('/linda', methods=['GET', 'POST'])
def linda():
    if request.form:
        name = request.form.get("name")
        if len(name) != 0:  # input field has content
            return render_template("linda.html", name=name)
    return render_template("linda.html")


@app.route('/khushi', methods=['GET', 'POST'])
def khushi():
    # submit button has been pushed
    if request.form:
        name = request.form.get("name")
        if len(name) != 0:  # input field has content
            return render_template("khushi.html", name=name)
    # starting and empty input default
    return render_template("khushi.html", name="World")


@app.route('/newapi', methods=['GET', 'POST'])
def newapi():
    url = "https://community-open-weather-map.p.rapidapi.com/climate/month"
    querystring = {"q": "San Diego"}

    headers = {
        'x-rapidapi-host': "community-open-weather-map.p.rapidapi.com",
        'x-rapidapi-key': "8d571b2f72msh44f8fd48e083624p19cce1jsnfb1e373c1716"
    }

    response = requests.request("GET", url, headers=headers, params=querystring)

    return render_template("newapi.html", stats=response.json())

@app.route('/quote', methods=['GET', 'POST'])
def quote():
    url = "https://motivational-quotes1.p.rapidapi.com/motivation"

    payload = {"key": "value"}

    headers = {
        'content-type': "application/json",
        'x-rapidapi-host': "motivational-quotes1.p.rapidapi.com",
        'x-rapidapi-key': "69b86a4f86msh0f84d36c298ca22p15693fjsne0d137318725"
    }


@app.route('/trivia', methods=['GET', 'POST'])
def trivia():
    url = "https://numbersapi.p.rapidapi.com/random/trivia"

    querystring = {"min":"1","max":"100","fragment":"true","json":"true"}

    headers = {
        'x-rapidapi-host': "numbersapi.p.rapidapi.com",
        'x-rapidapi-key': "69b86a4f86msh0f84d36c298ca22p15693fjsne0d137318725"
    }
    response = requests.request("GET", url, headers=headers, params=querystring)
    return render_template("trivia.html", numbers=response.json())
    print(response.text)


@app.route('/listmovie/', methods=['GET', 'POST'])
def listmovie():
    url = "https://watchmode.p.rapidapi.com/list-titles/"

    querystring = {"types": "movie,tv_series", "regions": "US", "source_types": "sub,free", "source_ids": "23,206",
                   "page": "1", "limit": "250", "genres": "4,9"}  # assigns values to specified parameters(keys)

    headers = {
        'x-rapidapi-host': "watchmode.p.rapidapi.com",
        'x-rapidapi-key': "f4480562c7mshcfebe0975d4fd48p16ab77jsnae6575329780"
    }

    response = requests.request("GET", url, headers=headers, params=querystring)
    response = response.json().get("titles")

    return render_template("listmovieapi.html", response=response)


@app.route('/dictionary', methods=['GET', 'POST'])
def dictionary():
    word = "fantastic"
    url = "https://dictionary-by-api-ninjas.p.rapidapi.com/v1/dictionary"
    querystring = {"word": word}
    headers = {
        'x-rapidapi-host': "dictionary-by-api-ninjas.p.rapidapi.com",
        'x-rapidapi-key': "69b86a4f86msh0f84d36c298ca22p15693fjsne0d137318725"
    }
    response = requests.request("GET", url, headers=headers, params=querystring)
    return render_template("dictionary.html", word=word, stats=response.json())

@app.route('/punnuapitest', methods=['GET', 'POST'])
def punnuapitest():
    url = "https://api.kuroganehammer.com/api/characters"
    response = requests.request("GET", url)
    text = response.json()
    return render_template("punnuapitest.html", text=text)


# runs the application on the development server
if __name__ == "__main__":
    app.run(debug=True, port="5001")
