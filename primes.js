var primes = [2];

function printPrimes(n) {
    for (var i=3; i<=n; i++) {
        for (var j=0; j<primes.length; j++) {
            if (i % primes[j] === 0) {
                break;
            }

            else if (j == primes.length-1) {
                primes.push(i);
                break;
            }
        }
    }
    return primes;
}

printPrimes(100);