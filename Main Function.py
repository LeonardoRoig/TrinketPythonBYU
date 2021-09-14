def prompt_number():
  numero = int(input("Enter a positive number:"))
  while numero <= 0:
    print ("Invalid entry. The number must be positive.")
  return numero

def compute_sum(numero1, numero2, numero3):
  result = numero1 + numero2 + numero3
  return result

def main():
  numero1 = prompt_number()
  numero2 = prompt_number()
  numero3 = prompt_number()
  total = compute_sum(numero1, numero2, numero3)
  print ("The sum is:{}".format(total))
  return

if __name__ == "__main__":
    main()
    