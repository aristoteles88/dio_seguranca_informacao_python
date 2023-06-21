import time
from threading import Thread


def car(speed, pilot):
    track = 0
    while track <= 100:
        track += speed
        time.sleep(0.5)
        print(f"Piloyo {pilot} Km {track}\n")


t_car1 = Thread(target=car, args=[1, 'Bruno'])
t_car2 = Thread(target=car, args=[2, 'Python'])

t_car1.start()
t_car2.start()