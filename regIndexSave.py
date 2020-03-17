############ VIRTUAL ##############

# EMAIL
# no backtracking 
validEmail = '(?=[A-Z0-9][A-Z0-9@._%+-]{5,253}+$)[A-Z0-9._%+-]{1,64}+@(?:(?=[A-Z0-9-]{1,63}+\.)[A-Z0-9]++(?:-[A-Z0-9]++)*+\.){1,8}+[A-Z]{2,63}+'

# IP ADRESS
# capturing group  + free spacing mode 
ip_adress = '\b(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\b'

# MAC ADRESS
macAdress = '[a-fA-F0-9:]{17}|[a-fA-F0-9]{12}'

# BITCOIN ADRESS

bitcoin = '^[13][a-km-zA-HJ-NP-Z0-9]{26,33}$'

# ONION/TOR ADRESS
onion_v2 = '([a-z2-7]{16}.onion)'
onion_v3 = '([a-z2-7]{56}.onion)'
onion = '([a-z2-7]{16}.onion)|([a-z2-7]{56}.onion)'


############ PHYSICAL ##############

# DATE
# Full Date 
date_full = '(19|20)\d\d[- /.](0[1-9]|1[012])[- /.](0[1-9]|[12][0-9]|3[01])'


# Building Code (DigiCode)
## FR
digicode_fr = '(?:\d{4,9}[A|B])'

# PHONE NUMBER
phone_wide = '((?:\+|00)[17](?: |\-)?|(?:\+|00)[1-9]\d{0,2}(?: |\-)?|(?:\+|00)1\-\d{3}(?: |\-)?)?(0\d|\([0-9]{3}\)|[1-9]{0,3})(?:((?: |\-)[0-9]{2}){4}|((?:[0-9]{2}){4})|((?: |\-)[0-9]{3}(?: |\-)[0-9]{4})|([0-9]{7}))'
phone_us = '[\\(]{0,1}([0-9]){3}[\\)]{0,1}[ ]?([^0-1]){1}([0-9]){2}[ ]?[-]?[ ]?([0-9]){4}[ ]*((x){0,1}([0-9]){1,5}){0,1}'
phone_us_nanp = '^(?:\([2-9]\d{2}\)\ ?|[2-9]\d{2}(?:\-?|\ ?))[2-9]\d{2}[- ]?\d{4}$'
phone_au = '(1300\d{6}$)|(^1800|1900|1902\d{6}$)|(^0[2|3|7|8]{1}[0-9]{8}$)|(^13\d{4}$)|(^04\d{2,3}\d{6})'
phone_uk = '(\+44\s?7\d{3}|\(?07\d{3}\)?)\s?\d{3}\s?\d{3}'
phone_fr = '((\+)33|0)[1-9](\d{2}){4}'

# POSTAL CODE 
postal_quebec = '[a-zA-Z]{1}[0-9]{1}[a-zA-Z]{1}(\-| |){1}[0-9]{1}[a-zA-Z]{1}[0-9]{1}'

# CREDIT CARD 
creditCard_Visa = '4[0-9]{12}(?:[0-9]{3})?'
creditCard_MasterCard = '^(?:5[1-5][0-9]{2}|222[1-9]|22[3-9][0-9]|2[3-6][0-9]{2}|27[01][0-9]|2720)[0-9]{12}$'
creditCard_AmericanExpress = '^3[47][0-9]{13}$'
creditCard_DinerClub = '^3(?:0[0-5]|[68][0-9])[0-9]{11}$'
creditCard_Discover = '^6(?:011|5[0-9]{2})[0-9]{12}$'
creditCard_JCB = '^(?:2131|1800|35\d{3})\d{11}$' 

creditCard = 'creditCard_Visa | creditCard_MasterCard | creditCard_AmericanExpress | creditCard_DinerClub | creditCard_Discover | creditCard_JCB'