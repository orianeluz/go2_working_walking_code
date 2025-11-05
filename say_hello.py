import json
from unitree_sdk2py.go2.sport.sport_client import SportClient
from unitree_sdk2py.core.channel import ChannelFactoryInitialize, ChannelSubscriber


def main():
    ChannelFactoryInitialize(0)
    print("🔧 Initializing SportClient...")
    client = SportClient()
    print("Initiailized")
    client.SetTimeout(10.0)
    client.Init()

    print("👋 Sending 'hello' motion command...")
    client.Hello()



if __name__ == "__main__":
    main()
