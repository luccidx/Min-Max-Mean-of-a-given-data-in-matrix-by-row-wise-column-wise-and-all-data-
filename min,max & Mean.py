# G Santosh Kumar
# 19 August 2020


data =[[23,33,33,33,3],
       [213,32,23,3,3],
       [55,66,44,66,7]]
# Q - to find min(), Max() and Mean()
# 1 - for all data 
# 2 - for row wise
# 3 - for col wise

#Q1
print("----------------------------------------- ")
print("Finding Min(),Max() & Mean() for all DATA ")
print("----------------------------------------- ")
#1
# MIN() FOR ALL DATA
allmin =[]
a = min(data[0])
b = min(data[1])
c = min(data[2])
allmin.append(a)
allmin.append(b)
allmin.append(c)
minimun_all_data = min(allmin)
print("The Minimum of all data is : ",minimun_all_data)

# MAX() FOR ALL DATA
allmax =[]
aa =max(data[0])
bb =max(data[1])
cc =max(data[2])
allmax.append(aa)
allmax.append(bb)
allmax.append(cc)

maximum_all_data = max(allmax)
print("The Maximum of all data is : ",maximum_all_data)

# MEAN() FOR ALL DATA
sumall =[]

a_sum = sum(data[0])
a_len = len(data[0])
sumall.append(a_sum)

b_sum = sum(data[1])
b_len = len(data[1])
sumall.append(b_sum)

c_sum = sum(data[2])
c_len = len(data[2])
sumall.append(c_sum)

lengthofall = a_len+b_len+c_len
sum_of_all_term = sumall[0]+sumall[1]+sumall[2]

mean = sum_of_all_term/lengthofall
print("The mean of all data is : ",mean)
print("\n")


#2 ROW WISE
print("----------------------------------------- ")
print("Finding Min(),Max() & Mean() ROW Wise")
print("----------------------------------------- ")
print("**************THE MINIMUM**************")
print("The minimum of 1st row : ",a)
print("The minimum of 2nd row : ",b)
print("The minimum of 3rd row : ",c)
print("**************THE MAXIMUM**************")
print("The Maximum of 1st row : ",aa)
print("The Maximum of 2nd row : ",bb)
print("The Maximum of 3rd row : ",cc)
print("**************THE MEAN**************")
print("The Mean of 1st Row: " ,sum(data[0])/len(data[0]))
print("The Mean of 2nd Row: " ,sum(data[1])/len(data[1]))
print("The Mean of 3rd Row: " ,sum(data[2])/len(data[2]))

#3 COLUMN
col1 = []
col1.append(data[0][0])
col1.append(data[1][0])
col1.append(data[2][0])
col2 =[]
col2.append(data[0][1])
col2.append(data[1][1])
col2.append(data[2][1])
col3 =[]
col3.append(data[0][2])
col3.append(data[1][2])
col3.append(data[2][2])
col4 =[]
col4.append(data[0][3])
col4.append(data[1][3])
col4.append(data[2][3])
col5 =[]
col5.append(data[0][4])
col5.append(data[1][4])
col5.append(data[2][4])

col_data =[]
col_data.append(col1)
col_data.append(col2)
col_data.append(col3)
col_data.append(col4)
col_data.append(col5)
print("\n")

print("----------------------------------------- ")
print("Finding Min(),Max() & Mean() COLUMN Wise")
print("----------------------------------------- ")
print("**************THE MINIMUM**************")
print("The minimum of 1st column : " ,min(col1))
print("The minimum of 2nd column : " ,min(col2))
print("The minimum of 3rd column : ", min(col3))
print("The minimum of 4th column : ", min(col4))
print("The minimum of 5th column : ", min(col5))
print("**************THE MAXIMUM**************")
print("The Maximum of 1st column : " ,max(col1))
print("The Maximum of 2nd column : " ,max(col2))
print("The Maximum of 3rd column : ", max(col3))
print("The Maximum of 4th column : ", max(col4))
print("The Maximum of 5th column : ", max(col5))
print("**************THE MEAN**************")
print("The Mean of 1st column : " ,sum(col1)/len(col1))
print("The Mean of 2nd column : " ,sum(col2)/len(col2))
print("The Mean of 3rd column : ", sum(col3)/len(col3))
print("The Mean of 4th column : ", sum(col4)/len(col4))
print("The Mean of 5th column : ", sum(col5)/len(col5))