def is_valid_walk(walk):
    coord = {"n":1, "s":-1, "e":1, "w":-1}
    coord_x = [coord[i] for i in walk if i=="n" or i=="s"]
    coord_y = [coord[i] for i in walk if i=="e" or i=="w"]

    if len(walk)==10 and (sum(coord_x)==0 and sum(coord_y)==0):
        return True
    else:
        return False
        