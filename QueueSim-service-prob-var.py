import numpy as np
import random
import matplotlib.pyplot as plt
import warnings

warnings.filterwarnings('ignore')


class Task:
    def __init__(self, id, arrival_time, waiting_time, departure_time):
        self.id = id
        self.arrival_time = arrival_time
        self.waiting_time = waiting_time
        self.departure_time = departure_time


# task_num = 2000
time_slots = 200000
mean_waiting = []
service_prob_var = [0.3, 0.4, 0.5, 0.6, 0.7, 0.8]
arrival_prob_var = [0.3, 0.4, 0.5, 0.6, 0.7]
service_prob = 0.3
arrival_prob = 0.2

for prob in range(len(service_prob_var)):
    qty = 0
    arrival_prob_random = 0
    service_prob_random = 0
    timeline = 0
    queue = []
    tmp = []
    qty_list = []
    sum = 0
    i = 0
    waiting_time = 0
    service_time = 0
    departure_time = 0
    index = 0
    print(service_prob_var[prob])
    while timeline < time_slots:

        arrival_prob_random = random.random()
        service_prob_random = random.random()

        if service_prob_random < service_prob_var[prob]:
            waiting_time = 0

            if qty > 0:
                qty -= 1
                queue[index].waiting_time = timeline - queue[index].arrival_time
                queue[index].departure_time = timeline
                index = index + 1

        if arrival_prob_random < arrival_prob:
            qty += 1
            i += 1
            arrival = timeline
            queue.append(Task(i, timeline, 0, 0))
        qty_list.append(qty)
        timeline += 1
        sum += qty

    mean = sum / len(qty_list)
    print("mean qty =", mean)
    mean_waiting.append(np.mean([task.waiting_time for task in queue]))
    print("mean waiting = ", mean_waiting)
    print(len(queue))


# ------------ Analytic ------------#
waiting_time_analytic = []
arrival_prob_analytic = 0.2
service_prob_analytic = [0.3, 0.4, 0.5, 0.6, 0.7, 0.8]

for i in range(len(service_prob_analytic)):
    waiting_time_analytic.append(abs((1 - service_prob_analytic[i]) / (arrival_prob_analytic - service_prob_analytic[i])))

print("waiting time analytic = ", waiting_time_analytic)

plt.xlabel("Service Probability")
plt.ylabel("Mean of Waiting time")
x_axis = service_prob_var
y_axis = mean_waiting
plt.plot(x_axis, y_axis, 'y', ls='--')
plt.plot(x_axis, waiting_time_analytic, 'c', ls='-.')
plt.legend(['Simulation', 'Analytic'])
plt.show()
