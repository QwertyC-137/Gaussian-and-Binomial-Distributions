class Dist:
    def __init__(self,mu=0,sigma=1):
        """Generic distribution class for cauculating and vislazing a prob distribution
        """
        self.mean=mu
        self.stdev=sigma
        self.data=[]
        
    def read_file(self,filename):
        """Method to read data from txt file, file should have one nr per line. Nums are stored in data attribute.
        """
        with open(filename) as file:
            data_list=[float(line.strip()) for line in file]
        self.data=data_list