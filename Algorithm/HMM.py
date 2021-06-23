#coding=utf-8
#author: Gray Hua

import numpy as np
import matplotlib.pyplot as plt
class HMM(object):
    def __init__(self, N, M, pi=None, A=None, B=None):
        self.N = N
        self.M = M
        self.pi = pi
        self.A = A
        self.B = B

    def getDistribution(self, dist): 
        r = np.random.rand()  
        for i, p in enumerate(dist):
            if r < p: return i
            r -= p

    def generate(self, T: int):
      
        z = self.getDistribution(self.pi)    
        x = self.getDistribution(self.B[z])  
        result = [x]
        for _ in range(T-1):        
            z = self.getDistribution(self.A[z])
            x = self.getDistribution(self.B[z])
            result.append(x)
        for i in range(len(result)):
            if 0 ==result[i]:
                result[i] = "redball"
            else:
                result[i] = "whiteball"
        return result
	
    def evaluate(self, X):
   
        alpha = self.pi * self.B[:,X[0]]
        for x in X[1:]:
            alpha_next = np.empty(self.N)
            for j in range(self.N):
                alpha_next[j] = np.sum(self.A[:,j] * alpha * self.B[j,x])
            alpha = alpha_next
            # alpha = np.sum(self.A * alpha.reshape(-1,1) * self.B[:,x].reshape(1,-1), axis=0)
        return "{:.9f}".format(alpha.sum())


    def evaluate_backward(self, X):
        beta = np.ones(self.N)
        for x in X[:0:-1]:
            beta_next = np.empty(self.N)
            for i in range(self.N):
                beta_next[i] = np.sum(self.A[i,:] * self.B[:,x] * beta)
            beta = beta_next
        return np.sum(beta * self.pi * self.B[:,X[0]])

    def decode(self, X):
        T = len(X) 
        x = X[0]
        delta = self.pi * self.B[:,x]
        varphi = np.zeros((T, self.N), dtype=int)
        path = [0] * T
        for i in range(1, T):
            delta = delta.reshape(-1,1)     
            tmp = delta * self.A
            varphi[i,:] = np.argmax(tmp, axis=0)
            delta = np.max(tmp, axis=0) * self.B[:,X[i]]
        path[-1] = np.argmax(delta)

        for i in range(T-1,0,-1):
            path[i-1] = varphi[i,path[i]]
        return path

    
    def fit(self, X):
        self.pi = np.random.sample(self.N)
        self.A = np.ones((self.N,self.N)) / self.N
        self.B = np.ones((self.N,self.M)) / self.M
        self.pi = self.pi / self.pi.sum()
        T = len(X)
        for _ in range(50):
            
            alpha, beta = self.get_something(X)
            gamma = alpha * beta

            for i in range(self.N):
                for j in range(self.N):
                    self.A[i,j] = np.sum(alpha[:-1,i]*beta[1:,j]*self.A[i,j]*self.B[j,X[1:]]) / gamma[:-1,i].sum()
            
            for j in range(self.N):
                for k in range(self.M):
                    self.B[j,k] = np.sum(gamma[:,j]*(X == k)) / gamma[:,j].sum()
            # print(self.A[i,j])
            # print(self.B[i,j])
            self.pi = gamma[0] / gamma[-1].sum()

    def get_something(self, X):
        T = len(X)
        alpha = np.zeros((T,self.N))
        alpha[0,:] = self.pi * self.B[:,X[0]]
        for i in range(T-1):
            x = X[i+1]
            alpha[i+1,:] = np.sum(self.A * alpha[i].reshape(-1,1) * self.B[:,x].reshape(1,-1), axis=0)

        beta = np.ones((T,self.N))
        for j in range(T-1,0,-1):
            for i in range(self.N):
                beta[j-1,i] = np.sum(self.A[i,:] * self.B[:,X[j]] * beta[j])
                
        return alpha, beta




 
def problem1():
    pi = np.array([.25, .25, .25, .25])
    A = np.array([
        [0,  1,  0, 0],
        [.4, 0, .6, 0],
        [0, .4, 0, .6],
        [0, 0, .5, .5]])
    B = np.array([
        [.5, .5],
        [.3, .7],
        [.6, .4],
        [.8, .2]])
    hmm = HMM(4, 2, pi, A, B)
    print(hmm.generate(10))  # 生成10个数据
    print(hmm.evaluate([0,0,1,1,0]))   # 0.026862016
    print(hmm.evaluate_backward([0,0,1,1,0]))



def model2(o):
    def getData(T):   
        data = []
        for _ in range(T):
            x = np.random.choice([0,1])
            data.append(x)#if x <= 1 else 3-x)
        return data
    data = np.array(getData(o))
    data1 = list(data)
    for i in range(len(data1)):
        if 0 ==data[i]:
            data1[i] = "redball"
        else:
            data1[i] = "whiteball"
    hmm = HMM(4, 2)
    hmm.fit(data)               # 先根据给定数据反推参数
    gen_obs = hmm.generate(o)  # 再根据学习的参数生成数据
    t=0
    for i in range(len(data)):
        if data1[i]==gen_obs[i]:
            t+=1
    return t/o
    # x = np.arange(10)
    # plt.scatter(x, gen_obs, marker='*', color='r')
    # plt.scatter(x, data, color='g',alpha=.3)
    # plt.show()

def problem2(T):
    lst=[]
    for i in range(T):
        tmp = model2(10)
        lst.append(tmp)
    # plt.scatter([x for x in range(len(lst))],lst)
    # plt.show()
    print("根据学习的参数生成数据的准确率的期望为：{:2f} ".format(sum(lst)/T))
    return sum(lst)/T


def problem3():
    pi = np.array([.2, .4, .4])
    A = np.array([
    [.5, .2, .3],
    [.3, .5, .2],
    [.2, .3, .5]])
    B = np.array([
    [.5, .5],
    [.4, .6],
    [.7, .3]])
    hmm = HMM(3, 2, pi, A, B)
    print("The probability of generating an observation sequence is{}".format(hmm.evaluate([0,1,0]))) 
    print("The state sequence with the highest probability of generating the observation sequence is{}".format(hmm.decode([0,1,0])))


if __name__ == "__main__":
    problem1()
    problem2(10)
    problem3()
    acc = problem2(10)
