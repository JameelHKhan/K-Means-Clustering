# Jameel H. Khan
# Module 5 Assignment

from math import sqrt

# Step 1 of assignment requirements:
# (1a) open file
# (1b) read initial fields into individual variables
# (1c) read points into list/tuple

# create initial list for file read
points = []

# variable to track count of number of iterations to achieve stability
convergence = 0

# (1a) open kmeans.txt for reading
f = open("C:/Users/Jameel/Desktop/kmeans.txt", "r")

# (1b) read first seven lines of file to individual variables, convert to int
maxIterations = int(f.readline())
pointsInFile = int(f.readline())
totalClusters = int(f.readline())
clusterOneIndex = int(f.readline())
clusterTwoIndex = int(f.readline())
clusterThreeIndex = int(f.readline())
clusterFourIndex = int(f.readline())

# (1c) read points into list
for line in f.readlines():
    # remove new lines, split points (x, y) on commas
    point = line.strip().split(",")
    # convert each number to int, store points (x, y) as tuples in list
    points.append((int(point[0]), int(point[1])))

# Step 2 of assignment requirements:
# create tuple/list containing 4 centroids from file
clustersFromFile = [list(points[clusterOneIndex]),
                    list(points[clusterTwoIndex]),
                    list(points[clusterThreeIndex]),
                    list(points[clusterFourIndex])]

# Step 3 of assignment requirements:
# create 2-D list where each inner list represents one of the k clusters
# create lists to track points and size of each cluster
clusters2DList = [[], [], [], []]
clusterSizeInitial = [0, 0, 0, 0]
clusterSizeIterate = [0, 0, 0, 0]  # final cluster sizes at end of loop
# the following lists are used to calculate averages of points
clus0XValues = []
clus0YValues = []
clus1XValues = []
clus1YValues = []
clus2XValues = []
clus2YValues = []
clus3XValues = []
clus3YValues = []

# Step 4 of assignment requirements:
# (4a) compute distance between each point and each k centroid
# (4b) after completing (a) check cluster sizes and update convergence
#      iteration variable
# (4c) compute the mean of all x values for each cluster
# (4d) clear contents of each cluster if not in final loop
for i in range(maxIterations + 1):
    for j in range(len(points)):
        # calculate distance of all points from 1st centroid
        disC1 = sqrt(((clustersFromFile[0][0] - points[j][0])**2)
                     + ((clustersFromFile[0][1] - points[j][1])**2))
        # calculate distance of all points from 2nd centroid
        disC2 = sqrt(((clustersFromFile[1][0] - points[j][0])**2)
                     + ((clustersFromFile[1][1] - points[j][1])**2))
        # calculate distance of all points from 3rd centroid
        disC3 = sqrt(((clustersFromFile[2][0] - points[j][0])**2)
                     + ((clustersFromFile[2][1] - points[j][1])**2))
        # calculate distance of all points from 4th centroid
        disC4 = sqrt(((clustersFromFile[3][0] - points[j][0])**2)
                     + ((clustersFromFile[3][1] - points[j][1])**2))

        # save four distances into a list and determine the smallest distance
        tempCList = [disC1, disC2, disC3, disC4]
        tempCListMin = min(tempCList)

        # determine closest cluster and assign point to that cluster
        if tempCListMin == disC1:
            clusters2DList[0].append(points[j])
        elif tempCListMin == disC2:
            clusters2DList[1].append(points[j])
        elif tempCListMin == disC3:
            clusters2DList[2].append(points[j])
        else:
            clusters2DList[3].append(points[j])

        # clear temp list for next iteration
        tempCList.clear()
        # end of j for loop

# (4b) determine size of each cluster, then check if any clusters changed
# if yes, increment convergence variable
    clusterSizeIterate[0] = len(clusters2DList[0])
    clusterSizeIterate[1] = len(clusters2DList[1])
    clusterSizeIterate[2] = len(clusters2DList[2])
    clusterSizeIterate[3] = len(clusters2DList[3])

    if clusterSizeIterate[0] != clusterSizeInitial[0]:
        convergence += 1
    elif clusterSizeIterate[1] != clusterSizeInitial[1]:
        convergence += 1
    elif clusterSizeIterate[2] != clusterSizeInitial[2]:
        convergence += 1
    elif clusterSizeIterate[3] != clusterSizeInitial[3]:
        convergence += 1

