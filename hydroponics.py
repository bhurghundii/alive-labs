
import time
from gpiozero import Energenie

# duration for the on and off state (in seconds)
on_duration = 60  # 1 minute
off_duration = 7 * 60  # 7 minutes

def hydroponics_schedule_run(lamp, max_duration=None):

    start_time = time.time()

    while (max_duration if max_duration else True):

        if max_duration and (time.time() - start_time) >= max_duration:
            print("Max duration exceeded")
            break

        lamp.on()
        print("lamp is on for one minute: ", time.time())
        time.sleep(on_duration)
    
        lamp.off()
        print("lamp is off for seven minutes: ", time.time())
        time.sleep(off_duration)

if __name__ == "__main__":
    # initialize the energenie device (lamp)
    lamp = Energenie(1)
    hydroponics_schedule_run(lamp)
