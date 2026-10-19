yh=[]
for i in range(8):
    yh.append([])
    for j in range(i+1) :
        if j ==0 or j==i:
            yh[i].append(1)
        else:
                yh[i].append(yh[i-1][j-1]+yh[i-1][j])
    print(yh[i])