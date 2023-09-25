# Q6. Explain the concept of multicollinearity in multiple linear regression. How can you detect and
# address this issue?

# Aanswer -- Multicollinearity is a phenomenon that occurs in multiple linear regression when two or more independent 
# variables in a model are highly correlated with each other. In other words, it indicates a linear relationship between predictor variables.

# Detecting Multicollinearity:

# There are several methods to detect multicollinearity:

# Correlation Matrix: Calculate the correlation coefficients between pairs of predictor variables. High absolute correlation values (close to 1 or -1) indicate potential multicollinearity.

# Variance Inflation Factor (VIF): Calculate the VIF for each predictor variable. VIF quantifies how much the variance of an estimated regression coefficient increases due to multicollinearity. A high VIF (typically above 5 or 10) suggests multicollinearity.

# Eigenvalues and Condition Indices: Use eigenvalues and condition indices of the correlation matrix to detect multicollinearity. Large condition indices indicate multicollinearity.

# Addressing Multicollinearity:
# Remove One of the Correlated Variables
# Feature Selection
# Ridge Regression or Lasso Regression