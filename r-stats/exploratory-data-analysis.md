# Exploratory Data Analysis

## Principles of Analytic Graphs

> Graphs give us a visual form of data, and the first principle of analytic graphs is to show some comparison. You'll hear more about this when you study statistical inference (another great course BTW), but evidence for a hypothesis is always relative to another competing or alternative hypothesis.

> When presented with a claim that something is good, you should always ask "Compared to What?" This is why in commercials you often hear the phrase "other leading brands". An implicit comparison, right?

So the first principle was to show a **comparison**.
The second principle is to show **causality** or a mechanism of **how your theory of the data works**
The third principle is to show **multivariate data**

Most hard problems have more variables

Restricting yourself to 2 variables you might be misled and draw an incorrect conclusion

A singel variable may give rise to Simpson's paradox where a trend appears in certain groups but dissapears when groups are combined. It happens when frequency data is unduly given causal interpretations.
Often in social science and medical science studies.

The fourth principle is **integrating evidence**. Don't use a single form of expression.

> Don't let the tool drive the analysis

The fifth principle of graphing involves **describing and documenting the evidence with sources and appropriate labels and scales**.

> Also, using R, you want to preserve any code you use to generate your data and graphics so that the research can be replicated if necessary. This allows for easy verification or finding bugs in your analysis.

The sixth principle is **Content is king**

> Analytical presentations ultimately stand or fall depending on the quality, relevance, and integrity of their content.

1. Comparison
2. Causality
3. Multivariate Data
4. Integrate Evidence
5. Describe and document evidence with sources, labels and scales
6. Content is king

## Exploratory Graphs

> So graphics give us some visual form of data, and since our brains are very good at seeing patterns, graphs give us a compact way to present data and find or display any pattern that may be present.

Exploratory graphs serve mostly the same functions as graphs. They help us find patterns in data and understand its properties. They suggest modeling strategies and help to debug analyses. We **DON'T** use exploratory graphs to communicate results.

Getting asummary of data:

    > summary(pollution$pm25)
    Min. 1st Qu.  Median    Mean 3rd Qu.    Max. 
    3.383   8.549  10.047   9.836  11.356  18.441 

* Minimum (0 percentile)
* Maximum (100 percentile)
* 25%: 1st quartile
* 50%: median
* 75%: 3rd quartile

The median specifies that half of the measured fact have a value less than or equal to that median.
Anohter half of the data set has greater or equal to that value.

### Quantile

    > quantile(ppm)
        0%       25%       50%       75%      100% 
    3.382626  8.548799 10.046697 11.356012 18.440731

We use a boxplot to display this:

    > boxplot(ppm, col="blue")

In a boxplot the top and bottom of the box represent the values of the 25% and 75% quartiles.
The midde horizontal line is the median.
The whiskers (horizontal lines) outside the box represent the range defualte to 1.5 the interquartile range.
The interquartile range is the difference between the 75% and 25% quartiles.

Data points outside the whiskers are outliers.

### Striaght Lines

You can overlay lines on the plot with:

     abline(h=12)

Create a green histogram

    > hist(ppm, col="green")

Some more detailed greyscale representation of occurances

This one-dimensional plot, with its grayscale representation, gives you a little more detailed information about how many data points are in each bucket and where they lie within the bucket.

Use `breaks` to set the number of buckets to split the data into:

    > hist(ppm, col="green", breaks=100)

> `rug` automatically adjusted its pocket size to that of the last plot plotted.

Add line with extra width:

    > abline(v=12, lwd=2)

Change colour of `abline`:

    > abline(v=median(ppm), col="magenta", lwd=4)

Make table of factor data:

    > table(pollution$region)

    east west 
    442  134

### Barplot

    barplot(reg, col = "wheat", main = "Number of Counties in Each Region")

### Boxplot

    > boxplot(formula=pm25~region, data=pollution, col="red")

### Multiple Histograms

To plot multiple histograms we need to set the layout with `par`

