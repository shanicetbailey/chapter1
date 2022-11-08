# Universal box budget function for SODA's data
# Given upper right / lower left cell coordinates, construct the tx_trans and ty_trans sections that bound it

def box_budget(da_i, da_j, left_i, right_i, lower_j, upper_j,):
    
    """Function to compute box budget given any set of boundaries"""

    upper = da_j.isel(xt_ocean=slice(left_i, right_i+1), yu_ocean=upper_j)
    lower = da_j.isel(xt_ocean=slice(left_i, right_i+1), yu_ocean=lower_j-1)
    right = da_i.isel(xu_ocean=right_i, yt_ocean=slice(lower_j, upper_j+1))
    left = da_i.isel(xu_ocean=left_i-1, yt_ocean=slice(lower_j, upper_j+1))
    
    return -upper.sum().load() + lower.sum().load() - right.sum().load() + left.sum().load()