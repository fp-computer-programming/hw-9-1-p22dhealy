#author:DMH 1/12/22

def find_thing(thing,value):
    for i, v in enumerate(thing):
        if v == value:
            print(i)
            break
        if value not in thing:
            print('-1')
            break

find_thing('aleep','p')
        
        

    

            