Also margins is a 4-long vector which indicates the number of lines for the bottom, left, top and right

    par(mfrow=c(2,1),mar=c(4,4,2,1))

`mfrow=c(2,1)` means 2 rows and 1 column

#### Subset

To split the data up:

    > east <- subset(pollution, region == 'east')

    > hist(east$pm25, col='green')

Doing the above in one command:

    > hist(subset(pollution,region=="west")$pm25, col = "green")

Using the `with` keyword:

    > with(pollution, plot(latitude, pm25))

So you can avoid using: `pollution$pm25`

Create a dashed horizontal line:

    abline(h=12, lwd=2, lty=2)

## Plot

You can set the colours of points based on region

    > plot(pollution$latitude, ppm, col=pollution$region)

* Exploratory plots are **quick and dirty**
* Plots let you summarize the data (usually graphically) and highlight any broad features

# Graphics Devices in R

There is a screen device (window on device) or file devices (PDF, JPEG, SVG)

> How you access your screen device depends on what computer system you're using. On a Mac the screen device is launched with the call `quartz()`, on Windows you use the call `windows()`, and on Unix/Linux `x11()`

View available devices with:

    > ?Devices

Create a box plot:

    > with(faithful, plot(eruptions, waiting))

Annotate the main title:

    > title(main='Old Faithful Geyser data')

View the current plotting device:

    > dev.cur()
    RStudioGD 
        2

### Creating a plot on a file device

Launch the file device

    > pdf(file="myplot.pdf")

Then run the plot again:

    > with(faithful, plot(eruptions, waiting))
    > title(main='Old Faithful Geyser data')

After done you have to close it with:

    > dev.off()

There are two basic types of file devices, vector and bitmap devices:
* `Vector` formats are good for line drawings and plots with solid colors using a modest number of points
* `Bitmap` formats are good for plots with a large number of points, natural scenes or web-based plots

#### Vector Formats

* `pdf`: line-type graphics and papers. It resizes well, is usually portable, but it is not efficient if a plot has many objects/points.
* `svg`: XML-based, scalable vector graphics. This supports animation and interactivity and is potentially useful for web-based plots.

> The last two vector formats are win.metafile, a Windows-only metafile format, and postscript (ps), an older format which also resizes well, is usually portable, and can be used to create encapsulated postscript files. Unfortunately, Windows systems often don’t have a postscript viewer.

#### Bitmap formats

* `png`: Portable Network Graphics which is good for line drawings or images with solid colors. It uses lossless compression (like the old GIF format), and most web browsers can read this format natively. In addition, png is good for plots with many points, but it does not resize well.
* `jpeg`: files are good for photographs or natural scenes. They use lossy compression, so they're good for plots with many points. Files in jpeg format don't resize well, but they can be read by almost any computer and any web browser. They're not great for line drawings.
* `tiff`: an older lossless compression meta-format and bmp which is a native Windows bitmapped format.

#### Devices

> Every open graphics device is assigned an integer greater than or equal to 2

You can change the active device with:

    dev.set(<integer>)

You can copy between devices:

> The function `dev.copy` copies a plot from one device to another, and `dev.copy2pdf` specifically copies a plot to a PDF file.

    > dev.copy(png, file='geyserplot.png')

## Plotting Systems

### Base Plotting System

* Comes with `R`
* Start with a blank canvas
* Intuitive and Exploratory
* You can't go backwards
* based on "Artist's Pallette"

### Lattice plots

* single function call such as `xyplot` or `bwplot`
* most useful for conditioning types of plots which display how y changes with x across levels of z
* Cannot add to the plot

Using the R forumla: `Life.Exp ~ Income | region`: we're plotting life expectancy as it depends on income for each region

    > xyplot(Life.Exp ~ Income | region, state, layout=c(4,1))

The second argument is data

and the third shows layout is 4 columns 1 row

### GGPlot2

The best of both worlds, does automatic titles and margins etc but also allows annotatins and adding.

    > qplot(displ, hwy, data = mpg)

