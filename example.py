#!/usr/bin/env python
"""Basic usage example and testing of pyfronius."""
import asyncio
import logging
import json
import sys
import aiohttp

import pyfronius


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
        for r in res:
            print(json.dumps(r, indent=4))


if __name__ == "__main__":
    #logging.basicConfig(level=logging.DEBUG)
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main(loop, sys.argv[1]))
