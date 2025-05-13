import asyncio
import websockets
import json

async def send_requests():
    uri = "ws://localhost:8765"
    async with websockets.connect(uri) as websocket:
        print("Connected to server. Type 'exit' to quit.")
        while True:
            try:
                a = input("Enter first number (or 'exit' to quit): ")
                if a.lower() == 'exit':
                    print("Closing connection.")
                    break
                b = input("Enter second number: ")

                # Convert inputs to numbers
                a = float(a)
                b = float(b)

                request = {
                    "type": "add",
                    "a": a,
                    "b": b
                }

                await websocket.send(json.dumps(request))
                response = await websocket.recv()
                print(f"Received from server: {response}")
            except ValueError:
                print("Please enter valid numbers.")
            except websockets.exceptions.ConnectionClosed:
                print("Connection closed by server.")
                break

if __name__ == "__main__":
    asyncio.run(send_requests())
