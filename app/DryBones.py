import json
import os
import random
import bottle
import time

from api import ping_response, start_response, move_response, end_response

from print_grid import *

@bottle.route('/')
def index():
    return '''
    Battlesnake documentation can be found at
       <a href="https://docs.battlesnake.io">https://docs.battlesnake.io</a>.
    '''

@bottle.route('/static/<path:path>')
def static(path):
    """
    Given a path, return the static file located relative
    to the static folder.

    This can be used to return the snake head URL in an API response.
    """
    return bottle.static_file(path, root='static/')

@bottle.post('/ping')
def ping():
    """
    A keep-alive endpoint used to prevent cloud application platforms,
    such as Heroku, from sleeping the application instance.
    """
    return ping_response()

@bottle.post('/start')
def start():
    data = bottle.request.json

    """
    TODO: If you intend to have a stateful snake AI,
            initialize your snake state here using the
            request's data if necessary.
    """
    #print(json.dumps(data))

    color = "#C0C0C0"

    return start_response(color)


@bottle.post('/move')
def move():
    starttime = time.time()
    jsonData = bottle.request.json
    #print(jsonData)
    
    height_of_board = jsonData["board"]["height"]
    width_of_board = jsonData["board"]["width"]
    my_head_x_component= jsonData["you"]["body"][0]["x"]
    my_head_y_component= jsonData["you"]["body"][0]["y"]
    
    #print("\n\n\n")
    
    
    
    ##print_grid(jsonData)
    ##print_grid_and_possible_movements(jsonData)
    #print_grid_and_safespots(jsonData)
    
    ##print(height_of_board)
    ##print(width_of_board)
    ##print("my location, x component", my_head_x_component)
    ##print("my location, y component", my_head_y_component)
    
    Direction = "up"
    
    possible_directions = ["left","right","up","down"]
    
    Direction= choose_direction(jsonData,my_head_x_component,my_head_y_component)
    
    

    # #Can you move towards the food in the y direction
    # Direction = look_for_food_y_precedence(jsonData,my_head_x_component,my_head_y_component)
    # #print("Am I going to kill myself?",am_i_about_to_kill_my_self(jsonData,my_head_x_component,my_head_y_component,Direction))
    
    # #No? Can you move towards the food in the x direction
    # if am_i_about_to_kill_my_self(jsonData,my_head_x_component,my_head_y_component,Direction):
        # ##print("Going into x-direction emergency mode")
        # possible_directions.remove(Direction)
        # Direction = look_for_food_x_precedence(jsonData,my_head_x_component,my_head_y_component)
        
    # #Am I still going to die?? Let's just choose any old direction
    # if am_i_about_to_kill_my_self(jsonData,my_head_x_component,my_head_y_component,Direction):
        # #print("Choosing random safe direction") 
        # possible_directions.remove(Direction)
        
        # Direction = possible_directions[0]
        
        # #lets go any way whatsoever as long as its safe
        
    
    ##print("Direction", Direction)
    
    test=snake_location_copyjsonData(jsonData,my_head_x_component,my_head_y_component)
    
    # simulation = simulate(test,my_head_x_component,my_head_y_component,Direction)
    # #print("one turn simulation is:", simulation)
    
    # #print_grid_and_safespots_simulation(simulation,jsonData,"1-1")
    
    # simulation2 = simulate(simulation,my_head_x_component,my_head_y_component,  choose_direction_simulation(simulation,jsonData)  )
    # #print_grid_and_safespots_simulation(simulation2,jsonData,"1-2")
    
    e = 1
    
    number_of_simulations_to_run=50
    
    
     # ------------------------------------------------------------------------------------------------------------------------------------------- 1
    while e<=number_of_simulations_to_run:
        if e==1:
            curent_simulation = simulate(snake_location_copyjsonData(jsonData,my_head_x_component,my_head_y_component),Direction,jsonData)[0]
            ##print(simulate(snake_location_copyjsonData(jsonData,my_head_x_component,my_head_y_component),Direction,jsonData)[1])
            if simulate(snake_location_copyjsonData(jsonData,my_head_x_component,my_head_y_component),Direction,jsonData)[1] == "Simulation snake is dead":
                ##print("break. Snake survived ",e, "simulations. Last location was: ", curent_simulation[0][0], "," , curent_simulation[0][1])
                break
            ##print_grid_and_safespots_simulation(curent_simulation,jsonData,"1-1")
        else:
            curent_simulation= simulate (curent_simulation,  choose_direction_simulation_close_precedence(curent_simulation,jsonData),jsonData)[0]
            ##print(simulate (curent_simulation,  choose_direction_simulation_close_precedence(curent_simulation,jsonData),jsonData)[1])
            if simulate (curent_simulation,  choose_direction_simulation_close_precedence(curent_simulation,jsonData),jsonData)[1] == "Simulation snake is dead":
                ##print("break. Snake survived ",e, "simulations. Last location was: ", curent_simulation[0][0], "," , curent_simulation[0][1])
                break
            r= "1-" +str(e)
            ##print_grid_and_safespots_simulation(curent_simulation,jsonData,r)
        e+=1
    
    best_direction= Direction
    last_location=[curent_simulation[0][0],curent_simulation[0][1]]
    number_of_simulations_survived=e-1
    
    e = 1
     # ------------------------------------------------------------------------------------------------------------------------------------------- 2
    while e<=number_of_simulations_to_run:
        if e==1:
            curent_simulation = simulate(snake_location_copyjsonData(jsonData,my_head_x_component,my_head_y_component),Direction,jsonData)[0]
            ##print(simulate(snake_location_copyjsonData(jsonData,my_head_x_component,my_head_y_component),Direction,jsonData)[1])
            if simulate(snake_location_copyjsonData(jsonData,my_head_x_component,my_head_y_component),Direction,jsonData)[1] == "Simulation snake is dead":
                ##print("break. Snake survived ",e, "simulations. Last location was: ", curent_simulation[0][0], "," , curent_simulation[0][1])
                break
            ##print_grid_and_safespots_simulation(curent_simulation,jsonData,"2-1")
        else:
            curent_simulation= simulate (curent_simulation,  choose_direction_simulation_far_precedence(curent_simulation,jsonData),jsonData)[0]
            ##print(simulate (curent_simulation,  choose_direction_simulation_far_precedence(curent_simulation,jsonData),jsonData)[1])
            if simulate (curent_simulation,  choose_direction_simulation_far_precedence(curent_simulation,jsonData),jsonData)[1] == "Simulation snake is dead":
                ##print("break. Snake survived ",e, "simulations. Last location was: ", curent_simulation[0][0], "," , curent_simulation[0][1])
                break
            r= "2-" +str(e)
            ##print_grid_and_safespots_simulation(curent_simulation,jsonData,r)
        e+=1
    
    if last_location!=[curent_simulation[0][0],curent_simulation[0][1]]:
        if number_of_simulations_survived<(e-1):
            best_direction= Direction
            last_location=[curent_simulation[0][0],curent_simulation[0][1]]
            number_of_simulations_survived=e-1
    
    # if last_location==[curent_simulation[0][0],curent_simulation[0][1]]:
        # if number_of_simulations_survived>(e-1):
            # best_direction= Direction
            # last_location=[curent_simulation[0][0],curent_simulation[0][1]]
            # number_of_simulations_survived=e-1
    
    e = 2
     # ------------------------------------------------------------------------------------------------------------------------------------------- 3
     # -------------------------------------------------------------------------------------------------------------------------------------------
    curent_simulation = simulate(snake_location_copyjsonData(jsonData,my_head_x_component,my_head_y_component),"left",jsonData)[0]
    ##print_grid_and_safespots_simulation(curent_simulation,jsonData,"3-1")
    if simulate(snake_location_copyjsonData(jsonData,my_head_x_component,my_head_y_component),"left",jsonData)[1] == "Simulation snake is dead":
        ##print("Don't simulate. Snake survived ",e, "simulations. Last location was: ", curent_simulation[0][0], "," , curent_simulation[0][1])
        spacesaver=1
    else:
        while e<=number_of_simulations_to_run:
            if e==1:
                curent_simulation = simulate(snake_location_copyjsonData(jsonData,my_head_x_component,my_head_y_component),Direction,jsonData)[0]
                ##print(simulate(snake_location_copyjsonData(jsonData,my_head_x_component,my_head_y_component),Direction,jsonData)[1])
                if simulate(snake_location_copyjsonData(jsonData,my_head_x_component,my_head_y_component),Direction,jsonData)[1] == "Simulation snake is dead":
                    ##print("break. Snake survived ",e, "simulations. Last location was: ", curent_simulation[0][0], "," , curent_simulation[0][1])
                    break
                ##print_grid_and_safespots_simulation(curent_simulation,jsonData,"3-2")
            else:
                curent_simulation= simulate (curent_simulation,  choose_direction_simulation_close_precedence(curent_simulation,jsonData),jsonData)[0]
                ##print(simulate (curent_simulation,  choose_direction_simulation_close_precedence(curent_simulation,jsonData),jsonData)[1])
                if simulate (curent_simulation,  choose_direction_simulation_close_precedence(curent_simulation,jsonData),jsonData)[1] == "Simulation snake is dead":
                    ##print("break. Snake survived ",e, "simulations. Last location was: ", curent_simulation[0][0], "," , curent_simulation[0][1])
                    break
                r= "3-" +str(e)
                ##print_grid_and_safespots_simulation(curent_simulation,jsonData,r)
            e+=1
    
    if last_location!=[curent_simulation[0][0],curent_simulation[0][1]]:
        if number_of_simulations_survived<(e-1):
            best_direction= "left"
            last_location=[curent_simulation[0][0],curent_simulation[0][1]]
            number_of_simulations_survived=e-1
    
    # if last_location==[curent_simulation[0][0],curent_simulation[0][1]]:
        # if number_of_simulations_survived>(e-1):
            # best_direction= "left"
            # last_location=[curent_simulation[0][0],curent_simulation[0][1]]
            # number_of_simulations_survived=e-1
    
    
    
    e = 2
     # ------------------------------------------------------------------------------------------------------------------------------------------- 4
    curent_simulation = simulate(snake_location_copyjsonData(jsonData,my_head_x_component,my_head_y_component),"up",jsonData)[0]
    ##print_grid_and_safespots_simulation(curent_simulation,jsonData,"4-1")
    if simulate(snake_location_copyjsonData(jsonData,my_head_x_component,my_head_y_component),"up",jsonData)[1] == "Simulation snake is dead":
        ##print("Don't simulate. Snake survived ",e, "simulations. Last location was: ", curent_simulation[0][0], "," , curent_simulation[0][1])
        spacesaver=1
    else:
        while e<=number_of_simulations_to_run:
            if e==1:
                curent_simulation = simulate(snake_location_copyjsonData(jsonData,my_head_x_component,my_head_y_component,jsonData),Direction)[0]
                ##print(simulate(snake_location_copyjsonData(jsonData,my_head_x_component,my_head_y_component),Direction,jsonData)[1])
                if simulate(snake_location_copyjsonData(jsonData,my_head_x_component,my_head_y_component),Direction,jsonData)[1] == "Simulation snake is dead":
                    ##print("break. Snake survived ",e, "simulations. Last location was: ", curent_simulation[0][0], "," , curent_simulation[0][1])
                    break
                ###print_grid_and_safespots_simulation(curent_simulation,jsonData,"4-2")
            else:
                curent_simulation= simulate (curent_simulation,  choose_direction_simulation_close_precedence(curent_simulation,jsonData),jsonData)[0]
                ##print(simulate (curent_simulation,  choose_direction_simulation_close_precedence(curent_simulation,jsonData),jsonData)[1])
                if simulate (curent_simulation,  choose_direction_simulation_close_precedence(curent_simulation,jsonData),jsonData)[1] == "Simulation snake is dead":
                    ##print("break. Snake survived ",e, "simulations. Last location was: ", curent_simulation[0][0], "," , curent_simulation[0][1])
                    break
                r= "4-" +str(e)
                ###print_grid_and_safespots_simulation(curent_simulation,jsonData,r)
            e+=1
    
    
    if last_location!=[curent_simulation[0][0],curent_simulation[0][1]]:
        if number_of_simulations_survived<(e-1):
            best_direction= "up"
            last_location=[curent_simulation[0][0],curent_simulation[0][1]]
            number_of_simulations_survived=e-1
    
    # if last_location==[curent_simulation[0][0],curent_simulation[0][1]]:
        # if number_of_simulations_survived>(e-1):
            # best_direction= "up"
            # last_location=[curent_simulation[0][0],curent_simulation[0][1]]
            # number_of_simulations_survived=e-1
    
    
    e = 2
     # ------------------------------------------------------------------------------------------------------------------------------------------- 5
    curent_simulation = simulate(snake_location_copyjsonData(jsonData,my_head_x_component,my_head_y_component),"right",jsonData)[0]
    ###print_grid_and_safespots_simulation(curent_simulation,jsonData,"5-1")
    if simulate(snake_location_copyjsonData(jsonData,my_head_x_component,my_head_y_component),"right",jsonData)[1] == "Simulation snake is dead":
        ##print("Don't simulate. Snake survived ",e, "simulations. Last location was: ", curent_simulation[0][0], "," , curent_simulation[0][1])
        spacesaver=1
    else:
        while e<=number_of_simulations_to_run:
            if e==1:
                curent_simulation = simulate(snake_location_copyjsonData(jsonData,my_head_x_component,my_head_y_component),Direction,jsonData)[0]
                ##print(simulate(snake_location_copyjsonData(jsonData,my_head_x_component,my_head_y_component),Direction,jsonData)[1])
                if simulate(snake_location_copyjsonData(jsonData,my_head_x_component,my_head_y_component),Direction,jsonData)[1] == "Simulation snake is dead":
                    ##print("break. Snake survived ",e, "simulations. Last location was: ", curent_simulation[0][0], "," , curent_simulation[0][1])
                    break
                ###print_grid_and_safespots_simulation(curent_simulation,jsonData,"5-2")
            else:
                curent_simulation= simulate (curent_simulation,  choose_direction_simulation_close_precedence(curent_simulation,jsonData),jsonData)[0]
                ##print(simulate (curent_simulation,  choose_direction_simulation_close_precedence(curent_simulation,jsonData),jsonData)[1])
                if simulate (curent_simulation,  choose_direction_simulation_close_precedence(curent_simulation,jsonData),jsonData)[1] == "Simulation snake is dead":
                    ##print("break. Snake survived ",e, "simulations. Last location was: ", curent_simulation[0][0], "," , curent_simulation[0][1])
                    break
                r= "5-" +str(e)
                ###print_grid_and_safespots_simulation(curent_simulation,jsonData,r)
            e+=1
        
    
    if last_location!=[curent_simulation[0][0],curent_simulation[0][1]]:
        if number_of_simulations_survived<(e-1):
            best_direction= "right"
            last_location=[curent_simulation[0][0],curent_simulation[0][1]]
            number_of_simulations_survived=e-1
    
    # if last_location==[curent_simulation[0][0],curent_simulation[0][1]]:
        # if number_of_simulations_survived>(e-1):
            # best_direction= "right"
            # last_location=[curent_simulation[0][0],curent_simulation[0][1]]
            # number_of_simulations_survived=e-1
    
    
    
    e = 2
     # ------------------------------------------------------------------------------------------------------------------------------------------- 6
    curent_simulation = simulate(snake_location_copyjsonData(jsonData,my_head_x_component,my_head_y_component),"down",jsonData)[0]
    ###print_grid_and_safespots_simulation(curent_simulation,jsonData,"6-1")
    if simulate(snake_location_copyjsonData(jsonData,my_head_x_component,my_head_y_component),"down",jsonData)[1] == "Simulation snake is dead":
        ##print("Don't simulate. Snake survived ",e, "simulations. Last location was: ", curent_simulation[0][0], "," , curent_simulation[0][1])
        spacesaver=1
    
    else:
        while e<=number_of_simulations_to_run:
            if e==1:
                curent_simulation = simulate(snake_location_copyjsonData(jsonData,my_head_x_component,my_head_y_component),Direction,jsonData)[0]
                ##print(simulate(snake_location_copyjsonData(jsonData,my_head_x_component,my_head_y_component),Direction,jsonData)[1])
                if simulate(snake_location_copyjsonData(jsonData,my_head_x_component,my_head_y_component),Direction,jsonData)[1] == "Simulation snake is dead":
                    ##print("break. Snake survived ",e, "simulations. Last location was: ", curent_simulation[0][0], "," , curent_simulation[0][1])
                    break
                ###print_grid_and_safespots_simulation(curent_simulation,jsonData,"6-2")
            else:
                curent_simulation= simulate (curent_simulation,  choose_direction_simulation_close_precedence(curent_simulation,jsonData),jsonData)[0]
                ##print(simulate (curent_simulation,  choose_direction_simulation_close_precedence(curent_simulation,jsonData),jsonData)[1])
                if simulate (curent_simulation,  choose_direction_simulation_close_precedence(curent_simulation,jsonData),jsonData)[1] == "Simulation snake is dead":
                    ##print("break. Snake survived ",e, "simulations. Last location was: ", curent_simulation[0][0], "," , curent_simulation[0][1])
                    break
                r= "6-" +str(e)
                ###print_grid_and_safespots_simulation(curent_simulation,jsonData,r)
            e+=1

    
    if last_location!=[curent_simulation[0][0],curent_simulation[0][1]]:
        if number_of_simulations_survived<(e-1):
            best_direction= "down"
            last_location=[curent_simulation[0][0],curent_simulation[0][1]]
            number_of_simulations_survived=e-1
    
    # if last_location==[curent_simulation[0][0],curent_simulation[0][1]]:
        # if number_of_simulations_survived>(e-1):
            # best_direction= "down"
            # last_location=[curent_simulation[0][0],curent_simulation[0][1]]
            # number_of_simulations_survived=e-1
    
    
    
    print("\n\nBest Direction: ", best_direction,"\nLast Location: ", last_location,"\n Number of simulations survived: ", number_of_simulations_survived)
    
    Direction=best_direction
    
    print("Direction is: ", Direction)

    
    endtime=time.time()
    print("time: " , endtime-starttime)
    
    return move_response(Direction)


