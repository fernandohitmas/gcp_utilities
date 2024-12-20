import pendulum 

RESOURCE_NAME = 'RESOURCE_NAME'

run_time = pendulum.datetime(2024, 1, 1)
end_dt = pendulum.datetime(2024, 1, 5)

command = f"bq mk --transfer_run --run_time='{run_time.isoformat()}' {RESOURCE_NAME}"
subprocess.run(command.split(' '), capture_output=True)


while run_time < end_dt:
    command = f"bq mk --transfer_run --run_time='{run_time.isoformat()}' {RESOURCE_NAME}"
    
    print(command)

    # Go to next day
    run_time = run_time.add(days=1)
