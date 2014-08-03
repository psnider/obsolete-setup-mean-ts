# remove quotes embedded in strings
s/\\['\"\]/ /g

# remove close square bracket
s/]/ /g
 # remove remaining non-string delimiter punctuation                                
s/[-~`!@#%^&*()+={}[|\\:;<>,\.?]/ /g

# remove double quote strings
s/"[^"]*"/ /g                           

# remove single quote strings
s/'[^']*'/ /g                           

# remove slash/regexp quote strings
s:/[^/]*/[gi]*: :g                      

# remove slashes
s:/: :g                      

# remove hex numeric constants
s/[[:<:]]0x[0-9a-fA-F]+[[:>:]]/ /g      

# remove other numeric constants
s/[[:<:]][0-9]+[[:>:]]/ /g              

# place each token on its own line
s/ /\
/g                               

