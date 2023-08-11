class trees:

    def __init__(self):
        self.count = 0


    def count_leaves(self, list_val):
        if list_val is None or len(list_val) < 1:
            return 0
        elif len(list_val) == 1 or any(isinstance(i,list) for i in list_val) is False:
            return 1
        else:
            return self.count_leaves(list_val[0:1]) + self.count_leaves(list_val[1:])