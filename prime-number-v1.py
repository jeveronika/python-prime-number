def prime_finder(n):
  result = []
  for i in range(2, n+1):
    is_prime = True
    for j in range(2, i):
      if i % j == 0:
        is_prime = False
        break
    if is_prime:
      result.append(i)
  return result

print(prime_finder(20))
