import asyncio
import websockets

async def main():
    async with websockets.connect("ws://185.8.174.133:9876/") as websocket:
        print("Connected to server")
        while True:
            message = input("Enter a message to send to the server: ")
            await websocket.send(message)

            async for message in websocket:
                print(f"Received message from server: {message}")

if __name__ == "__main__":
    asyncio.run(main())
