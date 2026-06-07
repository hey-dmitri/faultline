---
name: faultline
description: >
  Generates sharp, non-obvious probing questions to pressure-test work on a specific
  early-stage operations function (strategy, GTM, research, product positioning, pricing
  and packaging, hiring and org design, forecasting, prioritization, or similar). Use this
  skill whenever the user says "run faultline," "faultline this," "generate probing
  questions for," "what should I be asking about [function]," "pressure-test my thinking
  on," "find the holes in," "stress-test this," or asks for the questions an experienced
  operator or investor would ask to expose the weak points in a plan, deck, model, or
  strategy. The skill works ONLY on context the user has provided (files, folders, uploads,
  tool-accessible docs, or substantive material stated in the conversation) and produces a
  ranked list of questions. It does NOT answer the questions. Routing them is the user's job.
---

# Faultline

Faultline finds where the work cracks under load. Given a specific function and a body of
context the user has provided, it generates the questions that would expose the weak points:
the unstated assumptions, the fragile consensus, the conspicuous gaps, the logic that breaks
under a competent attack. The output is a ranked list of questions and nothing else. The user
decides whether to ask them, whom to ask, and how to answer.

The whole value is that Faultline derives questions from the actual material, not from a
generic checklist. A canned question list goes stale and reads as generic. Faultline reads
what is in front of it, finds what is load-bearing, and aims questions at that.

## Hard rules

1. **Works only on provided context.** Never generate questions from thin air. If the context
   is thin or absent, do not invent a subject and do not produce generic function-level
   questions. Go to the gate (Step 3).
2. **Generates, never answers.** The skill stops at the question list. Do not answer the
   questions, do not offer to answer them, do not route them. That is the user's job, and
   keeping the skill question-only is what makes it composable with the user's other
   workflows.
3. **No padding.** Generate as many questions as the context genuinely warrants and no more.
   A soft ceiling of roughly eight to ten. If you are reaching to hit a number, the extra
   questions are failing the engine test and should be cut.

## The engine test

This is the core of the skill. Every question Faultline emits must pass all four. The test
also governs the moves themselves: if the context suggests a probing angle that is not in the
library below, derive it, and keep it only if it passes the test.

1. **Not retrievable.** The question cannot be answered by summary or lookup. It forces
   inference or judgment. "What are the competitors" fails. "What do the competitors who won
   understand that they did not believe at the start" passes.
2. **Adversarial stance.** The question assumes something is flawed, missing, or hidden, and
   goes hunting for it. A neutral question fails. A question with a knife in it passes.
3. **Decision-changing.** The answer, once known, would change a decision. Interesting-but-inert
   fails. This is the filter that most question generators skip, and it is the difference
   between a thinking tool and a trivia generator.
4. **Load-bearing.** The question targets something the function actually rests on, not a
   peripheral detail. Probing a footnote fails. Probing the central assumption passes.

## Workflow

### Step 1 — Identify the function

The user names what they are working on: strategy for a market, GTM for a segment, pricing for
a product, an org design, a forecast. If they name a task but not a clean function, infer the
function from the task. The function determines what counts as load-bearing, so this has to be
settled before anything else.

The functions are illustrative, not a fixed menu. If the user names something not listed,
treat it as a function and proceed. The engine generalizes.

### Step 2 — Locate the context

Faultline operates only on context the user has provided. Sources, in any combination:

- Files or folders already in the project
- Files uploaded to the conversation
- Documents the user points you to via available tools (Drive, Notion, and so on)
- Substantive material the user has stated directly in the conversation

Take inventory of what is actually available for the named function. Do this silently.

### Step 3 — Gate on sufficiency

Sufficient context means there is enough concrete material to identify the load-bearing claims
of the named function. A folder of strategy docs, a positioning deck, a financial model, a set
of customer-call notes: sufficient. A one-line description with no supporting material: thin.

If the context is thin or absent, **do not refuse and do not generate from thin air.** Instead,
tell the user three things and stop:

- What you currently have
- What is missing to probe this specific function well
- What they could add to close the gap (a deck, a model, call notes, competitor pages)

Then wait. The user will add material, point you to it, or state it. This is the only correct
behavior when context is thin. A bare refusal is a dead end. A refusal with a shopping list is
useful.

### Step 4 — Summarize the load-bearing claims and confirm

Before generating, prove you actually ingested the material and give the user a chance to
correct your read. Summarize the **load-bearing claims** the function rests on, drawn from the
user's own material, as specifically as the context allows. This is not an inventory of files.

- Useless: "I have four strategy docs and a model."
- Confirmable: "Your strategy rests on capturing RevOps buyers before they standardize on an
  incumbent. Your model assumes an eighteen-month payback. Your deck claims a wedge it does not
  define."

Then ask once, combined: **is this right, and is there anything to add?**

If the user adds material, re-summarize the augmented context **once**. On any further
additions after that, acknowledge them and proceed without re-summarizing, unless the user
explicitly asks for a fresh summary. Re-summarizing every loop spirals; one re-summary catches
the common case.

### Step 5 — Diagnose (internal, never shown)

Scan the confirmed context for the targets that questions will aim at:

- Claims asserted as settled fact on thin or absent evidence
- Load-bearing assumptions the function depends on
- Logical gaps and weak inferences
- Conspicuous omissions: what a sophisticated operator would expect to see here and does not
- Fragile consensus: the comfortable belief everyone is accidentally defending
- Untested dependencies, including dependence on a rejected alternative being wrong

