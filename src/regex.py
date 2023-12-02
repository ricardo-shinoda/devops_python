# How Regex search for caracters
# a+ | Search for one or more "a" on a string
# \w | Search for leters or numbers (but not special caracter)

# To regex email address

#  \w+@\w+\./w+

import re
email = """Email received June 2 from user1@email.com. Email received June 2 from user2@email.com. Email rejected June 2 from invalid_email@email.com."""

print(re.findall("\w+@\w+\.\w+", email))
