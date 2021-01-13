import asyncio
import websockets
import json
from escpos import *

async def hello():
    port = 15753
    uri = "ws://example.com:%s" % (port)
    async with websockets.connect(uri) as websocket:
        while True:
            message = await websocket.recv()
            jsonData = json.loads(message)
            print("----------------")
            print(jsonData["message"])
            print("--%s" % jsonData["name"])
            print("----------------\n")

            # USB thermal printer variables, change respectively
            VenderID = 0x0416
            ProductID = 0x5011
            InterfaceID = 4
            EP_IN = 0x81
            EP_OUT = 0x03

            p = printer.Usb(VenderID,ProductID, InterfaceID, EP_IN, EP_OUT)
            message = jsonData["message"].center(32)
            name = "--%s" % jsonData["name"]
            nameCentered = name.center(32)
            p.text("\n\n" + message + "\n" + nameCentered + "\n\n\n\n")
            p.close()
asyncio.get_event_loop().run_until_complete(hello())