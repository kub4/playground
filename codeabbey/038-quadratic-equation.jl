#!/usr/bin/env julia

"""
Quadratic Equation
==================

* order of values inside the pair is important - for real roots output the
  bigger one first; for complex roots output a+bi first and a-bi last;
* roots would be always expressed with integer numbers in this task, so print
  no any decimal points etc.

input data:
2
3 -3 -6
1 0 1

answer:
2 -1; 0+1i 0-1i

"""

# define the quadratic equation solver function
function solve_quadratic(equation)
  a,b,c = equation
  x1 = (-b+sqrt(complex(b^2-4*a*c)))/(2*a)
  x2 = (-b-sqrt(complex(b^2-4*a*c)))/(2*a)
  [x1, x2]
end

# create lists to hold equations and solutions
equations = Array[]
solutions = Array[]

# read the input data from file
f=open(ARGS[1])
n=int(strip(readline(f)))
for i = 1:n
  push!(equations,[int(x) for x in split(readline(f))])
end

# now solve an equation by an equation
for i = 1:n
  push!(solutions,solve_quadratic(equations[i]))
end

# now print the results
# (ok, this is ugly, but it works :)
for i = 1:n
  x1,x2 = solutions[i]
  if imag(x1) == 0
    print(int(real(x1)))
    print(" ")
    print(int(real(x2)))
    if i!=n
      print("; ")
    else
      println()
    end
  else
    print(int(real(x1)))
    if imag(x1) > 0
      print("+")
    end
    print(int(imag(x1)))
    print("i ")
    print(int(real(x2)))
    if imag(x2) > 0
      print("+")
    end
    print(int(imag(x2)))
    print("i")
    if i!=n
      print("; ")
    else
      println()
    end
  end
end
