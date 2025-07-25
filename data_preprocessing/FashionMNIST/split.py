#Author: Muhammad Azizi Bin Mohd Ariffin
#Email: mazizi@fskm.uitm.edu.my
#Description: Split dataset for FL Client FASHION-MNIST and CIFAR-10

client_num = 3

#load dataset
import numpy as np
x_train = np.load("x_train-cifar10.npy")
y_train = np.load("y_train-cifar10.npy")
x_test = np.load("x_test-cifar10.npy")
y_test = np.load("y_test-cifar10.npy")

trainShape = x_train.shape[0]
testShape = x_test.shape[0]

print(trainShape)
print(testShape)

if trainShape % client_num == 0:
    x_train = np.array(np.split(x_train,client_num))
    y_train = np.array(np.split(y_train,client_num))
else:
    x_train = x_train[:trainShape-2]
    y_train = y_train[:trainShape-2]
    x_train = np.array(np.split(x_train,client_num))
    y_train = np.array(np.split(y_train,client_num))
    
if testShape % client_num == 0:
    x_test = np.array(np.split(x_test,client_num))
    y_test = np.array(np.split(y_test,client_num))
else:
    x_test = x_test[:testShape-1]
    y_test = y_test[:testShape-1]
    x_test = np.array(np.split(x_test,client_num))
    y_test = np.array(np.split(y_test,client_num))

count = 0

while count < client_num :
    np.save('x-train-cifar10-client ' + str(count + 1), x_train[count])
    np.save('y-train-cifar10-client ' + str(count + 1), y_train[count])
    
    np.save('x-test-cifar10-client ' + str(count + 1), x_test[count])
    np.save('y-test-cifar10-client ' + str(count + 1), y_test[count])
    count = count + 1