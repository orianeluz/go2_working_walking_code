import json
from unitree_sdk2py.g1.audio.g1_audio_client import AudioClient
from unitree_sdk2py.core.channel import ChannelFactoryInitialize


def main():
    ChannelFactoryInitialize(0)
    print("🔧 Initializing Audio...")
    client = AudioClient()
    print("Initiailized")
    client.SetTimeout(10.0)
    client.Init()
    client.SetVolume(80)
    client.TtsMaker("woooooooof", speaker_id=2)



if __name__ == "__main__":
    main()
