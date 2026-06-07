# Faultline

A Claude skill that generates the questions worth asking about a piece of operations work, then gets out of the way.

You give it a function (strategy, GTM, pricing, positioning, org design, a forecast) and the actual material behind it. Faultline reads the material, finds what the work is resting on, and hands back a ranked list of probing questions aimed at the weak points. It does not answer them. Answering is your job.

## Why it exists

Most people use Claude like a faster search engine: summarize this, list that, explain the other. The leverage was never in the volume of information. It's in knowing which questions actually matter, the ones a sharp operator or a hostile investor would ask to find where the thing breaks. Faultline encodes that instinct and points it at your own work.

## What makes a question good

Every question Faultline emits has to pass four tests:

1. **Not retrievable.** You can't answer it by looking something up. It forces judgment.
2. **Adversarial.** It assumes something is flawed, missing, or hidden, and goes looking.
3. **Decision-changing.** The answer would change what you do. Interesting-but-useless gets cut.
4. **Load-bearing.** It targets what the work rests on, not a detail at the edge.

A question that fails any of these doesn't ship.

## The moves

Faultline works from a library of eight question structures and applies only the ones the material warrants. Most runs use a handful, not all eight.

- **The unsaid.** What every winner in the space understands and never says out loud.
- **Load-bearing assumption + falsification.** The beliefs the work rests on, and what would prove each one false.
- **Adversarial expert + evidence leash.** A hostile expert attacks, with answers bound to your own material so the model can't invent reassurance.
- **Steelman + residual break.** The strongest version of the case, then the crack that survives it.
- **Consensus made visible.** The comfortable belief everyone's quietly defending, stated plainly so its weakness shows.
- **Omission probe.** What a seasoned operator would expect to see here and conspicuously doesn't.
- **Second-order consequence.** What strains or breaks downstream if this works exactly as intended.
- **Inversion / pre-mortem.** It's a year later and the work failed completely. What killed it.

## How it works

1. You name the function and point Faultline at the material: files, a folder, uploads, docs it can reach, or context you've stated in the conversation.
2. It summarizes the load-bearing claims it found and asks you to confirm them or add more. If you haven't given it enough to work on, it tells you what's missing instead of guessing.
3. It generates a ranked list of questions, sharpest first, each labeled with the move behind it.
4. It stops. You decide what to ask, whom to ask, and how to answer.

Faultline works only on context you provide. It won't invent a subject or produce generic questions from nothing.

## Install

Faultline follows the [Agent Skills](https://agentskills.io) open standard. A skill is a folder with a `SKILL.md` inside it, so installing is mostly a matter of putting that folder where Claude looks for it.

**Claude Code**

Clone into your personal skills folder to make it available across every project:

```bash
git clone https://github.com/hey-dmitri/faultline.git ~/.claude/skills/faultline
```

Or drop it into a single project at `.claude/skills/faultline/`. Start Claude Code and type `/faultline`, or just describe what you want pressure-tested and Claude will load it when relevant. Reference: https://code.claude.com/docs/en/skills

**claude.ai**

Add the skill in your settings (skill availability depends on your plan). Reference: https://support.claude.com/en/articles/12512198-how-to-create-custom-skills

**Claude API**

Upload the skill bundle through the Skills API. Reference: https://platform.claude.com/docs/en/agents-and-tools/agent-skills/overview

## Usage

Once installed, trigger it in plain language:

> Run faultline on my Series A pricing model.

(Attach or point to the model and the pricing deck. Faultline will summarize what it found and ask you to confirm before generating.)

Or invoke it directly:

> /faultline

A run on a pricing deck might return, ranked first:

> **[Load-bearing assumption + falsification]** Your pricing assumes seat count tracks the value a customer gets. Name the segment for whom value is fully decoupled from seats, and tell me how many of those you already have on the books.

You take that question wherever it does the most damage: a customer call, a team debate, a model you go rebuild.

## Requirements

- A folder containing `SKILL.md` (this repo).
- Claude with Agent Skills support: Claude Code, claude.ai, or the Claude API.
- Real material to work on. Faultline is only as sharp as the context you feed it.

## A note on trust

This is a prompt-only skill. It bundles no scripts and makes no network calls. Read `SKILL.md` before you install it, the way you should with any skill you download from someone you don't know. Auditing skills from outside sources is standard practice, and this one is short enough to read in a few minutes.

## License

Released into the public domain under the [Unlicense](LICENSE). Use it, fork it, rewrite it, ship your own. No attribution required.
