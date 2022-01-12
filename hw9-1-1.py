#author: DMH 1/12/22

even_lst = []

def even_index(lst):
    for i, v in enumerate(lst):
        if int(i) % 2 == 0:
            even_lst.append(v)
    return even_lst




