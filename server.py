from flask import Flask, render_template, request, redirect, session
import random
import datetime
app = Flask(__name__)
app.secret_key = 'secretKey'

@app.route('/')
def root():
    if 'total_gold' not in session:
        session['total_gold'] = 0
        print "Gold count: ",session['total_gold']
    if 'new_gold' not in session:
        session['new_gold'] = 0
    if 'building' not in session:
        session['building'] = ""
    if 'history' not in session:
        session['history'] = []
    return render_template('index.html')

@app.route('/process_money', methods=['post'])
def process():
    session['building'] = request.form['building']
    if request.form['building'] == 'farm':
        session['new_gold'] = random.randrange(10, 21)
        print "Found new farm gold: ",session['new_gold']
        session['total_gold']+=session['new_gold']
    elif request.form['building'] == 'cave':
        session['new_gold'] = random.randrange(5, 11)
        print "Found new cave gold: ",session['new_gold']
        session['total_gold']+=session['new_gold']
    elif request.form['building'] == 'house':
        session['new_gold'] = random.randrange(2, 6)
        print "Found new house gold: ",session['new_gold']
        session['total_gold']+=session['new_gold']
    elif request.form['building'] == 'casino':
        session['new_gold'] = random.randrange(-50, 51)
        print "Found new casino gold: ",session['new_gold']
        session['total_gold']+= session['new_gold']
        if session['total_gold'] < 0:
            session['total_gold'] = 0

    print "Session total_gold is now:", session['total_gold']
    session['history'].append( [session['new_gold'], session['building'],datetime.datetime.now().strftime("%m/%d/%Y %H:%M") ])
    print session['history']

    return redirect('/')

@app.route('/reset')
def reset():
    session.pop('total_gold')
    session.pop('new_gold')
    session.pop('history')
    return redirect('/')

app.run(debug=True)