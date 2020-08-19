This little (fun built) tool ist inspired by Flamable Maths (https://www.youtube.com/watch?v=f2lEB4nMmyI).

I've made 2 little improvements here:
1. Slightly improved the asymptotic runtime: \
    In the prime testing method, I've only checked whether the prime candidate ist divisible by the already found primes below its square root, not all numbers. Asymptotically, this means a runtime complexity of Theta(n/ln(n)) compared to Theta(n).
2. It bothered me, that the definition of right truncatable primes ist so dependent on the choice of basis (default and in the video: base 10), so I changed the tool to allow every base given.