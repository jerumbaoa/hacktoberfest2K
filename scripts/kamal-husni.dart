void main() {
  isPrimeNumber(7);
}

void isPrimeNumber(int num) {
  int i, m = 0;
  bool isPrime = true;

  m = num ~/ 2;

  for (i = 2; i <= m; i++) {
    if (num % i == 0) {
      print('$num is not a prime number');
      isPrime = false;
      break;
    }
  }

  if (isPrime) {
    print('$num is a prime number');
  }
}
