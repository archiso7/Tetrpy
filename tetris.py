import time
import Manager

Manager.Start()
while True:
    Manager.Update()
    time.sleep(0.075)