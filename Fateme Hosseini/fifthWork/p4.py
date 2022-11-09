def par(listA):
    myd = {}
    myl = list(listA.upper())
    for item in myl:
        if ["A" , "E" , "O", "I","Y","U"].count(item) >0:
            myd[item] = myd.get(item  , 0)+1
    return myd





