# FitFindr

> ### 👋 Start here
>
> **New to this repo? Read [RUNNING.md](RUNNING.md) first** — setup, every
> command, and what to do when something breaks.
>
> Once `python test.py` passes:
>
> ```bash
> python app.py listings --full -n 6      # read the data (Milestone 1)
> python app.py fields                    # what you can filter on
> python app.py ask 'vintage graphic tee under $30'
> ```
>
> All three tools are stubs, so that last command will do nothing useful yet.
> That's the starting position.
>
> **The rest of this file is your submission.** Fill it in as you go.

---

<!-- ─────────────────────────────────────────────────────────────────────────
     HOW TO USE THIS FILE

     This is your submission. Fill each section in as you finish the milestone
     it belongs to — don't leave it all to the end.

     Unit 3 asks for the first five sections. Unit 4 adds the five below them.
     Leave the unit 4 sections alone until then; they're here so you know
     what's coming.

     Everything is pasted as TEXT. No screenshots, no images, no video links.
     A typed block of output gets full credit; a picture of the same output
     gets none.
     ───────────────────────────────────────────────────────────────────────── -->

<!-- ═══════════════════════ UNIT 3 — THE BUILD ═══════════════════════ -->

## What This Does

<!-- Three or four sentences: what a user asks for, and what they get back. -->



---

## Tool Inventory

<!-- Four lines per tool. This is worth 2 points and it's the single most
     common place students lose them.

     "Returns a list" earns NOTHING. The description has to say what is IN
     the list.

     The empty case isn't optional either — it's the thing your loop branches
     on, and if you don't decide it here you'll discover it as a crash in
     Milestone 5. -->

### `search_listings`

- **What it does:** it receives as parameters: description(mandatory), size(optional) and max_price(optional) and returns a list of dictionaries 
- **Inputs:** <!-- name and type each: `max_price` (float), not "a price" --> 'description'(str), 'size'(str | None=None), 'max_price'(float | None=None )
- **Returns:** a list of dictionaries with every field in the listings for each item (dictionary)
- **When it has nothing:** it returns an empty list, not None

### `suggest_outfit`

- **What it does:** It receives as parameters: new item and wardrobe items and returns an outfit suggestions with what is in wardrobe
- **Inputs:** 'new_item'(dict), 'wardrobe'(dict)
- **Returns:** a non-empty string with outfit suggestions (string)
- **When it has nothing:** if wardrobe is empty, then returns a string with general outfit suggestions based on models trained knowledge, no empty returns

### `create_fit_card`

- **What it does:** It receives as parameters: outfit and new_item from suggest_outfit, then returns a 2-4 sentence caption
- **Inputs:** 'outfit'(str), 'new_item'(dict)
- **Returns:** 2-4 sentence caption which mentions the item, its price, and platform once each, and also more specific vibe (string) 
- **When it has nothing:** if outfit is empty/whitespace, it returns a descriptive message, no raising.

---

## Planning Loop

<!-- Your branch rule, stated as a rule — the condition AND both paths — plus
     the file and function that holds it.

     Like this:
       "If search_listings returns an empty list, put a message in the session
        and stop. Otherwise take the first result and go to suggest_outfit."
        — agent.py::run_agent

     The grader checks your code against what you claim here, so the file and
     function have to be real. -->

**Branch rule:** It should stop and not call 'suggest_outfit' if 'search_listings' returns an empty list. Otherwise, it should take the first result and continue to 'suggest_outfit'

**Where it lives:** `agent.py::run_agent`

**How the query is parsed:** <!-- regex, string splitting, or asking the model — say which --> 
Regex / string splitting pulls out 'max_price', 'size', and treats the rest as the description. So, no model call needed here.

**What moves through the session:** <!-- which fields, in what order -->
'query' -> 'parsed' -> 'search_results' -> 'selected_item' ->  'outfit_suggestion' -> 'fit_card'
---

## Sample Run

<!-- Two things go here.

     1. One FULL query and its output, pasted as text.
     2. Your three per-tool terminal tests — the command and what it printed. -->

**One full query**

```
$ python app.py ask 'vintage graphic tee under $30, size M'

```
Found:    90s Silk Slip Dress — Floral, Midi Length — $30.0 on depop

Outfit:   Layer the 90s floral silk slip dress over the white ribbed tank top and ground the feminine midi length with the edgy black combat boots. Throw on the vintage black denim jacket for an effortless 90s grunge contrast, and accessorize with the black crossbody bag.

Fit card: Channeling major 90s grunge with this floral silk slip! 🌸✨ Layered it over a ribbed tee and toughened up the midi length with combat boots and a denim jacket. A total steal for just $30—grab it on Depop before I change my mind!

2 model calls this session, 300 prompt + 114 output tokens


**The three tools, tested one at a time**

```
$ python -c "from tools import search_listings; print(search_listings('graphic tee', max_price=30))"

```
[{'id': 'lst_002', 'title': 'Y2K Baby Tee — Butterfly Print', 'description': 'Super cute early 2000s baby tee with butterfly graphic. Fitted crop length. Tag says medium but fits like a small.', 'category': 'tops', 'style_tags': ['y2k', 'vintage', 'graphic tee', 'cottagecore'], 'size': 'S/M', 'condition': 'excellent', 'price': 18.0, 'colors': ['white', 'pink', 'purple'], 'brand': None, 'platform': 'depop'}, {'id': 'lst_006', 'title': 'Graphic Tee — 2003 Tour Bootleg Style', 'description': 'Vintage-style bootleg tee with faded graphic. Slightly boxy fit. 100% cotton, soft and worn-in.', 'category': 'tops', 'style_tags': ['graphic tee', 'vintage', 'grunge', 'streetwear', 'band tee'], 'size': 'L', 'condition': 'good', 'price': 24.0, 'colors': ['black'], 'brand': None, 'platform': 'depop'}, {'id': 'lst_011', 'title': 'Low-Rise Cargo Pants — Khaki', 'description': 'Y2K era low-rise cargo pants. Lots of pockets. Khaki color, slightly distressed at the hems. Great for layering with a long tee.', 'category': 'bottoms', 'style_tags': ['y2k', 'cargo', '2000s', 'streetwear'], 'size': 'W29', 'condition': 'fair', 'price': 27.0, 'colors': ['khaki', 'tan'], 'brand': None, 'platform': 'poshmark'}, {'id': 'lst_012', 'title': 'Oversized Crewneck Sweatshirt — Vintage Navy', 'description': 'Perfectly faded navy crewneck. Genuinely vintage — not manufactured distressed. Ribbed cuffs and hem. No graphics, clean.', 'category': 'tops', 'style_tags': ['vintage', 'basics', 'oversized', 'classic'], 'size': 'XL (fits oversized)', 'condition': 'good', 'price': 20.0, 'colors': ['navy'], 'brand': None, 'platform': 'thredUp'}, {'id': 'lst_015', 'title': 'Vintage Graphic Hoodie — Faded Black', 'description': 'Faded black pullover hoodie with barely-visible vintage graphic on the chest. Cozy interior. Some pilling but adds to the worn-in look.', 'category': 'tops', 'style_tags': ['vintage', 'grunge', 'graphic', 'streetwear'], 'size': 'L', 'condition': 'fair', 'price': 26.0, 'colors': ['black', 'charcoal'], 'brand': None, 'platform': 'depop'}, {'id': 'lst_017', 'title': 'Mesh Long-Sleeve Top — Black', 'description': 'Sheer black mesh long-sleeve. Great for layering under a graphic tee or over a bralette. Stretchy material, fits true to size.', 'category': 'tops', 'style_tags': ['y2k', 'grunge', 'goth', 'layering'], 'size': 'S/M', 'condition': 'excellent', 'price': 15.0, 'colors': ['black'], 'brand': None, 'platform': 'depop'}, {'id': 'lst_033', 'title': 'Vintage Band Tee — Faded Grey', 'description': 'Faded grey band-style tee with distressed graphic. Crew neck. Fits boxy. Well-loved but no holes or major damage.', 'category': 'tops', 'style_tags': ['vintage', 'grunge', 'band tee', 'graphic tee', 'streetwear'], 'size': 'L', 'condition': 'fair', 'price': 19.0, 'colors': ['grey', 'charcoal'], 'brand': None, 'platform': 'depop'}]


