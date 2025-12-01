import numpy as np

def mask_and_classify_scores(arr):
    if type(arr) != np.ndarray:
        return None
    if arr.shape[0] != arr.shape[1]:
        return None
    if arr.shape[0] < 4:
        return None
    
    cleaned = np.copy(arr)
    cleaned[cleaned < 0] = 0
    cleaned[cleaned > 100] = 100

    levels = np.copy(cleaned)
    levels[levels < 40] = 0
    levels[(levels >= 40) & (levels < 70)] = 1
    levels[levels >= 70] = 2

    n = cleaned.shape[0]
    row_pass_counts = np.zeros(n, dtype=int)
    for i in range(n):
        row_pass_counts[i] = 0
        for score in cleaned[i]:
            if score >= 50:
                row_pass_counts[i] += 1
    
    return (cleaned, levels, row_pass_counts)