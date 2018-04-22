from flask import render_template, Flask
from main_form import CalcForm


app = Flask(__name__)
app.config['SECRET_KEY'] = 'you-will-never-guess'


@app.route('/', methods=['GET', 'POST'])
def calc():
    form = CalcForm()
    result = 0
    if form.validate_on_submit():
        result = 19

    return render_template('calc.html', title='Allstate', form=form, mpg=result)


if __name__ == '__main__':
    app.run()
