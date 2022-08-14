# import the necessary packages
import numpy as np
#import seaborn as sns
from matplotlib import cm
from matplotlib import pyplot as plt
from sklearn.datasets import make_blobs
#sns.set(style='darkgrid')

def sigmoid(z):
    return 1 / (1 + np.exp(-z))

def logistic_regression(X, y, alpha=0.01, epochs=30):
    m = np.shape(X)[0]  # total number of samples shape(150*2)
    n = np.shape(X)[1]  # total number of features
    X = np.concatenate((np.ones((m, 1)), X), axis=1)
    W = np.random.randn(n + 1, )
    cost_history_list = []
    for current_iteration in np.arange(epochs):  # begin the process
 
        y_estimated = sigmoid(X.dot(W))
        print(y_estimated)
        error = y_estimated - y
        cost = np.mean(-y * np.log(y_estimated) - (1 - y) * \
                       np.log(1 - y_estimated))

        gradient = (1 / m) * X.T.dot(error)
        W = W - alpha * gradient
        #if current_iteration % 5 == 0:
           # print(f"cost:{cost} \t iteration: {current_iteration}")
        cost_history_list.append(cost)
 
    return W, cost_history_list


def main():
    # generate a binary classification problem with 150 samples,
    # where each of the samples is a 2D feature vector
    (X, y) = make_blobs(n_samples=150, centers=2, n_features=2,
                        random_state=20)
 
    # calls the logistic regression method
    weight, cost_history_list = logistic_regression(X, y, alpha=0.01,
                                                    epochs=100)
    plt.subplot(2,1,1)
    plt.scatter(X[:,0],X[:,1], c=y)
    # compute the line of best fit by setting the sigmoid function
    # to 0; 0 = w0 + w1*x + w2*y and solving for X2
    # in terms of X1 ==> y = (-w0 - (w1*x)) / w2
    # (W0, W1, W2) = weight
    # Y = (-W0 - (W1 * X)) / W2
 
    # # plot the original data along with our line of best fit
    # plt.scatter(X[:, 0], X[:, 1], c=y, cmap=cm.jet)
    # plt.plot(X, Y, "r-")
    # plt.xlabel('feature 1')
    # plt.ylabel('feature 2')
    # plt.show()
 
    # visualize how our cost decreases over time
    plt.subplot(2,1,2)
    plt.plot(np.arange(len(cost_history_list)), cost_history_list)
    plt.xlabel("Number of iterations (Epochs)")
    plt.ylabel("Cost function  J(Θ)")
    plt.title("Training Loss")
    plt.show()

if __name__ == '__main__':
    main()