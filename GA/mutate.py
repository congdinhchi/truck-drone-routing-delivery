
import random
import copy

import sys
from config import NUM_DRONE, NUM_TRUCK
from util.load_data import load_list_device
from util.show import show_info_individual

sys.path.append('/Users/dinhchicong/Project/scheduled-delivery')

from util.duplicate import copy_individual
from object.turn import Turn

def choice_mutate(population):
    
    num_individual = len(population)-1
    random_number = random.randint(0,num_individual)

    return population[random_number]

def mutate_turn(turn):

    bound = turn.get_bound()
    weight_package = bound + random.randint(1,50)
    turn.update_bound(weight_package)
    
    # if lucky_num>=0.3:
    #     id_turn = hex(id(turn))

    #     # xoa trip khoi device cu
    #     id_device_old= turn.get_target()
    #     device_old = list_device[id_device_old]
    #     if id_device_old<NUM_DRONE:
    #         check = False
    #         trips = device_old.get_trips()
    #         for trip in trips:
    #             for i in range(0,len(trip)):
    #                 turn_tmp = trip[i]
    #                 if id_turn == hex(id(turn_tmp)):
    #                     trip.pop(i)
    #                     check = True
    #                 if check: break

    #             if check: break
        
    #     else:
    #         trips = device_old.get_trip()
    #         for i in range(0,len(trip)):
    #             turn_tmp = trip[i]
    #             if id_turn == hex(id(turn_tmp)):
    #                 trip.pop(i)
    #                 break

        
    #     id_device_new = random.randint(0, NUM_DRONE+NUM_TRUCK-1)
    #     turn.update_target(id_device_new)



def mutate_chromosomes(id, individual):

    new_individual = copy.deepcopy(individual)
    list_target = new_individual.get_list_target()
    list_device = new_individual.get_list_device()
    for j in range(0,len(list_target)):

        target = list_target[j]
        id_target = target.get_id()
        trip = target.get_trip()

        # dot bien
        for turn in trip:
            tmp = random.random()
            if tmp<0.3:
                mutate_turn(turn)
        
        tmp = random.random()
        if tmp<0.5:

            weight = random.randint(1,10)
            id_device = random.randint(0, NUM_DRONE+NUM_TRUCK-1)
            device = list_device[id_device]
            turn = Turn(id_target, id_device, weight)
            target.add_turn(turn)

            if id_device < NUM_DRONE:
                trips = device.get_trips()
                num_trip = len(trips)
                if num_trip != 0:
                    id_trip = random.randint(0, num_trip-1)
                else:
                    id_trip = 0
                trip_tmp = trips[id_trip]
                num_turn = len(trip_tmp)  
                id_turn = random.randint(0, num_turn-1)

                device.append_turn(turn, id_trip, id_turn)
            else:
                trip_tmp = device.get_trip()
                num_turn = len(trip_tmp)  
                id_turn = random.randint(0, num_turn-1)
                device.append_turn(turn, id_turn)

        # else:
        #     print("trip cu {}".format(trip))
        #     num_turn = len(trip)
        #     try:
        #         lucky_num = random.randint(0, num_turn-1)
        #     except: 
        #         lucky_num = 0
        #     # bo o ben device
        #     print("turn la {}".format(turn.get_target()))
        #     id_device = turn.get_device()
        #     device = list_device[id_device]

        #     if id_device < NUM_DRONE:
        #         trips = device.get_trips()
        #         for trip_tmp in trips:
        #             for i in range (0, len(trip_tmp)):
        #                 turn_tmp = trip_tmp[i]
        #                 if hex(id(turn_tmp)) == hex(id(trip[lucky_num])):
        #                     trip.pop(i)
        #     else:
        #         trip_tmp = device.get_trip()
        #         for i in range (0, len(trip)):
        #             turn_tmp = trip_tmp[i]
        #             if hex(id(turn_tmp)) == hex(id(trip[lucky_num])):
        #                 trip.pop(i)

        #     # bo o ben target
        #     trip.pop(lucky_num)
        #     print("trip moi {}".format(trip))

    new_individual = copy_individual(id, new_individual)
    return new_individual