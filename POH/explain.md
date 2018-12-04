|Date|Version|
|:-:|:-:|
|2018/12/4|1.0|

## Simple Explanation
- Honestly I couldn't quite understand the description given on that page.
- I figured out the process after manually re-implement the given example:
    1. Pick one card on the table (as the *field_card* in program);
    2. Keep searching the *first* larger card (according to the given sequence); Here we may encounter 2 situations:
        1. The larger card exists: in this case, switch the field_card with current larger card, and give the order to the current card;
        2. The larger card never exists: (like the field_card is '2' or the current largest card) In this case, this is a deadlock. The meaning of the description (I guessed) might be: If you keep searching the *larger card* and finally return back to the current *field_card*, you should first give the current order to that *field_card*, get rid of the current *field_card*, and take the following card as the *next field_card*.
- With this mechanism, I got the *Accept* for this problem. 

## Others
1. Obviously, this ugly solution is **Definitely NOT** the optimal one. You could search for others' solutions and learn from those.
2. If my understanding was wrong and you got the author's point, please please tell me about that.
3. :) 「制服」 was so fuxking awesome! :)

