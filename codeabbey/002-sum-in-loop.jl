#!/usr/bin/env julia
"""
data:
8
10 20 30 40 5 6 7 8

answer:
126
"""

f=open(ARGS[1])
n=int(strip(readline(f)))
a=split(readline(f))

sum = 0

for i = 1:n
  sum = sum + int(a[i])
end

println(sum)
