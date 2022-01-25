import numpy as np

print("P(A|B) = P(A will occur given that B has occured)")

print("P(A|B) = P(knows the material | answers correctly)")

print("P(A) = P(knows the material)")
print("P(B) = P(answers correctly)\n")

print("P(knows the materiial) = {}".format(0.6))
print("P(answers correctly) = {}\n".format(0.59))


print("P(B|A) = P(answers correctly | knows material)")
print("P(answers correctly | knows material) = {}\n".format(1-0.15))

print("P(answering correctly) = P(answers correctly | knows material) * P(knowms material) + P(answers correctly | does not know material) * P(does not know material)\n")

print("P(answers correctly) = {}\n".format((0.85 * 0.6) + (0.20 * 0.40)))

# Bayes' Theorem
print("P(A|B) = P(B|A) * P(A) / P(B)\n")

print("P(knows material | answers correctly) = P(answers correctly | knows material) * P(knows material) / P(answers correctly)\n")

print("P(knows material | answers correctly) = {}".format(0.85 * 0.6 / 0.59))