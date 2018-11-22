//"" by the and perceptron we can either increase the bias (1)""

w1=1
w2=1
b=-1

outputs=["False","False","False","True"]
inputs=[(0,0),(0,1),(1,0),(1,1)]
answers=0
for outputs_,inputs_ in zip(outputs,inputs):
    local=w1*inputs_[0]+w2*inputs_[1]+b
    answers+=int(local>=0)
print(answers)        


//"increase the weights(2) to any extent as the 0,0 is the only case where the output is false. bias is negative compulsory for bias>=0"
w1=2
w2=2
b=-1

outputs=["False","False","False","True"]
inputs=[(0,0),(0,1),(1,0),(1,1)]
answers=0
for outputs_,inputs_ in zip(outputs,inputs):
    local=w1*inputs_[0]+w2*inputs_[1]+b
    answers+=int(local>=0)
print(answers)        
