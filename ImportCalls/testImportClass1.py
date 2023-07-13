import httpimport

with httpimport.github_repo(ref='master', username="johnpuksta",repo="ipynbTest"):
  import testClass1 as tC1

testClass.func1()
#testClass.func2(3)