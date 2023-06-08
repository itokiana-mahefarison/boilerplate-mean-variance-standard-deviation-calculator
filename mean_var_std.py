import numpy as np

def calculate(list):
    calculations = {}
    np_list = np.array(list)

    if(np_list.size < 9):
      raise ValueError("List must contain nine numbers.")
    list_reshape = np.reshape(np_list, (3, 3))

    calculations["sum"] = [np.sum(list_reshape, axis = 0), np.sum(list_reshape, axis=1), np.sum(list_reshape)]
  
    calculations["min"] = [np.min(list_reshape, axis = 0), np.min(list_reshape, axis=1), np.min(list_reshape)]

    calculations["max"] = [np.max(list_reshape, axis = 0), np.max(list_reshape, axis=1), np.max(list_reshape)]

    calculations["mean"] = [np.mean(list_reshape, axis = 0), np.mean(list_reshape, axis=1), np.mean(list_reshape)]

    calculations["variance"] = [np.var(list_reshape, axis = 0), np.var(list_reshape, axis=1), np.var(list_reshape)]

    calculations["standard deviation"] = [np.std(list_reshape, axis = 0), np.std(list_reshape, axis=1), np.std(list_reshape)]



    return calculations