def choose_direction(jsonData,my_head_x_component,my_head_y_component):
    
    food_location_relative_to_me=find_food_location_relative_to_me(jsonData,my_head_x_component,my_head_y_component)
    #print("Food location relative to me: " ,food_location_relative_to_me)
    ##print("Food location[0]",food_location_relative_to_me[0])
    
    if abs(food_location_relative_to_me[0])>abs(food_location_relative_to_me[1]):
        if food_location_relative_to_me[0]>0:
            Direction="right"
            #print("Food is to the right. Direction equals ", Direction)
        elif food_location_relative_to_me[0]<0:
            Direction= "left"
            #print("Food is to the left. Direction equals ", Direction)
            
    else:
        if food_location_relative_to_me[1]>0:
            Direction="up"
            #print("Food is above. Direction equals ", Direction)
        elif food_location_relative_to_me[1]<0:
            Direction= "down"
            #print("Food is below. Direction equals ", Direction)
            
    
    #print("Am I going to kill myself? line 59",am_i_about_to_kill_my_self(jsonData,my_head_x_component,my_head_y_component,Direction))
    if am_i_about_to_kill_my_self(jsonData,my_head_x_component,my_head_y_component,Direction):
        if (Direction == "right") or (Direction == "left"):
            #print("line 62")
            if food_location_relative_to_me[1]>0:
                Direction="up"
                #print("Food is above. Direction equals ", Direction)
            else: #if food_location_relative_to_me[1]<0:
                Direction= "down"
                #print("Food is below. Direction equals ", Direction)
            #print("Am I going to kill myself? line 69",am_i_about_to_kill_my_self(jsonData,my_head_x_component,my_head_y_component,Direction))
            if am_i_about_to_kill_my_self(jsonData,my_head_x_component,my_head_y_component,Direction):
                Direction=switch_direction(Direction)
                #print("Direction equals ", Direction)
                
            #print("Am I going to kill myself? line 74",am_i_about_to_kill_my_self(jsonData,my_head_x_component,my_head_y_component,Direction))
            if am_i_about_to_kill_my_self(jsonData,my_head_x_component,my_head_y_component,Direction):
                Direction= go_any_safe_direction(jsonData,my_head_x_component,my_head_y_component)
                #print("Any safe direction.Direction equals ", Direction)

        elif (Direction == "up") or (Direction == "down"):
            #print("line 76")
            if food_location_relative_to_me[0]>0:
                Direction="right"
                #print("Food is to the right. Direction equals ", Direction)
            else: #if food_location_relative_to_me[0]<0:
                Direction= "left"
                #print("Food is to the left. Direction equals ", Direction)
            #print("Am I going to kill myself? line 87",am_i_about_to_kill_my_self(jsonData,my_head_x_component,my_head_y_component,Direction))
            if am_i_about_to_kill_my_self(jsonData,my_head_x_component,my_head_y_component,Direction):
                Direction=switch_direction(Direction)
                #print("Direction equals ", Direction)
                
            #print("Am I going to kill myself? line 92",am_i_about_to_kill_my_self(jsonData,my_head_x_component,my_head_y_component,Direction))
            if am_i_about_to_kill_my_self(jsonData,my_head_x_component,my_head_y_component,Direction):
                Direction= go_any_safe_direction(jsonData,my_head_x_component,my_head_y_component)
                #print("Any safe direction.Direction equals ", Direction)
    
    return (Direction)



