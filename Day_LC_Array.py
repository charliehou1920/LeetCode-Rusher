class LCArray:
    def __init__(self):
        self.a = [0]
        self.cur_size = 0
        self.maxsize = 1

    def push_back(self, n):
        if self.cur_size == self.maxsize:
            self.maxsize *= 2
            tmp = [0 for i in range(self.maxsize)]
            for i in range(self.cur_size):
                tmp[i] = self.a[i]
            self.a = tmp
            self.a[self.cur_size] = n
            self.cur_size += 1
