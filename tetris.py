import time

import Manager

print('\033[2J')
Manager.Start()
while True:
    Manager.Update()
    time.sleep(0.05)