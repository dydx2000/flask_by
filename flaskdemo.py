
from flask import Flask,render_template
app=Flask(__name__)

@app.route("/",methods=['GET',"POST"])
def index():
    # return "hello flask,good it heima teacher."

    myList=[1,3,5345,4343]
    return render_template('index.html',myList=myList)

@app.route("/orders/<int:order_id>")
def get_order(order_id):
    return "hello user, %s"%order_id
if __name__ == '__main__':
    app.run()



