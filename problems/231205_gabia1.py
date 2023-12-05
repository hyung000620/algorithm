"""

"""
import itertools
import math

def calc_time(power, distances, fuel):

    if fuel == 0:
        return float('INF')

    final_velocity = power*fuel
    accel_time = final_velocity / power
    dist_accel = 0.5 * power * accel_time ** 2
    remain_dist = distances - dist_accel
    total_time = remain_dist/ final_velocity + accel_time
    
    return total_time

def solution(fuel, powers, distances):
    min_time = float('INF')
    
    for fuel_dist in itertools.product(range(fuel+1), repeat = len(powers)):
        if sum(fuel_dist) == fuel:
            times = [calc_time(p,d,f) for p, d, f in zip(powers, distances, fuel_dist)]
            max_time = max(times)

            if max_time < min_time:
                min_time = max_time

    return int(math.ceil(min_time))