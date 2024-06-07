from datetime import datetime
from time import sleep

while True:
    dt = datetime.now().strftime("%Y-%m-%dT%H-%M-%S")
    print(f"[{dt}] Test Logging")
    sleep(1)
