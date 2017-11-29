# Before you can use the jobs API, you need to set up an access token.
# Log in to the Quantum Experience. Under "Account", generate a personal
# access token. Replace "None" below with the quoted token string.
# Uncomment the APItoken variable, and you will be ready to go.

APItoken = "c5c7e17ab37e81f6234edbc6f6a22f23910778cb4ecc8d041327ee26b38b311f5a9efcdaed72cc9a6b144d3bcaf21c8872a5d1ef139be621d385a5af0bb5b430"

config = {
  "url": 'https://quantumexperience.ng.bluemix.net/api'
}

if 'APItoken' not in locals():
  raise Exception("Please set up your access token. See Qconfig.py.")