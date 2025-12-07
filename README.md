# Advent of Code 2025

This is my first Advent of Code, and first year trying to take learning coding even remotely seriously. I thought I'd write out my thoughts about each day, but we'll see if I keep up with it. My thoughts below might contain some spoilers so I've hidden them away safely, but honestly I'm sure it doesn't really matter.

<details>
  <summary>Day 1</summary>
  
  ### Part 1
  First attempt was a failure since I was just simply subtracting or adding the numbers to the dial position and then "fixing" it by adding or subtracting 100. This obviously didn't account for when the dial was greater/less than 100/-100 (and of course I didn't account for both in my first "fix").

  Got it eventually, but the lesson of this round was not to do this stuff at 3am.

  ### Part 2
  I don't wanna talk about it. It works now though.
  
</details>

<details>
  <summary>Day 2</summary>
  
  ### Part 1
  Huge improvement from Day 1! The first time I *thought* I had the correct solution was the time I *did* have the correct solution! I did what felt like a pretty simple (mentally) method and just checked if the first half of an even length integer (but as a string) matched the second half. I talked with my partner about a way this could be done mathematically afterwards though, and depending on the requirements for Part 2 might update my code to do that (it took a hot second to run what I have now).

  ### Part 2
  I THOUGHT SO. I didn't think so enough to prepare for it in Part 1 though. I updated my day 1 code to do what I described above, but then had to use pen and paper to work out how to apply it to these new patterns. My first try was too high, but it turned out I just needed to delete the solution from Part 1 that was still in my Part 2 function. Success!
  
</details>

<details>
  <summary>Day 3</summary>
  
  ### Part 1
  Done first try! I've found using the example cases in the instructions very helpful to do the initial testing/debugging on a more manageable set of data. Once again though, it is 3am and I guess I forgot how math works so my solution for "smoosh two numbers together without *adding* them together" was to...turn the integers into strings, concatenate the strings, and then turn the result into an integer...
  
  (I immediately figured out the smarter way to do this when saying it out loud but it's so stupid I don't want to change it now)

  ### Part 2
  Part 2 makes me realize my `int(str(int()) + str(int()))` solution actually wasn't that crazy! Only problem is I think I may have to give up on solving Part 2 entirely because even forgetting entirely about how to *program* it, I'm just having trouble wrapping my head around how to most effectively eyeball what a single result should look like when it gets more complicated than say `818181911112111`.

  My new idea is to get the first instance of the biggest number in a subset of the bank - this subset will be the first X batteries, where X is the difference between the total in the bank and the 12 we need to pick out. For each number eliminated, the number being compared needs to reduce by that many. Need to be able to eliminate all X if the next one is larger than all of them, so subset should actually be X + 1.

  I'll have to reread these notes to make sense of them later, but the basic idea I had in my head above ended up being the solution I went with!
  
</details>

<details>
  <summary>Day 4</summary>
  
  ### Part 1
  Easier than I thought, right answer first try!

  ### Part 2
  I think this is the first day I've gotten both parts correct on the first try! My original code was set up pretty well to adapt it to do Part 2 thankfully (though hoo boy did it take a second to run).
  
</details>

<details>
  <summary>Day 5</summary>
  
  ### Part 1
  Again, easier than I expected! My first attempt would have actually accounted for Part 2 as well *buuuut* the way I was doing it was *maybe not the most efficient* and I might have done something terrible to WSL in the process (all good after restarting).

  ### Part 2
  tba
  
</details>

<details>
  <summary>Day 6</summary>
  
  ### Part 1
  tba

  ### Part 2
  tba
  
</details>

<details>
  <summary>Day 7</summary>
  
  ### Part 1
  tba

  ### Part 2
  tba
  
</details>

<details>
  <summary>Day 8</summary>
  
  ### Part 1
  tba

  ### Part 2
  tba
  
</details>

<details>
  <summary>Day 9</summary>
  
  ### Part 1
  tba

  ### Part 2
  tba
  
</details>

<details>
  <summary>Day 10</summary>
  
  ### Part 1
  tba

  ### Part 2
  tba
  
</details>

<details>
  <summary>Day 11</summary>
  
  ### Part 1
  tba

  ### Part 2
  tba
  
</details>

<details>
  <summary>Day 12</summary>
  
  ### Part 1
  tba

  ### Part 2
  tba
  
</details>