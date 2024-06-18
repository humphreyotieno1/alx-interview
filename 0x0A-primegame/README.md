# Prime Game
This is an implementation of the Prime Game, where two players (Maria and Ben) take turns choosing a prime number from a set of consecutive integers from 1 to n, and removing that number and its multiples from the set. The player who cannot make a move loses the game.

The isWinner function takes two parameters: x, the number of rounds, and nums, an array of values for n in each round. The function returns the name of the player who won the most rounds (either "Maria" or "Ben"). If the winner cannot be determined, it returns None.

The implementation uses the Sieve of Eratosthenes algorithm to generate the list of prime numbers up to n for each round, and then simulates the game play to determine the winner.