from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
@app.route('/index')
def index():
    return render_template('web_setup.html')

@app.route('/test-email')
def test_email_render():
    # context = {"FirstName":"FirstName",
    #     "LastName":"LastName",
    #     "Program":"Program",
    #     "ProgramYear":"ProgramYear",
    #     "ProgramName":"ProgramName",
    #     "DocumentDeadlineDate":"DocumentDeadlineDate",
    #     "Finalist":True,
    #     "Alternate":False}
    return render_template('sample_email.html', FirstName = "FirstName",
    LastName = "LastName",
    Program = "Program",
    ProgramYear = "ProgramYear",
    ProgramName = "ProgramName",
    DocumentDeadlineDate = "DocumentDeadlineDate",
    Finalist = True,
    Alternate = False)