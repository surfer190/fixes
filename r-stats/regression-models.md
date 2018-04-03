# R Regression Models

Regression towards the mean

> Sir Francis studied the relationship between heights of parents and their children. His work showed that parents who were taller than average had children who were also tall but closer to the average height. Similarly, parents who were shorter than average had children who were also shorter than average but less so than mom and dad. That is, they were closer to the average height. From one generation to the next the heights moved closer to the average or regressed toward the mean.

    > plot(child ~ parent, galton)

> by using R's function "jitter" on the children's heights, we can spread out the data to simulate the measurement errors and make high frequency heights more visible.

    > plot(jitter(child, 4) ~ parent, galton)

Generate and store the regression line:

    > regrline <- lm(child ~ parent, galton)

Add the regression line to the chart:

    > abline(regrline, lwd=3, col='red')

> The slope of the line is the estimate of the coefficient, or multiplier, of "parent", the independent variable of our data (in this case, the parents' heights).

> The slope of a line shows how much of a change in the vertical direction is produced by a change in the horizontal direction. So, parents "1 inch" above the mean in height tend to have children who are only .65 inches above the mean.

## Residuals

`residuals` are the distances between the actual plotted points and the estimates given by the regression line

> Since all lines are characterized by two parameters, a slope and an intercept, we'll use the least squares criteria to provide two equations in two unknowns so we can solve for these parameters, the slope and intercept.

> The first equation says that the "errors" in our estimates, the residuals, have mean zero. In other words, the residuals are "balanced" among the data points; they're just as likely to be positive as negative. The second equation says that our residuals must be uncorrelated with our predictors, the parents’ height. This makes sense - if the residuals and predictors were correlated then you could make a better prediction and reduce the distances (residuals) between the actual outcomes and the predictions.

See the correlation between the residuals and predictors:

    > cov(fit$residuals, galton$parent)

The residuals of a regression line are: `fit$residuals`

### Variance

Calculate variance

    > varChild <- var(galton$child)

### Calculate estimate of y-coordinate

    est(slope, intercept)

The variance of estimates:

    > varEst <- var(est(ols.slope, ols.ic))

> Since variances are sums of squares (and hence always positive), this equation which we've just demonstrated, var(data)=var(estimate)+var(residuals), shows that the variance of the estimate is ALWAYS less than the variance of the data.

## Multiple Predictors

When more than one variable predicts the outcome of an event.
Eg. Accelerations of earthquakes based on distance and magnitude.

Generating a regression line for the above:

    > efit <- lm(accel ~ mag+dist, attenu)

You can verify that residuals are not correlated with the predictors

    > cov(efit$residuals, attenu$mag)

# Least Squares Estimation

Galton data: The regression line summarizes the relationship between parents' heights (the **predictors**) and their children's (the **outcomes**).

> We learned in the last lesson that the regression line is the line through the data which has the minimum (least) squared "error", the vertical distance between the 928 actual children's heights and the heights predicted by the line. Squaring the distances ensures that data points above and below the line are treated the same. This method of choosing the 'best' regression line (or 'fitting' a line to the data) is known as ordinary least squares.

>  the slope of the regression line is the correlation between the two sets of heights multiplied by the ratio of the standard deviations (childrens' to parents' or outcomes to predictors)

> You normalize data by subtracting its mean and dividing by its standard deviation

Remember, 'lm' needs a formula of the form dependent ~ independent

The slope of the line represents the **correlation** of the 2 data sets

# Residual Variation

> Residuals are useful for indicating how well data points fit a statistical model. They "can be thought of as the outcome (Y) with the linear association of the predictor (X) removed

> One differentiates residual variation (variation after removing the predictor) from systematic variation (variation explained by the regression model).

> The maximum likelihood estimate of the variance of the random error is the average squared residual

    Total Variation = Residual Variation + Regression Variation

Total Variation of the data...Recall that centering data means subtracting the mean from each data point. Now calculate the sum of the squares of the centered children's heights and store the result in a variable called `sTot`

Residual Variation...is the deviance of the regression line

    sRes <- deviance(fit)

The regression variation: `1 - ResidualVariation/TotalVariation`

Which is equal to:

    > summary(fit)$r.squared
    > cor(galton$child, galton$parent)^2

`r^2` is the percentage of variation explained by the regression model.
As a percentage it is between 0 and 1.
It also equals the sample correlation squared

# Introduction to Multivariable Regression

Regression in many variables amounts to a series of regressions in one.

> When we perform a regression in one variable, such as lm(child ~ parent, galton), we get two coefficients, a slope and an intercept. The intercept is really the coefficient of a special regressor which has the same value, 1, at every sample. The function, lm, includes this regressor by default.

> The regression in one variable really involves two regressors, the variable, parent, and a regressor of all ones

> We also showed that if we subtract the mean from each variable, the regression line goes through the origin, x=0, y=0, hence its intercept is zero. Thus, by subtracting the means, we eliminate one of the two regressors, the constant, leaving just one, parent. The coefficient of the remaining regressor is the slope.

Gaussian Elimination - Subtracting the means to eliminate the intercept is a special case of a general technique

> The mean of a variable is the coefficient of its regression against the constant, 1. Thus, subtracting the mean is equivalent to replacing a variable by the residual of its regression against 1

`The mean of a variable is equal to its regression against the constant, 1.`

Eg. Predict the Volume of timber which a tree might produce from measurements of its Height and Girth

You can view the data nicely formatted with:

    > View(trees)

> The general technique is to pick one predictor and to replace all other variables by the residuals of their regressions against that one

Create the regression line for one or more variables:

    > fit <- lm(Volume ~ Girth + Height + Constant - 1, trees)

Reducing to a problem with `N -1` regressors: Pick any regressor and replace the outcome and all other regressors by their residuals against the chosen one.

# MultiVar Examples

Generate a linear model and put a single variable as dependent on others:

    > all <- lm(dataset$Var ~ ., dataset)

Checking `summary(all)`

    Coefficients:
                    Estimate Std. Error t value Pr(>|t|)    
    (Intercept)      66.91518   10.70604   6.250 1.91e-07 ***
    Agriculture      -0.17211    0.07030  -2.448  0.01873 *  
    Examination      -0.25801    0.25388  -1.016  0.31546    
    Education        -0.87094    0.18303  -4.758 2.43e-05 ***
    Catholic          0.10412    0.03526   2.953  0.00519 ** 
    Infant.Mortality  1.07705    0.38172   2.822  0.00734 ** 

> Estimates are the coefficients of the independent variables of the linear model they reflect an estimated change in the dependent variable

The `*` shows the variable is significant

Viewing just `Agriculture` on `Fertility`:

    > summary(lm(Fertility ~ Agriculture, swiss))

    Coefficients:
                Estimate Std. Error t value Pr(>|t|)    
    (Intercept) 60.30438    4.25126  14.185   <2e-16 ***
    Agriculture  0.19420    0.07671   2.532   0.0149 * 

The coefficient changes to positive with just 2 variables.

Clearly the presence of other factors is affecting it.

Check the correlation between variables:

    > cor(swiss$Examination, swiss$Education)
    [1] 0.6984153

Showing they are correlated

    > cor(swiss$Agriculture, swiss$Education)
    [1] -0.6395225

The negative correlation may be affecting the influence on Fertility

Sometimes you have completely unrelated figures (like 2 fields added together as a field)
Adding it doesn't change the model

    Intercept + estimate of coefficients = mean

The least significant result (ie. which has the highest probability) 
when a spray is refernced from 0:

    > nfit <- lm(count ~ spray - 1, InsectSprays)
    > summary(nfit)$coef
        Estimate Std. Error   t value     Pr(>|t|)
        sprayA 14.500000   1.132156 12.807428 1.470512e-19
        sprayB 15.333333   1.132156 13.543487 1.001994e-20
        sprayC  2.083333   1.132156  1.840148 7.024334e-02
        sprayD  4.916667   1.132156  4.342749 4.953047e-05
        sprayE  3.500000   1.132156  3.091448 2.916794e-03
        sprayF 16.666667   1.132156 14.721181 1.573471e-22

Create linear model from a different factor reference:

    > spray2 <- relevel(InsectSprays$spray, 'C')
    > fit2 <- lm(count ~ spray2, InsectSprays)

**A negative coefficient based on time, shows that as time goes on the value decreases**

Create a linear model of a split dataset:

    > lmF <- lm(hunger$Numeric[hunger$Sex=="Female"] ~ hunger$Year[hunger$Sex=="Female"])

Creating the linear model with 2 or more variables:

    > lmBoth <- lm(Numeric ~ Year + Sex, hunger)

> Suppose we have two interacting predictors and one of them is held constant. The expected change in the outcome for a unit change in the other predictor is the coefficient of that changing predictor + the coefficient of the interaction * the value of the predictor held constant.

# Residuals Diagnostics and Variation

When an outlier does not affect the fitm, it is said to `lack influence`.
Otherwise it is `influential`

> The change which inclusion or exclusion of a sample induces in coefficents is a simple measure of its influence

You can measure the influence of a point with:

    > View(dfbeta(fit))

It is sometimes called `influence`, sometimes `leverage`, and sometimes `hat value`

You can use `hatvalues`:

    > View(hatvalues(fit))

The close to 1, the more influential

Standardized and Studentized residuals attempt to compensate for outliers

Standardized residuals:

    rstandard: The function, rstandard, computes the standardized residual

> Studentized residuals, (sometimes called externally Studentized residuals,) estimate the standard deviations of individual residuals using, in addition to individual hat values, the deviance of a model which leaves the associated sample out.

Studentized residuals:

    rstudent: The function, rstudent, calculates Studentized residuals for each sample

    > View(rstudent(fit))

cooks.distance: The function, cooks.distance, will calculate Cook's distance for each sample

# Variance Inflation Factors




