def longestCommonPrefix(strs):
    pref = ""
    for n in range(len(strs[0]), 0, -1):
        present = True
        pref_ = strs[0][0:n]
        for word in strs:
            if not word.startswith(pref_):
                present = False
        if present:
            pref = pref_
            break 
    return pref

print(longestCommonPrefix(["flower","flow","flight"]))