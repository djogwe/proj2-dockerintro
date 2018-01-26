from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def page_generator(path):
    page_index =['index.html', 'trivia.html']
    parts = path.split('/')
    last_part = parts[-1]
    if (".." in path or "//" in path or "~" in path):
        return error_403(403)
    elif (last_part in page_index):
        name = request.args.get("name")
        if (name == None):
            name = "World"
        return render_template(last_part, name=name), 200
    else:
        return error_404(404)

def error_404(error):
    return render_template("404.html"), 404

def error_403(error):
    return render_template("403.html"), 403

if __name__ == "__main__":
    app.run(debug=True,port=5000)
