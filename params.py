from math import sqrt

eta = 2
tau = 39
sigmasq = ((2 * eta) ** 2 - 1) / 12 * tau

sigma2 = 2 * sqrt(sigmasq)

beta = tau * eta

# zij <= sigma2 with high probability
# csij <= beta, so zij <= beta for zero y
# discard zij > beta

error_bound = beta + sigma2

# 91.96424004376894
print(error_bound)