from flask import Flask, jsonify, render_template
import speedtest

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/speedtest')
def run_speedtest():
    try:
        st = speedtest.Speedtest()
        download = st.download() / 1_000_000
        upload = st.upload() / 1_000_000
        return jsonify({
            "download": round(download, 2),
            "upload": round(upload, 2)
        })
    except Exception as e:
        return jsonify({"error": str(e)})

if __name__ == '__main__':
    app.run(debug=True)
