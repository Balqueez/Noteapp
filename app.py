from flask import Flask, render_template_string, request, redirect, url_for

app = Flask(__name__)

notes = []

HTML = """
<!doctype html>
<head>
<title>Simple Note App</title>
<h1>Simple Note App</h1>
 <style>
    body {
      font-family: Arial, sans-serif;
      background-color: #f4f6f8;
      margin: 0;
      padding: 20px;
    }

    h1 {
      color: #333;
      text-align: center;
    }

    form {
      max-width: 600px;
      margin: 0 auto;
      background-color: #ffffff;
      padding: 20px;
      border-radius: 8px;
      box-shadow: 0 4px 6px rgba(0,0,0,0.1);
    }

    textarea {
      width: 100%;
      padding: 10px;
      font-size: 14px;
      border: 1px solid #ccc;
      border-radius: 4px;
      resize: none;
      margin-bottom: 10px;
    }

    button {
      background-color: #007BFF;
      color: white;
      border: none;
      padding: 10px 15px;
      border-radius: 4px;
      cursor: pointer;
      font-size: 14px;
    }

    button:hover {
      background-color: #0056b3;
    }

    .notes {
      max-width: 600px;
      margin: 30px auto;
      background-color: #ffffff;
      padding: 20px;
      border-radius: 8px;
      box-shadow: 0 4px 6px rgba(0,0,0,0.1);
    }

    li {
      padding: 8px 0;
      border-bottom: 1px solid #eee;
      display: flex;
      justify-content: space-between;
    }

    a {
      color: #dc3545;
      text-decoration: none;
      font-size: 13px;
    }

    a:hover {
      text-decoration: underline;
    }
  </style>
  </head>
<form action="/add" method="post">
  <textarea name="note" rows="4" cols="50" placeholder="Enter your note here"></textarea><br>
  <button type="submit">Add Note</button>
</form>

<h2>Your Notes:</h2>
<ul>
  {% for note in notes %}
  <li>{{ note }} 
    <a href="{{ url_for('delete_note', note_id=loop.index0) }}">[Delete]</a>
  </li>
{% endfor %}
</ul>
"""

@app.route("/")
def index():
    return render_template_string(HTML, notes=notes)

@app.route("/add", methods=["POST"])
def add():
    note = request.form.get("note")
    if note:
        notes.append(note)
    return redirect("/")

@app.route("/delete/<int:note_id>")
def delete_note(note_id):
    if 0 <= note_id < len(notes):
        notes.pop(note_id)
    return redirect("/")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