def choose_direction_simulation_close_precedence(simulation_data,jsonData):
    my_head_x_component= simulation_data[0][0]
    my_head_y_component= simulation_data[0][1]
    
    Direction = "up"
    
    food_location_relative_to_me= find_food_location_relative_to_me_simulation(simulation_data,jsonData)
    ##print("Food location relative to me: " ,food_location_relative_to_me)
    ##print("Food location[0]",food_location_relative_to_me[0])
    
    if abs(food_location_relative_to_me[0])>abs(food_location_relative_to_me[1]):
        if food_location_relative_to_me[0]>0:
            Direction="right"
            ##print("Food is to the right. Direction equals ", Direction)
        elif food_location_relative_to_me[0]<0:
            Direction= "left"
            ##print("Food is to the left. Direction equals ", Direction)
            
    else:
        if food_location_relative_to_me[1]>0:
            Direction="up"
            ##print("Food is above. Direction equals ", Direction)
        elif food_location_relative_to_me[1]<0:
            Direction= "down"
            ##print("Food is below. Direction equals ", Direction)
            
    
    ##print("Am I going to kill myself? line 190",am_i_about_to_kill_my_self_simulation(simulation_data,jsonData,Direction))
    if am_i_about_to_kill_my_self_simulation(simulation_data,jsonData,Direction):
        if (Direction == "right") or (Direction == "left"):
            ##print("line 193")
            if food_location_relative_to_me[1]>0:
                Direction="up"
                ##print("Food is above. Direction equals ", Direction)
            else: #if food_location_relative_to_me[1]<0:
                Direction= "down"
                ##print("Food is below. Direction equals ", Direction)
            ##print("Am I going to kill myself? line 200",am_i_about_to_kill_my_self_simulation(simulation_data,jsonData,Direction))
            if am_i_about_to_kill_my_self_simulation(simulation_data,jsonData,Direction):
                Direction=switch_direction(Direction)
                ##print("Direction equals ", Direction)
                
            ##print("Am I going to kill myself? line 206",am_i_about_to_kill_my_self_simulation(simulation_data,jsonData,Direction))
            if am_i_about_to_kill_my_self_simulation(simulation_data,jsonData,Direction):
                Direction= go_any_safe_direction_simulation(simulation_data,jsonData)
                ##print("Any safe direction.Direction equals ", Direction)

        elif (Direction == "up") or (Direction == "down"):
            ##print("line 212")
            if food_location_relative_to_me[0]>0:
                Direction="right"
                ##print("Food is to the right. Direction equals ", Direction)
            else: #if food_location_relative_to_me[0]<0:
                Direction= "left"
                ##print("Food is to the left. Direction equals ", Direction)
            ##print("Am I going to kill myself? line 218",am_i_about_to_kill_my_self_simulation(simulation_data,jsonData,Direction))
            if am_i_about_to_kill_my_self(jsonData,my_head_x_component,my_head_y_component,Direction):
                Direction=switch_direction(Direction)
                ##print("Direction equals ", Direction)
                
            ##print("Am I going to kill myself? line 223",am_i_about_to_kill_my_self_simulation(simulation_data,jsonData,Direction))
            if am_i_about_to_kill_my_self_simulation(simulation_data,jsonData,Direction):
                Direction= go_any_safe_direction_simulation(simulation_data,jsonData)
                ##print("Any safe direction.Direction equals ", Direction)
    
    return (Direction)



