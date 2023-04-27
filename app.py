import asyncio
import websockets
from flask import Flask, render_template
import multiprocessing as mp

app = Flask(__name__)
app.config["messages"] = []

async def handle_client(websocket, path):
    print("Client connected")
    await websocket.send("Hello, client!")

    async for message in websocket:
        print(f"Received message from client: {message}")
        app.config["messages"].append(message)

@app.route("/")
def index():
    return render_template("index.html", messages=app.config["messages"])

async def start_websocket_server():
    return await websockets.serve(handle_client, "185.8.174.133", 9876,subprotocols=["ws"])

def start_flask_app():
    app.run(debug=True, host="185.8.174.133", port=5000)

if __name__ == "__main__":
    websocket_server_process = mp.Process(target=asyncio.run, args=(start_websocket_server(),))
    flask_app_process = mp.Process(target=start_flask_app)

    websocket_server_process.start()
    flask_app_process.start()

    websocket_server_process.join()
    flask_app_process.join()
