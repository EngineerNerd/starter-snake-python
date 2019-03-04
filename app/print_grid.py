from DryBones import *

def printblankgrid(jsonData):
    index = 0
    y=0
    x=0
    row= "|"
    underscore= "    " 
    i=0
    column_counting="    "
    
    for ligament in jsonData["you"]["body"]:
        index +=1
    
    
    while x<= (jsonData["board"]["width"]-1): 
        row += "   |"
        column_counting += "  {} ".format(x)
        x+=1
        #if x=(jsonData["board"]["width"]-1):
        #    row += "|"
    
    while i<= len(row)-1:
        underscore += "_"
        i+=1
    
    print(column_counting)
    
    while y<= (jsonData["board"]["height"] -1):
        print(underscore)
        print(" {} ".format(y), row)
        y+=1
    
    print(underscore)
    print("\n")


def print_grid(jsonData):
    index = 0
    y=0
    x=0
    row= "|"
    underscore= "    " 
    i=0
    column_counting="    "
    temp= " "
    
    
    while y<= (jsonData["board"]["height"] -1):
        x=0
        row= "|"
        while x<= (jsonData["board"]["width"]-1): 
            #print("while x. x =",x)
            index=0
            temp= " "
            for ligament in jsonData["you"]["body"]:
                
                
                if ligament["x"] == x and ligament["y"] == y:
                    temp =index
                
                #print("\n x equals:", x, "y equals:", y, "temp equals:", temp)
                
                
                index +=1
                
            column_counting += "   {} ".format(x)
            x+=1
            
            if temp== " ":
                row += " {}  |".format(temp)
            elif temp>9:
                row += " {} |".format(temp)
            else:
                row += " {}  |".format(temp)
            
            #print("testing {} ".format(y), row)
            
            
            #end of "for ligament in jsonData["you"]["body"]:"
        #end of "while x<= (jsonData["board"]["width"]-1): "
        #print("while y. y =",y)
        if y==0:
            print(column_counting)
            while i<= len(row)-1:
                underscore += "_"
                i+=1
                
        print(underscore)
        print(" {} ".format(y), row)
        y+=1
    #end of while y<= (jsonData["board"]["height"] -1):
    
    print(underscore)
    print("\n")


def print_grid_and_possible_movements(jsonData):
    
    my_head_x_component= jsonData["you"]["body"][0]["x"]
    my_head_y_component= jsonData["you"]["body"][0]["y"]
    
    #print("Function test. Am I going to die? ", am_i_about_to_kill_my_self(jsonData,my_head_x_component,my_head_y_component,"up"))
    index = 0
    y=0
    x=0
    row= "|"
    underscore= "    " 
    i=0
    column_counting="    "
    temp= " "
    
    
    while y<= (jsonData["board"]["height"] -1):
        x=0
        row= "|"
        while x<= (jsonData["board"]["width"]-1): 
            #print("while x. x =",x)
            index=0
            temp= " "
            for ligament in jsonData["you"]["body"]:
                
                
                if abs(my_head_x_component-x)==1 and abs(my_head_y_component-y)==0 and temp == " " :
                    temp = "*"
                
                if abs(my_head_x_component-x)==0 and abs(my_head_y_component-y)==1 and temp == " ":
                    temp = "*"
                
                if ligament["x"] == x and ligament["y"] == y:
                    temp =index
                
                #print("\n x equals:", x, "y equals:", y, "temp equals:", temp)
                
                
                index +=1
                
            column_counting += "   {} ".format(x)
            x+=1
            
            if temp== " " or temp=="*":
                row += " {}  |".format(temp)
            elif temp>9:
                row += " {} |".format(temp)
            else:
                row += " {}  |".format(temp)
            
            #print("testing {} ".format(y), row)
            
            
            #end of "for ligament in jsonData["you"]["body"]:"
        #end of "while x<= (jsonData["board"]["width"]-1): "
        #print("while y. y =",y)
        if y==0:
            print(column_counting)
            while i<= len(row)-1:
                underscore += "_"
                i+=1
                
        print(underscore)
        print(" {} ".format(y), row)
        y+=1
    #end of while y<= (jsonData["board"]["height"] -1):
    
    print(underscore)
    print("\n")


