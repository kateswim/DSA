import time

def golomb(n,dict={}):
    if n==1:
        return 1
    if n in dict:
        value=dict[n]
    else:
        value=golomb(n-golomb(golomb(n-1)))
        dict[n]=value

    return 1+value


start_time = time.time()

print(golomb(67))
print("faster--- %s seconds ---" % (time.time() - start_time))

