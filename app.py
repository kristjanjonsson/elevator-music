import trollius as asyncio

import player


def main():
    loop = asyncio.get_event_loop()
    loop.run_until_complete(player.play())


if __name__ == "__main__":
    main()
