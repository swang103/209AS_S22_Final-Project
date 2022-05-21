import asyncio
import kasa

async def main():
    
    dev = kasa.SmartDevice("192.168.137.49")  # We create the instance inside the main loop
    while True:
        await dev.update()  # Request an update
        print(dev.emeter_realtime)
        await asyncio.sleep(0.5)  # Sleep some time between updates

if __name__ == "__main__":
    asyncio.run(main())