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


class Simulation:
    if __name__ == "__main__":
        # task_num = 2000
        service_is_var = 0
        arrival_is_var = 0
        time_slots = 10000
        qty = 0
        arrival_prob_random = 0
        service_prob_random = 0
        service_prob = 0.3
        arrival_prob = 0.2
        timeline = 0
        queue = []
        tmp = []
        qty_list = []
        sum = 0
        i = 0
        arrival = 0
        waiting_time = 0
        service_time = 0
        departure_time = 0
        index = 0
        while timeline < time_slots:

            arrival_prob_random = random.random()
            service_prob_random = random.random()
            # runs if service prob is not const
            if service_prob_random < service_prob:
                waiting_time = 0

                if qty > 0:
                    qty -= 1

                    # if index < len(queue):
                    queue[index].waiting_time = timeline - queue[index].arrival_time
                    queue[index].departure_time = timeline
                    index = index + 1

            if arrival_prob_random < arrival_prob:
                qty += 1
                i += 1
                arrival = timeline
                queue.append(Task(i, timeline, 0, 0))
                        # tmp.append(Task(i, timeline, 0, 0))
            qty_list.append(qty)
            timeline += 1
            sum += qty

        mean = sum / len(qty_list)
        print("mean qty =", mean)
        mean_waiting = np.mean([task.waiting_time for task in queue])
        print("mean waiting = ", mean_waiting)
        print(len(queue))
        plt.plot(qty_list)
        plt.show()

        plt.plot([task.waiting_time for task in queue])
        plt.show()

        print("id", [task.id for task in queue])
        # print("index", inde)
        print("arrival_time", [task.arrival_time for task in queue])
        print("waiting_time", [task.waiting_time for task in queue])
        print("departure_time", [task.departure_time for task in queue])
