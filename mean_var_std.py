import numpy as np

def calculate(list):
  if len(list) == 9:
    matrix = np.array(list).reshape(3,3)

    mean = []
    mean.append(matrix.mean(axis=0).tolist())
    mean.append(matrix.mean(axis=1).tolist())
    mean.append(matrix.mean())

    var = []
    var.append(matrix.var(axis=0).tolist())
    var.append(matrix.var(axis=1).tolist())
    var.append(matrix.var())

    std = []
    std.append(matrix.std(axis=0).tolist())
    std.append(matrix.std(axis=1).tolist())
    std.append(matrix.std())
    
    max = []
    max.append(matrix.max(axis=0).tolist())
    max.append(matrix.max(axis=1).tolist())
    max.append(matrix.max())
    
    min = []
    min.append(matrix.min(axis=0).tolist())
    min.append(matrix.min(axis=1).tolist())
    min.append(matrix.min())

    sum = []
    sum.append(matrix.sum(axis=0).tolist())
    sum.append(matrix.sum(axis=1).tolist())
    sum.append(matrix.sum())

    calculations = {
      'mean': mean,
      'variance': var,
      'standard deviation': std,
      'max': max,
      'min': min,
      'sum': sum
    }

    return calculations
  else:
    raise ValueError("List must contain nine numbers.")
