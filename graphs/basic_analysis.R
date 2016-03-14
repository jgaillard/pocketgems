data = read.csv('data/Data_Science_Homework.csv', h=T)

kept=sample(1:nrow(data), 1000)
subs=data[kept,]
pairs(subs)
