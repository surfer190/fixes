---
author: ''
category: R-Stats
date: '2018-05-23'
summary: ''
title: Regression Models
---
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

> In modeling, our interest lies in parsimonious, interpretable representations of the data that enhance our understanding of the phenomena under study. Omitting variables results in bias in the coefficients of interest - unless their regressors are uncorrelated with the omitted ones.

> On the other hand, including any new variables increases (actual, not estimated) standard errors of other regressors.S o we don't want to idly throw variables into the model causing **variance inflation**


            x1      x1      x1 
        0.00110 0.00240 0.00981 

variance inflation due to correlated regressors is clear

Theoretical estimates contain an unknown constant of proportionality - we therefore depend on ratios of theoretical estimates called Variance Inflation Factors (VIF)

A variance inflation factor (VIF) is a ratio of estimated variances

Create a linear regression model for Fertility, dataset is swiss

    > mdl <- lm(swiss$Fertility ~ ., swiss)

You can calculate the VIF's for each regressor:

    > vif(mdl)
     Agriculture      Examination        Education         Catholic Infant.Mortality 
        2.284129         3.675420         2.774943         1.937160         1.107542 

> These VIF's show, for each regression coefficient, the variance inflation due to including all the others.

The variance in the estimated coefficient of Education is 2.774943 times what it might have been if Education were not correlated with the other regressors

Exclude examination regressor:

    > mdl2 <- lm(swiss$Fertility ~ . -Examination, swiss)

with variable inflation factors:

    > vif(mdl2)
        Agriculture        Education         Catholic Infant.Mortality 
            2.147153         1.816361         1.299916         1.107528

It has decreased the VIF for education, omitting examination has almost no effect on Infant mortality.
Chances are they are not correlated.

Variance is the square of standard deviation, and standard error is the standard deviation of an estimated coefficient.

**VIF is the square of standard error inflation.**

If a regressor is strongly correlated with others, hence will increase their VIF's, why shouldn't we just exclude it?

Excluding it might bias coefficient estimates of regressors with which it is correlated.

> The problems of variance inflation and bias due to excluded regressors both involve correlated regressors. However there are methods, such as factor analysis or principal componenent analysis, which can convert regressors to an equivalent uncorrelated set.

Converting regressors to uncorrelated makes interpretation difficult.

## Overfitting and Underfitting

To demonstrate the effect of omitted variables and discuss the use of ANOVA to construct parsimonious, interpretable representations of the data.

Analysis of variance (ANOVA) is a useful way to quantify the significance of additional regressors

The null hypothesis is that the added regressors are not significant

    > fit1 <- lm(swiss$Fertility ~ swiss$Agriculture, swiss)
    > fit3 <- lm(swiss$Fertility ~ swiss$Agriculture + swiss$Examination + swiss$Education, swiss)
    > anova(fit1, fit3)

    Analysis of Variance Table

    Model 1: swiss$Fertility ~ swiss$Agriculture
    Model 2: swiss$Fertility ~ swiss$Agriculture + swiss$Examination + swiss$Education
    Res.Df    RSS Df Sum of Sq      F    Pr(>F)    
    1     45 6283.1                                  
    2     43 3180.9  2    3102.2 20.968 4.407e-07 ***
    ---
    Signif. codes:  0 ‘***’ 0.001 ‘**’ 0.01 ‘*’ 0.05 ‘.’ 0.1 ‘ ’ 1

The three asterisks, ***, at the lower right of the printed table indicate that the null hypothesis is rejected at the 0.001 level

An F statistic is a ratio of two sums of squares divided by their respective degrees of freedom.

R's function, deviance(model), calculates the residual sum of squares, also known as the deviance, of the linear model given as its argument. 

    > deviance(fit3)
    [1] 3180.925

> Based on the calculated p-value, a false rejection of the null hypothesis is extremely unlikely. We are confident that fit3 is significantly better than fit1, with one caveat: analysis of variance is sensitive to its assumption that model residuals are approximately normal. If they are not, we could get a small p-value for that reason. It is thus worth testing residuals for normality. The Shapiro-Wilk test is quick and easy in R. Normality is its null hypothesis.

    > shapiro.test(fit3$residuals)

        Shapiro-Wilk normality test

    data:  fit3$residuals
    W = 0.97276, p-value = 0.336

The Shapiro-Wilk p-value of 0.336 fails to reject normality, supporting confidence in our analysis of variance.

Omitting a regressor can bias estimation of the coefficient of certain other correlated regressors

Including more regressors will reduce a model's residual sum of squares, even if the new regressors are irrelevant.

When adding regressors, the reduction in residual sums of squares should be tested for significance above and beyond that of reducing residual degrees of freedom. R's anova() function uses an F-test for this purpose.

To ensure anova applies ensure Model residuals are normal

## Binary Outcomes

