import math
import matplotlib.pyplot as plt
from .general import Dist

class Binomial(Dist):
    """Binomial distribution class for calculating and visualizing a Binomial distribution
    """
    def __init__(self,prob=.5,size=20):
        self.n=size
        self.p=prob
        super().__init__(self.get_mean(),self.get_stdev())
    
    def get_mean(self):
        """Method to get mean by multipliying number of trials(n) by the probability of sucesses(p)
        """
        self.mean=self.p *self.n
        return self.mean
    
    def get_stdev(self):
        """Method to get standard deviation
        """
        self.stdev=math.sqrt(self.n*self.p*(1-self.p))
        return self.stdev
    
    def get_p_n(self):
        """Method to get p(probability of sucesses) and n(size) from data
        """
        self.n=len(self.data)
        self.p=1.0*sum(self.data)/len(self.data)
        self.mean=self.get_mean()
        self.stdev=self.get_stdev()
        return self.p, self.n
    
    def plot_bar(self):
        """Method to plot histogram for data
        """
        plt.bar(x=['0','1'], height=[(1-self.p)*self.n,self.p*self.n])
        plt.title('Bar chart of Data')
        plt.xlabel('outcome')
        plt.ylabel('count')
    
    def pdf(self,k):
        """Method to calculate probability density function for binomial distribution 
        """
        a=math.factorial(self.n)/(math.factorial(k)*(math.factorial(self.n-k)))
        b=(self.p**k)*(1-self.p)**(self.n-k)
        return a*b
    
    def plot_bar_pdf(self):
        """Method to plot the pdf of the binomial distribution
        """
        x=[]
        y=[]
        
        for i in range(self.n+1):
            x.append(i)
            y.append(self.pdf(i))
        
        plt.bar(x,y)
        plt.title('Distribution of outcomes')
        plt.ylabel('Probability')
        plt.xlabel('Outcome')
        
        plt.show()
        return x,y
    
    def __add__(self,other):
        """"Method to add together two Binomial distributions with equal probability
        """
        try:
            assert self.p==other.p, 'probabilities are not equal'
        except AssertionError as error:
            raise
        
        result=Binomial()
        result.n=self.n+other.n
        result.p=self.p
        result.get_mean()
        result.get_stdev()
        return result
    
    def __repr__(self):
        """"Method to output information regarding Binomial distribution
        """
        return "mean {}, standard deviation {}, p {}, n  {}".format(self.mean,self.stdev,self.p,self.n)