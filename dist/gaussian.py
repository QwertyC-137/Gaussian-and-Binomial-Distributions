import math
import matplotlib.pyplot as plt
from .general import Dist

class Gaussian(Dist):
    """Gaussian distribution class
    """
    def __init__(self,mu=0,sigma=1):
        super().__init__(mu,sigma)
        
    def get_mean(self):
        """Method to calculate mean
        """
        avg=1.0*sum(self.data)/len(self.data)
        self.mean=avg
        return self.mean
    
    def get_stdev(self,sample=True):
        """Method to calculate standard deviation. Sample=True means that data represents sample 
        """
        if sample:
            n=len(self.data)-1
        else:
            n=len(self.data)
            
        mean=self.get_mean()
        sigma=0
        
        for d in self.data:
            sigma+=(d-mean)**2
        sigma=math.sqrt(sigma/n)
        self.stdev = sigma
        return self.stdev
    
    def hist_plot(self):
        """Method to plot histogram of the data
        """
        plt.hist(self.data)
        plt.title('Histogram of Data')
        plt.xlabel('Data')
        plt.ylabel('Count')
        
    def pdf(self,x):
        """Method to calculate probability density function for gaussian distribution
        """
        return (1.0/(self.stdev*math.sqrt(2*math.pi))) *math.exp(-0.5*((x-self.mean)/self.stdev)**2)
    
    def plot_hist_pdf(self,n_spaces=50):
        """Method to plot normalized histogram
        """
        mu=self.mean
        sigma=self.stdev
        min_range=min(self.data)
        max_range=max(self.data)
        
        interval=1.0*(max_range-min_range)/n_spaces
        
        x=[]
        y=[]
        
        for i in range(n_spaces):
            tmp=min_range+interval*i
            x.append(tmp)
            y.append(self.pdf(tmp))
        
        fig, axes = plt.subplots(2,sharex=True)
        fig.subplots_adjust(hspace=.5)
        axes[0].hist(self.data,density=True)
        axes[0].set_title('Normalized histogram of data')
        axes[0].set_ylabel('Density')
        axes[1].plot(x,y)
        axes[1].set_title('Normal distribution for sample mean and sample stdev')
        axes[0].set_ylabel('Density')
        plt.show()
        return x,y
    
    def __add__(self,other):
        """Method to add two gaussian distributions
        """
        result=Gaussian()
        result.mean=self.mean+other.mean
        result.stdev=math.sqrt(self.stdev**2+other.stdev**2)
        return result
    
    def __repr__(self):
        """Method to output information regarding Gaussian distribution
        """
        return "mean {}, standard deviation {}".format(self.mean, self.stdev)