import asyncio

# async def make_tea():
#     print("Boiling water...")
#     await asyncio.sleep(3)
#     print("Tea ready")

# async def make_toast():
#     print("Toasting bread...")
#     await asyncio.sleep(2)
#     print("Toast ready")

# # async def main():
# #     await make_tea()
# #     await make_toast()

# # asyncio.run(main())

# async def main():
#     await asyncio.gather(
#         make_tea(),
#         make_toast(),
#     )

# asyncio.run(main())


async def get_number(n, delay):
    await asyncio.sleep(delay)
    return n

async def main():
    results = await asyncio.gather(
        get_number(1, 3),
        get_number(2, 1),
        get_number(3, 2),
    return_exceptions=True)
    print(results)   # [1, 2, 3] — order matches how you called gather, not finish order

asyncio.run(main())