def print_grid_and_safespots(jsonData):
    
    my_head_x_component= jsonData["you"]["body"][0]["x"]
    my_head_y_component= jsonData["you"]["body"][0]["y"]
    food_location = [jsonData["board"]["food"][0]["x"],jsonData["board"]["food"][0]["y"]]
    
    #print("Function test. Am I going to die? ", am_i_about_to_kill_my_self(jsonData,my_head_x_component,my_head_y_component,"up"))
    index = 0
    y=0
    x=0
    row= "|"
    underscore= "    " 
    i=0
    column_counting="    "
    temp= " "
    
    
    while y<= (jsonData["board"]["height"] -1):
        x=0
        row= "|"
        while x<= (jsonData["board"]["width"]-1): 
            #print("while x. x =",x)
            index=0
            temp= " "
            for ligament in jsonData["you"]["body"]:
                
                
                if abs(my_head_x_component-x)==1 and abs(my_head_y_component-y)==0 and temp == " " :
                    if my_head_x_component <x:
                        if not(am_i_about_to_kill_my_self(jsonData,my_head_x_component,my_head_y_component,"right"))and temp == " ":
                            temp = "**"
                    
                    if my_head_x_component >x:
                        if not(am_i_about_to_kill_my_self(jsonData,my_head_x_component,my_head_y_component,"left"))and temp == " ":
                            temp = "**"
                        
                    
                    if my_head_y_component >y:
                        if not(am_i_about_to_kill_my_self(jsonData,my_head_x_component,my_head_y_component,"up"))and temp == " ":
                            temp = "**"
                        
                    if my_head_y_component <y:
                        if not(am_i_about_to_kill_my_self(jsonData,my_head_x_component,my_head_y_component,"down"))and temp == " ":
                            temp = "**"
                        
                    
                    
                    
                    
                
                if abs(my_head_x_component-x)==0 and abs(my_head_y_component-y)==1 and temp == " ":
                    if my_head_x_component <x:
                        if not(am_i_about_to_kill_my_self(jsonData,my_head_x_component,my_head_y_component,"right"))and temp == " ":
                            temp = "**"
                    
                    if my_head_x_component >x:
                        if not(am_i_about_to_kill_my_self(jsonData,my_head_x_component,my_head_y_component,"left"))and temp == " ":
                            temp = "**"
                        
                    
                    if my_head_y_component >y:
                        if not(am_i_about_to_kill_my_self(jsonData,my_head_x_component,my_head_y_component,"up"))and temp == " ":
                            temp = "**"
                        
                    if my_head_y_component <y:
                        if not(am_i_about_to_kill_my_self(jsonData,my_head_x_component,my_head_y_component,"down"))and temp == " ":
                            temp = "**"
                        
                    
                    
                    
                    
                
                if ligament["x"] == x and ligament["y"] == y:
                    temp =index
                
                if food_location[0] ==x and food_location[1]  == y:
                    temp = "F"
                #print("\n x equals:", x, "y equals:", y, "temp equals:", temp)
                
                
                index +=1
                
            column_counting += "   {} ".format(x)
            x+=1
            
            if temp== " " or temp=="*" or temp == "F":
                row += " {}  |".format(temp)
            elif temp== "**" or temp>9  :
                row += " {} |".format(temp)
            else:
                row += " {}  |".format(temp)
            
            #print("testing {} ".format(y), row)
            
            
            #end of "for ligament in jsonData["you"]["body"]:"
        #end of "while x<= (jsonData["board"]["width"]-1): "
        #print("while y. y =",y)
        if y==0:
            print(column_counting)
            while i<= len(row)-1:
                underscore += "_"
                i+=1
                
        print(underscore)
        print(" {} ".format(y), row)
        y+=1
    #end of while y<= (jsonData["board"]["height"] -1):
    
    print(underscore)
    print("\n")


