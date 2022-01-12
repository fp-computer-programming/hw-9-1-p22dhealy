#author: DMH 1/12/22

odd_lst = []

def odd_index(lst):
    for i, v in enumerate(lst):
        if int(v) % 2 != 0:
            odd_lst.append(i)
            odd_lst.append(v)
    print(odd_lst)


odd_index([3,56,78,53,2123567,8])



