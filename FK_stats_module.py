def mean_equation(numbers):
    return sum(numbers) / len(numbers)

def variance_equation(numbers):
    mean = calculate_mean(numbers)
    variance = sum((x - mean) ** 2 for x in numbers) / len(numbers)
    return variance

def std_deviation_equation(numbers):
    variance = calculate_variance(numbers)
    return variance ** 0.5

def standard_error_equation(numbers):
    standard_deviation = calculate_standard_deviation(numbers)
    return standard_deviation / len(numbers) ** 0.5

def z_score_equation(observation, numbers):
    mean = calculate_mean(numbers)
    standard_deviation = calculate_standard_deviation(numbers)
    z_score = (observation - mean) / standard_deviation
    return z_score
