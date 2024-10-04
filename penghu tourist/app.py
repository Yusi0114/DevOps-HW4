from flask import Flask, render_template
import ssl
import urllib.request as request
import json

ssl._create_default_https_context = ssl._create_unverified_context
app = Flask(__name__)

# TEST


src="https://opendataap2.penghu.gov.tw/resource/files/2023-05-15/f48cf59c0182058f219572e8250befe1.json"
with request.urlopen(src) as response:
    data = json.load(response)
    # print(data)
    eng_data = []
    for tourist in data:
        eng_tourist = {
        "month": tourist["月份"],
        "tourists_110": int(tourist["年分-110年：觀光客人次"]),
        "tourists_111": int(tourist["年分-111年：觀光客人次"]),
        "tourists_change": int(tourist["年分-111年：觀光客增減人數"]),
        "flights_111": int(tourist["年分-111年：航空人次"]),
        "ships_111": int(tourist["年分-111年：輪船人次"]),
        "tansportation_ratio_flight": round((int(tourist["年分-111年：航空人次"])/int(tourist["年分-111年：觀光客人次"]))*100,2),
        "tansportation_ratio_ship": round((int(tourist["年分-111年：輪船人次"])/int(tourist["年分-111年：觀光客人次"]))*100,2)
        } 
        eng_data.append(eng_tourist)
        print(eng_tourist["tourists_change"])

@app.route('/')
def index():
    return render_template('bike_list.html', data = eng_data)


    
if __name__ == '__main__' : 
    app.run()

    