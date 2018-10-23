# Create matrix

m1 <- matrix(1,2,3) # default value, row dimension, col dimention
m1

rownames = c("row1", "row2")
colnames = c("col1", "col2", "col3")
m2 <- matrix(
    c(2, 4, 3, 1, 5, 7), # the data elements 
    nrow=2,              # number of rows 
    ncol=3,              # number of columns 
    byrow = TRUE,        # fill matrix by rows  
    dimnames = list(rownames, colnames)) # rwn and col names
m2

# Create tricks
m3 <- diag(3) # Identity matrix
m3

m4 = seq(0, 1.5, l = 11) # Start value, step value, total number of value generated
m4

result <- m3 + m3
result

# Accessing
# plot(m["c",], m["b",]) # print row c (row number 3) 
# print("See Rplots.pdf")


# plot(m[,"v"], m[,"w"])

