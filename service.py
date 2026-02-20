import dataclasses
import requests
import enum
import random


# connect to the primary a.py
# failover is b.py
#
#

X = 5
Y = 10
PRIMARY_TRAFFIC = 95.0 / 100
primary_gateway = "localhost:9000"
secondary_gateway = "localhost:9001"


@dataclasses.dataclass
class AvailabilityState:
    n_fails: int = 0
    n_successes: int = 0


class Health(enum.Enum):
    healthy = 0
    unhealthy = 1


# I can combine  the two states, but then it is not granular for different modules

global_availablity = AvailabilityState()
global_health_status = Health.healthy


def service(_):
    # primary block
    if global_health_status == Health.healthy:
        req = requests.get(primary_gateway)
        if req.ok:
            global_availablity.n_successes += 1
            global_availablity.n_fails = 0
            # failure means anything not 2xx
        else:
            global_availablity.n_successes = 0
            global_availablity.n_fails += 1

    else:
        if random.random() < PRIMARY_TRAFFIC:
            req = requests.get(primary_gateway)
            if req.ok:
                global_availablity.n_successes = 0
                global_availablity.n_fails += 1
                # failure means
            else:
                global_availablity.n_successes += 1
                global_availablity.n_fails = 0
        else:
            req = requests.get(secondary_gateway)


if __name__ == "__main__ ":
    queue = [0 for _ in range(10000)]
    for task in queue:
        print(f"queueing {task}")
