import random
import math



def nCr(n,r):
    f = math.factorial
    return f(n) // f(r) // f(n-r)

''' Generate the k number of random index to start the k mean clustering'''
def random_points(k,length):
    random_index=[0]*k
    for i in range(k):
        random_index[i]=random.randrange(0,length)
    return random_index

''' Compute the euclidean distance between two points'''
def euclidean_distance(start, end, n):
    #print(start,end)
    #assert(len(start)==len(end))
    diff_sq=[0]*n
    for i in range(n):
        diff_sq[i]=(start[i]-end[i])**2
    return math.sqrt(sum(diff_sq))

'''Find the center of the vector space and return the center vector'''
def find_center(cluster, n):
    assert(len(cluster)!=0)
    x=[]
    center=[]
    for i in range(n):
        x=[]
        for instance in cluster:
            assert (len(instance) != 0)
            x.append(instance[i])
        center.append(sum(x)/len(x))
    return center

'''Base on the index, return the vectors'''
def Get_point(index,dataset):
    points=[]
    for i in index:
        points.append(dataset[i])
    return points

def Hamming_distance(dataset):
    counter=0
    for i in range(len(dataset)-1):
        for j  in range(i+1, len(dataset)):
            if (dataset[i][-2]==dataset[j][-2] and dataset[i][-1]!=dataset[j][-1]) or (dataset[i][-2]!=dataset[j][-2] and dataset[i][-1]==dataset[j][-1]):
                counter+=1
    return counter/nCr(len(dataset),2)


def Lloyd_method(dataset, k, n):
    print("length of the dataset:", len(dataset))
    start_index = random_points(k, len(dataset))
    print("starting index:", start_index)
    start_points = Get_point(start_index, dataset)

    '''Assign the starting point with cluster number'''
    j=0
    for pt in start_points:
        pt.append(j)
        j+=1

    '''Initialize the starting clusters'''
    newclusters=[]
    oldclusters=[]
    for i in range(k):
        newclusters.append([])
        oldclusters.append([])
    #print("length of new clusters", len(newclusters))

    print("start points:", start_points)

    '''Put the start points to the clusters'''
    for item in newclusters:
        item.append(start_points[newclusters.index(item)])

    '''Put the points to the clusters'''
    for vector in dataset:
        distances=[]
        for pt in start_points:
            distances.append(euclidean_distance(vector, pt, n))
        '''Put the data points into the clusters'''
        newclusters[distances.index(min(distances))].append(vector)
        if vector in start_points:
            vector.pop()
        '''Assign the data points with cluster number'''
        vector.append(distances.index(min(distances)))
        #newclusters[distances.index(min(distances))].append(start_points[distances.index(min(distances))])

    '''If the clusters are not converge'''
    while(oldclusters!=newclusters):
        '''keep the copy of the old cluster, start to create new ones'''
        oldclusters = newclusters.copy()
        '''Calculate the new centers'''
        centers=[]
        for cluster in oldclusters:
            #print("index of the cluster in clusters:", newclusters.index(cluster))
            centers.append(find_center(cluster, n))

        '''Initialize the new clusters'''
        newclusters=[]
        for i in range(k):
            newclusters.append([])

        '''Assign the new center with the cluster number'''
        j = 0
        for pt in centers:
            pt.append(j)
            j += 1

        '''for item in newclusters:
            item.append(centers[newclusters.index(item)])'''

        ''''Put the data points to the new clusters'''
        for vector in dataset:
            distances=[]
            for pt in centers:
                #print("data:", vector, "center:", pt)
                distances.append(euclidean_distance(vector, pt, n))
            newclusters[distances.index(min(distances))].append(vector)
            #print("vector before pop:", vector)
            ''''delete the old cluster number'''
            vector.pop()
            #print("vector after pop:", vector)
            '''append new cluster number'''
            vector.append(distances.index(min(distances)))
            #print("vector:", vector)
            #newclusters[distances.index(min(distances))].append(centers[distances.index(min(distances))])


    print("converge happened!!\n\n")




def test():
    ''''format the data'''
    f=open("wdbc.data")
    sample=f.readlines()
    for i in range(len(sample)):
        sample[i] = sample[i].strip().split(',')

    for s in sample:
        s.pop(0)
    print(sample)

    data = []
    for item in sample:
        list=[]
        for i in range(len(item)):
            if i!=0:
                list.append(float(item[i]))
        list.append(item[0])
        data.append(list)

    print(data)
    print(len(data))
    '''Initialize the number of clusters'''
    k=2
    n_attr = 30
    print(random_points(k, len(data)))

    '''clustering the data and calculate the hamming distance'''
    Hdistance=[]
    for i in range(100):
        Lloyd_method(data, k, n_attr)
        distance=Hamming_distance(data)
        print("\t\t\thamming distance:", distance)
        Hdistance.append(distance)
        for instance in data:
            instance.pop()

    print("\t\t\t\t\t\t\tthe lowest Hamming distance is:", min(Hdistance))









if __name__ == '__main__':
    test()
