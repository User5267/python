from flask import Flask
from flask import url_for
from flask import request
from flask import render_template
import psycopg2
import requests

#1
conn = psycopg2.connect(database="project", user = "root", password = "toor", host = "127.0.0.1", port = "5432")
cursor = conn.cursor()
table = '''CREATE TABLE SomeTable(

   INDEX varchar(255),

   ADDRESS varchar(255)

)'''



cursor.execute("CREATE TABLE IF NOT EXISTS nft_test (name text, count integer)")
conn.commit

#2
app = Flask(__name__)
@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        address = request.form.get('address')
        # address = '4Jb9EzcUd6k1gC7GSH2iu6H7UcL2ez3NgvAF8n6a1QDs'

        url = "https://solana-gateway.moralis.io/nft/mainnet/" + address + "/metadata"

        headers = {

            "accept": "application/json",
            "X-API-Key": "LjGAwuNINRJaraC0W7OBdU4fBL9beJvwgGW7jq2FVtZtXb0G5lMl4aZ0VYnPDUif"

        }

        response = requests.get(url, headers=headers)
        print(response.text)
        # print(response.text)

        return "<h1>{blablabla}</h1>".format(response.text)

    return render_template('index.html')

if __name__ == '__main__':
   app.run()

