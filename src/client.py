import asyncio

from grpclib.client import Channel

from ledapi_pb2 import Void, Success
from ledapi_grpc import LEDServiceStub

async def main():
  async with Channel('localhost', 5001) as channel:
    greeter = LEDServiceStub(channel)

    reply = await greeter.IsAlive(Void())
    print(reply.result)

if __name__ == '__main__':
  asyncio.run(main())
