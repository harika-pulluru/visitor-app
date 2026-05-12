from flask import Flask
import redis
import os

app = Flask(__name__)
redis_host = os.getenv('REDIS_HOST', 'localhost')
r = redis.Redis(host=redis_host, port=6379, decode_responses=True)

@app.route('/')
def home():
    count = r.incr('hits')
    return f"Total visits: {count}"

@app.route('/reset')
def reset():
    r.set('hits', 0)
    return "Counter reset"

@app.route('/get')
def get():
    c=r.get('hits')
    if c is None:
        c = 0
    return f"Total visits: {c}"
   

if __name__ == '__main__':
  app.run(host='0.0.0.0', port=5000)