```
$ python -c "from tools import suggest_outfit; from utils.data_loader import get_example_wardrobe, load_listings; print(suggest_outfit(load_listings()[0], get_example_wardrobe()))"

```
Pair your new Vintage Levi's 501 Jeans with the white ribbed tank top and black cropped zip hoodie layered on top, finishing the look with chunky white sneakers and the black crossbody bag for a casual streetwear vibe. Alternatively, tuck the white ribbed tank into the jeans, cinch your waist with the brown leather belt, and wear the black combat boots and vintage black denim jacket for an edgy, classic aesthetic.

```
$ python -c "from tools import create_fit_card; from utils.data_loader import load_listings; print(create_fit_card('jeans and white sneakers', load_listings()[0]))"

```
Nothing beats the fit of broken-in vintage denim. 👖✨ Just scored these perfect medium-wash Levi's 501s and I’m obsessed. Keepin' it classic with crisp white sneakers for that effortless off-duty look. Grabbed them on Depop for just $38!
---

## How I Used AI

<!-- Two specific moments. What you asked, what came back, what you changed.

     "I used Claude to help me code" is not enough.

     "I gave Claude my search_listings spec. It returned None on no match
     instead of an empty list, so I changed it" is the level we want. -->

**Moment 1**

- *What I asked for:* having 'suggest_outfit' call 'search_listings' internally when the wardrobe is empty.
- *What came back:* Claude pointed out that hides the step from the loop and breaks branch visibility
- *What I changed:* so I dropped it and kept the simpler general_advice version instead

**Moment 2**

- *What I asked for:* Feedback on my `create_fit_card` empty-case spec, which said "if outfit is empty returns a descriptive message, no raising."
- *What came back:* Claude pointed out that Python's `not outfit` check doesn't catch whitespace-only strings (`"   "` is truthy, not falsy), so my spec was missing that edge case.
- *What I changed:* Updated the line to "if outfit is empty/whitespace," and the actual code check uses `.strip()` instead of just `not outfit`.

