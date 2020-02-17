#!/usr/bin/env python3
# rand.py

import asyncio
import random

# ANSI colors
c = (
    "\033[1;0;40m", # End of color
    "\033[1;36;40m", # Cyan
    "\033[1;91;40m", # Red
    "\033[1;35;40m" # Magenta
)

async def makaerndom(idx: int, threshold: int = 6) -> int:
    print(c[idx+1] + f"Initiated makerandom({idx}).")
    i = random.randint(0,10)
    while i <= threshold:
        print(c[idx+1] + f"makerandom({idx}) == {i} too low; retrying.")
        await asyncio.sleep(idx+1)
        i = random.randint(0,10)
    print(c[idx+1] + f"---> Finished: makerandom({idx}) == {i}" + c[0])
    return i

async def main():
    res = await asyncio.gather(*(makaerndom(i, 10-i-1) for i in range(3)))
    return res

if __name__ == "__main__":
    random.seed(444)
    r1, r2, r3 = asyncio.run(main())
    print()
    print(f"r1: {r1}, r2: {r2}, r3: {r3}")