def choose_direction_simulation_far_precedence(simulation_data,jsonData):
    my_head_x_component= simulation_data[0][0]
    my_head_y_component= simulation_data[0][1]
    
    Direction = "up"
    
    food_location_relative_to_me= find_food_location_relative_to_me_simulation(simulation_data,jsonData)
    ##print("Food location relative to me: " ,food_location_relative_to_me)
    ###print("Food location[0]",food_location_relative_to_me[0])
    
    if abs(food_location_relative_to_me[0])<abs(food_location_relative_to_me[1]):
        if food_location_relative_to_me[0]>0:
            Direction="right"
            ##print("Food is to the right. Direction equals ", Direction)
        elif food_location_relative_to_me[0]<0:
            Direction= "left"
            ##print("Food is to the left. Direction equals ", Direction)
            
    else:
        if food_location_relative_to_me[1]>0:
            Direction="up"
            ##print("Food is above. Direction equals ", Direction)
        elif food_location_relative_to_me[1]<0:
            Direction= "down"
            ##print("Food is below. Direction equals ", Direction)
            
    
    ##print("Am I going to kill myself? line 190",am_i_about_to_kill_my_self_simulation(simulation_data,jsonData,Direction))
    if am_i_about_to_kill_my_self_simulation(simulation_data,jsonData,Direction):
        if (Direction == "right") or (Direction == "left"):
            ##print("line 193")
            if food_location_relative_to_me[1]>0:
                Direction="up"
                ##print("Food is above. Direction equals ", Direction)
            else: #if food_location_relative_to_me[1]<0:
                Direction= "down"
                ##print("Food is below. Direction equals ", Direction)
            ##print("Am I going to kill myself? line 200",am_i_about_to_kill_my_self_simulation(simulation_data,jsonData,Direction))
            if am_i_about_to_kill_my_self_simulation(simulation_data,jsonData,Direction):
                Direction=switch_direction(Direction)
                ##print("Direction equals ", Direction)
                
            ##print("Am I going to kill myself? line 206",am_i_about_to_kill_my_self_simulation(simulation_data,jsonData,Direction))
            if am_i_about_to_kill_my_self_simulation(simulation_data,jsonData,Direction):
                Direction= go_any_safe_direction_simulation(simulation_data,jsonData)
                ##print("Any safe direction.Direction equals ", Direction)

        elif (Direction == "up") or (Direction == "down"):
            ##print("line 212")
            if food_location_relative_to_me[0]>0:
                Direction="right"
                ##print("Food is to the right. Direction equals ", Direction)
            else: #if food_location_relative_to_me[0]<0:
                Direction= "left"
                ##print("Food is to the left. Direction equals ", Direction)
            ##print("Am I going to kill myself? line 218",am_i_about_to_kill_my_self_simulation(simulation_data,jsonData,Direction))
            if am_i_about_to_kill_my_self(jsonData,my_head_x_component,my_head_y_component,Direction):
                Direction=switch_direction(Direction)
                ##print("Direction equals ", Direction)
                
            ##print("Am I going to kill myself? line 223",am_i_about_to_kill_my_self_simulation(simulation_data,jsonData,Direction))
            if am_i_about_to_kill_my_self_simulation(simulation_data,jsonData,Direction):
                Direction= go_any_safe_direction_simulation(simulation_data,jsonData)
                ##print("Any safe direction.Direction equals ", Direction)
    
    return (Direction)



