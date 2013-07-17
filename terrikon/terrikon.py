from flask import Flask, render_template


app = Flask(__name__)

@app.route('/')
@app.route('/index')
def index():
    return render_template('web_setup.html')

@app.route('/test-email')
def email_render_test():

    return render_template('sample_email.html', 
    LastName = "LastName",
    Program = "Program",
    ProgramYear = "ProgramYear",
    ProgramName = "ProgramName",
    DocumentDeadlineDate = "Test",
    Finalist = True,
    Alternate = False)


if __name__ == "__main__":
    app.run()