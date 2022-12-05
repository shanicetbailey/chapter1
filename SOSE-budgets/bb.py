# Universal box budget function for SOSE's data
# Given upper right / lower left cell coordinates, construct the tx_trans and ty_trans sections that bound it

def box_budget(da_i, da_j, left_i, right_i, lower_j, upper_j, bs=None):
    
    """Function to compute box budget given any set of boundaries.
        da_i and da_j are the zonal and meridional dataarrays, respectively.
        bs is the boundary side argument specification."""

    upper = da_j.isel(XC=slice(left_i, right_i), YG=upper_j).rename('upper')
    lower = da_j.isel(XC=slice(left_i, right_i), YG=lower_j).rename('lower')
    right = da_i.isel(XG=right_i, YC=slice(lower_j, upper_j)).rename('right')
    left = da_i.isel(XG=left_i, YC=slice(lower_j, upper_j)).rename('left')
    
    if bs=='upper':
        return upper
    elif bs=='lower':
        return lower
    elif bs=='right':
        return right
    elif bs=='left':
        return left
    else:
        None 
    
    return -upper.sum(('Z', 'XC')) + lower.sum(('Z', 'XC')) - right.sum(('Z', 'YC')) + left.sum(('Z', 'YC'))