from flask import Flask 

app =Flask(__name__)


@app.route('/')
def index():
  return "Hello word this test for firs docker test"

if __name__ == "__main__":
    app.run(debug=True)
