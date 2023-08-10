class trees:

    def __init__(self):
        self.count = 0


    def count_leaves(self, list_val):
        if list_val is None or len(list_val) < 1:
            return 0
        elif len(list_val) == 1:
            return 1
        return self.count_leaves(list_val[0:1] + list_val[1:])