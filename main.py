
#1


from flask import Flask, jsonify

app = Flask(__name__)

def is_prime(number):
    if number < 2:
        return False
    for i in range(2, int(number**0.5) + 1):
        if number % i == 0:
            return False
    return True

@app.route('/prime_number/<int:number>', methods=['GET'])
def check_prime_number(number):
    result = {"Number": number, "isPrime": is_prime(number)}
    return jsonify(result)

if __name__ == '__main__':
    app.run(debug=True)


#2

import mysql.connector

connection = mysql.connector.connect(
    host='127.0.0.1',
    port='3306',
    database='flight_game',
    user='dbuser',
    password='theminons',
)

def fetch_airport(code):
    cursor = connection.cursor(buffered=True)
    cursor.execute("SELECT name, municipality FROM airport WHERE ident='" + code + "'")

    for row in cursor.fetchall():
        return row[0], row[1]


@app.route('/airport/<path:icao>')
def check_airport(icao):
    result = fetch_airport(icao)
    if result:
        return jsonify({"ICAO": icao, "Name": result[0], "Location": result[1]})
    else:
        return "That ICAO is not in our system!"


if __name__ == '__main__':
    app.run(debug=True)