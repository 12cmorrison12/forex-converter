from flask import Flask, render_template, request
import requests

app = Flask(__name__)

EXCHANGE_API_BASE_URL = "https://open.er-api.com/v6/latest/"

def get_exchange_rate(base_currency, target_currency):
    url = f"{EXCHANGE_API_BASE_URL}{base_currency}"
    params = {'symbols': target_currency}
    
    response = requests.get(url, params=params)
    
    if response.status_code == 200:
        data = response.json()
        if target_currency in data['rates']:
            return data['rates'][target_currency]
        else:
            return None
    else:
        return None

@app.route('/', methods=['GET', 'POST'])
def forex_converter():
    if request.method == 'POST':
        base_currency = request.form['base_currency']
        target_currency = request.form['target_currency']
        amount = float(request.form['amount'])

        exchange_rate = get_exchange_rate(base_currency, target_currency)

        if exchange_rate is not None:
            converted_amount = amount * exchange_rate
            return render_template('index_forex.html', result=True, base_currency=base_currency,
                                   target_currency=target_currency, amount=amount, converted_amount=converted_amount)
        else:
            return render_template('index_forex.html', result=False)

    return render_template('index_forex.html', result=None)

if __name__ == '__main__':
    app.run(debug=True)