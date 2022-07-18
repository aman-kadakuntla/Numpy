import numpy as np

# a=np.array([1,2,3,4]) # single dimensional array
# print(a) # print array

# b=np.array([[1,2,3,4],[1,2,3,4]])# two dimensional array
# print(b)

# s=b.size # returns number of elements
# print(s)

# single_element_size=a.itemsize # returns the size of the single element in bytes
# print("Single element size=",single_element_size)

# total_size_in_bytes=a.nbytes # returns the size of the all the elements in bytes
# print("total size in bytes=", total_size_in_bytes)

# dimension=a.ndim # returns the dimension of the array
# print("a dimension=",dimension)

# dimension=b.ndim # returns the dimension of the array
# print("b dimension=",dimension)

# # To find the shape of the array, we use shape property of the array. It returns a tuple(rows,columns)
# shape_of_array=a.shape
# print("shape of array a = ",shape_of_array)

# shape_of_array=b.shape
# print("shape of array b = ",shape_of_array)

# # access the elements of single dimensional array
# print(a[1])

# #access the individual element of two dimensional array
# print(b[0,1])
# print(b[1,2])

# # print a single row of two dimensional array
# b=np.array([[1,2,3,4],[5,6,7,8]])
# print(b[1,:])

# #print a single column of two dimensional array
# print(b[:,1])

# #fill an array with all zeros
# a=np.zeros((2,3))# returns an array of 2 rows and 3 columns with 0 as element
# print(a)

# #fill an array with all ones. By default all values will be float values
# a=np.ones((3,4))
# print(a)

# #fill an array with all ones(integers)
# a=np.ones((3,4),dtype=np.int16)
# print(a)

# #fill an array with a number
# a=np.full((3,3),9)
# print(a)

# #fill an array with random numbers
# a=np.random.rand(4,2)
# print(a)

# #identity matrix
# a=np.identity(4,dtype=np.int16)
# print(a)

# #copy array a to b
# a=np.array([1,2,3,4])
# b=a.copy()
# print(b)

# #increase all the elements by n
# a=a+2
# print(a)

# #decrease all the elements by n
# a=np.array([1,2,3,4])
# print(a-2)

# #print the power of all elements
# a=np.array([1,2,3,4])
# a=a**2
# print(a)

# #matrix slicing
# a=np.array([[1,2,3],[4,5,6],[7,8,9]])
# print(a) # prints whole matrix
# print(a[0:4,0:2])# prints a part of matrix


# # create a single dimension array dynamically
# size = int(input("Size="))
# arr=np.ndarray(shape=(size),dtype=int)#ndarray is used to create arrays dynamically
# print("Enter {0} elements",size)
# for i in range(size):
#     arr[i]=int(input())
# print(arr)

# # create a two dimensional array dynamically
# rows = int(input("rows="))
# cols = int(input("cols="))
# arr=np.ndarray(shape=(rows,cols),dtype=int)#ndarray is used to create arrays dynamically
# print("Enter %d elements"%(rows*cols))
# for i in range(rows):
#     for j in range(cols):
#         arr[i][j]=int(input())
# print(arr)


#numpy arange function is used to fill the array with a range of numbers
a=np.arange(10)
print(a)

#numpy arange function using a step
a=np.arange(1,10,2)#starts with 1 and goes upto 10 skipping one element
print(a)

#generate a diagonal matrix
a=np.diag([1,2,3])
print(a)