def go_any_safe_direction(jsonData,my_head_x_component,my_head_y_component):
    go_any_safe_direction_direction="left"
    #print("Is left safe?")
    if am_i_about_to_kill_my_self(jsonData,my_head_x_component,my_head_y_component,go_any_safe_direction_direction):
        #print("No, is right safe?")
        go_any_safe_direction_direction="right"
        if am_i_about_to_kill_my_self(jsonData,my_head_x_component,my_head_y_component,go_any_safe_direction_direction):
            #print("No, is up safe?")
            go_any_safe_direction_direction="up"
            if am_i_about_to_kill_my_self(jsonData,my_head_x_component,my_head_y_component,go_any_safe_direction_direction):
                #print("No, is down safe?")
                go_any_safe_direction_direction="down"
                if am_i_about_to_kill_my_self(jsonData,my_head_x_component,my_head_y_component,go_any_safe_direction_direction):
                    #print("Nothing is safe")
                    return("Nonesafe")
                else:
                    return(go_any_safe_direction_direction)
            else:
                return(go_any_safe_direction_direction)
        else:
            return(go_any_safe_direction_direction)
    else:
        return(go_any_safe_direction_direction)



def go_any_safe_direction_simulation(simulation_data,jsonData):
    my_head_x_component= simulation_data[0][0]
    my_head_y_component= simulation_data[0][1]
    
    
    go_any_safe_direction_direction="left"
    ##print("Is left safe?")
    if am_i_about_to_kill_my_self_simulation(simulation_data,jsonData,go_any_safe_direction_direction):
        ##print("No, is right safe?")
        go_any_safe_direction_direction="right"
        if am_i_about_to_kill_my_self_simulation(simulation_data,jsonData,go_any_safe_direction_direction):
            ##print("No, is up safe?")
            go_any_safe_direction_direction="up"
            if am_i_about_to_kill_my_self_simulation(simulation_data,jsonData,go_any_safe_direction_direction):
                ##print("No, is down safe?")
                go_any_safe_direction_direction="down"
                if am_i_about_to_kill_my_self_simulation(simulation_data,jsonData,go_any_safe_direction_direction):
                    ##print("Nothing is safe")
                    return("Nonesafe")
                else:
                    return(go_any_safe_direction_direction)
            else:
                return(go_any_safe_direction_direction)
        else:
            return(go_any_safe_direction_direction)
    else:
        return(go_any_safe_direction_direction)