Frequently we care about outcomes that have two values such as alive or dead, win or lose, success or failure. Such outcomes are called binary, Bernoulli, or 0/1.

A collection of exchangeable binary outcomes for the same covariate data are called binomial outcomes

For break even odds:

If p is the probability of an event, the associated odds are `p/(1-p)`

Now suppose we want to see how the Ravens' odds depends on their offense. In other words, we want to model how p, or some function of it, depends on how many points the Ravens are able to score. Of course, we can't observe p, we can only observe wins, losses, and the associated scores. Here is a Box plot of one season's worth of such observations.

> A generalized linear model which has these properties supposes that the log odds of a win depend linearly on the score. That is, log(p/(1-p)) = b0 + b1*score. The link function, log(p/(1-p)), is called the logit, and the process of finding the best b0 and b1, is called logistic regression.

Get the maximum likelihood estimates:

    > mdl <- glm(ravenWinNum ~ ravenScore, binomial, ravenData)

The model is less credible at scores lower than 9. Of course, there is no data in that region.

We can use R's predict() function to see the model's estimates for lower scores

The function will take mdl and a data frame of scores as arguments and will return log odds for the give scores

    > lodds <- predict(mdl, data.frame(ravenScore=c(0, 3, 6)))

Since predict() gives us log odds, we will have to convert to probabilities.

    > exp(lodds)/(1+exp(lodds))
            1         2         3 
    0.1570943 0.2041977 0.2610505 

As it turns out, though, the model is not that sure of itself. Typing summary(mdl) you can see the estimated coefficients are both within 2 standard errors of zero. Check out the summary now.

    > summary(mdl)

    Call:
    glm(formula = ravenWinNum ~ ravenScore, family = binomial, data = ravenData)

    Deviance Residuals: 
        Min       1Q   Median       3Q      Max  
    -1.7575  -1.0999   0.5305   0.8060   1.4947  

    Coefficients:
                Estimate Std. Error z value Pr(>|z|)
    (Intercept) -1.68001    1.55412  -1.081     0.28
    ravenScore   0.10658    0.06674   1.597     0.11

    (Dispersion parameter for binomial family taken to be 1)

        Null deviance: 24.435  on 19  degrees of freedom
    Residual deviance: 20.895  on 18  degrees of freedom
    AIC: 24.895

    Number of Fisher Scoring iterations: 5

The coefficients have relatively large standard errors. A 95% confidence interval is roughly 2 standard errors either side of a coefficient

    > exp(confint(mdl))
    Waiting for profiling to be done...
                    2.5 %   97.5 %
    (Intercept) 0.005674966 3.106384
    ravenScore  0.996229662 1.303304

The lower confidence bound on the odds of winning with a score of 0 is near zero, which seems much more realistic than the 16/84 figure of the maximum likelihood model

The lower confidence bound on exp(b1) suggests that the odds of winning would decrease slightly with every additional point scored. This is obviously unrealistic.Of course, confidence intervals are based on large sample assumptions and our sample consists of only 20 games

> Linear regression minimizes the squared difference between predicted and actual observations

    > anova(mdl)
    Analysis of Deviance Table

    Model: binomial, link: logit

    Response: ravenWinNum

    Terms added sequentially (first to last)


            Df Deviance Resid. Df Resid. Dev
    NULL                          19     24.435
    ravenScore  1   3.5398        18     20.895

The value, 3.5398, labeled as the deviance of ravenScore, is actually the difference between the deviance of our model, which includes a slope, and that of a model which includes only an intercept, b0. This value is centrally chi-square distributed (for large samples) with 1 degree of freedom (2 parameters minus 1 parameter, or equivalently 19-18.) The null hypothesis is that the coefficient of ravenScore is zero. To confidently reject this hypothesis, we would want 3.5398 to be larger than the 95th percentile of chi-square distribution with one degree of freedom. Use qchisq(0.95, 1) to compute the threshold of this percentile.

## Count Outcomes

Many data take the form of counts. These might be calls to a call center, number of flu cases in an area, or number of cars that cross a bridge. Data may also be in the form of rates, e.g., percent of children passing a test. In this lesson we will use Poisson regression to analyze daily visits to a web site as the web site's popularity grows, and to analyze the percent of visits which are due to references from a different site.

A Poisson process is characterized by a single parameter, the expected rate of occurrence, which is usually called lambda.

Somwhat remarkably, the variance of a Poisson process has the same value as its mean, lambda. You can quickly illustrate this by generating, say, n=1000 samples from a Poisson process using R's rpois(n, lambda) and calculating the sample variance. For example, type var(rpois(1000, 50)). The sample variance won't be exactly equal to the theoretical value, of course, but it will be fairly close.

    > var(rpois(1000, 50))
    [1] 51.05576

