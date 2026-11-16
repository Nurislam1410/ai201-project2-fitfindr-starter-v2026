# Acceptance criteria — FitFindr

Five criteria that say what "working" means for this agent, written in unit 3
**before** any results existed.

An acceptance criterion names a target: a number, a count, a rate, or something
a person could plainly observe. *"The agent handles errors"* is an opinion.
*"When search returns nothing, the agent stops before calling the second tool,
in 5 of 5 tries"* is a criterion.

Under each one, write a sentence or two on **why that target** and not a
stricter one. A reason that says something about your tools, your loop, or the
data earns credit; *"80% seemed reasonable"* does not.

> Missing your own targets next unit costs you nothing. Setting a target so
> easy you can't miss it does.

**Two are written for you. You write three.**

---

## 1. A matching query completes all three tools

Given a query that matches at least one listing, the agent completes all three
tool calls and returns a fit card — in at least 4 of 5 tries.

**Why this target:**
<!-- Why 4 of 5 and not 5 of 5? Something about your search, probably —
     "my search is a plain keyword match and some phrasings will miss" is a
     real answer. -->

---

## 2. An impossible query stops before the second tool

Given a query that matches no listings, the agent stops before calling
`suggest_outfit` and returns a message naming what to change — 5 of 5 tries.

**Why this target:**
<!-- Why is 5 of 5 reasonable here when criterion 1 isn't? What's different
     about this path? -->
Because no model will be called in this path, so a miss would be a bug.
---

## 3. Something about state

<!-- YOU WRITE THIS ONE.

     How would you know that the item your search found is the same item the
     next tool received? Name something countable or observable.

     This is the criterion people find hardest, because state failure doesn't
     look like state failure — it looks like a tool problem. Something that
     compares session["selected_item"] against what actually reached
     suggest_outfit is the shape you're after. -->
Given a matching query, the item X has the same id as the item Y in 5 of 5 tries.


**Why this target:**
Because no model involved in passing state, so less than 5/5 means something is broken.


---

## 4. Something about the fit card

<!-- YOU WRITE THIS ONE.

     The fit card calls a model, so the same input can produce different words
     each time. That's not a bug — it's the nature of the tool. So what would
     make it acceptable?

     Think about what you'd actually be unhappy to see. A caption that never
     mentions the price? Two different items producing the same opening
     sentence? A card longer than a caption anyone would post? Any of those can
     be turned into a number. -->
Model must mention the price, the platform and never exceed 60 words in 4 of 5 tries.


**Why this target:**
Because here the model is actually called, so some run-to-run variance in hitting every requirement might happen.


---

## 5. Your choice

<!-- YOU WRITE THIS ONE TOO.

     Pick something you actually care about getting right. Speed, the empty
     wardrobe path, what happens when the model can't be reached, whether the
     search respects a price ceiling — anything, as long as it names a number
     or an observable outcome. -->
Search for sizes must include the related listings and exclude unrelated ones in 5 of 5 tries.


**Why this target:**
Because model won't be called in this step, and any misses would mean a bug in the code.


---

<!-- ─────────────────────────────────────────────────────────────────────────
     UNIT 4 — read this before you change anything above.

     If a criterion turns out to be BROKEN rather than merely unmet, you can
     revise it, and that earns credit. But never delete or edit the original
     line. Add the revision underneath it, like this:

         ## 4. Something about the fit card

         The fit card is different every time.

         **Why this target:** ...

         > **Revised in unit 4:** For 5 different items, the 5 fit cards share
         > no opening sentence.
         >
         > **Why revised:** "different" wasn't checkable — two cards that
         > differed by one word still counted. The new version is something I
         > can actually score.

     That's a revision because the criterion couldn't be MEASURED.

     Lowering a target because you missed it is not a revision, and it costs
     you the point:

         ✗ "I said the empty search stops it 5 of 5 times, but I got 3 of 5,
            so 3 of 5 is more realistic."

     A number you missed stays where it is, gets diagnosed, and gets a fix
     attempted. That's where the points are.
     ───────────────────────────────────────────────────────────────────────── -->

---

# Capstone criteria

Written before any capstone results existed. The system is FitFindr, deployed at https://fitfindr-anl0.onrender.com. Faults are switched on per request with the `X-FitFindr-Fault` header (see RUNNING.md). Times are `duration_ms` from the request log.

**1. A stuck model fails within 25 seconds.**
At least 4 of 5 requests sent with `X-FitFindr-Fault: timeout` return HTTP 503 with an error message (not a hang, not a 500), and each of those requests takes no more than 25 seconds, measured by `duration_ms` in the log.

Why: after 15–30 seconds the user is just going to be wasting their time, so they have to get a response in that window. 25 s is in it. With the current settings the worst case is about 41 s (two 20 s attempts), so it can absolutely fail.

**2. Each failure tells you what went wrong.**
For all 4 fault types (`timeout`, `server_error`, `empty`, `rate_limit`), the 503's error message names the fault. The words checked are: timeout → "didn't answer" or "timed out"; server_error → "having trouble"; empty → "empty"; rate_limit → "rate limited".

Why: if the user can't work out what kind of failure it was, then they can't decide whether to retry, whether to wait, or whether to modify their request. Every type has to name itself, because a user who hits the one vague message is just as stuck as if they were all vague.

**3. No request goes unrecorded.**
Every request sent during the trials (for all five criteria, including the failures and the 400s) has exactly one corresponding record in the request log (same `request_id`) with `status`, `outcome` and `duration_ms` all populated.

Why: the wrong timeout message was only spotted because the failed request was logged. A failure that leaves no record at all is one you can never get to the bottom of, so missing one record is too many.

**4. Bad input results in a 400, never a crash.**
Of 5 malformed requests (no query, empty query, spaces only, a number, not JSON), at least 3 return HTTP 400 with a message telling you to send JSON with a `query` field, and none of the 5 returns a 500.

Why: a caller who's sent the wrong thing should be told how to fix it. An empty query and non-JSON are pretty self-explanatory, so 3 of 5 is sufficient for the wording, but a crash is absolutely not acceptable.

**5. Normal requests are quick.**
At least 9 of 10 warm requests (i.e. not the very first request after the service has been idle for 15+ minutes) complete in under 10 s by `duration_ms`.

Why: speed is far more important to the user than cost. The measured median is 5.9 s and one run took 14.2 s, so 10 s is a real bar and not a free pass.