def switch_direction(Direction):
    if Direction == "right":
        return("left")
    elif Direction == "left":
        return("right")
    elif Direction == "up":
        return("down")
    elif Direction == "down":
        return("up")



def find_food_location_relative_to_me(jsonData,my_head_x_component,my_head_y_component):
    for fud in jsonData["board"]["food"]:
        fud_x = fud["x"]
        fud_y = fud["y"]
        x_location = fud_x - my_head_x_component
        y_location = my_head_y_component - fud_y
        return([x_location,y_location])


def find_food_location_relative_to_me_simulation(simulation_data,jsonData):
    my_head_x_component= simulation_data[0][0]
    my_head_y_component= simulation_data[0][1]
    
    # count=0
    # while count<=(len(simulation_data)-1):
        # fud_x = simulation_data[count][0]
        # fud_y = simulation_data[count][1]
        # x_location = fud_x - my_head_x_component
        # y_location = my_head_y_component - fud_y
        # count +=1
        # return([x_location,y_location])
    
    for fud in jsonData["board"]["food"]:
        fud_x = fud["x"]
        fud_y = fud["y"]
        x_location = fud_x - my_head_x_component
        y_location = my_head_y_component - fud_y
        return([x_location,y_location])
    



def look_for_food_y_precedence(jsonData,my_head_x_component,my_head_y_component):
    for fud in jsonData["board"]["food"]:
        fud_x = fud["x"]
        fud_y = fud["y"]
        ##print("food location, x component", fud_x)
        ##print("food location, y component", fud_y)
        
        #temp_direction
        
        # if my_head_x_component< fud_x:
            # temp_direction= "right"
        # if my_head_x_component> fud_x:
            # temp_direction="left"
        if my_head_y_component< fud_y:
            temp_direction= "down"
        if my_head_y_component> fud_y:
            temp_direction="up"
        #print("Returning from y mode direction: ", temp_direction)
        ##print("food location, x component", fud_x, " \n","food location, y component", fud_y)
        return(temp_direction)



