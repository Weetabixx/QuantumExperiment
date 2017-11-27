# Before you can use the jobs API, you need to set up an access token.
# Log in to the Quantum Experience. Under "Account", generate a personal
# access token. Replace "None" below with the quoted token string.
# Uncomment the APItoken variable, and you will be ready to go.

APItoken = "00882c4913bb27a31791d060a29d1d4afdc0eda3d0c3a7b75b936347663cf93f76b10af424a4ab9295dfd27fe7f0e41d71bb5d5baac90067baa1c2de2e060ba6"

config = {
  "url": 'https://quantumexperience.ng.bluemix.net/api'
}

if 'APItoken' not in locals():
  raise Exception("Please set up your access token. See Qconfig.py.")