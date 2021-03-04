# K-Means-Clustering

Week 5 assignments from Intro to Python at JHU

Skills: lists, tuples, file I/O, control structures, string functions

This program performs data anlaysis through k-means clustering. A text file called kmeans.txt, provided by my instructor, provides the data to be used.

The primary data structure I used for the (x, y) points is a list. I read the first seven lines of the text file into individual variables and saved the (x, y) points in a list called points (after having stripped the white space, split each line by commas, and set each point as a tuple within the list). Next, I stored the four cluster points into a list and initialized the variables that will be used in each iteration of the various loops.

The main body of my code starts with a main for loop followed immediately by a nested for loop.  The main for loop iterates through the provided number of iterations found in the kmeans.txt file. The nested for loop iterates through each of the (x, y) points, calculates the distance from each of the four cluster points, and saves the distance to their respective variables. Those variables are stored in another list. The minimum value is determined within that list and from there the closet cluster to the point is determined. Next, the point is assigned to the corresponding cluster and the distance lists are cleared in preparation for the next iteration (of the nested for loop).

The next few blocks of code (which exist outside of the nested for loop but inside of the first/initial for loop) determine the size of each cluster (after each point has been iterated and assigned based on closest proximity), computes the x and y means for each cluster, and determines new coordinates for the cluster centroids. The variable that tracks the number of iterations needed to achieve stability is also incremented based on changes in cluster size. The four new centroid points are also inserted into the list containing 
all of the data points in place of the previous centroid coordinates. Lastly, all lists required for the for loop are cleared in preparation for the next iteration.
