import pandas as pd

# Load the dataset using pandas
df = pd.read_csv('C:\\Users\\This PC\\Desktop\\training\\Mall_Customers.csv')

# Function to cal the mode
def cal_mode(data):
    freq_dict = {}
    max_count = 0
    mode_values = []

    for value in data:
        if value in freq_dict:
            freq_dict[value] += 1
        else:
            freq_dict[value] = 1

        if freq_dict[value] > max_count:
            max_count = freq_dict[value]
            mode_values = [value]
        elif freq_dict[value] == max_count:
            mode_values.append(value)

    return mode_values

# Function to cal the median
def cal_median(data):
    n = len(data)
    data=sorted(data)
    if n % 2 == 1:
        median = data[n // 2]
    else:
        mid1 = data[(n - 1) // 2]
        mid2 = data[n // 2]
        median = (mid1 + mid2) / 2
    return median

# Function to cal the mean
def cal_mean(data):
    total = sum(data)
    mean = total / len(data)
    return mean

# cal the mean, median, and mode for 'Age'
age = df['Age']
mean_age = cal_mean(age)
median_age = cal_median(age)
mode_age = cal_mode(age)

# cal the mean, median, and mode for 'Annual Income (k$)'
annual_income = df['Annual Income (k$)']
mean_income = cal_mean(annual_income)
median_income = cal_median(annual_income)
mode_income = cal_mode(annual_income)

# cal the mean, median, and mode for 'Spending Score (1-100)'
spending_score = df['Spending Score (1-100)']
mean_spending = cal_mean(spending_score)
median_spending = cal_median(spending_score)
mode_spending = cal_mode(spending_score)

# Print the results
print("Mean of Age:", mean_age)
print("Median of Age:", median_age)
print("Mode of Age:", mode_age)

print("Mean of Annual Income:", mean_income)
print("Median of Annual Income:", median_income)
print("Mode of Annual Income:", mode_income)

print("Mean of Spending Score:", mean_spending)
print("Median of Spending Score:", median_spending)
print("Mode of Spending Score:", mode_spending)