**Moment 3 (Unit 4, Milestone 2's sanctioned exercise)**

- *What I asked for:* copied the three actual failure messages my agent generates and asked what I should attempt next as a user who is unable to see the code, for each of these messages, and also whether any of them left me with no possible next step.
- *What came back:* for the empty search message, that one of the three named filters should be adjusted; for the model unavailable message, there was also an action to take — check the env file or get a new key from the specified URL; regarding the empty wardrobe message, it was observed that this is not in fact an error message at all, since the branch succeeds by giving general advice rather than personalized advice, so the question doesn't apply in the same way.
- *What I changed:* The code contains nothing since all three messages had already given the user something to try; however, the observation about the empty wardrobe altered the way I viewed that particular path in comparison to the other two — it should be classified as a success case, not as a failure message.

<!-- ═══════════════════════ UNIT 4 — THE TEST ═══════════════════════

     Don't fill these in during unit 3.
     ═══════════════════════════════════════════════════════════════════ -->

---

## Run Log — Before

<!-- Five criteria, five tries each, in this exact format.

     Five, because your criteria are written out of five. Mark each try PASS
     or FAIL, count the passes, and read that count against your target — a
     row targeting 4 of 5 with three PASS cells is MISSED (3/5).

     `python run_eval.py --label before` runs everything and writes the table
     into results/. Paste it here and fill in the verdicts. -->

| Criterion | Target | Try 1 | Try 2 | Try 3 | Try 4 | Try 5 | Verdict |
|---|---|---|---|---|---|---|---|
| 1. Matching query completes all three tools | 4 of 5 | PASS | PASS | PASS | PASS | PASS | MET (5/5) |
| 2. Impossible query stops before second tool | 5 of 5 | PASS | PASS | PASS | PASS | PASS | MET (5/5) |
| 3. Selected item id stays consistent | 5 of 5 | PASS | PASS | PASS | PASS | PASS | MET (5/5) |
| 4. Fit card mentions price, platform, ≤60 words | 4 of 5 | PASS | PASS | PASS | PASS | PASS | MET (5/5) |
| 5. Size filter includes related, excludes unrelated | 5 of 5 | FAIL | FAIL | FAIL | FAIL | FAIL | MISSED (0/5) |

Full output for all 30 tries (6 scenarios × 5) is in
`results/run_2026-10-13_2120_before.md`.

**Real output from one try**, from `tools.py::search_listings` as called by
`agent.py::run_agent` for criterion 5, scenario "size filter matches related
sizes only," query `"graphic tee size M"` — identical on all 5 tries since
nothing here calls the model:

```
selected_item: 90s Silk Slip Dress — Floral, Midi Length ($30.0, depop)
search_results: 4
[1] search_listings (via MCP)
      in:  dict with keys: description, size, max_price
      out: 4 items: 90s Silk Slip Dress — Floral, Midi Length, 90s Leather Bomber — Black, Vintage Knit Vest — Argyle Brown/Cream … +1 more
```

None of the 4 results are graphic tees.

---

## Verdicts and Diagnoses

<!-- MET or MISSED per criterion against LAST UNIT's target, plus a sentence on
     how you decided.

     Then, for every miss: which of the four places it happened — a tool, the
     loop's branch, the session, or the model's output — AND the mechanism.

     Not a diagnosis:  "The fit card was bad."
     A diagnosis:      "The fit card criterion missed on 2 of 5 items. Both had
                        an empty brand field. My prompt puts the brand in the
                        first sentence, so the card opened with a blank and read
                        like a fragment. The tool worked; the prompt assumed a
                        field that isn't always there."

     Look for a pattern. Three misses on the same tool is one problem, not
     three. -->

| # | Criterion | Target | Verdict | How I decided |
|---|---|---|---|---|
| 1 | Matching query completes all three tools | 4 of 5 | MET (5/5) | Counted a pass where the session's error field was `None` and a non-empty fit card existed. All five tries completed. |
| 2 | Impossible query stops before second tool | 5 of 5 | MET (5/5) | Whenever the search results were empty, a PASS was recorded: the error field named what to change, the trace showed only step 1, and no `suggest_outfit`/`create_fit_card` calls happened. All five attempts halted properly. |
| 3 | Selected item id stays consistent | 5 of 5 | MET (5/5) | For each of the five attempts, the item logged at search time was compared with the item referenced in the fit card text, by title, price, and platform — the same item was obtained throughout the entire process every time. |
| 4 | Fit card mentions price, platform, ≤60 words | 4 of 5 | MET (5/5) | Each of the five fit cards was checked to ensure it included a dollar amount, the platform name, and a word count under 60; all five met the requirements, the longest being about 41 words. |
| 5 | Size filter includes related, excludes unrelated | 5 of 5 | MISSED (0/5) | On all five attempts the same four non-tee items were returned — a dress, a bomber jacket, a vest, and one more — with no actual graphic tees. Since nothing here calls the model, zero out of five indicates a real bug, not random variation. |

**Diagnoses**

On all five attempts, criterion 5 failed, with the same four incorrect items appearing each time. This indicates the presence of a bug in `search_listings`'s keyword matching mechanism, not a problem with the branch or the session. In the loop the complete raw query is passed through as the `description` argument, even though the size value has already been parsed out separately. Within `search_listings`, the match test breaks the full string down into words and then checks each of them to see if it appears as a substring in both the title and the description of each listing. The single character token remaining from the size value acts like a wildcard, since that letter occurs in almost every listing's text, causing it to include items that are unrelated even if the actual keywords would have matched individually. There is also no scoring or sorting stage, even though the tool's documentation states that the best match should appear first, so it just returns the items that pass the filter in the original order of the data. This constitutes one root cause leading to one failing criterion, not three separate problems.

---

## Loop Trace

<!-- One full run, printed step by step, with the MCP call visible in it.

     `python app.py ask '...' --trace` once you've added the trace.step()
     calls in Milestone 2.

     Worth pasting BOTH the happy path and the empty-search path. The empty
     one should be visibly shorter, because it stops. If your two traces are
     the same length, your branch isn't working — and this is the fastest way
     anyone will ever find that out. -->

**Happy path**

```
$ python app.py ask 'vintage graphic tee under $30' --trace

[1] search_listings (via MCP)
      in:  dict with keys: description, size, max_price
      out: 9 items: Y2K Baby Tee — Butterfly Print, Graphic Tee — 2003 Tour Bootleg Style, Low-Rise Cargo Pants — Khaki … +6 more
[2] suggest_outfit
      in:  dict with keys: item, wardrobe_empty
      out: Pair the Y2K baby tee with your baggy straight-leg jeans and chunky white sneakers for an effortless…
[3] create_fit_card
      in:  dict with keys: outfit
      out: Obsessed with this Y2K butterfly baby tee! 🦋 Pair it with baggy dark wash jeans, chunky white sneakers, a brown…

  Found:    Y2K Baby Tee — Butterfly Print — $18.0 on depop
  Outfit:   Pair the Y2K baby tee with your baggy straight-leg jeans and chunky white sneakers for an effortless, nostalgic streetwear look. Cinch the outfit with your brown leather belt and sling your black crossbody bag across your chest to complete the vibe.
  Fit card: Obsessed with this Y2K butterfly baby tee! 🦋✨ Pair it with baggy dark wash jeans, chunky white sneakers, a brown belt, and a black crossbody for the ultimate nostalgic fit. Grab this gem on Depop before I change my mind!
```

**Empty search**

```
$ python app.py ask 'designer ballgown size XXS under $5' --trace

[1] search_listings (via MCP)
      in:  dict with keys: description, size, max_price
      out: [] (empty)

  No listings matched 'designer ballgown size XXS under $5'. Try a broader description, a higher price limit, or a different size.
```

Three steps on the happy path, one on the empty-search path — the branch is visibly doing something, not just claimed.

**On the MCP move:** `search_listings` has now been registered on the MCP server, with a description written for someone who can't see the code, and the inputs it accepts matching those in the Tool Inventory. The agent no longer imports or directly calls `search_listings` — instead it calls the function via the MCP client. After that point there was no difference in behaviour: both the successful search scenario and the case of an empty search gave exactly the same output as in the previous version where the call was made directly, since that was the aim of the exercise — the way the call was made has changed, but the return value has not.



---

## The Improvement

<!-- What you changed, why your diagnosis pointed at it, and the after-run in
     the same table format. One change, measured properly.

     `python run_eval.py --label after` -->

**What I changed:** In `tools.py::search_listings`, filtered the keyword list down to tokens of 3+ characters before the `any(word in title/description ...)` match, instead of matching on every word in the raw query:

```python
keywords = [w for w in description.split() if len(w) >= 3]
...
if keywords and any(word.lower() in item["description"].lower() or word.lower() in item["title"].lower() for word in keywords):
    results.append(item)
```

**Which failure it was meant to fix:** It directly addresses the diagnosis required by criterion 5 — the single character token that remained from the parsed size value was matching almost any listing as a substring and was thus acting like a wildcard by including unrelated items.

### Run Log — After

| Criterion | Target | Try 1 | Try 2 | Try 3 | Try 4 | Try 5 | Verdict |
|---|---|---|---|---|---|---|---|
| 1. Matching query completes all three tools | 4 of 5 | PASS | PASS | PASS | PASS | PASS | MET (5/5) |
| 2. Impossible query stops before second tool | 5 of 5 | PASS | PASS | PASS | PASS | PASS | MET (5/5) |
| 3. Selected item id stays consistent | 5 of 5 | PASS | PASS | PASS | PASS | PASS | MET (5/5) |
| 4. Fit card mentions price, platform, ≤60 words | 4 of 5 | PASS | PASS | PASS | PASS | PASS | MET (5/5) |
| 5. Size filter includes related, excludes unrelated | 5 of 5 | FAIL | FAIL | FAIL | FAIL | FAIL | MISSED (0/5) |

Full output in `results/run_2026-10-13_2127_after.md`.

**Did it help, and how do I know:** In part, and by giving an honest report rather than rounding it up to a win. The wildcard matching bug has in fact been fixed, as can be seen when the search function is tested directly afterwards — it now properly displays the genuine graphic tees which the previous code completely failed to return for this query. However, criterion 5 still fails, with zero out of five. The way in which the failure manifests has changed. Previously, the search used to return four incorrect items each time; now it returns no items at all, since the size filter carries out an exact match after splitting on whitespace, and a combined size value with no internal space will never match the single letter token that is being searched for. The graphic tees in this dataset are never tagged with that single letter by themselves, so none of them satisfy the size filter no matter what the fix for the keyword issue is. That second bug has always existed, it was merely hidden by the first bug which was allowing irrelevant items to pass through anyway. Once this change was made and properly measured, a second real problem emerged rather than being concealed.


---

## What's Still Broken

**Criterion 5 (size filter) is still not being met, with zero out of five**, against a target of five out of five, and is now failing by returning nothing rather than the incorrect results. The remaining bug lies in the size check itself:

```python
if size is not None and size.lower() not in [t.lower() for t in item["size"].split()]:
    continue
```

which only splits on whitespace, so a combined size value with no space remains as a single token and never matches the plain letter that the user is searching for, even though the tool's own specification states that it should match. The solution would be to also split on the slash, or else to check the individual parts separately before comparing. I did not make this change because the rule for this unit is one improvement, measured, and I had already selected and measured the keyword-matching fix. This second bug is separate from the first one, and the first fix revealed it rather than caused it. I ran out of time today to properly go through a full before-and-after cycle again. This would be the next thing I would fix if I returned to it.

**Everything else (criteria 1-4) is MET**, both before and after the improvement — no other misses to report.

<!-- ═════════════════════════════════════════════════════════════════════

     SUBMISSION CHECKLIST — unit 3

       [ ] criteria.md has five numbered criteria, each with a target
       [ ] Each criterion has a reason underneath it
       [ ] All five unit 3 sections above have real content
       [ ] Tool Inventory: all three tools, inputs WITH TYPES, a specific
           return value, and the empty case
       [ ] Planning Loop names the branch rule and agent.py::run_agent
       [ ] Sample Run: one full query plus the three per-tool tests, as text
       [ ] At least four new commits
       [ ] Repository URL submitted — WRITE IT DOWN, you submit the same one
           next unit

     SUBMISSION CHECKLIST — unit 4

       [ ] mcp_server.py exists with one tool registered
           (or a written record of exactly where the rewire broke)
       [ ] Run Log — Before, five criteria, five tries each
       [ ] Real output pasted underneath, naming file and function
       [ ] A verdict on every criterion
       [ ] A diagnosis for every miss, naming a place AND a mechanism
       [ ] Loop Trace, with the MCP call visible in it
       [ ] All three failure modes triggered and handled
       [ ] One improvement, with Run Log — After in the same format
       [ ] What's Still Broken
       [ ] At least four new commits
       [ ] The SAME repository URL as last unit

     Do not delete and recreate this repository. Your commit history is what
     shows your criteria existed before your results did.
     ═════════════════════════════════════════════════════════════════════ -->

---

📖 **How to run this project: [RUNNING.md](RUNNING.md)**

---

## Capstone

**What This Extends**

FitFindr, the Project 2 agent: a user describes a secondhand piece they want, the agent searches the listings (over MCP), picks one, and makes two Gemini calls — `suggest_outfit` styles it against the user's wardrobe and `create_fit_card` writes a short caption. It is served over HTTP by `serve.py` (`POST /ask`).

What's new this unit is the failure handling around the model call. Until now FitFindr only behaved well when Gemini behaved well. Reading `generate.py` and `agent.py` before starting, I found four bad paths:

1. **No timeout.** `generate_content()` has no time limit, so a slow or stuck Gemini call holds the request (and, because `serve.py` runs one request at a time, every request queued behind it) indefinitely.
2. **Only rate limits are retried.** A one-off `500`/`503` from Gemini fails the run on the first try, even though the same call a second later would usually succeed.
3. **An empty reply passes silently.** If Gemini returns no text (`response.text` is `None` or blank — e.g. a safety block), `generate()` returns `""` and the user gets a blank outfit suggestion or fit card with no error at all.
4. **Retries running out crashes the request.** After `MAX_RETRIES` rate-limit attempts, `generate()` raises a plain `RuntimeError`. `agent.py` only catches `ModelUnavailable`, so the exception escapes `run_agent()` and `/ask` returns a `500` with a raw exception string.

**The Shape**

**Shape B — harden against failure**, on **Path A (hosted on Render)**.

The one thing I'm adding is a hardening layer on the single place every model call goes through, `generate.py::generate()`: a per-call timeout, one retry on transient server errors (5xx / timeout), an empty-reply check, and turning "retries exhausted" into the same `ModelUnavailable` the agent already handles. The goal is that every way a Gemini call can fail ends the run with a clear message in `session["error"]` that says what happened and what to do — never a hang, a `500`, or a blank card. To test it honestly I'm also adding a fault-injection switch (`FITFINDR_FAULT` env var) that makes the model call fail on purpose in each of those ways, so the bad path can be triggered on demand instead of waited for. As every shape requires, the service also gets a structured JSON-lines log of every `/ask` request (failures included) and a Render deployment.

**Out of scope** — things I considered and decided not to do this unit:

- **No new tools and no real listings.** Connecting a real marketplace (e.g. eBay's API) in place of `data/listings.json` is the obvious next step for this as a product, but it's a capability (shape C), not hardening.
- **No changes to the planning loop, the prompts, or search.** The still-broken size filter from Project 2 (criterion 5) stays as it is; fixing it would be a second, unrelated change.
- **No change to concurrency.** `serve.py` keeps its one-request-at-a-time lock; replacing it with a real queue is a bigger change than one unit allows.

**Running It**

Hosted on Render (Path A): **https://fitfindr-anl0.onrender.com** (`GET /health`, `POST /ask`). Free Web Service, built from `main` with `pip install -r requirements-lock.txt`, started with `gunicorn serve:app --timeout 180`. Every setting, the environment it needs, and the one-command local equivalent are in [RUNNING.md](RUNNING.md) under *Capstone: how it is deployed, logged and tested*. I followed RUNNING.md from a fresh clone (new folder, new venv, `requirements-lock.txt`, gunicorn): it started, `/health` answered, and `/ask` wrote log records — about 124 MB resident, well inside the free tier's 512 MB.

**Instrumentation**

Every `/ask` request writes exactly one record — `requestlog.py::write()`, called from `serve.py::ask()` on every return path, including `400`s, `503`s and `500`s. One line of JSON per request, to `logs/requests.jsonl` and to stdout with a `REQUESTLOG ` prefix (Render's disk is wiped when the instance sleeps; its Logs tab keeps stdout). Fields: `ts`, `request_id`, `route`, `status`, `outcome` (`ok` / `no_results` / `model_unavailable` / `bad_input` / `crash`), `query` (what came in), `wardrobe_items`, `fault`, `selected_item`, `output` (the fit card that went out), `error`, `failed_stage`, `duration_ms`, `wait_ms` (time queued behind the one-at-a-time lock), `model_calls`, `prompt_tokens`, `output_tokens`, `transient_retries`, `rate_limit_retries`. The token counts come from Gemini's own `usage_metadata`; the retry counts are how many times the hardening layer had to step in.

The extract below was copied from Render's Logs tab for the deployed service on 16 Nov 2026 (05:46–05:48 UTC), same session it was produced, and is also saved as `results/capstone_m3_render_requestlog.jsonl`.

Eleven successful requests (the first one is the cold request after deploy — 20.7 s, against 5.3–14.2 s for the rest):

```json
{"ts": "2026-11-16T05:46:17.378Z", "request_id": "45a3082f", "route": "/ask", "status": 200, "outcome": "ok", "query": "vintage graphic tee under $30", "wardrobe_items": 10, "fault": "", "selected_item": "lst_002", "output": "Serving pure 2000s energy with this butterfly baby tee! 🦋✨ Grab it on Depop for just $18 before it’s gone. Style it with baggy dark denim, chunky sneakers, and a cropped hoodie for the ultimate retro streetwear fit. #Y2Kstyle #DepopFinds", "error": null, "failed_stage": null, "duration_ms": 20729, "wait_ms": 0, "model_calls": 2, "prompt_tokens": 294, "output_tokens": 122, "transient_retries": 0, "rate_limit_retries": 0}
{"ts": "2026-11-16T05:46:48.069Z", "request_id": "194a6e78", "route": "/ask", "status": 200, "outcome": "ok", "query": "vintage graphic tee under $30", "wardrobe_items": 10, "fault": "", "selected_item": "lst_002", "output": "Living in my Y2K era with this butterfly baby tee! 🦋 Throw it on with baggy denim, combat boots, and a vintage jacket for the ultimate effortless streetwear fit. Grab this beauty on Depop for just $18 before it’s gone!", "error": null, "failed_stage": null, "duration_ms": 5883, "wait_ms": 0, "model_calls": 2, "prompt_tokens": 300, "output_tokens": 116, "transient_retries": 0, "rate_limit_retries": 0}
{"ts": "2026-11-16T05:46:54.056Z", "request_id": "f7e62216", "route": "/ask", "status": 200, "outcome": "ok", "query": "y2k baby tee", "wardrobe_items": 10, "fault": "", "selected_item": "lst_002", "output": "Obsessed with this Y2K butterfly baby tee! 🦋 Pair it with baggy jeans, combat boots, and a vintage denim jacket for the ultimate nostalgic street fit. Grab it on Depop for just $18 before someone else does! ✨", "error": null, "failed_stage": null, "duration_ms": 5875, "wait_ms": 0, "model_calls": 2, "prompt_tokens": 293, "output_tokens": 106, "transient_retries": 0, "rate_limit_retries": 0}
{"ts": "2026-11-16T05:47:00.001Z", "request_id": "bf84fc8c", "route": "/ask", "status": 200, "outcome": "ok", "query": "cargo pants under $40", "wardrobe_items": 10, "fault": "", "selected_item": "lst_005", "output": "Obsessed with the texture on these rust corduroy wide-leg pants! 🤎 Style them with a fitted white tank, vintage black denim jacket, and chunky sneakers for the easiest everyday vintage fit. Grab them now on Depop for just $32!", "error": null, "failed_stage": null, "duration_ms": 7824, "wait_ms": 0, "model_calls": 2, "prompt_tokens": 298, "output_tokens": 113, "transient_retries": 0, "rate_limit_retries": 0}
{"ts": "2026-11-16T05:47:07.891Z", "request_id": "7e4a65ed", "route": "/ask", "status": 200, "outcome": "ok", "query": "denim jacket", "wardrobe_items": 10, "fault": "", "selected_item": "lst_004", "output": "Scored the ultimate 90s navy and white track jacket! ✨ Throw it over a ribbed tank and baggy jeans with chunky sneakers for that effortless streetwear fit. Grab this vintage gem for $45 on Poshmark before I change my mind! 🛍️", "error": null, "failed_stage": null, "duration_ms": 5491, "wait_ms": 0, "model_calls": 2, "prompt_tokens": 297, "output_tokens": 108, "transient_retries": 0, "rate_limit_retries": 0}
{"ts": "2026-11-16T05:47:13.514Z", "request_id": "6db124cb", "route": "/ask", "status": 200, "outcome": "ok", "query": "graphic tee", "wardrobe_items": 10, "fault": "", "selected_item": "lst_002", "output": "Obsessed with this Y2K butterfly baby tee! 🦋 Grab it on Depop for just $18. Style it with baggy denim, chunky sneakers, and a vintage jacket for the ultimate nostalgic fit. ✨", "error": null, "failed_stage": null, "duration_ms": 5285, "wait_ms": 0, "model_calls": 2, "prompt_tokens": 297, "output_tokens": 104, "transient_retries": 0, "rate_limit_retries": 0}
{"ts": "2026-11-16T05:47:27.726Z", "request_id": "c7562fbe", "route": "/ask", "status": 200, "outcome": "ok", "query": "vintage graphic tee under $30", "wardrobe_items": 10, "fault": "", "selected_item": "lst_002", "output": "Obsessed with this Y2K butterfly baby tee! 🦋 Grab it on Depop for just $18. Style it with baggy jeans, a cropped zip hoodie, and chunky sneakers for the ultimate retro street fit. Link in bio to shop!", "error": null, "failed_stage": null, "duration_ms": 5938, "wait_ms": 0, "model_calls": 2, "prompt_tokens": 294, "output_tokens": 108, "transient_retries": 0, "rate_limit_retries": 0}
{"ts": "2026-11-16T05:47:33.731Z", "request_id": "9ddfa97d", "route": "/ask", "status": 200, "outcome": "ok", "query": "y2k baby tee", "wardrobe_items": 10, "fault": "", "selected_item": "lst_002", "output": "Channeling peak 2000s energy with this butterfly baby tee! 🦋 Grab it on Depop for just $18. Style it with baggy jeans, chunky sneakers, and a zip hoodie for the ultimate nostalgic street fit. ✨", "error": null, "failed_stage": null, "duration_ms": 5302, "wait_ms": 0, "model_calls": 2, "prompt_tokens": 294, "output_tokens": 107, "transient_retries": 0, "rate_limit_retries": 0}
{"ts": "2026-11-16T05:47:39.213Z", "request_id": "3fa50b0d", "route": "/ask", "status": 200, "outcome": "ok", "query": "cargo pants under $40", "wardrobe_items": 10, "fault": "", "selected_item": "lst_005", "output": "Fall outfit formula secured! 🤎 Obsessed with these thrifted rust corduroy pants—the texture is everything. Just styled them with a basic tank, vintage denim jacket, and chunky sneaks for that easy streetwear look. Grab them on Depop for $32 before I change my mind!", "error": null, "failed_stage": null, "duration_ms": 14201, "wait_ms": 0, "model_calls": 2, "prompt_tokens": 297, "output_tokens": 120, "transient_retries": 0, "rate_limit_retries": 0}
{"ts": "2026-11-16T05:47:53.516Z", "request_id": "cbc2bd72", "route": "/ask", "status": 200, "outcome": "ok", "query": "denim jacket", "wardrobe_items": 10, "fault": "", "selected_item": "lst_004", "output": "Serving major 90s athletic energy with this navy and white stripe track jacket! ✨ Style it over a ribbed white tank, baggy dark wash jeans, and chunky sneakers for the ultimate retro streetwear fit. Grab this vintage find on Poshmark for just $45!", "error": null, "failed_stage": null, "duration_ms": 5538, "wait_ms": 0, "model_calls": 2, "prompt_tokens": 298, "output_tokens": 110, "transient_retries": 0, "rate_limit_retries": 0}
{"ts": "2026-11-16T05:47:59.172Z", "request_id": "019bfaec", "route": "/ask", "status": 200, "outcome": "ok", "query": "graphic tee", "wardrobe_items": 10, "fault": "", "selected_item": "lst_002", "output": "Obsessed with this butterfly baby tee! 🦋 Grab it on Depop for just $18 before I change my mind. Style it with baggy denim, combat boots, and a vintage jacket for the ultimate effortless Y2K streetwear fit. ✨", "error": null, "failed_stage": null, "duration_ms": 6652, "wait_ms": 0, "model_calls": 2, "prompt_tokens": 293, "output_tokens": 106, "transient_retries": 0, "rate_limit_retries": 0}
```

Two failures — a forced model timeout (`X-FitFindr-Fault: timeout`) and a rejected empty query:

```json
{"ts": "2026-11-16T05:48:05.932Z", "request_id": "b8ba1be0", "route": "/ask", "status": 503, "outcome": "model_unavailable", "query": "vintage graphic tee under $30", "wardrobe_items": 10, "fault": "timeout", "selected_item": "lst_002", "output": null, "error": "Model unavailable: Couldn't reach the model. Check your internet connection and try again.", "failed_stage": "suggest_outfit", "duration_ms": 6128, "wait_ms": 0, "model_calls": 2, "prompt_tokens": 0, "output_tokens": 0, "transient_retries": 1, "rate_limit_retries": 0}
{"ts": "2026-11-16T05:48:12.174Z", "request_id": "9b884fff", "route": "/ask", "status": 400, "outcome": "bad_input", "query": "", "wardrobe_items": null, "fault": "", "selected_item": null, "output": null, "error": "missing or empty 'query'", "failed_stage": null, "duration_ms": 0, "wait_ms": 0, "model_calls": 0, "prompt_tokens": 0, "output_tokens": 0, "transient_retries": 0, "rate_limit_retries": 0}
```

What the failed entries already show, before any testing: the timeout was caught, retried once (`transient_retries: 1`), and ended as a `503` with no fit card instead of a hang or a crash — but the message it ended with is the generic "Couldn't reach the model. Check your internet connection", not the timeout message, and it took 6.1 s for two calls with a 1 ms limit. Something in how the second attempt's exception is classified isn't what I expected. I've left it as found; criteria come first.

**What It Costs**

**Measured: about $0.00036 per run**, plus **~6.8 s** of wall-clock time.

*How I measured it:* 10 real `POST /ask` requests to the deployed service (five different queries, each twice, cache off with `AI201_CACHE=0`), sent from a browser on my machine between 05:46 and 05:48 UTC on 16 Nov 2026. Each response's `meta` block carries the token counts Gemini itself reported for that request (`usage_metadata`, summed by `generate.py` across the run's two model calls) — not an estimate from the prompt length. The raw numbers are in `results/capstone_m3_render_cost_runs.json`.

| | Average of 10 runs | Range |
|---|---|---|
| Model calls | 2 | 2–2 |
| Input (prompt) tokens | 296.1 | 293–300 |
| Output tokens | 109.8 | 104–120 |
| Server time (`duration_ms`) | 6,799 ms (median 5,879) | 5,285–14,201 ms |

At Gemini 3.5 Flash-Lite's paid rate ($0.30 per 1M input tokens, $2.50 per 1M output tokens):

```
input   296.1 tokens × $0.30 / 1,000,000 = $0.0000888
output  109.8 tokens × $2.50 / 1,000,000 = $0.0002745
                                 per run ≈ $0.000363
```

*A hundred people a day*, one search each: 100 × $0.000363 = **$0.036 a day**, about **$1.09 a month** (× 30). On what I actually run today it's $0: the course key is on Gemini's free tier and Render's free instance costs nothing. The real limit at that volume is the free tier's 15 requests a minute, not money: each run is 2 calls, so about 7 runs a minute before `generate.py` starts pacing, and a burst of people at once would queue behind the one-at-a-time lock.

**Run Log and Verdicts**

*Run Log — Before.* Three trials, run back to back against the deployed service (https://fitfindr-anl0.onrender.com) on 16 Nov 2026, 07:11–07:20 UTC, after `criteria.md` was committed (`e1a5db1`, 07:10 UTC). Nothing was changed between trials: all three ran on the same gunicorn worker (pid 59, booted 07:11:05 by the redeploy that the criteria commit triggered). Each trial was the same 24 requests, sent one at a time from the browser on my machine, in this order: 10 normal queries (criterion 5), 5 × `X-FitFindr-Fault: timeout` (criterion 1), one each of `timeout` / `server_error` / `empty` / `rate_limit` (criterion 2), and the 5 malformed bodies (criterion 4). Criterion 3 is scored over all 24. Every response is in `results/capstone_m5_before_trials.csv`; the server's own log for the window, copied from Render's Logs tab, is `results/capstone_m5_before_render_log.txt`.

| Criterion | Target | Run 1 | Run 2 | Run 3 | Verdict |
|---|---|---|---|---|---|
| 1. A stuck model fails within 25 s (503 + message) | 4 of 5 | 5/5 | 5/5 | 5/5 | MET |
| 2. Each failure names itself (all 4 fault types) | 4 of 4 | 3/4 | 3/4 | 3/4 | MISSED |
| 3. Every request has exactly one populated log record | 24 of 24 | 24/24 | 24/24 | 24/24 | MET |
| 4. Bad input → 400 with "send JSON with a `query`", no 500 | ≥3 of 5, 0 × 500 | 5/5, 0 | 5/5, 0 | 5/5, 0 | MET |
| 5. Warm requests finish under 10 s | 9 of 10 | 8/10 | 9/10 | 9/10 | MISSED |

*Real output, criterion by criterion.* All `REQUESTLOG` lines are written by `requestlog.py::write()`, called from `serve.py::ask()`; the messages inside them come from `generate.py` (named per criterion).

Criterion 1 — run 2, the first of the five forced timeouts (message from `generate.py::_explain`, set into the session by `agent.py::run_agent`). 503, 5,351 ms, one transient retry:

```json
REQUESTLOG {"ts": "2026-11-16T07:15:52.050Z", "request_id": "ac176ec5", "route": "/ask", "status": 503, "outcome": "model_unavailable", "query": "vintage graphic tee under $30", "wardrobe_items": 10, "fault": "timeout", "selected_item": "lst_002", "output": null, "error": "Model unavailable: Couldn't reach the model. Check your internet connection and try again.", "failed_stage": "suggest_outfit", "duration_ms": 5351, "wait_ms": 0, "model_calls": 2, "prompt_tokens": 0, "output_tokens": 0, "transient_retries": 1, "rate_limit_retries": 0}
```

All 15 forced-timeout requests (5 per run) came back 503 in 3,976–5,675 ms — comfortably inside 25 s.

Criterion 2 — run 3, one request per fault type. Three name their fault (`_explain_transient`, `_explain_empty`, and the retries-exhausted message at the end of `generate.py::generate`); the timeout does not — it says "Couldn't reach the model. Check your internet connection" (`_explain`), which contains neither "didn't answer" nor "timed out". Same result in all three runs:

```json
REQUESTLOG {"ts": "2026-11-16T07:19:20.757Z", "request_id": "c0c896a7", "route": "/ask", "status": 503, "outcome": "model_unavailable", "query": "vintage graphic tee under $30", "wardrobe_items": 10, "fault": "timeout", "selected_item": "lst_002", "output": null, "error": "Model unavailable: Couldn't reach the model. Check your internet connection and try again.", "failed_stage": "suggest_outfit", "duration_ms": 4232, "wait_ms": 0, "model_calls": 1, "prompt_tokens": 0, "output_tokens": 0, "transient_retries": 0, "rate_limit_retries": 0}
REQUESTLOG {"ts": "2026-11-16T07:19:25.052Z", "request_id": "5e3e188f", "route": "/ask", "status": 503, "outcome": "model_unavailable", "query": "vintage graphic tee under $30", "wardrobe_items": 10, "fault": "server_error", "selected_item": "lst_002", "output": null, "error": "Model unavailable: The model service is having trouble right now (503 UNAVAILABLE. The model is overloaded. Please try again later. [injected]; 2 tries). Nothing is wrong with your request — try again in a minute.", "failed_stage": "suggest_outfit", "duration_ms": 5033, "wait_ms": 0, "model_calls": 2, "prompt_tokens": 0, "output_tokens": 0, "transient_retries": 1, "rate_limit_retries": 0}
REQUESTLOG {"ts": "2026-11-16T07:19:30.146Z", "request_id": "ccb041dc", "route": "/ask", "status": 503, "outcome": "model_unavailable", "query": "vintage graphic tee under $30", "wardrobe_items": 10, "fault": "empty", "selected_item": "lst_002", "output": null, "error": "Model unavailable: The model sent back an empty reply. Try rewording the request, or try again in a minute.", "failed_stage": "suggest_outfit", "duration_ms": 4050, "wait_ms": 0, "model_calls": 1, "prompt_tokens": 0, "output_tokens": 0, "transient_retries": 0, "rate_limit_retries": 0}
REQUESTLOG {"ts": "2026-11-16T07:19:34.331Z", "request_id": "01062a03", "route": "/ask", "status": 503, "outcome": "model_unavailable", "query": "vintage graphic tee under $30", "wardrobe_items": 10, "fault": "rate_limit", "selected_item": "lst_002", "output": null, "error": "Model unavailable: The model is rate limited and still was after 5 attempts. Wait a minute and try again — nothing is wrong with your request.", "failed_stage": "suggest_outfit", "duration_ms": 28866, "wait_ms": 0, "model_calls": 5, "prompt_tokens": 0, "output_tokens": 0, "transient_retries": 0, "rate_limit_retries": 4}
```

Criterion 3 — matching the 72 `request_id`s the client received against the 72 `REQUESTLOG` records in the Render log (script run over the two files above):

```
records 72  unique 72  sent 72  missing set()  extra set()
records with status/outcome/duration_ms unpopulated: []
run 1: 24 / 24    run 2: 24 / 24    run 3: 24 / 24
```

Criterion 4 — run 1, all five malformed bodies (`serve.py::ask`, rejected before the agent runs). The `query` field shows what came in (`null` = absent or unparseable, `"42"` = the number, logged as text):

```json
REQUESTLOG {"ts": "2026-11-16T07:14:05.872Z", "request_id": "9c611298", "route": "/ask", "status": 400, "outcome": "bad_input", "query": null, "wardrobe_items": null, "fault": "", "selected_item": null, "output": null, "error": "missing or empty 'query'", "failed_stage": null, "duration_ms": 0, "wait_ms": 0, "model_calls": 0, "prompt_tokens": 0, "output_tokens": 0, "transient_retries": 0, "rate_limit_retries": 0}
REQUESTLOG {"ts": "2026-11-16T07:14:05.937Z", "request_id": "e054c1c7", "route": "/ask", "status": 400, "outcome": "bad_input", "query": "", "wardrobe_items": null, "fault": "", "selected_item": null, "output": null, "error": "missing or empty 'query'", "failed_stage": null, "duration_ms": 0, "wait_ms": 0, "model_calls": 0, "prompt_tokens": 0, "output_tokens": 0, "transient_retries": 0, "rate_limit_retries": 0}
REQUESTLOG {"ts": "2026-11-16T07:14:06.033Z", "request_id": "d1563ce1", "route": "/ask", "status": 400, "outcome": "bad_input", "query": "   ", "wardrobe_items": null, "fault": "", "selected_item": null, "output": null, "error": "missing or empty 'query'", "failed_stage": null, "duration_ms": 0, "wait_ms": 0, "model_calls": 0, "prompt_tokens": 0, "output_tokens": 0, "transient_retries": 0, "rate_limit_retries": 0}
REQUESTLOG {"ts": "2026-11-16T07:14:06.103Z", "request_id": "9318b87b", "route": "/ask", "status": 400, "outcome": "bad_input", "query": "42", "wardrobe_items": null, "fault": "", "selected_item": null, "output": null, "error": "missing or empty 'query'", "failed_stage": null, "duration_ms": 0, "wait_ms": 0, "model_calls": 0, "prompt_tokens": 0, "output_tokens": 0, "transient_retries": 0, "rate_limit_retries": 0}
REQUESTLOG {"ts": "2026-11-16T07:14:06.165Z", "request_id": "92af86c0", "route": "/ask", "status": 400, "outcome": "bad_input", "query": null, "wardrobe_items": null, "fault": "", "selected_item": null, "output": null, "error": "missing or empty 'query'", "failed_stage": null, "duration_ms": 0, "wait_ms": 0, "model_calls": 0, "prompt_tokens": 0, "output_tokens": 0, "transient_retries": 0, "rate_limit_retries": 0}
```

Criterion 5 — run 1's two slow requests, with the line the pacer in `generate.py::_wait_for_slot` printed between the two model calls of the second one (fit cards shortened here; full text in the log file):

```
REQUESTLOG {"ts": "2026-11-16T07:11:15.836Z", "request_id": "1354125f", "route": "/ask", "status": 200, "outcome": "ok", "query": "vintage graphic tee under $30", "wardrobe_items": 10, "fault": "", "selected_item": "lst_002", "output": "Living my best 2000s dream in this butterfly baby tee! 🦋 Gra…", "error": null, "failed_stage": null, "duration_ms": 17333, "wait_ms": 0, "model_calls": 2, "prompt_tokens": 284, "output_tokens": 94, "transient_retries": 0, "rate_limit_retries": 0}
  [rate limit] 15 requests used this minute. Waiting 20s. This is normal.
REQUESTLOG {"ts": "2026-11-16T07:12:06.592Z", "request_id": "d7f8d80e", "route": "/ask", "status": 200, "outcome": "ok", "query": "cargo pants under $40", "wardrobe_items": 10, "fault": "", "selected_item": "lst_005", "output": "Fall texture of my dreams! 🤎 These rust corduroy wide-legs a…", "error": null, "failed_stage": null, "duration_ms": 26462, "wait_ms": 0, "model_calls": 2, "prompt_tokens": 300, "output_tokens": 129, "transient_retries": 0, "rate_limit_retries": 0}
```

The 10 durations per run (ms) — run 1: 17,333 · 5,200 · 5,427 · 5,887 · 5,294 · 5,355 · 5,600 · **26,462** · 6,225 · 5,821; run 2: 6,396 · 5,373 · 5,514 · 7,401 · 6,645 · 5,940 · 6,069 · **21,256** · 6,430 · 6,759; run 3: 6,062 · 5,375 · 6,217 · 5,531 · 6,880 · 6,268 · 6,364 · **22,271** · 5,925 · 6,432.

*Verdicts and diagnoses.*

- **Criterion 1 — MET (5/5 every run), but for the wrong reason.** The forced timeout failed in about 4–6 s, while a stuck model really takes two 20 s attempts plus search, about 45 s. *Stage:* the `timeout` fault in `generate.py::_injected_fault`/`generate()`. *Mechanism:* the fault made a real call with a 1 ms limit, so the call died while **connecting**, before any request reached the model, so it never measured how long a stuck model takes. I'd tighten this criterion's test, not its target.
- **Criterion 2 — MISSED (3/4 every run).** *Stage:* same place. *Mechanism:* the connect-phase failure raised a connection error, not a timeout type, so `_is_timeout()` didn't recognise it. `_explain()` then matched the word "connection" and returned "Check your internet connection", which is wrong advice from a server. Evidence: only the first timeout after normal requests retried (`transient_retries: 1`, a pooled connection timing out on the read); every later one, which needed a fresh connection, got `transient_retries: 0`.
- **Criterion 5 — MISSED in run 1 (8/10; runs 2 and 3 were 9/10).** *Stage:* `generate.py::_wait_for_slot`, the 15-requests-per-minute pacer. *Mechanism:* each run makes 2 model calls, so the 8th request's second call is the 16th in a minute and waits for the window. The Render log shows "Waiting 20s / 15s / 16s" right inside requests 8 of each run. Run 1 also lost its first request (17.3 s): it arrived 10 s after the redeploy booted a fresh worker, a cold start my "warm" definition doesn't exclude.
- **Pattern:** criteria 1 and 2 are one problem with two symptoms: the timeout fault didn't behave like a stuck model. Criterion 5 is a separate one: free-tier quota pacing.

**The Improvement**

**What I changed** (commit `f87f74d`): the `timeout` fault now behaves like a stuck model. It waits the full per-call limit (20 s) and then raises the same read-timeout error the HTTP client raises, instead of a real call cut off after 1 ms. This follows the shared diagnosis of criteria 1 and 2. Tested locally: a stuck model now ends with "The model didn't answer within 20s (2 tries)" after about 42 s.

**After-run: not completed before the deadline.** The re-run (same 72 requests, `run_capstone_trials.py --label after`) was started at 23:49 PT and takes about 20 minutes because each stuck request now really waits. I submitted before it finished, so there is no after table yet. Expected from the local test, and to be confirmed: criterion 2 → MET (the message now says "didn't answer"), criterion 1 → MISSED (about 45 s against 25 s). If that holds, the fix trades a passing number for an honest one: criterion 1's earlier pass was an artifact of the test.

**What's Still Broken**

- **The after-run isn't recorded.** I ran out of time; the before results and the fix are committed, the measured after is not.
- **A stuck model takes ~45 s (criterion 1, expected miss).** The fix would be lowering `FITFINDR_MODEL_TIMEOUT` to about 10 s so two attempts plus search fit in 25 s. I didn't, because the unit allows one improvement.
- **Criterion 5 (pacer).** The 15/min free-tier limit makes every 8th back-to-back request wait 15–20 s. Fixing it means one model call per run instead of two (merging `suggest_outfit` and `create_fit_card`), which changes the prompts, out of scope this unit.
- **Real connection failures** still get "check your internet connection", with no retry. That message is wrong for a server.

**The one next thing:** connect real secondhand listings (e.g. eBay's API) in place of `data/listings.json`. It's the step that turns this from a demo into something people would actually use, and the hardening I built this unit is what makes it safe to put in front of them.

**How I Used AI**

- **Choosing the system and the shape.**
  - *What I asked for:* I wanted to take the four AI201 projects and combine them into one big project, and I asked Claude to help me pick which system would be most useful to other people and had the most potential as a portfolio piece or a product.
  - *What came back:* Claude pointed out that the assignment is to extend exactly one system. It compared the four on hosting limits (torch doesn't fit Render's 512 MB) and real-world usefulness, and recommended FitFindr with shape B.
  - *What I decided:* FitFindr, shape B, on Render (Path A). Connecting real marketplace listings is the "next thing", not this unit.
- **The build.**
  - *What I asked for:* Claude writes the code and documentation, and I stay in control of every git add, commit and push. I wouldn't let it delete files on my machine or copy my API key into its workspace.
  - *What came back:* Claude read the code and found four bad paths (no timeout, only rate limits retried, empty replies passing silently, exhausted retries crashing with a 500). It wrote the hardening layer in `generate.py`, the fault-injection switch, the structured log, the trial client, `run_capstone_trials.py` and `RUNNING.md`, and tested the failure paths from a clean clone with a dummy key.
  - *What I did:* I set up the Render service myself, entered the API key there, and copied the log lines out of Render's Logs tab. Claude ran the cost runs and the before-trials against my deployed URL through the browser on my machine.
- **The criteria.**
  - *What I asked for:* Options for my five criteria.
  - *What came back:* Claude declined to write them, since the instructions say not to, and instead asked me six questions about what I'd accept (how long a user could wait, what a failure message must say, how many missing log records are acceptable…), with the measured numbers I needed to answer.
  - *What I decided:* Every target is mine: 25 s and 4 of 5 for timeouts, 4 of 4 for messages, no missing log records, 3 of 5 for bad input, and 9 of 10 under 10 s for warm requests, with the reasons. When I asked again, Claude turned my answers into sentences, marking the bits I still had to decide, and I rewrote them in my own words.
- **The diagnosis and fix.** Claude diagnosed the misses from the logs and proposed three possible fixes; I chose the realistic stuck-model fault.
