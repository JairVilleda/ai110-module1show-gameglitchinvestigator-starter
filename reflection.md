# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

- What did the game look like the first time you ran it?
- List at least two concrete bugs you noticed at the start  
  (for example: "the secret number kept changing" or "the hints were backwards").

---
The first thing I noticed that was wrong was the hints were backwards. When my guess was lower than the secret number, the hint said "Go LOWER!" and when my guess was higher than the secret number, the hint said to go higher.
Another bug that I found was that that the "new game" button did not really work since it would show the secret number changing but did not let me start submitting guesses. Another issue is that the number range based on teh difficulty level was not being applied correctly. For example. the range for the easy mode is 1-20 but the secret numbers would be out of this range.

## 2. How did you use AI as a teammate?

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)?
- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result).
- Give one example of an AI suggestion that was incorrect or misleading (including what the AI suggested and how you verified the result).

---
One example of a correct AI suggestion was when I asked Claude how to verify that the difficulty ranges were working correctly. It suggested writing a pytest to check that the get_range_for_difficulty function for each difficulty level return the expected values, which was verified by the passed pytest and in-game logic. One example of an incorrect AI suggestion was related to the "New Game" button in which Claude suggested that simply resetting st.session_state.attempts would fix the button. I verified the problem by testing the button in the app and it still did not allow a new game to start properly. I asked Claude to explain the code logic where the issue was occuring and fixed the bug together.


## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?
- Describe at least one test you ran (manual or using pytest)  
  and what it showed you about your code.
- Did AI help you design or understand any tests? How?

---
I decided that a bug was fixed by testing the app manually and verifying the pytests that targeted the fixed bugs. For example, to verify that check_guess() gave the correct hints, I manually guessed a number above and below the secret number and checked that the messages now matched the logic. Claude helped me design the pytest by suggesting specific cases to check, like confirming the difficulty ranges. Claude also helped me understand how pytest worked in general and how to implement them since I never really used pystest.

## 4. What did you learn about Streamlit and state?

- In your own words, explain why the secret number kept changing in the original app.
- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?
- What change did you make that finally gave the game a stable secret number?

---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
  - This could be a testing habit, a prompting strategy, or a way you used Git.
- What is one thing you would do differently next time you work with AI on a coding task?
- In one or two sentences, describe how this project changed the way you think about AI generated code.
