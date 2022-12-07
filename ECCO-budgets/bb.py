# Universal box budget function for ECCO's data
# Given upper right / lower left cell coordinates, construct the x and y sections that bound it

def box_budget(da_i, da_j, left_i, right_i, lower_j, upper_j, bs=None):
    
    """Function to compute box budget given any set of boundaries.
        da_i and da_j are the zonal and meridional dataarrays, respectively.
        bs is the boundary side argument specification."""

    upper = da_j.isel(i=slice(left_i, right_i), j_g=upper_j).rename('upper')
    lower = da_j.isel(i=slice(left_i, right_i), j_g=lower_j).rename('lower')
    right = da_i.isel(i_g=right_i, j=slice(lower_j, upper_j)).rename('right')
    left = da_i.isel(i_g=left_i, j=slice(lower_j, upper_j)).rename('left')
    
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
    
    return -upper.sum(('k', 'i')) + lower.sum(('k', 'i')) - right.sum(('k', 'j')) + left.sum(('k', 'j'))



#Slicing instead of slice and sum

def slice_box(da, left_i=None, right_i=None, lower_j=None, upper_j=None, cell=None):
    
    """Function to simply slice data to desired box boundary.
        Specify if data array's grid is only grid center, or
        some combination of grid center and face."""
    
    if cell=='c':
        box = da.isel(j=slice(lower_j, upper_j), i=slice(left_i, right_i))
    elif cell=='xg':
        box = da.isel(j=slice(lower_j, upper_j), i_g=slice(left_i, right_i))
    elif cell=='yg':
        box = da.isel(j_g=slice(lower_j, upper_j), i=slice(left_i, right_i))
    else:
        None
    
    return box