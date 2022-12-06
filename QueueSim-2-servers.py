import numpy as np
import pandas as pd
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
        time_slots = 1000000
        qty = 0
        qty_2nd = 0
        service_prob = 0.3
        service_prob_2nd = 0.3
        arrival_prob = 0.2
        timeline = 0
        queue = []
        queue_2nd = []
        qty_list = []
        qty_list_2nd = []
        total_waiting_time = []
        sum = 0
        sum_2nd = 0
        i = 0
        i_2nd = 0
        arrival = 0
        waiting_time = 0
        service_time = 0
        departure_time = 0
        index = 0
        index2 = 0
        while timeline < time_slots:
            is_arrival = 0
            arrival_prob_random = random.random()
            service_prob_random = random.random()

            if service_prob_random < service_prob:
                waiting_time = 0
                if qty > 0:
                    qty -= 1
                    is_arrival = 1
                    # server 1 packet departure
                    queue[index].waiting_time = timeline - queue[index].arrival_time
                    queue[index].departure_time = timeline
                    index = index + 1
                else:
                    is_arrival = 0

            if arrival_prob_random < arrival_prob:
                qty += 1
                i += 1
                # arrival = timeline
                queue.append(Task(i, timeline, 0, 0))
            qty_list.append(qty)
            timeline += 1
            sum += qty

            service_prob_random_2nd = random.random()

            # server 2 departure
            if service_prob_random_2nd < service_prob_2nd:
                if qty_2nd > 0:
                    qty_2nd -= 1
                    queue_2nd[index2].waiting_time = timeline - queue_2nd[index2].arrival_time
                    queue_2nd[index2].departure_time = timeline
                    index2 += 1

            if is_arrival == 1:
                queue_2nd.append(Task(i_2nd, queue[i_2nd].departure_time, 0, 0))
                i_2nd += 1
                qty_2nd += 1
            qty_list_2nd.append(qty_2nd)
            sum_2nd += qty_2nd

        mean_1 = sum / len(qty_list)
        print("mean qty 1 =", mean_1)
        mean = sum_2nd / len(qty_list_2nd)
        print("mean qty 2 =", mean)
        mean_waiting_1 = np.mean([task.waiting_time for task in queue])
        print("mean waiting queue 1 = ", mean_waiting_1)
        mean_waiting = np.mean([task.waiting_time for task in queue_2nd])
        print("mean waiting queue 2 = ", mean_waiting)
        print("len queue 1 = ", len(queue))
        print("len queue 2 = ", len(queue_2nd))
        for i in range(len(queue_2nd)):
            if queue_2nd[i].departure_time > 0:
                total_waiting_time.append(queue_2nd[i].departure_time - queue[i].arrival_time)
        mean_total_waiting = np.mean(total_waiting_time)
        # total_waiting_time = [[task.departure_time for task in queue_2nd] - [task.arrival_time for task in queue]]
        print("mean total waiting = ", mean_total_waiting)
        # total_waiting = np.mean(np.mean([task.waiting_time for task in queue]) + np.mean([task.waiting_time for
        # task in queue_2nd]))
        # sum_waiting_1 = np.sum([task.waiting_time for task in queue])
        # sum_waiting_2 = np.sum([task.waiting_time for task in queue_2nd])
        # total_waiting = (sum_waiting_1 + sum_waiting_2) / (len(queue) + len(queue_2nd))
        # print("total waiting = ", total_waiting)

        plt.plot(qty_list_2nd)
        plt.show()

        plt.plot([task.waiting_time for task in queue_2nd])
        plt.show()

        data = pd.DataFrame(
            list(zip([task.arrival_time for task in queue], [task.arrival_time for task in queue_2nd],
                     [task.waiting_time for task in queue], [task.waiting_time for task in queue_2nd],
                     [task.departure_time for task in queue], [task.departure_time for task in queue_2nd])),

            columns=['arrival time 1', 'arrival time 2',
                     'waiting time 1', 'waiting time 2',
                     'departure time 1', 'departure time 2'])
        data.to_csv('out.csv')
        # print("id", [task.id for task in queue_2nd])
        # # print("index", inde)
        # print("departure_time", [task.departure_time for task in queue_2nd])
        # print("arrival_time", [task.arrival_time for task in queue])
        # print("waiting_time", [task.waiting_time for task in queue_2nd])

