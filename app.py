from datetime import datetime

from trollius import From
import trollius as asyncio


from player import Player
from sensor import Sensor


# This function is just to test the stop and next features.
@asyncio.coroutine
def run_sensor(player):
    sensor = Sensor()
    start_time = datetime.now()
    while True:
        print
        if sensor.get_light_sensor_reading() < 1000:
            player.play()
            start_time = datetime.now()

        if (datetime.now() - start_time).seconds > 30 and player.is_playing():
            player.stop()

        yield From(asyncio.sleep(0.1))


def main():
    player = Player()
    player.play()
    loop = asyncio.get_event_loop()

    try:
        tasks = [
            # asyncio.async(stop_player(player, seconds=3)),
            asyncio.async(player.init()),
            asyncio.async(run_sensor(player))

        ]
        loop.run_until_complete(asyncio.wait(tasks))
    finally:
        player.stop()
        loop.close()


if __name__ == "__main__":
    main()
