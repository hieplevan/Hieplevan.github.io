
class Lib:
    def __init__(self):
        pass
    
    def read_data(self):
        with open('thongtincuahiepngu.txt','r') as f:
            for line in f:
                print(line)
