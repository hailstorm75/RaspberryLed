from grpclib.utils import graceful_exit
from grpclib.server import Server, Stream

import sys
import inspect
import asyncio
from datetime import datetime
from ledapi_pb2 import Void, Success, Color
from ledapi_grpc import LEDServiceBase

class LEDService(LEDServiceBase):
  def _logName(self, input):
    now = datetime.now()
    print(f"[{now.strftime('%H:%M:%S')}] Received command:\t{input.__name__}")

  async def IsAlive(self, stream: Stream[Void,Success]) -> None:
    self._logName(self.IsAlive)
    await stream.send_message(Success(result = True))
  async def SetColor(self, stream: Stream[Color,Success]) -> None:
    self._logName(self.IsAlive)
    await stream.send_message(Success(result = True))

async def main():
  server = Server([LEDService()])

  with graceful_exit([server]):
    await server.start(sys.argv[1], "5001")
    print(f"Server running on {sys.argv[1]}")
    await server.wait_closed()

if __name__ == '__main__':
  asyncio.run(main())
