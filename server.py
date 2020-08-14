from flask import Flask, jsonify, request, make_response
import crawl
import service

app = Flask(__name__)


@app.route('/api/today', methods=['GET'])
def today():
    weathers = crawl.getToday()
    return jsonify(weathers)


@app.route('/api/tomorrow', methods=['GET'])
def tomorrow():
    weathers = crawl.getTomorrow()
    return jsonify(weathers)

@app.route('/api/getday', methods=['GET'])
def getday():
    day = request.args['day']
    weathers = service.getDay(day)
    if weathers == False:
        return jsonify({
            "Error":"Datetime invalid"
        })
    else:
        return jsonify(weathers)


if __name__ == "__main__":
    app.run(host='localhost', port=5000, debug=True, threaded=True)
