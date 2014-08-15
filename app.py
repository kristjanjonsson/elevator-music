import trollius as asyncio

from player import Player


def main():
    player = Player()
    loop = asyncio.get_event_loop()

    try:
        loop.run_until_complete(player.play())
    finally:
        player.stop()
        loop.close()


if __name__ == "__main__":
    main()