* Uses Graphics Grammar

## Base Plotting System

See the range for a column of data excluding `NA`:

    range(airquality$Ozone, na.rm=TRUE)

#### Histogram

Uses one variable

    > hist(airquality$Ozone)

#### Boxplot

    > boxplot(Ozone~Month, airquality)

Adding labels and colours:

    > boxplot(Ozone~Month, airquality, xlab='Month', ylab='Ozone (ppb)', col.axis='blue', col.lab='red')

Check number of parameters you can give to `par()`

    > length(par())
    [1] 72

The available options are:

    > names(par())
    [1] "xlog"      "ylog"      "adj"       "ann"       "ask"       "bg"        "bty"      
    [8] "cex"       "cex.axis"  "cex.lab"   "cex.main"  "cex.sub"   "cin"       "col"      
    [15] "col.axis"  "col.lab"   "col.main"  "col.sub"   "cra"       "crt"       "csi"      
    [22] "cxy"       "din"       "err"       "family"    "fg"        "fig"       "fin"      
    [29] "font"      "font.axis" "font.lab"  "font.main" "font.sub"  "lab"       "las"      
    [36] "lend"      "lheight"   "ljoin"     "lmitre"    "lty"       "lwd"       "mai"      
    [43] "mar"       "mex"       "mfcol"     "mfg"       "mfrow"     "mgp"       "mkh"      
    [50] "new"       "oma"       "omd"       "omi"       "page"      "pch"       "pin"      
    [57] "plt"       "ps"        "pty"       "smo"       "srt"       "tck"       "tcl"      
    [64] "usr"       "xaxp"      "xaxs"      "xaxt"      "xpd"       "yaxp"      "yaxs"     
    [71] "yaxt"      "ylbias"

Background colour

    > par('fg')
    [1] "black"

Plot character

    > par('pch')
    [1] 1 (Circle)

Line type

    > par('lty')
    [1] "solid"

> The `par()` function is used to specify global graphics parameters that affect all plots in an R session. (Use dev.off or plot.new to reset to the defaults.)

* `las` (the orientation of the axis labels on the plot)
* `bg` (background color)
* `mar` (margin size)
* `oma` (outer margin size)
* `mfrow` (plots per row)
* `mfcol` (plots per column)

`lines` can be used to add lines to the plot

Create a plot but do not plot the points:

    plot(airquality$Wind, airquality$Ozone, type='n')

Then add points

    > points(may$Wind,may$Ozone,col="blue",pch=17)

Adding a legend:

    > legend('topright', pch=c(17, 8), co=c("blue", "red"), legend=c("May", "Other Months"))

Add absolute line at the median:

    abline(v=median(airquality$Wind), lty=2, lwd=2)

Giving a title to many plots

    > mtext("Ozone and Weather in New York City", outer=TRUE)

## Lattice Plotting System

Must be loaded: `library('lattice')`

Lattice is implemented using 2 packages:
* `lattice` contains code for producing trellis graphics. These include `xyplot`, `bwplot`, and `levelplot`
* `grid` system: low level functions

* `xyplot` produces a scatterplot
* `bwplot` produces a box and whisker plot
* `histogram` produces a histogram


All plotting is done in a single call
Lattice functions gnerally take a formua as their first argument. (`y ~ x`)

    xyplot(y ~ x | f * g, data)

`g` would represent optional conditions

    xyplot(Ozone ~ Wind, data=airquality)

Add snowflake marks:

    > xyplot(Ozone~Wind, data=airquality, col='red', pch=8, main='Big Apple Data')

As factor:

    > xyplot(Ozone ~ Wind | as.factor(Month), data=airquality, layout=c(5,1))

> Since Month is a named column of the airquality dataframe we had to tell R to treat it as a factor

> Lattice functions behave differently from base graphics functions in one critical way.
Recall that base graphics functions plot data directly to the graphics device (e.g., screen, or file such as a PDF file). In contrast, lattice graphics functions return an object of class trellis.

