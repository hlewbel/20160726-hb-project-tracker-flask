from flask import Flask, request, render_template

import hackbright

app = Flask(__name__)


@app.route("/student")
def get_student():
    """Show information about a student."""

    
    github = request.args.get('github', 'jhacks')

    first, last, github = hackbright.get_student_by_github(github)
    return render_template('student_info.html',
                            first=first,
                            last=last,
                            github=github,
                            )

@app.route("/student_search.html")
def get_student_form():

    return render_template("student_search.html")

@app.route("/new_student_form.html")
def new_student_form():

    return render_template("new_student_form.html")

@app.route("/student-add", methods=['POST'])
def student_add():

    first_name = request.form['first']
    last_name = request.form['last']
    github = request.form['github']

    hackbright.make_new_student(first_name, last_name, github)

    #we need to link to the actual database and put content in here.
    
    return render_template("confirmation.html",
                            first_name=first_name,
                            last_name=last_name,
                            github=github,
                            )



if __name__ == "__main__":
    hackbright.connect_to_db(app)
    app.run(debug=True, host="0.0.0.0", port=int("5000"))