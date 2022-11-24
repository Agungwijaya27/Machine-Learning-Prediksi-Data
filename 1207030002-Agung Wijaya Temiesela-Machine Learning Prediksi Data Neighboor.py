from sklearn.neighbors import NearestCentroid

# Dtabase : Gerbang logika AND
# x = Data, y = Target
x = [[0,0],[0,1],[1,0],[1,1], [0,3], [3,0], [3,1], [3,2], [3,3], [0,4], [4,0], [4,1], [4,2],]
y = [0,0,0,1,0,0,0,0,1,0,0,0,0]

# Traininy and Classify
clf = NearestCentroid()
clf = clf.fit(x,y)

# Prediksi
print ("Logika AND Metode Nearest Neighbots")
print ("Logika = Prediksi")
print ("0 0 = ", clf.predict([[0,0]]))
print ("0 1 = ", clf.predict([[0,1]]))
print ("1 0 = ", clf.predict([[1,0]]))
print ("1 1 = ", clf.predict([[1,1]]))
print ("0 4 = ", clf.predict([[0,4]]))
print ("3 0 = ", clf.predict([[3,0]]))
print ("3 1 = ", clf.predict([[3,1]]))
print ("3 2 = ", clf.predict([[3,2]]))
print ("3 3 = ", clf.predict([[3,3]]))
print ("0 4 = ", clf.predict([[0,4]]))
print ("4 0 = ", clf.predict([[4,0]]))
print ("4 1 = ", clf.predict([[4,1]]))
print ("4 2 = ", clf.predict([[4,2]]))
