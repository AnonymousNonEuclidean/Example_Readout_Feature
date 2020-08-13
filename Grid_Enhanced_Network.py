# We base our hyper-parameter grids on the ones from this paper https://arxiv.org/pdf/2006.14378.pdf#page=13
# Since we have the same test/train sets already available to us.  


# Training Parameters
#----------------------#
# Number of Jobs (Cores to use)
n_jobs = 4
# Number of Random CV Draws
n_iter = 5
# Number of CV Folds
CV_folds = 2#

#----------------------#
########################
# Hyperparameter Grids #
########################
#----------------------#

# Hyperparameter Grid
#---------------------#

param_grid_Nice_Nets = {'batch_size': [32],
                    'epochs': [1200],
                      'learning_rate': [0.0001],
                      'height': [200],
                        'Depth_Feature_Map': [4],
                        'Depth_Readout_Map': [4],
                      'input_dim':[10],
                       'output_dim':[1]}

