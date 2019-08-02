import matplotlib.pyplot as plt
import numpy as np

"""
Originally sourced from https://github.com/sarvasvkulpati/LinearRegression
Improvement is made on the iterations based on the Cost, in order to better 
converge instead of hardcoded 1000 iterations as per original code.
"""


class LinearRegressionV2:
    """
        This helper class will perform the Linear Regressions
        Sample:
        -------
        from sklearn.datasets import make_regression
        X, y = make_regression(n_samples=100, n_features=1, noise=0.4, bias=20)

        # invoke the class
        linreg = LinearRegressionV2(X, y, alpha=0.005, enableVisualization=True)
    """
    
    def __init__(self, X, y, alpha=0.005, enableVisualization=False):
        self.fit(X, y, alpha, enableVisualization)
        
    def plotLine(self, theta0, theta1, X, y):
        max_x = np.max(X) + 100
        min_x = np.min(X) - 100

        xplot = np.linspace(min_x, max_x, 1000)
        yplot = theta0 + theta1 * xplot

        plt.plot(xplot, yplot, color='#58b970', label='Regression Line')

        plt.scatter(X,y)
        plt.axis([-10, 10, 0, 200])
        plt.show()

    def hypothesis(self, theta0, theta1, x):
        return theta0 + (theta1*x) 

    def cost(self, theta0, theta1, X, y):
        costValue = 0 
        for (xi, yi) in zip(X, y):
            costValue += 0.5 * ((self.hypothesis(theta0, theta1, xi) - yi)**2)
        return costValue

    def derivatives(self, theta0, theta1, X, y):
        dtheta0 = 0
        dtheta1 = 0
        for (xi, yi) in zip(X, y):
            dtheta0 += self.hypothesis(theta0, theta1, xi) - yi
            dtheta1 += (self.hypothesis(theta0, theta1, xi) - yi)*xi

        dtheta0 /= len(X)
        dtheta1 /= len(X)

        return dtheta0, dtheta1

    def updateParameters(self, theta0, theta1, X, y, alpha):
        dtheta0, dtheta1 = self.derivatives(theta0, theta1, X, y)
        theta0 = theta0 - (alpha * dtheta0)
        theta1 = theta1 - (alpha * dtheta1)

        return theta0, theta1

    def fit(self, X, y, alpha, enableVisualization):
        theta0 = np.random.rand()
        theta1 = np.random.rand()
        inconsistent_cost = True
        previous_cost = 0
        current_cost = 0
        i = 0
        
        while (inconsistent_cost):
            current_cost = self.cost(theta0, theta1, X, y)
            if enableVisualization:
                if i % 100 == 0:
                    self.plotLine(theta0, theta1, X, y)
                    print("Cost: ", current_cost)
                    
            theta0, theta1 = self.updateParameters(theta0, theta1, X, y, alpha)
            
            if (previous_cost != current_cost):
                previous_cost = current_cost
            else:
                inconsistent_cost = False
            
            i+=1
