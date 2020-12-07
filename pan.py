from random import randrange
from flask import Flask,request,render_template
import json
app=Flask(__name__)

datapencard = {}
panmat = []

class BackendError(Exception):
    def __init__(self):
        self.data=Exception
    def action(self):
        if self.data:
            return "there is error"
        else:
            return True






def get_pan_data(pan_number):
    num = randrange(10)
    if num in (8, 9):
        raise BackendError

    else:
        pandata = json.loads(pan_number)
        pan_number = pandata['pan_number']
        if pan_number in panmat:
            return datapencard[pan_number]
        else:
            return "data is not available for this pen card"





@app.route('/')
def student():
   return render_template('show.html')

@app.route('/pandata')
def pan1():
    return render_template('index.html')

@app.route('/result',methods = ['POST', 'GET'])
def result():
   if request.method == 'POST':
      result = request.form
      panno=None
      for key, value in result.items():
          panno=value
      data=get_pan_data(panno)
      return data


@app.route('/formfill')
def students():
   return render_template('pandata.html')

@app.route('/form',methods=['POST','GET'])
def put_pan_data():
    pan_number=None
    name=None
    dob=None
    father_name=None
    if request.method=='POST':
        datapan=request.form
        for key,value in datapan.items():
            if key=="pan_no":
                pan_number=value
            elif key=="name":
                name=value
            elif key=="dob":
                dob=value
            elif key=="fathername":
                father_name=value

        panmat.append(pan_number)
        datapencard[pan_number]={'pan': pan_number,
            'name':name,
            'dob': dob,
            'father_name': father_name}


    return "thankyou your response is recorded"

if __name__=="__main__":
    app.run(debug=True)