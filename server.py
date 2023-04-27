import asyncio
import websockets

messages = []

async def handle_client(websocket, path):
    print("Client connected")
    await websocket.send("Hello, client!")

    async for message in websocket:
        print(f"Received message from client: {message}")
        messages.append(message)

async def main():
    async with websockets.serve(handle_client, "185.8.174.133", 8787):
        print("Server started")
        await asyncio.Future()  # Keep the server running indefinitely

if __name__ == "__main__":
    asyncio.run(main())
