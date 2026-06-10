# FAQ — Claude Chat

> 📖 Pairs with [Module 02](../guide/index.html#m2).

## "I hit a usage limit / Claude says come back later"
Usage limits exist on all plans and vary by plan and model; they reset over time.
What helps: shorter conversations (long chats consume more per message because the
whole history is re-read), starting fresh chats per task, and checking your plan's
current limits at https://support.claude.com. If you consistently hit limits doing
real work, that's the signal to consider a higher tier — not a bug.

## "My file won't upload / Claude can't read my file"
Check, in order: (1) file size and type — very large files and unusual formats can
fail; (2) scanned PDFs — a scan is an *image* of text, and may need OCR; try asking
Claude to read it anyway (it can often read images of text), or re-export the source
as a text PDF; (3) password-protected files won't open — remove protection first;
(4) spreadsheets with many tabs — tell Claude which tab matters.

## "Claude forgot what we discussed yesterday"
Separate chats are separate by default. Fixes by intent: ongoing body of work →
**Project** (knowledge + instructions persist); personal context that should follow
you around → **Memory** (Settings → check it's enabled, review what's stored);
one-off continuation → just link/paste the relevant part of the old chat.

## "The answer is confidently wrong"
This is hallucination — fluent, plausible, false. It happens most with: niche facts,
citations, current events, and arithmetic at a glance. Countermeasures: ask Claude to
search the web for anything current or factual; ask "how confident are you, and what
would you check?"; verify citations yourself, always (guide, Module 09).

## "It won't help with something I think is reasonable"
Occasionally Claude declines or hedges more than the situation warrants. Rephrasing
with context about your legitimate purpose often resolves it. The thumbs-down button
sends feedback to Anthropic — use it; it's read.

## "My Project's knowledge doesn't seem to be used"
Confirm you're chatting *inside* the Project (its name shows at the top). Very large
knowledge bases: be specific about which document matters ("using the style guide in
project knowledge…"). Instructions conflicting with your message? Your message wins —
check for contradictions.

## Escalate
Help center: https://support.claude.com → if unresolved, use its contact options.
Service status: https://status.claude.com
