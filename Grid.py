#!/usr/bin/env python
# coding: utf-8

# In[1]:


# grid of parameters for training
import os


# In[2]:


def get_param_grid(is_test, input_dim, type):
    if is_test:
        partition_epochs = [10]
        normal_epochs = [20]
        param_grid = {
            "model__learning_rate": [0.14051589252206744],
            "model__height": [50,100,200,400],
            "model__input_dim": [input_dim],
            "model__batch_size": [16,32,64],
            "model__dp": [0],
            "model__depth": [1,5,20],
            "model__transitive_depth": [0,10,50],
            "model__istype": [1],
            "model__ismodulated": [0,1],
        }
    else:
        partition_epochs = [50, 100, 150, 200, 250, 300, 350, 400]
        normal_epochs = [200, 400, 750, 1000, 1200, 1500, 2000, 2500]
        param_grid = {
            "model__learning_rate": [
				0.0005,
                0.001,
                0.005,
                0.01,
                0.05,
                0.1,
            ],
            "model__height": [
                15,
                25,
                75,
                100,
                150,
                200,
                450,
                500,
                600,
                700,
                900,
                1000,
            ],
            "model__input_dim": [input_dim],
            "model__batch_size": [16,32,64,128],
            "model__dp": [0],
            "model__depth": [1,5,20,50],
            "model__transitive_depth": [0,10,50,100],
            "model__istype": [1],
            "model__ismodulated": [0,1],
        }

    if type == "partition":
        param_grid["model__epochs"] = partition_epochs
    elif type == "normal":
        param_grid["model__epochs"] = normal_epochs

    return param_grid


def ret_files(path):
    # k is the number of folde for k-fold cross validation
    # grid speciffies the parameter Grid in which we look for the optimal hyper parameters
    files = {
        "TCP": {"file": "housing_complete.csv", "k": 4, "grid": "normal"},
    }
    for key in files.keys():
        files[key]["file"] = os.path.join(path, files[key]["file"])
    return files