lattice returns the `Trellis` object.

    p <- xyplot(Ozone~Wind,data=airquality)

Type `p` or `print(p)` to show the chart

See arguments for the object:

    > names(p)
    [1] "formula"           "as.table"          "aspect.fill"       "legend"           
    [5] "panel"             "page"              "layout"            "skip"             
    [9] "strip"             "strip.left"        "xscale.components" "yscale.components"
    [13] "axis"              "xlab"              "ylab"              "xlab.default"     
    [17] "ylab.default"      "xlab.top"          "ylab.right"        "main"             
    [21] "sub"               "x.between"         "y.between"         "par.settings"     
    [25] "plot.args"         "lattice.options"   "par.strip.text"    "index.cond"       
    [29] "perm.cond"         "condlevels"        "call"              "x.scales"         
    [33] "y.scales"          "panel.args.common" "panel.args"        "packet.sizes"     
    [37] "x.limits"          "y.limits"          "x.used.at"         "y.used.at"        
    [41] "x.num.limit"       "y.num.limit"       "aspect.ratio"      "prepanel.default" 
    [45] "prepanel"  

Get the formula

    > p[["formula"]]
    Ozone ~ Wind

Check the limits of the x value:

    > p[['x.limits']]
    [1]  0.37 22.03

Lattice create a file to create the plot:

    p2 <- xyplot(y ~ x | f, panel = function(x, y, ...) {
        panel.xyplot(x, y, ...)  ## First call default panel function
        panel.lmline(x, y, col = 2)  ## Overlay a simple linear regression line
    })
    print(p2)
    invisible()

to  run this do:

    source(pathtofile("plot2.R"), local=TRUE)

Table of multiple values:

    > table(diamonds$color, diamonds$cut)
   
        Fair Good Very Good Premium Ideal
    D  163  662      1513    1603  2834
    E  224  933      2400    2337  3903
    F  312  909      2164    2331  3826
    G  314  871      2299    2924  4884
    H  303  702      1824    2360  3115
    I  175  522      1204    1428  2093
    J  119  307       678     808   896

Edit `myLabels.R`:

    > myedit('myLabels.R')
    source(pathtofile('myLabels.R'), local=TRUE)

Using the labels:

    > xyplot(price~carat | color*cut,data=diamonds,  strip=FALSE, pch=20, xlab = myxlab, ylab=myylab, main=mymain)

The `strip=FALSE` variable removes labels from the panels

> The lattice system is ideal for creating conditioning plots where you examine the same kind of plot under many different conditions.

## Working with Colors

> Effectively using colors can enhance your plots and presentations, emphasizing the important points you're trying to convey

`grDevices` gives you the `colouors()` function

Get a sample of some colours:

    > sample(colors(), 10)
    [1] "cornsilk2"       "aquamarine4"     "gray75"          "grey46"         
    [5] "honeydew"        "gray43"          "grey50"          "palegoldenrod"  
    [9] "lightsteelblue2" "indianred3"

`colorRamp` and `colorRampPalette` blend colours together

> The first, colorRamp, takes a palette of colors (the arguments) and returns a function that takes values between 0 and 1 as arguments. The 0 and 1 correspond to the extremes of the color palette. Arguments between 0 and 1 return blends of these extremes.

    > pal <- colorRamp(c('red', 'blue'))

So:

    > pal(0)
    [,1] [,2] [,3]
    [1,]  255    0    0

Which gives `RGB` colours

So pal creates colors using the palette we specified when we called colorRamp

    > pal(seq(0,1,len=6))
        [,1] [,2] [,3]
    [1,]  255    0    0
    [2,]  204    0   51
    [3,]  153    0  102
    [4,]  102    0  153
    [5,]   51    0  204
    [6,]    0    0  255

ColorRampalette

    > p1 <- colorRampPalette(c('red', 'blue'))

    > p1(2)
    [1] "#FF0000" "#0000FF"