def look_for_food_x_precedence(jsonData,my_head_x_component,my_head_y_component):
    for fud in jsonData["board"]["food"]:
        fud_x = fud["x"]
        fud_y = fud["y"]
        ##print("food location, x component", fud_x)
        ##print("food location, y component", fud_y)
        
        #temp_direction
        
        # if my_head_y_component< fud_y:
            # temp_direction= "down"
        # if my_head_y_component> fud_y:
            # temp_direction="up"
        if my_head_x_component< fud_x:
            temp_direction= "right"
        if my_head_x_component> fud_x:
            temp_direction="left"
        #print("Returning from x-emergency mode direction: ", temp_direction)
        ##print("food location, x component", fud_x, " \n","food location, y component", fud_y)
        return(temp_direction)



def am_i_about_to_kill_my_self(jsonData,my_head_x_component,my_head_y_component,Direction):
    
    nextsquare_x = my_head_x_component
    if Direction == "left":
        nextsquare_x = my_head_x_component -1
    if Direction == "right":
        nextsquare_x = my_head_x_component +1
    
    
    nextsquare_y = my_head_y_component
    if Direction == "up":
        nextsquare_y = my_head_y_component -1
    if Direction == "down":
        nextsquare_y = my_head_y_component +1
    
    
    
    for bodypart in jsonData["you"]["body"]:
        if nextsquare_x == bodypart["x"] and nextsquare_y == bodypart["y"]:
            ##print(nextsquare_x, bodypart["x"])
            ##print(nextsquare_y, bodypart["y"])
            return True
        if nextsquare_x == -1 and Direction=="left":
            return True
        if nextsquare_x == jsonData["board"]["width"] and Direction=="right":
            return True
        if nextsquare_y == -1 and Direction=="up":
            return True
        if nextsquare_y == jsonData["board"]["height"] and Direction=="down":
            return True
    return False



