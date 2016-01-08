uk_x <- runif(1000, -6.37988 , 1.76896)
uk_y <- runif(1000, 49.871159, 55.811741)

coords <- cbind(uk_x,uk_y)


require(rgdal)
require(sp)

a <- readOGR("C:/Users/jpd205/Desktop/GBR_adm","GBR_adm0")
b <- readOGR("C:/Users/jpd205/Desktop/GBR_adm", "GBR_adm2")
plot(a)

york <- b[b$NAME_2 == "York",]
bromley <- b[b$NAME_2 == "Bromley",]

test <- spsample(a, n = 10000, "random")
test2 <- spsample(york, n = 800, "random")
test3 <- spsample(bromley, n = 800, "random")

plot(test)

test.df <- rbind(as.data.frame(test),as.data.frame(test2),as.data.frame(test3))



#####
##Add in some random hashtags as an extra column

hashes <- rep(c("#gary","#bernard","#francois","#lily"),each=nrow(test.df)/4)

final.df <- cbind(test.df,hashes)

write.table(final.df,"C:/Dropbox/PhD/Coding_Projects/Software_Carpentry/Day3/MapTweet/randomsampletweets3.txt",row.names=F)