> `colorRamp` and `colorRampPalette` could return a 3 or 4 long vector of colors

Set the alpha

    p3 <- colorRampPalette(c('blue', 'green'), alpha=.5)

> Alpha represents an opacity level, that is, how transparent should the colors be

An alpha will help you if there are manny scatter points together and you want to know the density

    > plot(x, y, pch=19, col=rgb(0, .5, .5, .3))

In the above `.3` is the density

### RColorBrewer

Three types:
* `sequential` - light to dark
* `divergent` - divergent (neutral colour white is centre)
* `qualitative` - random colours used to distinguish data

Use a palette:

    > cols <- brewer.pal(3, 'BuGn')
    [1] "#E5F5F9" "#99D8C9" "#2CA25F"

    > pal <- colorRampPalette(cols)

Using the pallete:

    > image(volcano, col=pal(20))

## GGPlot2 Part1

[Complete docuemtnation on ggplot2](http://ggplot2.org)

Grammar of Graphics

`ggplot2` combines the best of base and lattice

2 workhorse functions:
* qplot - Less flexible
* ggplot - More flexible

Basic plot:

    > qplot(displ, hwy, data=mpg)

Add an aestheitc (colour based on factor)

    > qplot(displ, hwy, data=mpg, color=drv)

We can automatically add a trendlines with the use of `geom`, the first element means data piint and second is trnedline.

    > qplot(displ, hwy, data=mpg, color=drv, geom=c('point', 'smooth'))

> Notice the gray areas surrounding each trend lines. These indicate the 95% confidence intervals for the lines

If no x-axis is given the plot will just show the index /order of the value in the dataset:

    > qplot(y=hwy, data=mpg, color=drv)

Create a box and whisker plot:

    > qplot(drv, hwy, data=mpg, geom='boxplot')

Set the colour to a factor:

    > qplot(drv, hwy, data=mpg, geom='boxplot', color=manufacturer)

Create a histogram with coloured attribute:

    > qplot(hwy, data=mpg, fill=drv)

> `. ~ drv` is ggplot2's shorthand for number of rows (to the left of the `~`)

#### Scatterplot split into panels / facets

    > qplot(displ, hwy, data=mpg, facets=. ~ drv)

#### Histogram split into panels

    > qplot(hwy, data=mpg, facets=drv ~ ., binwidth=2)

The facet argument `drv ~ .` resulted in a `3 by 1` setup.

## GGPlot2 Part2

### Components of GGPLot2

* DATA FRAME - data you are plotting
* AESTHETIC MAPPINGS - how data is mapped to color, size, etc.
* GEOMS (geometric objects) - are what you see in the plot (points, lines, shapes)
* FACETS - panels used in conditional plots
* STATS - statistical transformations (binning, quantiles, and smoothing)
* SCALES - what coding an aesthetic map uses (for example, male = red, female = blue)
* COORDINATE SYSTEM - how plots are depicted

Point and smooth scatterplot:

    > qplot(displ, hwy, data=mpg, geom=c('point', 'smooth'), facets=.~drv)

Creating a mapping:

    > g <- ggplot(mpg, aes(displ, hwy))

Summary of graphical object:

    > summary(g)
    data: manufacturer, model, displ, year, cyl, trans, drv, cty, hwy, fl, class
    [234x11]
    mapping:  x = displ, y = hwy

A `234 x 11` matrix and a `x (displ) and y (hwy)` mapping

Tell `ggplot2` how to show the data:

    > g+geom_point()

Show points and trend line:

    > g+geom_point()+geom_smooth()

Change the smoothing function to linear model:

    > g+geom_point()+geom_smooth(method="lm")

Split it into `facets`:

    > g+geom_point()+geom_smooth(method="lm")+facet_grid(. ~ drv)

Add a title to the chart:

    > g+geom_point()+geom_smooth(method="lm")+facet_grid(. ~ drv)+ggtitle('Swirl Rules!')

> Two standard appearance themes are included in ggplot. These are `theme_gray()` which is the default theme (gray background with white grid lines) and `theme_bw()` which is a plainer (black and white) color scheme.

Create geometric points with colour, alpha and size:

    > g+geom_point(color='pink', size=4, alpha=1/2)

Color based on factor:

    > g+geom_point(size=4, alpha=1/2, aes(color=drv))

Changing labels:

    g + geom_point(aes(color = drv)) + labs(title="Swirl Rules!") + labs(x="Displacement", y="Hwy Mileage")

Dashed linear regression line and turn off confidence level grey area:

    > g + geom_point(size=2, alpha=1/2, aes(color = drv)) + geom_smooth(size=4, linetype=3, method='lm', se=FALSE)

Change the theme and font style:

    > g+geom_point(aes(color=drv))+theme_bw(base_family='Times')

### Outlier Data

Set limits to not show an outlier

Using plot with outlier data:

    > plot(myx, myy, type='l', ylim=c(-3,3))

With ggplot:

    > g <- ggplot(testdat, aes(x=myx, y=myy))
    > g+geom_line()+ylim(-3,3)

Can also be done by limiting the coordinate system:

    > g + geom_line() + coord_cartesian(ylim=c(-3,3))

Create facetted scatterplot with marginal totals:

    > g + geom_point() + facet_grid(drv~cyl, margins=TRUE)

With a smooth trendline:

    > g + geom_point() + facet_grid(drv~cyl, margins=TRUE) + geom_smooth(method='lm', se=FALSE, size=2, color='black')

## GGPlot2 Extras

You can specify the binwidth (usually range / x):

    > qplot(price, data=diamonds, binwidth=18497/30)

Change fill of histogram based on factor:

    > qplot(price, data=diamonds, binwidth=18497/30, fill=cut)

Histogram as a density function:

    > qplot(price, data=diamonds, geom='density')

Density by colour:

    > qplot(price, data=diamonds, geom='density', color=cut)

Change shape based on cut:

    > qplot(carat, price, data=diamonds, shape=cut)

Add regression lines for each cut:

    > qplot(carat, price, data=diamonds, color=cut) + geom_smooth(method='lm')

> facets: The symbol to the left of the tilde indicates rows and the symbol to the right of the tilde indicates columns

    > qplot(carat, price, data=diamonds, color=cut, facets=.~cut) + geom_smooth(method='lm')

> cut, which allows you to divide your data into sets and label each entry as belonging to one of the sets

So you can create a factor out of numerical data

    > cutpoints <- quantile(diamonds$carat,seq(0,1,length=4),na.rm=TRUE)
    > cutpoints
       0% 33.33333% 66.66667%      100% 
     0.20      0.50      1.00      5.01

Create a new name for the data:

    > diamonds$car2 <- cut(diamonds$carat,cutpoints); stageVariable("diamonds$car2",diamonds$car2)

Because the dataset was changed we have to create the graphical object again:

    > g <- ggplot(diamonds, aes(depth, price))

    > g+geom_point(alpha=1/3) + facet_grid(cut ~ car2)

### Boxplot

    > ggplot(diamonds, aes(carat, price))+geom_boxplot()+facet_grid(. ~ cut)

## Hierarchical Clustering

A simple way of quickly examining and displaying multi-dimensional data. This technique is usually most useful in the early stages of analysis when you're trying to get an understanding of the data

> Clustering organizes data points that are close into groups. So obvious questions are "How do we define close?", "How do we group things?", and "How do we interpret the grouping?" Cluster analysis is a very important topic in data analysis.

Closeness: Distance or similarity are usually the metrics used

Measuring distance: Euclidean distance and correlation similarity are continuous measures, while Manhattan distance is a binary measure

> Euclidean distance is distance "as the crow flies". Many applications, however, can't realistically use crow-flying distance. Cars, for instance, have to follow roads.

> Manhattan distance is the sum of the absolute values of the distances between each coordinate

Computer euclidean distances between points:

    > dist(dataFrame)

You can create the dendogram with:

    > hc <- hclust(distxy)

You can plot the dendogram:

    > plot(hc)

Printing at the same level:

    > plot(as.dendrogram(hc))

Then you can cut a line at a certain distance to create clusters

Measuring distance between clusters:

* complete linkage - furtherest distance of elements in respective clusters
* average linkage - get the mean x and y coordinates

#### Heatmap

    > heatmap(dataMatrix, col=cm.colors(25))

## K Means Clustering

Another simple way of examining and organizing multi-dimensional data. Most useful in the early stages of analysis when you're trying to get an understanding of the data, e.g., finding some pattern or relationship between different factors or variables.

> R documentation tells us that the k-means method "aims to partition the points into k groups such that the sum of squares from points to the assigned cluster centres is minimized."

1. First guess how many clusters you have or want
2. Randomly create a "centroid" (a phantom point) for each cluster
3. Readjust the centroid's position by making it the average of the points assigned to it.

k-means clustering requires some distance metric (say Euclidean), a hypothesized fixed number of clusters, and an initial guess as to cluster centroids.

> k-means clustering returns a final position of each cluster's centroid as well as the assignment of each data point or observation to a cluster

Add centroids to chart:

    > points(cx, cy, col=c('red', 'orange', 'purple'), pch=3, cex=2, lwd=2)

Check distnace between centroid and points:

    > mdist(x,y,cx,cy)

You can find the minimum with:

    > apply(distTmp, 2, which.min)
    [1] 2 2 2 1 3 3 3 1 3 3 3 3

Can colour based on above output:

    > points(x,y,pch=19, cex=2, col=cols1[newClust])

Recaculate the centroids based on clusters:

    > tapply(x, newClust, mean)
       1        2        3 
    1.210767 1.010320 2.498011 

    > tapply(y, newClust, mean)
        1        2        3 
    1.730555 1.016513 1.354373 

Apply the points on plot:

    > points(newCx, newCy, col=cols1, pch=8, cex=2, lwd=2)

Some points will need to change. Recolour the points again:

    > points(x,y,pch=19, cex=2, col=cols1[newClust2])

Create a kmeans object:

    > kmeans(dataFrame, centers=3)

Check number of iterations:

    > kmObj$iter
    [1] 2

## Dimension Reduction

principal component analysis (PCA)
singular value decomposition (SVD)

> PCA and SVD are used in both the exploratory phase and the more formal modelling stage of analysis

> we'd like to find a smaller set of multivariate variables that are uncorrelated AND explain as much variance (or variability) of the data as possible.

    Orthagonal == Uncorrelated

### Singular Value Decomposition

    > svd(mat)
    $d
    [1] 9.5899624 0.1806108

    $u
            [,1]       [,2]
    [1,] -0.3897782 -0.9209087
    [2,] -0.9209087  0.3897782

    $v
            [,1]       [,2]
    [1,] -0.2327012 -0.7826345
    [2,] -0.5614308  0.5928424
    [3,] -0.7941320 -0.1897921

> Recall that in R matrix multiplication requires you to use the operator %*%

    > matu %*% diag %*% t(matv)
     [,1] [,2] [,3]
    [1,]    1    2    3
    [2,]    2    5    7

### Principal Component Analysis

a simple, non-parametric method for extracting relevant information from confusing data sets.

> PCA is a method to reduce a high-dimensional data set to its essential elements (not lose information) and explain the variability in the data

    > svd(scale(mat))
    $d
    [1] 1.732051 0.000000

    $u
            [,1]      [,2]
    [1,] -0.7071068 0.7071068
    [2,]  0.7071068 0.7071068

    $v
            [,1]       [,2]
    [1,] 0.5773503 -0.5773503
    [2,] 0.5773503  0.7886751
    [3,] 0.5773503 -0.2113249


    > prcomp(scale(mat))
    Standard deviations (1, .., p=2):
    [1] 1.732051 0.000000

    Rotation (n x k) = (3 x 2):
            PC1        PC2
    [1,] 0.5773503 -0.5773503
    [2,] 0.5773503  0.7886751
    [3,] 0.5773503 -0.2113249

SVD and PCA cannot deal with `MISSING` data

> Singular value decomposition is a good way to approximate data without having to store a lot.

Make sure data is on consistent units
Seperating out real patterns requires detective work

distance matrix as first 3 columns of `dist`

    > mdist <- dist(sub1[,1:3])

Create clusters

    > hclustering <- hclust(mdist)

## Case Study

You can use `read.table` to read in data. `R` is smart enough to unzip it.

    > dim(pm0)
    [1] 117421      5

The data set has `117421` lines and `5` columns

Reassign a variable by splitting with `|` character:

    > cnames <- strsplit(cnames, '|', fixed=TRUE)

Make syntactically valid names:

    > names(pm0) <- make.names(cnames[[1]][wcol])
    > names(pm1) <- make.names(cnames[[1]][wcol])

Create `x1` by assigning it to `Sample.Value`

    > x1 <- pm1$Sample.Value

The 1999 data:

    > summary(x0)
   Min. 1st Qu.  Median    Mean 3rd Qu.    Max.    NA's 
   0.00    7.20   11.50   13.74   17.90  157.10   13217 

The 2012 data:

    > summary(x1)
   Min. 1st Qu.  Median    Mean 3rd Qu.    Max.    NA's 
    -10.00    4.00    7.63    9.14   12.00  908.97   73133 

Indicates an improved situation. The maximum increases indicates possible malfunction with the capturing devices.

Boxplot the data:

    > boxplot(x0, x1)

> There are so many values outside the boxes and the range of x1 is so big that the boxes are flattened. It might be more informative to call boxplot on the logs (base 10) of x0 and x1. Do this now using log10(x0) and log10(x1) as the 2 arguments.

    > boxplot(log10(x0), log10(x1))

`R` will warn about values that can't be `log` ed

Get sum of all the negative values excluding `NA`:

    > negative <- x1<0
    > sum(negative, na.rm=TRUE)
    [1] 26474

    > mean(negative, na.rm=TRUE)
    [1] 0.0215034

> We see that just 2% of the x1 values are negative. Perhaps that's a small enough percentage that we can ignore them

Get array of dates:

    > str(dates)
    int [1:1304287] 20120101 20120104 20120107 20120110 20120113 20120116 20120119 20120122 20120125 20120128 ...

The dates are hard to read though, imporved with:

    > dates <- as.Date(as.character(dates), '%Y%m%d')

Show a histogram of the dates that are negative:

    > hist(dates[negative], "month")

> We see the bulk of the negative measurements were taken in the winter months, with a spike in May. Not many of these negative measurements occurred in summer months. We can take a guess that because particulate measures tend to be low in winter and high in summer, coupled with the fact that higher densities are easier to measure, that measurement errors occurred when the values were low. For now we'll attribute these negative measurements to errors. Also, since they account for only 2% of the 2012 data, we'll ignore them.

View data that intersects:

    > both <- intersect(site0, site1)

Subset the data for a certain county and site:

    > cnt0 <- subset(pm0, State.Code == 36 & county.site %in% both)

> Membership is denoted with `%in%`

Split data:

    > sapply(split(cnt1, cnt1$county.site), nrow)
   1.12     1.5   101.3   13.11    29.5    31.3    5.80 63.2008 67.1015   85.55 
     31      64      31      31      33      15      31      30      31      31

### Create the plot

    > par(mfrow=c(1,2), mar=c(4,4,2,1))
    > plot(dates0, x0sub, pch=20)

Add a line:

    > abline(h=median(x0sub, na.rm=TRUE), lwd=2)

Merge data:

    > mrg <- merge(d0, d1, by='state')





