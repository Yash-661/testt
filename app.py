from flask import *
import yaml

app = Flask(__name__)

dt = {
    'x': 0,
    'y': 0,
    'z': 0,

    'l1': 'off',
    'f1': 'off',
    'l2': 'off'
}



def dumpp(d):
    with open('app.yml', 'w') as fw:
        yaml.dump(d, fw)
dumpp(dt)


def onoff(var):
    if var == 0:
        var = 1
        return var,'on'
    else:
        var = 0
        return var,'off'

@app.route('/')
def home():
    return render_template('index.html',l = dt['l1'], f = dt['f1'], ll = dt['l2'])

@app.route('/fan') # x 
def fan():
    global dt
    dt['x'], dt['f1'] = onoff(dt['x']) 
    dumpp(dt)      
    return render_template('index.html',l = dt['l1'], f = dt['f1'], ll = dt['l2'])    

@app.route('/led') # y
def led():
    global dt          
    dt['y'], dt['l1'] = onoff(dt['y'])
    dumpp(dt)
    return render_template('index.html',l = dt['l1'], f = dt['f1'], ll = dt['l2'])

@app.route('/led2') # z
def led2():
    global dt          
    dt['z'], dt['l2'] = onoff(dt['z'])
    dumpp(dt)
    return render_template('index.html',l = dt['l1'], f = dt['f1'], ll = dt['l2'])

# @app.route('/led') # y
# def led():
#     global x, y, l1, f1           
#     y, l1 = onoff(y)
#     return render_template('index.html',l = l1, f = f1)

#server
if __name__ == '__main__':
    app.run(host='0.0.0.0',debug=True)