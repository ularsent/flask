from flask import Flask
from flask import url_for, render_template, request, redirect

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')

# Страница с вопросом
@app.route('/question', methods=['GET', 'POST'])
def question():
    return render_template('question.html')

@app.route('/process', methods=['get', 'post'])
def answer_process(): # полностью повторяет конспект, кроме параметров
    if not request.args:
        return redirect(url_for('question'))
    
    who_flies = request.args.get('who_flies')
    who_flies_txt = request.args.get ('who_flies_txt')
    greedy = request.args.get('greedy')
    greedy_txt = request.args.get('greedy_txt')
    area = request.args.get('area')
    
    user = User(
        who_flies = who_flies,
        who_flies_txt = who_flies_txt,
        greedy = greedy,
        greedy_txt = greedy_txt,
        area = area
    )
    db.session.add(user)
    db.session.commit()
    db.session.refresh(user)
    

    q1 = request.args.get('q1')
    q2 = request.args.get('q2')

    answer = Answers(id=user.id, q1=q1, q2=q2)

    db.session.add(answer)
    db.session.commit() 
    return 'Ok'

@app.route('/result') # результаты вывести не смогла
def result():
    return render_template('result.html')

if __name__ == '__main__':
    app.run(debug=True)