def print_grid_and_safespots_simulation(simulation_data,jsonData,simulation_number):
    
    my_head_x_component= simulation_data[0][0]
    my_head_y_component= simulation_data[0][1]
    food_location = [jsonData["board"]["food"][0]["x"],jsonData["board"]["food"][0]["y"]]
    
    #print("Function test. Am I going to die? ", am_i_about_to_kill_my_self(jsonData,my_head_x_component,my_head_y_component,"up"))
    index = 0
    y=0
    x=0
    row= "|"
    underscore= "    " 
    i=0
    column_counting="    "
    temp= " "
    
    print("\n ----Simulation number ",simulation_number,"---- \n") 
    
    while y<= (jsonData["board"]["height"] -1):
        x=0
        row= "|"
        while x<= (jsonData["board"]["width"]-1): 
            #print("while x. x =",x)
            index=0
            temp= " "
            count=0
            while count<=(len(simulation_data)-1):
                
                
                if abs(my_head_x_component-x)==1 and abs(my_head_y_component-y)==0 and temp == " " :
                    if my_head_x_component <x:
                        if not(am_i_about_to_kill_my_self_simulation(simulation_data,jsonData,"right"))and temp == " ":
                            temp = "**"
                    
                    if my_head_x_component >x:
                        if not(am_i_about_to_kill_my_self_simulation(simulation_data,jsonData,"left"))and temp == " ":
                            temp = "**"
                        
                    
                    if my_head_y_component >y:
                        if not(am_i_about_to_kill_my_self_simulation(simulation_data,jsonData,"up"))and temp == " ":
                            temp = "**"
                        
                    if my_head_y_component <y:
                        if not(am_i_about_to_kill_my_self_simulation(simulation_data,jsonData,"down"))and temp == " ":
                            temp = "**"
                        
                    
                    
                    
                    
                
                if abs(my_head_x_component-x)==0 and abs(my_head_y_component-y)==1 and temp == " ":
                    if my_head_x_component <x:
                        if not(am_i_about_to_kill_my_self_simulation(simulation_data,jsonData,"right"))and temp == " ":
                            temp = "**"
                    
                    if my_head_x_component >x:
                        if not(am_i_about_to_kill_my_self_simulation(simulation_data,jsonData,""))and temp == " ":
                            temp = "**"
                        
                    
                    if my_head_y_component >y:
                        if not(am_i_about_to_kill_my_self_simulation(simulation_data,jsonData,"up"))and temp == " ":
                            temp = "**"
                        
                    if my_head_y_component <y:
                        if not(am_i_about_to_kill_my_self_simulation(simulation_data,jsonData,"down"))and temp == " ":
                            temp = "**"
                        
                    
                    
                    
                    
                
                if simulation_data[count][0] == x and simulation_data[count][1] == y:
                    temp =index
                
                if food_location[0] ==x and food_location[1]  == y :
                    if temp == " ":
                        temp = "F"
                    elif temp !="F" and temp !="*F" and temp!="**F" and temp!="0F" and temp!="1F":
                        copy = str(temp)
                        temp= " "
                        temp = copy + "F"
                #print("\n x equals:", x, "y equals:", y, "temp equals:", temp)
                
                
                index +=1
                count+=1
            
            column_counting += "   {} ".format(x)
            x+=1
            
            
            #print("temp is:*",temp,"*")
            if temp== " " or temp=="*" or temp == "F":
                row += " {}  |".format(temp)
            elif temp== "**" or temp=="**F" or temp=="0F" or temp=="1F" :
                row += " {} |".format(temp)
            elif len(str(temp))>1:
                row += " {} |".format(temp)
            else:
                row += " {}  |".format(temp)
            
            
            # if int(temp)>9:
                # row += " {} |".format(temp)
            # elif temp== "**" or temp=="**F"  :
                # row += " {} |".format(temp)
            # else:
                # row += " {}  |".format(temp)
            
            
            #print("testing {} ".format(y), row)
            
            
            #end of "for ligament in jsonData["you"]["body"]:"
        #end of "while x<= (jsonData["board"]["width"]-1): "
        #print("while y. y =",y)
        if y==0:
            print(column_counting)
            while i<= len(row)-1:
                underscore += "_"
                i+=1
                
        print(underscore)
        print(" {} ".format(y), row)
        y+=1
    #end of while y<= (jsonData["board"]["height"] -1):
    
    print(underscore)
    print("\n")



