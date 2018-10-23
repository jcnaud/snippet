plot(sin, -pi, 2*pi) # see ?plot.function


plot(table(rpois(100, 5)), 
    type = "h",
    col = "red",
    lwd = 10,
    main = "rpois(100, lambda = 5)")


# par : adjusts plotting parameters 
#  mar : margin size, "bottom, left, top, and right" (DEFAULT : 5.1 4.1 4.1 2.1)
#  mgp : axis label locations, "location, tick-mark labels, tick." (DEFAULT : 3 1 0)
#  las : axis label orientation "0: default, 1: horizontal, 2: axis vectical, 3: vertical"

set.seed(5)
x <- rnorm(200)
y <- 25 - 22*x + 5*x^2 + rnorm(200)

png("par-example.png")
par(mar=c(3.5, 3.5, 2, 1), mgp=c(2.4, 0.8, 0), las=1)
plot(x, y, main="par(mar=c(3.5, 3.5, 2, 1), mgp=c(2.4, 0.8, 0), las=1)")
dev.off()


print("finish")