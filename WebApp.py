from block import Blockchain
import json
from flask import Flask, request
from flask import render_template

app =  Flask(__name__)
blockchain = Blockchain()
# fileOpen = open('format.json')
# things = json.load(fileOpen)
# fileOpen.close()

@app.route('/', methods=['POST','GET'])         #('/chain', methods=['GET'])
def index():
    #result = get_chain()
    user = request.form.get('lender')
    lender = request.form.get('borrower')
    amount = request.form.get('amount')
    print(user)
    print(lender)
    print(amount)
    rep = user + " bought " + amount + " of Phong's crypto coins from " + lender + " ,You fool :))"
    return render_template('UI.html',value_suggest=rep) #+ result + render_template('temp.html')

def get_chain():
    chain_data = []
    for block in blockchain.chain:
        chain_data.append(block.__dict__)
    result = ""
    # for sir in things['BlockList']:
    #     result += sir['author'] + " , "
    # result += json.dumps({"blockchain length": len(chain_data), "chain_data": chain_data})
    return result

app.run(debug=True, host='0.0.0.0') # port=5000 or something idk but I didnt set port since I need port of Render
