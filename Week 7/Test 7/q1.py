def matchingStrings(stringList, queries):
    #creating an empty list ans
    ans=[]
    #calculating length of m and n
    m=len(stringList)
    n=len(queries)
    #iterating over queries list
    for i in range(0,n):
        count=0
        #iterating over stringList
        for j in range(0,m):
            #if we find the current element of queries in stringList, we will increment the count
            if queries[i]==stringList[j]:
                count+=1
        #append count of the current element of queries 
        ans.append(count)
    return ans