# (4c.i & ii) compute the mean of all x values for each cluster
# save the points of each cluster in unique variables
    cluster0Points = clusters2DList[0]
    cluster1Points = clusters2DList[1]
    cluster2Points = clusters2DList[2]
    cluster3Points = clusters2DList[3]

    # extract x, y coordinates from each cluster
    # cluster 0
    for l in range(len(cluster0Points)):
        clus0XValues.append(cluster0Points[l][0])
        clus0YValues.append(cluster0Points[l][1])
    # cluster 1:
    for l in range(len(cluster1Points)):
        clus1XValues.append(cluster1Points[l][0])
        clus1YValues.append(cluster1Points[l][1])
    # cluster 2:
    for l in range(len(cluster2Points)):
        clus2XValues.append(cluster2Points[l][0])
        clus2YValues.append(cluster2Points[l][1])
    # cluster 3:
    for l in range(len(cluster3Points)):
        clus3XValues.append(cluster3Points[l][0])
        clus3YValues.append(cluster3Points[l][1])

    # Compute mean
    # cluster 0 x, y mean
    meanOfClus0XValues = sum(clus0XValues)/len(clus0XValues)
    meanofClus0YValues = sum(clus0YValues)/len(clus0YValues)
    # cluster 1 x, y mean
    meanOfClus1XValues = sum(clus1XValues)/len(clus1XValues)
    meanofClus1YValues = sum(clus1YValues)/len(clus1YValues)
    # cluster 2 x, y mean
    meanOfClus2XValues = sum(clus2XValues)/len(clus2XValues)
    meanofClus2YValues = sum(clus2YValues)/len(clus2YValues)
    # cluster 3 x, y mean
    meanOfClus3XValues = sum(clus3XValues)/len(clus3XValues)
    meanofClus3YValues = sum(clus3YValues)/len(clus3YValues)

# (4c.iii) Update the cluster centroids
    clustersFromFile = [[meanOfClus0XValues, meanofClus0YValues],
                        [meanOfClus1XValues, meanofClus1YValues],
                        [meanOfClus2XValues, meanofClus2YValues],
                        [meanOfClus3XValues, meanofClus3YValues]]

    # replace original cluster points with new average points in points list
    points[clusterOneIndex] = (meanOfClus0XValues, meanofClus0YValues)
    points[clusterTwoIndex] = (meanOfClus1XValues, meanofClus1YValues)
    points[clusterThreeIndex] = (meanOfClus2XValues, meanofClus2YValues)
    points[clusterFourIndex] = (meanOfClus3XValues, meanofClus3YValues)

    # clear list of cluster sizes from previous iteration and set it equal to
    # values from current cluster size determination in preparation for next
    # iteration
    clusterSizeInitial = [0, 0, 0, 0]
    # clusterSizeIterate fulfills assignment requirement 4c.iv: store/update
    # the current size of each cluster in a list
    clusterSizeInitial[0] = clusterSizeIterate[0]
    clusterSizeInitial[1] = clusterSizeIterate[1]
    clusterSizeInitial[2] = clusterSizeIterate[2]
    clusterSizeInitial[3] = clusterSizeIterate[3]
    # clearing other lists needed to be reused for each iteration
    cluster0Points = []
    cluster1Points = []
    cluster2Points = []
    cluster3Points = []
    clus0XValues = []
    clus0YValues = []
    clus1XValues = []
    clus1YValues = []
    clus2XValues = []
    clus2YValues = []
    clus3XValues = []
    clus3YValues = []

# (4d) clear contents of each cluster if not in final loop
    if i == maxIterations:
        pass
    else:
        clusters2DList = [[], [], [], []]

# Step 5 of assignment requirements: print output
print("\n")
print("Iterations to achieve stabiilty: " + str(convergence))
print("Centroid 0: " + str(clustersFromFile[0]))
print("Number of points in Cluster 0: " + str(clusterSizeIterate[0]))
print("Cluster 0: " + str(clusters2DList[0]))
print("\n")
print("Centroid 1: " + str(clustersFromFile[1]))
print("Number of points in Cluster 1: " + str(clusterSizeIterate[1]))
print("Cluster 1: " + str(clusters2DList[1]))
print("\n")
print("Centroid 2: " + str(clustersFromFile[2]))
print("Number of points in Cluster 2: " + str(clusterSizeIterate[2]))
print("Cluster 2: " + str(clusters2DList[2]))
print("\n")
print("Centroid 3: " + str(clustersFromFile[3]))
print("Number of points in Cluster 3: " + str(clusterSizeIterate[3]))
print("Cluster 3: " + str(clusters2DList[3]))
