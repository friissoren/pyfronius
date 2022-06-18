import http.server
from prometheus_client import start_http_server
from prometheus_client import Gauge

import asyncio
import sys
import aiohttp
import pyfronius

ENERGY_DAY = Gauge('energy_day', 'Energy produced today in Wh')
ENERGY_TOTAL = Gauge('energy_total', 'Energy produced in total in Wh')
ENERGY_YEAR = Gauge('energy_year', 'Energy produced this year in Wh')
POWER_AC = Gauge('power_ac', 'Power produced right now in W')

async def main(loop, host):
    timeout = aiohttp.ClientTimeout(total=10)
    async with aiohttp.ClientSession(loop=loop, timeout=timeout) as session:
        fronius = pyfronius.Fronius(session, host)

        # use the optional fetch parameters to configure
        # which endpoints are acessed
        # NOTE: configuring the wrong devices may cause Exceptions to be thrown
        res = await fronius.fetch(
            active_device_info=False,
            inverter_info=False,
            logger_info=False,
            power_flow=False,
            system_meter=False,
            system_inverter=True,
            system_ohmpilot=False,
            system_storage=False,
            device_meter=[],
            # storage is not necessarily supported by every fronius device
            device_storage=[],
            device_inverter=[],
        )
        return res


class ServerHandler(http.server.BaseHTTPRequestHandler):
    def do_GET(self):
        loop = asyncio.get_event_loop()
        res = loop.run_until_complete(main(loop, sys.argv[1]))

        self.send_response(200)
        self.end_headers()
        self.wfile.write(b"Hello World!")

        data = res[0]
        ENERGY_DAY.set(data["energy_day"]["value"])
        ENERGY_TOTAL.set(data["energy_total"]["value"])
        ENERGY_YEAR.set(data["energy_year"]["value"])
        POWER_AC.set(data["power_ac"]["value"])


if __name__ == "__main__":
    start_http_server(8000)
    server = http.server.HTTPServer(('', 8001), ServerHandler)
    print("Prometheus metrics available on port 8000 /metrics")
    print("HTTP server available on port 8001")
    server.serve_forever()
