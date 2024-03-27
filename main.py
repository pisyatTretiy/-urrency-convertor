from flask import Flask, request, jsonify, render_template
import requests

app = Flask(__name__)

currency_symbols = {
    'USD': '$',  
    'EUR': '€',  
    'RUB': '₽',  
}

@app.route('/', methods=['GET'])
def home():
    return render_template('index.html')

@app.route('/convert', methods=['POST'])
def convert():
    amount = request.form.get('amount', type=float)
    from_currency = request.form.get('from_currency', type=str).upper()
    to_currency = request.form.get('to_currency', type=str).upper()

    # заглушка
    rates = {'USD': 1, 'EUR': 0.9, 'RUB': 75}

    converted_amount, currency_symbol = convert_currency(amount, from_currency, to_currency, rates)
    if converted_amount is not None:
        result = f"{converted_amount:.2f} {currency_symbol}"
        return render_template('index.html', converted_amount=result)
    else:
        return render_template('index.html', error='Некорректная пара валют')

def convert_currency(amount, from_currency, to_currency, rates):
    if from_currency == to_currency:
        return amount, currency_symbols.get(to_currency, '')
    if from_currency in rates and to_currency in rates:
        converted_amount = amount * rates[to_currency] / rates[from_currency]
        currency_symbol = currency_symbols.get(to_currency, '')
        return converted_amount, currency_symbol
    else:
        return None, None
    
if __name__ == '__main__':
    app.run(debug=True)
