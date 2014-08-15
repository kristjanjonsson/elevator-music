from trollius import From
import trollius as asyncio

from player import Player


# This function is just to test the stop and next features.
@asyncio.coroutine
def stop_player(player, seconds):
    yield From(asyncio.sleep(seconds))
    player.stop()


def main():
    player = Player()
    loop = asyncio.get_event_loop()

    try:
        tasks = [
            # asyncio.async(stop_player(player, seconds=3)),
            asyncio.async(player.play())
        ]
        loop.run_until_complete(asyncio.wait(tasks))
    finally:
        player.stop()
        loop.close()


if __name__ == "__main__":
    main()
