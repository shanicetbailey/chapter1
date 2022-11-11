# Universal box budget function for SODA's data
# Given upper right / lower left cell coordinates, construct the tx_trans and ty_trans sections that bound it

def box_budget(da_i, da_j, left_i, right_i, lower_j, upper_j, bs=None):
    
    """Function to compute box budget given any set of boundaries.
        da_i and da_j are the zonal and meridional dataarrays, respectively.
        bs is the boundary side argument specification."""

    upper = da_j.isel(xt_ocean=slice(left_i, right_i+1), yu_ocean=upper_j).rename('upper')
    lower = da_j.isel(xt_ocean=slice(left_i, right_i+1), yu_ocean=lower_j-1).rename('lower')
    right = da_i.isel(xu_ocean=right_i, yt_ocean=slice(lower_j, upper_j+1)).rename('right')
    left = da_i.isel(xu_ocean=left_i-1, yt_ocean=slice(lower_j, upper_j+1)).rename('left')
    
    if bs == 'upper':
        return upper
    elif bs=='lower':
        return lower
    elif bs=='right':
        return right
    elif bs=='left':
        return left
    else:
        print('total: ', -upper.sum('xt_ocean') + lower.sum('xt_ocean') - right.sum('yt_ocean') + left.sum('yt_ocean'))
    
    
    return -upper.sum('xt_ocean') + lower.sum('xt_ocean') - right.sum('yt_ocean') + left.sum('yt_ocean')