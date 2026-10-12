## ----setup, include=FALSE----------------------------------------------------------------------------------------------------------------------------
knitr::opts_chunk$set(echo = TRUE)


## ----------------------------------------------------------------------------------------------------------------------------------------------------
library(forecast)
library(tseries)
library(astsa)  
library(ggplot2)


## ----------------------------------------------------------------------------------------------------------------------------------------------------
df <- read.csv("retail_canada_1992_2019.csv")
ts_retail <- ts(df$sales, start = c(1992, 1), frequency = 12)


## ----------------------------------------------------------------------------------------------------------------------------------------------------
autoplot(ts_retail) +
  labs(title = "Canadian Retail Trade Sales Unadjusted (1992–2019)",
       y = "Sales (millions CAD)",
       x = "Year",
       caption = "Source: Statistics Canada") +
  theme_minimal()


## ----------------------------------------------------------------------------------------------------------------------------------------------------
decomp <- stl(ts_retail, s.window = "periodic", robust = TRUE)
autoplot(decomp) +
  labs(title = "STL Decomposition Canadian Retail Sales") +
  theme_minimal()


## ----------------------------------------------------------------------------------------------------------------------------------------------------
Acf(ts_retail,  lag.max = 60, main = "ACF Raw Series")


## ----------------------------------------------------------------------------------------------------------------------------------------------------
Pacf(ts_retail, lag.max = 60, main = "PACF Raw Series")


## ----------------------------------------------------------------------------------------------------------------------------------------------------
library(urca)

test <- ur.df(ts_retail, type = "drift")
summary(test)   


## ----------------------------------------------------------------------------------------------------------------------------------------------------
seas_diff <- diff(ts_retail, lag = 12, differences = 1)
Acf(seas_diff,  lag.max = 60, main = "ACF Seasonal Diff (D=1)")


## ----------------------------------------------------------------------------------------------------------------------------------------------------
Pacf(seas_diff, lag.max = 60, main = "PACF Seasonal Diff (D=1)")


## ----------------------------------------------------------------------------------------------------------------------------------------------------
# Decomposition
decomp_1 <- stl(seas_diff, s.window = "periodic", robust = TRUE)
autoplot(decomp_1) +
  labs(title = "STL Decomposition — Canadian Retail Sales") +
  theme_minimal()


## ----------------------------------------------------------------------------------------------------------------------------------------------------
# Regular difference d=1
diff1_seas <- diff(seas_diff, differences = 1)
test_seas <- ur.df(diff1_seas, type = "drift", lags = 6)
summary(test_seas)


## ----------------------------------------------------------------------------------------------------------------------------------------------------
Acf(diff1_seas,  lag.max = 36, main = "ACF (Stationary)")

## ----------------------------------------------------------------------------------------------------------------------------------------------------
Pacf(diff1_seas, lag.max = 36, main = "PACF (Stationary)")


## ----------------------------------------------------------------------------------------------------------------------------------------------------
# Iteration 1 : simple baseline
# Start minimal just d=1, D=1, no AR/MA terms
fit1 <- sarima(ts_retail, p=0, d=1, q=0, P=0, D=1, Q=0, S=12)

# Iteration 2 : adding seasonal MA 
fit2 <- sarima(ts_retail, p=0, d=1, q=0, P=0, D=1, Q=1, S=12)

# Iteration 3 : adding non-seasonal MA
fit3 <- sarima(ts_retail, p=0, d=1, q=1, P=0, D=1, Q=1, S=12)

# Iteration 4 : candidate models
fit4 <- sarima(ts_retail, p=1, d=1, q=1, P=1, D=1, Q=1, S=12)
fit5 <- sarima(ts_retail, p=1, d=1, q=0, P=0, D=1, Q=1, S=12)


## ----------------------------------------------------------------------------------------------------------------------------------------------------
# Split-sample : train 1992–2015 | test 2016–2019
ts_train <- window(ts_retail, end   = c(2015, 12))
ts_test  <- window(ts_retail, start = c(2016,  1))
h_test   <- length(ts_test)  # 48 months

# Fit best model on train
fit_train <- sarima(ts_train, p=0, d=1, q=1, P=0, D=1, Q=1, S=12) # fit3 is found to be the best model

# Forecast on test period
fc_train <- sarima.for(ts_train, n.ahead = h_test, p=0, d=1, q=1, P=0, D=1, Q=1, S=12)

## ----------------------------------------------------------------------------------------------------------------------------------------------------
# Metrics
actuals   <- as.numeric(ts_test)
predicted <- as.numeric(fc_train$pred)

mse_split  <- mean((actuals - predicted)^2)
mae_split  <- mean(abs(actuals - predicted))
mape_split <- mean(abs((actuals - predicted) / actuals)) * 100


## ----------------------------------------------------------------------------------------------------------------------------------------------------
# Metrics

data.frame(
  Model = "SARIMA",
  MSE   = round(mse_split, 2),
  MAE   = round(mae_split, 2),
  MAPE  = paste0(round(mape_split, 2), "%")
)


## ----------------------------------------------------------------------------------------------------------------------------------------------------
# final 2 years forcast
fc_final <- sarima.for(ts_retail,
                       n.ahead = 24,
                       p=0, d=1, q=1,
                       P=0, D=1, Q=1, S=12)

