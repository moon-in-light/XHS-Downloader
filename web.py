from flask import Flask, request, jsonify
from xhs_spider import XhsDownloader

app = Flask(__name__)

@app.route('/parse', methods=['POST'])
def parse_xhs():
    try:
        data = request.json
        url = data.get("url")
        if not url:
            return jsonify({"error": "URL missing"}), 400

        result = XhsDownloader().get_xhs_data(url)
        return jsonify(result)
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10086)