def am_i_about_to_kill_my_self_simulation(simulation_data,jsonData,Direction):
    
    my_head_x_component= simulation_data[0][0]
    my_head_y_component= simulation_data[0][1]
    
    
    nextsquare_x = my_head_x_component
    if Direction == "left":
        nextsquare_x = my_head_x_component -1
    if Direction == "right":
        nextsquare_x = my_head_x_component +1
    
    
    nextsquare_y = my_head_y_component
    if Direction == "up":
        nextsquare_y = my_head_y_component -1
    if Direction == "down":
        nextsquare_y = my_head_y_component +1
    
    count=0
    while count<=(len(simulation_data)-1):
        if nextsquare_x == simulation_data[count][0] and nextsquare_y == simulation_data[count][1]:
            ##print(nextsquare_x, bodypart["x"])
            ##print(nextsquare_y, bodypart["y"])
            return True
        if nextsquare_x == -1 and Direction=="left":
            return True
        if nextsquare_x == jsonData["board"]["width"] and Direction=="right":
            return True
        if nextsquare_y == -1 and Direction=="up":
            return True
        if nextsquare_y == jsonData["board"]["height"] and Direction=="down":
            return True
        count+=1
    return False





def snake_location_copyjsonData(jsonData,my_head_x_component,my_head_y_component):
    index=-1
    for bodypart in jsonData["you"]["body"]:
        index+=1
    x_direction=0
    y_direction=0
    
    ##print("index equals:", index)
    
    # n = 1
    # m = 2
    # simulation = [0] * n
    # for i in range(n):
        # simulation[i] = [0] * m
    
    
    m = 2
    jsonData_copy=[-1]*(index+1)
    for i in range(index+1):
        jsonData_copy[i] = [-1] * m
    
    q=0
    for bodypart in jsonData["you"]["body"]: 
        jsonData_copy[q][0]=bodypart["x"]
        jsonData_copy[q][1]=bodypart["y"]
        q+=1
    
    ##print("jsonData_copy is :",jsonData_copy)
    return(jsonData_copy)



def simulate(jsonData_copy,Direction,jsonData):
    
    if Direction== "Nonesafe":
        ##print("In simulate, returning jsonData_copy", ""'Simulation snake is dead"')
        return(jsonData_copy,"Simulation snake is dead")
    
    index=len(jsonData_copy)-1
    x_direction=0
    y_direction=0
    
    m = 2
    simulation = [-1] * (index+1)
    for i in range(index+1):
        simulation[i] = [-1] * m
    
    
    if Direction == "left":
        x_direction= -1
    
    if Direction == "right":
        x_direction=1
    
    if Direction == "up":
        y_direction=-1
    
    if Direction == "down":
        y_direction=1
    
    
    
    count=index
    while count >= 0:
        if count==0:
            simulation[count][0]=jsonData_copy[count][0]+x_direction
            simulation[count][1]=jsonData_copy[count][1]+y_direction
        else:
            simulation[count][0]=jsonData_copy[count-1][0]
            simulation[count][1]=jsonData_copy[count-1][1]
            
        count -=1
    
    count=index
    while count >= 0:
        y=index
        while y>=0:
            if simulation[count][0]==simulation[y][0] and simulation[count][1]==simulation[y][1] and count != y:
                ##print("In simulate body parts overlap, returning jsonData_copy", ""'Simulation snake is dead"')
                return(jsonData_copy,"Simulation snake is dead")
            if simulation[count][0]<0 or simulation[count][1]<0:
                ##print("In simulate hit border (1), returning jsonData_copy", ""'Simulation snake is dead"')
                return(jsonData_copy,"Simulation snake is dead")
            if simulation[count][0]>(jsonData["board"]["width"]-1) or simulation[count][1]>(jsonData["board"]["height"]-1):
                ##print("In simulate hit border (1), returning jsonData_copy", ""'Simulation snake is dead"')
                return(jsonData_copy,"Simulation snake is dead")
            y-=1
        count -=1
    
    
    # if Direction== "Nonesafe":
        # #print("Simulation, no direction is safe")
        # #print("x_direction equals: ",x_direction,"\ny_direction=equals", y_direction)
        # #print("Head location is: ", simulation[0][0], "," , simulation[0][1])
        # #print("Tail location is: ", simulation[index][0], "," , simulation[index][1])
    
    
    return(simulation,"Simulation snake is alive")

    
    
@bottle.post('/end')
def end():
    data = bottle.request.json

    """
    TODO: If your snake AI was stateful,
        clean up any stateful objects here.
    """
    #print(json.dumps(data))

    return end_response()

# Expose WSGI app (so gunicorn can find it)
application = bottle.default_app()

if __name__ == '__main__':
    bottle.run(
        application,
        host=os.getenv('IP', '0.0.0.0'),
        port=os.getenv('PORT', '8080'),
        debug=os.getenv('DEBUG', True)
    )
