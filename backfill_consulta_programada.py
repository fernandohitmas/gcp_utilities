import pendulum 
import pyperclip
RESOURCE_NAME = 'RESOURCE_NAME'

run_time = pendulum.datetime(2024, 2, 1)
end_dt = pendulum.datetime(2024, 12, 8)

command = ''

while run_time <= end_dt:
    command = command + f"bq mk --transfer_run --run_time='{run_time.isoformat()}' {RESOURCE_NAME}\n"
    
    # Go to next day
    run_time = run_time.add(days=1)

pyperclip.copy(command)