import numpy as np
import array as arr
from scipy import stats

pp_scores = [52.72, 66.04, 65.45, 144.35, 144.21, 28.46, 4.69, 19.56, 4.89]

def show_stats(population):
    sample_data = arr.array('f', population)
    print(f"Mean: {np.mean(population)}")
    print(f"Median: {np.median(population)}")
    print(f"Mode: {stats.mode(population)}")
    print(f"Range: {np.ptp(population)}")
    print(f"Variance: {round(np.var(population), 2)}")
    print(f"Standard Deviation: {round(np.std(population), 2)}")
    print(f"Sample variance: {round(np.var(sample_data[0:5].tolist(), ddof=1), 2)}")
    print(f"Sample standard Deviation: {round(np.std(sample_data[0:5].tolist(), ddof=1), 2)}")

show_stats(pp_scores)
#show_stats([5,4,3,5,8,2,5,2,5,8,10,8,7,9,10,5,7,5,7,5,4,3,5,8,4])
show_stats([1,4,4,1,5,8,2,1,1])
