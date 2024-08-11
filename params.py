from math import sqrt

eta = 2
tau = 39

sigma_squared = ((2 * eta) ** 2 - 1) / 12 * tau
sigma_doubled = 2 * sqrt(sigma_squared)

beta = tau * eta

# zij <= sigma2 with high probability
# csij <= beta, so zij <= beta for zero y
# discard zij > beta

# 91.96424004376894
error_bound = beta + sigma_doubled
error_int = int(error_bound)