A famous theorem implies that properly normalized sums of independent, identically distributed random variables will tend to become normally distributed as the number of samples grows large.

    The Central Limit Theorem

In a Poisson regression, the log of lambda is assumed to be a linear function of the predictors. 

    > class(hits[,'date'])
    [1] "Date"

R's Date class represents dates as days since or prior to January 1, 1970

You can view a date as an integer

    > as.integer(head(hits[,'date']))
    [1] 14975 14976 14977 14978 14979 14980

The arithmetic properties of Dates allow us to use them as predictors.

Since our outcomes (visits) are counts, our family will be 'poisson', and our third argument will be the data, hits

    > mdl <- glm(visits ~ date, poisson, hits)

    > summary(mdl)

    Call:
    glm(formula = visits ~ date, family = poisson, data = hits)

    Deviance Residuals: 
        Min       1Q   Median       3Q      Max  
    -5.0466  -1.5908  -0.3198   0.9128  10.6545  

    Coefficients:
                Estimate Std. Error z value Pr(>|z|)    
    (Intercept) -3.275e+01  8.130e-01  -40.28   <2e-16 ***
    date         2.293e-03  5.266e-05   43.55   <2e-16 ***
    ---
    Signif. codes:  0 ‘***’ 0.001 ‘**’ 0.01 ‘*’ 0.05 ‘.’ 0.1 ‘ ’ 1

    (Dispersion parameter for poisson family taken to be 1)

        Null deviance: 5150.0  on 730  degrees of freedom
    Residual deviance: 3121.6  on 729  degrees of freedom
    AIC: 6069.6

    Number of Fisher Scoring iterations: 5

Both coefficients are significant, being far more than two standard errors from zero.
The Residual deviance is also very significantly less than the Null, indicating a
strong effect.

Get the 95% confidence interval for exp(b1) by exponentiating confint(mdl, 'date')

    > exp(confint(mdl, 'date'))
    Waiting for profiling to be done...
    2.5 %   97.5 % 
    1.002192 1.002399 

ie. Visits are estimated to increase by a factor of between 1.002192 and 1.002399 per day

Representing more than doubling each year

Our model looks like a pretty good description of the data, but no model is perfect and we can often learn about a data generation process by looking for a model's shortcomings. As shown in the figure, one thing about our model is 'zero inflation' in the first two weeks of January 2011, before the site had any visits. The model systematically overestimates the number of visits during this time. A less obvious thing is that the standard deviation of the data may be increasing with lambda faster than a Poisson model allows. This possibility can be seen in the rightmost plot by visually comparing the spread of green dots with the standard deviation predicted by the model (black dashes.) Also, there are four or five bursts of popularity during which the number of visits far exceeds two standard deviations over average. Perhaps these are due to mentions on another site.

Find the date of the maximum visits:

    > which.max(hits[,'visits'])
    [1] 704 

Giving row 704

    > hits[704,]
          date visits simplystats
          704 2012-12-04     94          64

We might consider the 64 visits to be a special event, over and above normal. Can the difference, 94-64=30 visits, be attributed to normal traffic as estimated by our model? To check, we will need the value of lambda on December 4, 2012. This will be entry 704 of the fitted.values element of our model. Extract mdl$fitted.values[704] and store it in a variable named lambda

    > lambda <- mdl$fitted.values[704]
    > qpois(.95, lambda)
    [1] 33

95% of the time we would see 33 or fewer visits, hence 30 visits would not be rare according to our model.

To gauge the importance of references from Simply Statistics we may wish to model the proportion of traffic such references represent. Doing so will also illustrate the use of glm's parameter, offset, to model frequencies and proportions.

A Poisson process generates counts, and counts are whole numbers, 0, 1, 2, 3, etc. A proportion is a fraction.

We would like to model the fraction simplystats/visits, but to avoid division by zero we'll actually use simplystats/(visits+1)

glm's parameter, offset, has precisely this effect. It fixes the coefficient of the offset to 1

    > mdl2 <- glm(simplystats ~ date, poisson, hits, offset= log(visits + 1))

Although summary(mdl2) will show that the estimated coefficients are significantly different than zero, the model is actually not impressive. We can illustrate why by looking at December 4, 2012, once again. On that day there were 64 actual visits from Simply Statistics. However, according to mdl2, 64 visits would be extremely unlikely. You can verify this weakness in the model by finding mdl2's 95th percentile for that day. Recalling that December 4, 2012 was sample 704, find qpois(.95, mdl2$fitted.values[704]).

    > qpois(.95, mdl2$fitted.values[704])
    [1] 47

A Poisson distribution with lambda=1000 will be well approximated by a normal distribution. The variance is lambda.

Count outcomes and their means are never negative, but linear combinations of predictors may be.

When modeling count outcomes as a Poisson process, The log of the mean is modeled as a linear combination of the predictors

