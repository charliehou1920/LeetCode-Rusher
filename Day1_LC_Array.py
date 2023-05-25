class LCArray:
    def __init__(self):
        self.a = []
        self.cur_size = 0
        self.maxsize = 1

    def push_back(self, n):
        if self.cur_size == 0:
            self.a = [n]
        if self.cur_size == self.maxsize:
            self.maxsize *= 2
            tmp = [0 for i in range(self.maxsize)]
            for i in range(self.cur_size):
                tmp[i] = self.a[i]
            self.a = tmp
            self.a[self.cur_size] = n
        self.cur_size += 1    

    def pop_back(self):
        self.cur_size -= 1

    def size(self):
        return self.cur_size
    
    def index(self, idx):
        return self.a[idx]

def main():
    lc_array = LCArray()
    # Testing push_back
    lc_array.push_back(10)
    lc_array.push_back(20)
    lc_array.push_back(30)
    lc_array.push_back(40)
    lc_array.push_back(50)

    # Testing size
    print("Current size:", lc_array.size())

    # Testing index
    print("Element at index 2:", lc_array.index(2))

    # Testing pop_back
    lc_array.pop_back()

    # Testing size after pop_back
    print("Current size after pop_back:", lc_array.size())

    # Testing index after pop_back
    print("Element at index 2 after pop_back:", lc_array.index(2))

if __name__ == "__main__":
    main()