import time
import math
from unitree_sdk2py.core.channel import ChannelFactoryInitialize, ChannelSubscriber
from unitree_sdk2py.idl.unitree_go.msg.dds_ import UwbState_

# Global state
remote_state = UwbState_(
    version=[0, 0],
    channel=0,
    joy_mode=0,
    orientation_est=0.0,
    pitch_est=0.0,
    distance_est=0.0,
    yaw_est=0.0,
    tag_roll=0.0,
    tag_pitch=0.0,
    tag_yaw=0.0,
    base_roll=0.0,
    base_pitch=0.0,
    base_yaw=0.0,
    joystick=[0.0, 0.0],
    error_state=0,
    buttons=0,
    enabled_from_app=0,
)

last_buttons_state = 0  # For detecting changes

BUTTON_MAP = {
    0: "A",
    1: "B",
    2: "X",
    3: "Y",
    4: "L1",
    5: "R1",
    6: "Select",
    7: "Start"
}

def check_buttons(current_buttons):
    global last_buttons_state
    changed = current_buttons ^ last_buttons_state
    if changed == 0:
        return

    for bit, name in BUTTON_MAP.items():
        mask = 1 << bit
        if changed & mask:
            if current_buttons & mask:
                print(f"[Button] Pressed: {name}")
            else:
                print(f"[Button] Released: {name}")

    last_buttons_state = current_buttons

# Callback for updating UWB state
def UwbStateHandler(msg: UwbState_):
    global remote_state
    remote_state = msg
    check_buttons(msg.buttons)

def monitor_orientation_and_buttons():
    ChannelFactoryInitialize(0)
    uwb_sub = ChannelSubscriber("rt/uwbstate", UwbState_)
    uwb_sub.Init(UwbStateHandler, 10)
    time.sleep(1)

    start_time = time.time()
    while time.time() - start_time < 20.0:
        time.sleep(1)


if __name__ == "__main__":
    monitor_orientation_and_buttons()