# Prompts: Research & Sources

> 📖 Pairs with [Module 03](../guide/index.html#m3) (web search, file uploads) and
> [Module 10](../guide/index.html#m10) (verification).
>
> ⚠️ **The iron rule of AI-assisted research:** verify every citation before it enters
> your work. AI can hallucinate sources that look perfectly real.

## The source summarizer
*Attach the PDF or paste the link.*

```text
Summarize this paper for someone outside the field: (1) the question it asks,
(2) the method in one plain-English paragraph, (3) the main finding,
(4) stated limitations. Quote the paper's own words only for the main finding,
and give me the page number.
```

## The literature mapper

```text
I'm starting research on [topic]. Search the web for recent, credible
sources and map the landscape: the main schools of thought, the key open
questions, and where the disagreements are. Cite each source with enough
detail that I can find and verify it myself.
```

## The counter-argument finder

```text
Here's my thesis: [thesis]. Make the strongest honest case against it — the
version a smart, informed critic would make, not a strawman. Then list what
evidence would help me respond to each point.
```

## The methods sanity check

```text
Here's my plan for [survey/experiment/analysis]: [plan]. Identify weaknesses
a reviewer would flag: sampling problems, confounds, missing controls,
overclaiming. Rank them by how much they threaten my conclusions.
```

## The citation verifier
*Run this on Claude's own earlier output. Yes, really.*

```text
Earlier you gave me these citations: [paste]. For each one, search the web
to confirm: does this source exist, and does it actually support the claim
I'm attaching it to? Flag anything you can't confirm as UNVERIFIED.
```
