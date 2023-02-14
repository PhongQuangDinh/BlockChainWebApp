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
    return render_template('UI.html') #+ result + render_template('temp.html')

def get_chain():
    chain_data = []
    for block in blockchain.chain:
        chain_data.append(block.__dict__)
    result = ""
    # for sir in things['BlockList']:
    #     result += sir['author'] + " , "
    # result += json.dumps({"blockchain length": len(chain_data), "chain_data": chain_data})
    return result

app.run(debug=True, port=5000)