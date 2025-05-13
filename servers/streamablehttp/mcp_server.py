# import asyncio
# import websockets
# import logging

# logger = logging.getLogger('websockets')
# logger.setLevel(logging.DEBUG)
# logger.addHandler(logging.StreamHandler())

# async def mcp_server(websocket):
#     print(f"Connection established with {websocket.remote_address}")
#     try:
#         async for message in websocket:
#             print(f"Received message: {message}")
#             response = {"type": "message", "data": "Hello from server!"}
#             await websocket.send(str(response))
#     except websockets.exceptions.ConnectionClosedError as e:
#         print("Connection closed with error:", e)
#     finally:
#         print(f"Connection closed with {websocket.remote_address}")

# async def start_server():
#     server = await websockets.serve(mcp_server, "localhost", 8765)
#     print("Server started at ws://localhost:8765")
#     await server.wait_closed()

# if __name__ == "__main__":
#     asyncio.run(start_server())


import asyncio
import websockets
import logging
import json

logger = logging.getLogger('websockets')
logger.setLevel(logging.DEBUG)
logger.addHandler(logging.StreamHandler())

async def mcp_server(websocket):
    print(f"Connection established with {websocket.remote_address}")
    try:
        async for message in websocket:
            print(f"Received message: {message}")
            try:
                data = json.loads(message)

                if data.get("type") == "add":
                    a = data.get("a", 0)
                    b = data.get("b", 0)
                    result = a + b
                    response = {"type": "result", "result": result}
                else:
                    response = {"type": "error", "message": "Unknown request type."}
            except json.JSONDecodeError:
                response = {"type": "error", "message": "Invalid JSON format."}

            await websocket.send(json.dumps(response))

    except websockets.exceptions.ConnectionClosedError as e:
        print("Connection closed with error:", e)
    finally:
        print(f"Connection closed with {websocket.remote_address}")

async def start_server():
    server = await websockets.serve(mcp_server, "localhost", 8765)
    print("Server started at ws://localhost:8765")
    await server.wait_closed()

if __name__ == "__main__":
    asyncio.run(start_server())
