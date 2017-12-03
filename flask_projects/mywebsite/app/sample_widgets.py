from flask import Flask
from flask import render_template, request
from sample_widgets_form import SampleWidgetsForm

app = Flask(__name__)
app.secret_key = 'my secret key'

@app.route('/samplewidgets', methods = ['GET','POST'])
def samplewidgets():
    form = SampleWidgetsForm()
    if request.method =='POST':
        response_message=("<H1>you selected the following values</H1>/Button Field: %s" % (form.sample_radio_field.data))
        return (response_message)
    else:
        return render_template('sample_widgets.html', form=form)

if __name__ == '__main__':
    app.run(debug=True)
