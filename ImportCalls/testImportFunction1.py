import httpimport

with httpimport.github_repo(ref='master', username="johnpuksta",repo="ipynbTest"):
  import testFunction1 as tF1

tF1.testFunction1()