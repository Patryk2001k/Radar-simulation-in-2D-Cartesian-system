from objects import Radar, Object, World
import asyncio

# Example of how we can use it
#world = World(100, 100)
#obj = Object(1, 0, 0, 1)
#world.add_object(obj)
#radar = Radar(0, 0, 20, 45, world)

    
async def update_world(world):
    while True:
        world.update()
        await asyncio.sleep(2)

async def rotate_radar(radar):
    while True:
        print(radar.rotate_and_scan())
        await asyncio.sleep(2)

async def main():
    world = World(100, 100)
    obj = Object(5, 5, 1, 1)
    world.add_object(obj)

    radar = Radar(0, 0, 20, 90, world)

    world_task = asyncio.create_task(update_world(world))
    radar_task = asyncio.create_task(rotate_radar(radar))

    try:
        await asyncio.gather(world_task, radar_task)
    except asyncio.CancelledError as Error:
        print(Error)

if __name__ == "__main__":
    asyncio.run(main())