**This pass is hidden.** Do not narrate it, do not surface it, do not label questions with the
diagnosis. It exists only to determine which moves are warranted and what each question
targets. The output is cleaner without it.

### Step 6 — Generate

For each diagnosed weak point, select the move or moves that fit and write the question. Fill
the move's variable slots with the specific subject from the context, never with placeholders.
A move runs only when the context gives it something real to bite on. Do not run a move because
it is in the library. Most runs will not use all eight moves, and that is correct.

Every generated question must pass the engine test. If it does not, cut it or rewrite it.

### Step 7 — Filter, rank, label, output

- **Filter.** Drop any question whose answer would not change a decision (engine test #3). This
  is the last guard against interesting-but-inert questions.
- **Rank.** Most load-bearing first. The sharpest, most central question sits at the top.
- **Label.** Tag each question with the move it uses, quietly, so the user can see coverage and
  spot over-reliance on one move. This is not the hidden diagnosis. It is just the move name.
- **Output and stop.** Emit the ranked, labeled list. Do not answer. Do not offer to answer. Do
  not summarize what the questions mean. The skill ends at the list.

## The move library

Eight moves. Each is a structure for converting a diagnosed weak point into a question that
passes the engine test. Apply only the ones the context warrants.

| Move | What it targets | Shape |
|---|---|---|
| **The unsaid** | Tacit knowledge that practitioners hold but never state, and that customers never say out loud | "What does every [winner in this space] understand about [X] that [they / the customer] would never put into words?" |
| **Load-bearing assumption + falsification** | The few beliefs the function rests on, and the conditions that would prove each false | "Name the [N] beliefs this rests on. For each, what is the cheapest test that would show it is false, and how fast?" |
| **Adversarial expert + evidence leash** | Weak points a hostile expert would attack, with answers bound to the provided material so the model cannot invent reassurance | "You are a [hostile expert]. Attack this using only the evidence in the provided context. Where does it break?" |
| **Steelman + residual break** | The crack that survives even the strongest version of the case | "Make the strongest version of [the case / the rejected alternative]. Where does the chosen path still break, or quietly depend on the rejected one being wrong?" |
| **Consensus made visible** | The comfortable belief the team is accidentally defending, stated plainly so its weakness shows. Include only when probing it is warranted, meaningful, and actionable | "State the version of [X] that everyone here assumes is true. Now: what is the case that it is wrong?" |
| **Omission probe** | The white space. What a sophisticated operator would expect to see and conspicuously does not | "What would a [seasoned operator] expect to find in this [plan / model / deck] that is missing, and what does its absence imply?" |
| **Second-order consequence** | The downstream cost of the thing being true, as opposed to whether it is true | "Assume this works exactly as intended. What does it break, strain, or foreclose downstream?" |
| **Inversion / pre-mortem** | Failure of the whole effort, narrated backward from the autopsy | "It is [timeframe] later and this failed completely. Using only failure modes realistic for this context, narrate what killed it." |

Reference-class questions (what the companies that failed at exactly this share, and which of
those traits the user shares) are deliberately not in the library. If a run feels like it is
missing outside-view thinking, that move can be added, but it is heavier and benched by default.

## Worked examples

These show the pattern: a diagnosed weak point becomes a slot-filled, labeled question. They
are illustrative. Faultline does not reuse them. It derives fresh questions from the actual
context every time.

**Example A. Function: pricing and packaging. Context: a SaaS pricing deck and usage data.**

Diagnosed weak point (hidden): pricing scales on seats, but the deck's own value story is about
automated workflows, not headcount. The value metric may be misaligned.

Output question, ranked first:
> **[Load-bearing assumption + falsification]** Your pricing assumes seat count tracks the
> value a customer gets. Name the customer segment for whom value is fully decoupled from
> seats, and tell me how many of those you already have on the books.

**Example B. Function: GTM. Context: a PLG motion doc targeting RevOps leads.**

Diagnosed weak point (hidden): the motion assumes a clean path from free signup to paid, but
never names the moment the buyer actually decides to pay.

Output question, ranked first:
> **[The unsaid]** What do the teams that already cracked this segment understand about the
> RevOps buyer's real trigger to pay, the thing that buyer would never write down in a survey?

Second question:
> **[Adversarial expert + evidence leash]** You are a RevOps lead who signed up, used the
> product, and never converted. Using only objections realistic for this segment, walk through
> the exact moment you decided it was not worth paying for.

## Anti-patterns

These are the failure modes that make the skill worthless. Watch for them.

- **Generating from thin context.** If the subject is vague, the questions come out generic in
  context-specific costume. The gate exists to prevent this. Use it.
- **Padding to a number.** Eight mediocre questions are worse than four sharp ones. The ceiling
  is a ceiling, not a target.
- **Retrieval questions in disguise.** "What are the three competitors" wearing a probing tone
  is still retrieval. Run the engine test.
- **Inert questions.** Clever, surprising, and decision-irrelevant. Filter them in Step 7.
- **Answering the questions.** The single most common scope violation. The skill ends at the
  list. The user routes from there.
- **Surfacing the diagnosis.** The diagnosis pass is internal. Showing it clutters the output
  and is not what the user asked for.
