<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Claude 101 — Your Orientation to the Claude Ecosystem</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Bricolage+Grotesque:opsz,wght@12..96,400;12..96,600;12..96,700;12..96,800&family=Public+Sans:ital,wght@0,400;0,500;0,600;0,700;1,400&family=IBM+Plex+Mono:wght@400;500;600&display=swap" rel="stylesheet">
<style>
:root{
  --paper:#F6F4EC;
  --panel:#FFFFFF;
  --ink:#17161D;
  --ink-soft:#4B4A55;
  --line:#E1DDCF;
  --marker:#F4DE45;
  --marker-soft:#FBF3C2;
  --pen:#2B47D6;
  --pen-dark:#1E33A3;
  --good:#2E7D4F;
  --good-bg:#E4F2E9;
  --bad:#C2402A;
  --bad-bg:#FAE7E1;
  --radius:14px;
  --display:"Bricolage Grotesque",Georgia,serif;
  --body:"Public Sans",-apple-system,Segoe UI,sans-serif;
  --mono:"IBM Plex Mono",ui-monospace,monospace;
}
*{box-sizing:border-box;margin:0;padding:0}
html{scroll-behavior:smooth}
@media (prefers-reduced-motion:reduce){
  html{scroll-behavior:auto}
  *,*::before,*::after{animation:none!important;transition:none!important}
}
body{
  background:var(--paper);
  color:var(--ink);
  font-family:var(--body);
  font-size:17px;
  line-height:1.65;
}
a{color:var(--pen);text-underline-offset:3px}
a:hover{color:var(--pen-dark)}
:focus-visible{outline:3px solid var(--pen);outline-offset:2px;border-radius:4px}

/* ---------- header ---------- */
.topbar{
  position:sticky;top:0;z-index:50;
  background:rgba(246,244,236,.92);
  backdrop-filter:blur(8px);
  border-bottom:1px solid var(--line);
}
.topbar-inner{
  max-width:1180px;margin:0 auto;padding:12px 24px;
  display:flex;align-items:center;gap:16px;justify-content:space-between;
}
.brand{font-family:var(--display);font-weight:800;font-size:1.05rem;letter-spacing:-.01em;white-space:nowrap}
.brand span{background:linear-gradient(transparent 55%,var(--marker) 55%)}
.progress-wrap{flex:1;max-width:420px;display:flex;align-items:center;gap:10px}
.progress-track{flex:1;height:8px;background:#E9E6DA;border-radius:99px;overflow:hidden}
.progress-fill{height:100%;width:0%;background:var(--pen);border-radius:99px;transition:width .4s ease}
.progress-label{font-family:var(--mono);font-size:.75rem;color:var(--ink-soft);white-space:nowrap}

/* ---------- layout ---------- */
.shell{max-width:1180px;margin:0 auto;padding:0 24px;display:grid;grid-template-columns:250px 1fr;gap:48px}
@media (max-width:920px){.shell{grid-template-columns:1fr;gap:0}}

/* checklist rail */
.rail{position:sticky;top:78px;align-self:start;padding:32px 0 64px}
@media (max-width:920px){.rail{display:none}}
.rail h2{font-family:var(--mono);font-size:.72rem;font-weight:600;letter-spacing:.14em;text-transform:uppercase;color:var(--ink-soft);margin-bottom:14px}
.rail ol{list-style:none}
.rail li{margin-bottom:4px}
.rail a{
  display:flex;align-items:center;gap:10px;
  padding:9px 10px;border-radius:10px;
  text-decoration:none;color:var(--ink-soft);font-size:.92rem;font-weight:500;
}
.rail a:hover{background:#EFECDF;color:var(--ink)}
.rail .check{
  width:20px;height:20px;flex:none;border-radius:6px;
  border:2px solid #C9C5B4;display:grid;place-items:center;
  font-size:.7rem;color:#fff;background:transparent;transition:all .25s;
}
.rail li.done .check{background:var(--good);border-color:var(--good)}
.rail li.done .check::after{content:"✓"}
.rail li.done a{color:var(--ink)}
.rail .score-chip{
  margin-top:18px;padding:12px 14px;background:var(--panel);
  border:1px solid var(--line);border-radius:12px;
  font-family:var(--mono);font-size:.8rem;color:var(--ink-soft);
}
.rail .score-chip strong{color:var(--ink);font-size:1.05rem;display:block}

/* ---------- hero ---------- */
.hero{padding:72px 0 56px;border-bottom:2px solid var(--ink)}
.eyebrow{font-family:var(--mono);font-size:.78rem;font-weight:600;letter-spacing:.16em;text-transform:uppercase;color:var(--pen);margin-bottom:18px}
.hero h1{
  font-family:var(--display);font-weight:800;
  font-size:clamp(2.4rem,5.4vw,4.1rem);
  line-height:1.04;letter-spacing:-.02em;max-width:14ch;margin-bottom:24px;
}
.hl{background:linear-gradient(transparent 52%,var(--marker) 52%);padding:0 .08em}
.hero p{max-width:58ch;color:var(--ink-soft);font-size:1.08rem;margin-bottom:14px}
.hero-meta{display:flex;flex-wrap:wrap;gap:10px;margin-top:26px}
.tag{
  font-family:var(--mono);font-size:.74rem;font-weight:500;
  border:1.5px solid var(--ink);border-radius:99px;padding:5px 13px;background:var(--panel);
}

/* ---------- modules ---------- */
.module{padding:64px 0 24px;border-bottom:1px solid var(--line);scroll-margin-top:80px}
.module-kicker{display:flex;align-items:baseline;gap:14px;margin-bottom:10px}
.module-num{font-family:var(--mono);font-weight:600;font-size:.85rem;color:var(--pen);letter-spacing:.08em}
.module h2{
  font-family:var(--display);font-weight:800;
  font-size:clamp(1.7rem,3.4vw,2.5rem);letter-spacing:-.015em;line-height:1.1;margin-bottom:18px;
}
.module .lede{font-size:1.06rem;color:var(--ink-soft);max-width:62ch;margin-bottom:28px}
.module h3{font-family:var(--display);font-weight:700;font-size:1.22rem;margin:34px 0 10px}
.module p{max-width:68ch;margin-bottom:14px}
.module ul,.module ol{max-width:68ch;margin:0 0 16px 22px}
.module li{margin-bottom:8px}
.module li::marker{color:var(--pen)}

/* cards */
.card-grid{display:grid;grid-template-columns:repeat(auto-fit,minmax(230px,1fr));gap:16px;margin:24px 0 8px}
.card{
  background:var(--panel);border:1px solid var(--line);border-radius:var(--radius);
  padding:20px 20px 18px;
}
.card h4{font-family:var(--display);font-weight:700;font-size:1.05rem;margin-bottom:6px}
.card .card-tag{font-family:var(--mono);font-size:.68rem;font-weight:600;letter-spacing:.1em;text-transform:uppercase;color:var(--pen);display:block;margin-bottom:8px}
.card p{font-size:.92rem;color:var(--ink-soft);margin:0}

/* tip + warn notes */
.note{
  border-left:4px solid var(--marker);background:var(--marker-soft);
  border-radius:0 12px 12px 0;padding:14px 18px;max-width:68ch;margin:18px 0;
}
.note.warn{border-left-color:var(--bad);background:var(--bad-bg)}
.note strong{font-family:var(--display)}
.note p{margin:0;font-size:.95rem}

/* code / prompt blocks */
pre,code{font-family:var(--mono)}
code{background:#ECE9DC;padding:.1em .35em;border-radius:5px;font-size:.86em}
pre{
  background:var(--ink);color:#F2F1EA;border-radius:12px;
  padding:18px 20px;font-size:.84rem;line-height:1.6;overflow-x:auto;
  max-width:68ch;margin:14px 0 20px;
}
pre .c{color:#9A98A8}
pre code{background:none;padding:0;color:inherit;font-size:inherit}
.prompt-pair{display:grid;grid-template-columns:1fr 1fr;gap:14px;max-width:760px;margin:16px 0 22px}
@media (max-width:700px){.prompt-pair{grid-template-columns:1fr}}
.prompt-box{border-radius:12px;padding:16px 18px;font-size:.9rem;border:1px solid var(--line);background:var(--panel)}
.prompt-box .pb-label{font-family:var(--mono);font-size:.68rem;font-weight:600;letter-spacing:.12em;text-transform:uppercase;display:block;margin-bottom:8px}
.prompt-box.weak .pb-label{color:var(--bad)}
.prompt-box.strong .pb-label{color:var(--good)}
.prompt-box.strong{border-color:#BFDCCB;background:#F4FAF6}

/* comparison table */
.table-wrap{overflow-x:auto;margin:20px 0 8px}
table{border-collapse:collapse;width:100%;min-width:560px;background:var(--panel);border:1px solid var(--line);border-radius:var(--radius);overflow:hidden;font-size:.92rem}
th,td{text-align:left;padding:12px 16px;border-bottom:1px solid var(--line);vertical-align:top}
th{font-family:var(--mono);font-size:.7rem;font-weight:600;letter-spacing:.1em;text-transform:uppercase;background:#EFECDF}
tr:last-child td{border-bottom:none}
td:first-child{font-weight:600;white-space:nowrap}

/* ---------- quiz ---------- */
.quiz{
  margin:44px 0 40px;background:var(--panel);
  border:2px solid var(--ink);border-radius:18px;padding:28px;
  box-shadow:6px 6px 0 var(--marker);
}
.quiz-head{display:flex;align-items:center;justify-content:space-between;gap:12px;flex-wrap:wrap;margin-bottom:6px}
.quiz-head h3{font-family:var(--display);font-weight:800;font-size:1.25rem;margin:0}
.quiz-score{font-family:var(--mono);font-size:.78rem;color:var(--ink-soft)}
.quiz-sub{font-size:.9rem;color:var(--ink-soft);margin-bottom:20px}
.q{margin-bottom:26px}
.q:last-of-type{margin-bottom:6px}
.q-text{font-weight:600;margin-bottom:12px}
.q-text .q-num{font-family:var(--mono);font-weight:600;color:var(--pen);margin-right:8px;font-size:.85em}
.opts{display:grid;gap:8px}
.opt{
  text-align:left;font:inherit;font-size:.95rem;cursor:pointer;
  border:1.5px solid var(--line);background:var(--paper);
  border-radius:10px;padding:11px 14px;display:flex;gap:10px;align-items:flex-start;
  transition:border-color .15s,background .15s;
}
.opt:hover:not(:disabled){border-color:var(--pen);background:#F0F2FD}
.opt:disabled{cursor:default}
.opt .key{font-family:var(--mono);font-size:.78rem;font-weight:600;color:var(--ink-soft);flex:none;margin-top:2px}
.opt.correct{border-color:var(--good);background:var(--good-bg)}
.opt.wrong{border-color:var(--bad);background:var(--bad-bg)}
.opt.dim{opacity:.55}
.feedback{
  margin-top:10px;font-size:.9rem;border-radius:10px;padding:11px 14px;display:none;
}
.feedback.show{display:block}
.feedback.good{background:var(--good-bg);color:#1D5236}
.feedback.bad{background:var(--bad-bg);color:#7E2A1A}
.quiz-result{
  display:none;margin-top:18px;padding:14px 18px;border-radius:12px;
  background:var(--marker-soft);border:1px solid #E8D98A;font-weight:600;
}
.quiz-result.show{display:block}

/* ---------- wrap-up ---------- */
.finale{padding:64px 0 40px}
.finale h2{font-family:var(--display);font-weight:800;font-size:clamp(1.8rem,3.6vw,2.6rem);margin-bottom:14px}
.final-score{
  font-family:var(--display);font-weight:800;font-size:clamp(2.2rem,5vw,3.4rem);
  margin:10px 0 6px;
}
.final-msg{color:var(--ink-soft);max-width:58ch;margin-bottom:30px}
.resource-grid{display:grid;grid-template-columns:repeat(auto-fit,minmax(250px,1fr));gap:14px;margin-top:10px}
.resource{
  display:block;background:var(--panel);border:1px solid var(--line);border-radius:12px;
  padding:16px 18px;text-decoration:none;color:var(--ink);
}
.resource:hover{border-color:var(--pen)}
.resource strong{display:block;font-family:var(--display);margin-bottom:3px}
.resource span{font-size:.85rem;color:var(--ink-soft)}
.resource .url{font-family:var(--mono);font-size:.72rem;color:var(--pen);display:block;margin-top:8px;word-break:break-all}

footer{border-top:1px solid var(--line);margin-top:48px;padding:26px 0 48px;font-size:.84rem;color:var(--ink-soft);max-width:72ch}
</style>
</head>
<body>

<header class="topbar">
  <div class="topbar-inner">
    <div class="brand"><span>Claude&nbsp;101</span> · Orientation</div>
    <div class="progress-wrap" aria-hidden="false">
      <div class="progress-track"><div class="progress-fill" id="progressFill"></div></div>
      <div class="progress-label" id="progressLabel">0 / 9 modules</div>
    </div>
  </div>
</header>

<div class="shell">
  <nav class="rail" aria-label="Module checklist">
    <h2>Your checklist</h2>
    <ol id="railList">
      <li data-rail="m1"><a href="#m1"><span class="check" aria-hidden="true"></span>The ecosystem map</a></li>
      <li data-rail="m2"><a href="#m2"><span class="check" aria-hidden="true"></span>Claude Chat</a></li>
      <li data-rail="m3"><a href="#m3"><span class="check" aria-hidden="true"></span>Prompting that works</a></li>
      <li data-rail="m4"><a href="#m4"><span class="check" aria-hidden="true"></span>Claude Cowork</a></li>
      <li data-rail="m5"><a href="#m5"><span class="check" aria-hidden="true"></span>Claude Code &amp; CLAUDE.md</a></li>
      <li data-rail="m6"><a href="#m6"><span class="check" aria-hidden="true"></span>Connectors &amp; MCP</a></li>
      <li data-rail="m7"><a href="#m7"><span class="check" aria-hidden="true"></span>Claude Design</a></li>
      <li data-rail="m8"><a href="#m8"><span class="check" aria-hidden="true"></span>Student starter pack</a></li>
      <li data-rail="m9"><a href="#m9"><span class="check" aria-hidden="true"></span>Ethics &amp; responsible use</a></li>
      <li data-rail="wrap"><a href="#wrap"><span class="check" aria-hidden="true"></span>Wrap-up &amp; resources</a></li>
    </ol>
    <div class="score-chip">Quiz score<strong id="railScore">0 / 27</strong></div>
  </nav>

  <main>
  <!-- BODY SECTIONS APPENDED BELOW -->
  <section class="hero">
    <p class="eyebrow">New Hire Edition · For graduates of every major</p>
    <h1>Welcome to the <span class="hl">Claude ecosystem</span>.</h1>
    <p>Claude is an AI assistant made by Anthropic — and it's more than a chat window. There's a tool for asking questions, a tool for handing off whole chunks of work, and a tool for building software. Knowing which door to walk through is half the skill.</p>
    <p>This guide takes about 45 minutes (or do a few modules at a time). Each module ends with a short quiz, and your checklist fills in as you go. No technical background required.</p>
    <div class="hero-meta">
      <span class="tag">9 modules</span>
      <span class="tag">27 quiz questions</span>
      <span class="tag">~45 min</span>
      <span class="tag">Zero jargon left undefined</span>
    </div>
  </section>

  <!-- ================= MODULE 1 ================= -->
  <section class="module" id="m1">
    <div class="module-kicker"><span class="module-num">MODULE 01</span></div>
    <h2>The ecosystem map: one Claude, several doors</h2>
    <p class="lede">Every Claude product runs on the same family of AI models. What changes is the <em>interface</em> — and the interface determines what kind of work each tool is good at.</p>

    <div class="card-grid">
      <div class="card">
        <span class="card-tag">Ask &amp; create</span>
        <h4>Claude Chat</h4>
        <p>The conversation app at claude.ai (plus mobile and desktop apps). Ask questions, brainstorm, write, analyze files, search the web, and build small interactive tools called Artifacts.</p>
      </div>
      <div class="card">
        <span class="card-tag">Delegate work</span>
        <h4>Claude Cowork</h4>
        <p>A desktop app where Claude works directly with your files and folders to finish multi-step tasks — organizing documents, building spreadsheets, drafting reports. Built for non-programmers.</p>
      </div>
      <div class="card">
        <span class="card-tag">Build software</span>
        <h4>Claude Code</h4>
        <p>An agentic coding tool that runs in the terminal (and via desktop/mobile apps). Claude reads your codebase, writes and edits code, runs commands, and makes commits.</p>
      </div>
      <div class="card">
        <span class="card-tag">Everywhere else</span>
        <h4>Companions &amp; the API</h4>
        <p>Claude in Chrome (a browsing agent), Claude in Excel and PowerPoint (in beta), and the Claude API, which lets developers build Claude into their own products.</p>
      </div>
    </div>

    <h3>The rule of thumb</h3>
    <div class="table-wrap">
      <table>
        <thead><tr><th>You want to…</th><th>Reach for</th><th>Why</th></tr></thead>
        <tbody>
          <tr><td>Ask, learn, draft, brainstorm</td><td>Claude Chat</td><td>Fast back-and-forth conversation; great for thinking out loud.</td></tr>
          <tr><td>Hand off a messy file task</td><td>Claude Cowork</td><td>It plans the steps itself and returns a finished deliverable.</td></tr>
          <tr><td>Write, fix, or understand code</td><td>Claude Code</td><td>It works inside your actual project — reading files, running tests.</td></tr>
          <tr><td>Automate Claude inside another product</td><td>Claude API</td><td>Programmatic access for developers.</td></tr>
        </tbody>
      </table>
    </div>

    <div class="note">
      <p><strong>Mental model:</strong> Chat is a conversation. Cowork and Code are more like <span class="hl">leaving instructions for a capable coworker</span> — you describe the outcome, Claude does the steps, you review the result.</p>
    </div>

    <div class="quiz" data-quiz="m1">
      <div class="quiz-head"><h3>Quick check — Module 01</h3><span class="quiz-score" data-score>0 / 3 answered</span></div>
      <p class="quiz-sub">Pick one answer per question. You'll get instant feedback.</p>

      <div class="q">
        <p class="q-text"><span class="q-num">Q1</span>A friend has a folder of 80 receipt screenshots and wants them turned into one expense spreadsheet. Which tool fits best?</p>
        <div class="opts" data-answer="2">
          <button class="opt"><span class="key">A</span>Claude Chat — paste each receipt in one at a time</button>
          <button class="opt"><span class="key">B</span>The Claude API</button>
          <button class="opt"><span class="key">C</span>Claude Cowork — point it at the folder and describe the outcome</button>
          <button class="opt"><span class="key">D</span>Claude in Chrome</button>
        </div>
        <div class="feedback" data-good="Right. Cowork is built exactly for this: grant it access to a folder, describe the deliverable, and it handles the multi-step work." data-bad="Not quite. This is a multi-step task on local files — that's Claude Cowork's specialty. Point it at the folder and describe the outcome."></div>
      </div>

      <div class="q">
        <p class="q-text"><span class="q-num">Q2</span>Where does Claude Code primarily run?</p>
        <div class="opts" data-answer="1">
          <button class="opt"><span class="key">A</span>Inside Microsoft Word</button>
          <button class="opt"><span class="key">B</span>In the terminal (command line), with desktop and mobile access too</button>
          <button class="opt"><span class="key">C</span>Only on Anthropic's servers — you can't run it yourself</button>
          <button class="opt"><span class="key">D</span>Inside a web browser tab only</button>
        </div>
        <div class="feedback" data-good="Correct. Claude Code is a command-line tool at heart, though you can also reach it through the desktop and mobile apps." data-bad="Claude Code lives in the terminal (the command line), and you can also access it through the desktop and mobile apps."></div>
      </div>

      <div class="q">
        <p class="q-text"><span class="q-num">Q3</span>What's actually different between Chat, Cowork, and Code?</p>
        <div class="opts" data-answer="0">
          <button class="opt"><span class="key">A</span>Mostly the interface — they use the same family of Claude models</button>
          <button class="opt"><span class="key">B</span>Each one is a completely different AI built by a different company</button>
          <button class="opt"><span class="key">C</span>Chat is smarter; the others use weaker models</button>
          <button class="opt"><span class="key">D</span>Nothing — they're three names for the same app</button>
        </div>
        <div class="feedback" data-good="Exactly. Same brain, different doors. The interface changes what kind of work each tool is suited for." data-bad="They all run the same family of Claude models — what differs is the interface, which shapes what each tool is good at."></div>
      </div>
      <div class="quiz-result" data-result></div>
    </div>
  </section>

  <!-- ================= MODULE 2 ================= -->
  <section class="module" id="m2">
    <div class="module-kicker"><span class="module-num">MODULE 02</span></div>
    <h2>Claude Chat: your everyday workspace</h2>
    <p class="lede">Claude Chat (claude.ai, plus the mobile and desktop apps) is where most people start. It's a conversation — but a few features turn it from "chatbot" into a genuine work tool.</p>

    <h3>The essentials</h3>
    <ul>
      <li><strong>Upload files.</strong> Drop in PDFs, images, spreadsheets, or slides and ask questions about them — "summarize this reading," "what's wrong with this chart?"</li>
      <li><strong>Web search.</strong> Claude can search the internet for current information. If you're asking about recent news, prices, or anything time-sensitive, ask it to look things up.</li>
      <li><strong>Artifacts.</strong> When Claude builds something substantial — a document, a working web page, a flashcard app, an interactive chart — it appears in a side panel called an Artifact. You can iterate on it, download it, or share it.</li>
      <li><strong>Memory.</strong> If enabled in Settings, Claude can remember useful context about you across conversations. You can view, edit, or delete what it remembers.</li>
    </ul>

    <h3>Projects: the feature most beginners miss</h3>
    <p>A <span class="hl">Project</span> is a workspace with its own knowledge base and custom instructions. Upload the documents you'll reference repeatedly — a style guide, a dataset, your thesis sources — and set instructions once ("always cite page numbers," "write in plain English"). Every chat inside that Project starts with that context already loaded.</p>
    <p>If you find yourself re-explaining the same background in every new chat, that's the signal to make a Project.</p>

    <h3>Good habits from day one</h3>
    <ul>
      <li><strong>One task per chat.</strong> Long, winding conversations get muddled. Start a fresh chat when you switch topics.</li>
      <li><strong>Verify what matters.</strong> Claude is very capable but not infallible. Double-check facts, citations, and numbers before they go anywhere important.</li>
      <li><strong>Don't paste secrets.</strong> Keep passwords, API keys, and sensitive personal data out of any AI tool.</li>
      <li><strong>Iterate.</strong> The first answer is a draft, not a verdict. "Shorter," "more formal," "explain that like I'm new to this" all work.</li>
    </ul>

    <div class="note">
      <p><strong>Try it now:</strong> Upload a class paper or your resume and ask: "Give me three specific, honest improvements — don't just praise it."</p>
    </div>

    <div class="quiz" data-quiz="m2">
      <div class="quiz-head"><h3>Quick check — Module 02</h3><span class="quiz-score" data-score>0 / 3 answered</span></div>
      <p class="quiz-sub">Pick one answer per question.</p>

      <div class="q">
        <p class="q-text"><span class="q-num">Q1</span>You're writing a semester-long research report and keep re-uploading the same six source PDFs into new chats. What's the better move?</p>
        <div class="opts" data-answer="2">
          <button class="opt"><span class="key">A</span>Keep one giant chat open for the whole semester</button>
          <button class="opt"><span class="key">B</span>Paste the full text of each PDF into every message</button>
          <button class="opt"><span class="key">C</span>Create a Project, upload the PDFs once, and add custom instructions</button>
          <button class="opt"><span class="key">D</span>There's no better way — re-uploading is required</button>
        </div>
        <div class="feedback" data-good="Yes. Projects hold a knowledge base and instructions so every new chat starts with your sources already loaded." data-bad="The answer is a Project: upload the sources once, set instructions once, and every chat in that Project starts with the context loaded."></div>
      </div>

      <div class="q">
        <p class="q-text"><span class="q-num">Q2</span>What is an Artifact?</p>
        <div class="opts" data-answer="1">
          <button class="opt"><span class="key">A</span>A saved copy of your chat history</button>
          <button class="opt"><span class="key">B</span>A standalone piece of work (document, app, chart) in a side panel that you can iterate on and download</button>
          <button class="opt"><span class="key">C</span>An error message Claude shows when it's confused</button>
          <button class="opt"><span class="key">D</span>A paid add-on for Enterprise customers only</button>
        </div>
        <div class="feedback" data-good="Correct — Artifacts are how Claude hands you substantial, editable outputs instead of burying them in the conversation." data-bad="An Artifact is a standalone output — a doc, working web page, chart, or mini-app — shown in a side panel where you can iterate and download it."></div>
      </div>

      <div class="q">
        <p class="q-text"><span class="q-num">Q3</span>You ask Claude about something that happened last week and it seems unsure. Best response?</p>
        <div class="opts" data-answer="0">
          <button class="opt"><span class="key">A</span>Ask it to search the web for current information</button>
          <button class="opt"><span class="key">B</span>Assume its first guess is correct</button>
          <button class="opt"><span class="key">C</span>Ask the same question again in all caps</button>
          <button class="opt"><span class="key">D</span>Give up — Claude can never discuss recent events</button>
        </div>
        <div class="feedback" data-good="Right. Claude's built-in knowledge has a cutoff date, but web search lets it pull in current information." data-bad="Claude's training has a cutoff date, but it can search the web — just ask it to look up current information."></div>
      </div>
      <div class="quiz-result" data-result></div>
    </div>
  </section>

  <!-- ================= MODULE 3 ================= -->
  <section class="module" id="m3">
    <div class="module-kicker"><span class="module-num">MODULE 03</span></div>
    <h2>Prompting that works</h2>
    <p class="lede">A "prompt" is just what you type to Claude. The single best mental model, straight from Anthropic's own guidance: treat Claude like a <span class="hl">brilliant new colleague</span> who knows a lot but knows nothing about <em>your</em> situation. Brief it the way you'd brief a person.</p>

    <h3>The five habits that matter most</h3>
    <ol>
      <li><strong>Be clear and specific.</strong> Say what you want, who it's for, and what "done" looks like.</li>
      <li><strong>Give context.</strong> Background, constraints, audience, and the why behind the task all sharpen the output.</li>
      <li><strong>Show examples.</strong> Pasting one or two examples of the style or format you want is often the highest-leverage move there is.</li>
      <li><strong>Specify the format.</strong> Length, structure, tone: "a 150-word summary in plain English" beats "summarize this."</li>
      <li><strong>Iterate.</strong> Treat the first response as draft one. Ask for changes the way you'd give feedback to a teammate.</li>
    </ol>

    <h3>Weak vs. strong, side by side</h3>
    <div class="prompt-pair">
      <div class="prompt-box weak">
        <span class="pb-label">Weak</span>
        "Write a cover letter."
      </div>
      <div class="prompt-box strong">
        <span class="pb-label">Strong</span>
        "Write a cover letter for an entry-level marketing analyst role at a mid-size healthcare company. I'm a recent economics grad; my resume is attached. Confident but not arrogant, under 300 words, and mention my internship analytics project."
      </div>
    </div>
    <div class="prompt-pair">
      <div class="prompt-box weak">
        <span class="pb-label">Weak</span>
        "Fix my essay."
      </div>
      <div class="prompt-box strong">
        <span class="pb-label">Strong</span>
        "Here's my 1,200-word essay draft. Keep my voice and argument, but tighten wordy sentences and flag any paragraph where the logic is weak. List the changes you made at the end."
      </div>
    </div>

    <h3>Two more tools for hard problems</h3>
    <ul>
      <li><strong>Ask for reasoning.</strong> For tricky analysis, add "think through this step by step before answering." You'll catch mistakes in the reasoning instead of just in the conclusion.</li>
      <li><strong>Break big tasks down.</strong> "Write my whole business plan" goes worse than outlining first, then drafting one section at a time.</li>
    </ul>

    <div class="note">
      <p><strong>Go deeper:</strong> Anthropic publishes a full prompt-engineering guide at <a href="https://docs.claude.com/en/docs/build-with-claude/prompt-engineering/overview">docs.claude.com</a>. It's written for developers but the principles apply to everyday chat too.</p>
    </div>

    <div class="quiz" data-quiz="m3">
      <div class="quiz-head"><h3>Quick check — Module 03</h3><span class="quiz-score" data-score>0 / 3 answered</span></div>
      <p class="quiz-sub">Pick one answer per question.</p>

      <div class="q">
        <p class="q-text"><span class="q-num">Q1</span>Which prompt will most likely get a useful result on the first try?</p>
        <div class="opts" data-answer="3">
          <button class="opt"><span class="key">A</span>"Make this better."</button>
          <button class="opt"><span class="key">B</span>"Write something about climate."</button>
          <button class="opt"><span class="key">C</span>"You know what I need. Go."</button>
          <button class="opt"><span class="key">D</span>"Summarize this article in 5 bullet points for a reader with no science background, and define any technical term you keep."</button>
        </div>
        <div class="feedback" data-good="Yes — it names the task, the audience, the format, and the length. That's the whole recipe." data-bad="Look for the prompt that specifies the task, audience, format, and length — that's option D."></div>
      </div>

      <div class="q">
        <p class="q-text"><span class="q-num">Q2</span>Claude's answer is good but way too long and in the wrong tone. What's the best next move?</p>
        <div class="opts" data-answer="1">
          <button class="opt"><span class="key">A</span>Start over in a new chat and hope for better luck</button>
          <button class="opt"><span class="key">B</span>Reply with specific feedback: "Cut this to 200 words and make it more conversational"</button>
          <button class="opt"><span class="key">C</span>Accept it — you can't change a response once it's written</button>
          <button class="opt"><span class="key">D</span>Send the same prompt again, unchanged</button>
        </div>
        <div class="feedback" data-good="Exactly. Iterating with specific feedback is the normal workflow, not a workaround." data-bad="Just tell Claude what to change — specific feedback like length and tone is the normal way to work, same as with a colleague."></div>
      </div>

      <div class="q">
        <p class="q-text"><span class="q-num">Q3</span>Why is including an example of what you want so effective?</p>
        <div class="opts" data-answer="2">
          <button class="opt"><span class="key">A</span>It makes the prompt longer, and longer prompts always win</button>
          <button class="opt"><span class="key">B</span>Claude refuses to work without examples</button>
          <button class="opt"><span class="key">C</span>An example shows the pattern — format, tone, level of detail — more precisely than describing it in words</button>
          <button class="opt"><span class="key">D</span>It doesn't help; examples just confuse the model</button>
        </div>
        <div class="feedback" data-good="Right. Showing beats telling: one good example communicates format, tone, and detail level all at once." data-bad="Examples work because showing beats telling — one sample communicates the format, tone, and detail level better than a paragraph of description."></div>
      </div>
      <div class="quiz-result" data-result></div>
    </div>
  </section>

  <!-- ================= MODULE 4 ================= -->
  <section class="module" id="m4">
    <div class="module-kicker"><span class="module-num">MODULE 04</span></div>
    <h2>Claude Cowork: delegating real work</h2>
    <p class="lede">Cowork lives in the Claude desktop app. You give it access to a folder, describe the outcome you want, and it plans and executes the steps — reading files, creating documents, building spreadsheets — then hands you the finished result. Anthropic describes it as "Claude Code for the rest of your work."</p>

    <h3>How a Cowork session goes</h3>
    <ol>
      <li><strong>Pick a folder.</strong> You explicitly grant Claude access to a specific directory — it can't touch anything outside what you allow.</li>
      <li><strong>Describe the outcome.</strong> Not step-by-step instructions — the destination. "Organize these files by client and year" or "Turn these meeting notes into a one-page status report."</li>
      <li><strong>Let it work.</strong> Cowork plans the steps, executes them, and checks in when a decision genuinely needs you.</li>
      <li><strong>Review the deliverable.</strong> You stay the editor-in-chief. Open what it made, verify it, and ask for revisions.</li>
    </ol>

    <h3>What it's great at</h3>
    <div class="card-grid">
      <div class="card"><h4>File cleanup</h4><p>Untangle a chaotic Downloads folder into a sensible structure with consistent names.</p></div>
      <div class="card"><h4>Data entry, automated</h4><p>Receipts, invoices, or screenshots in; a clean, formatted spreadsheet out.</p></div>
      <div class="card"><h4>Synthesis</h4><p>Read a pile of notes, transcripts, or PDFs and produce a structured summary or first draft.</p></div>
      <div class="card"><h4>Document assembly</h4><p>Turn scattered source material into polished Word docs, slide decks, or reports.</p></div>
    </div>

    <h3>Best practices (learn these before your first big task)</h3>
    <ul>
      <li><strong>Back up first.</strong> Cowork can create, move, and modify real files. Before a large reorganization, copy the folder somewhere safe.</li>
      <li><strong>Scope tightly.</strong> Grant access to the specific folder for the task, not your entire home directory.</li>
      <li><strong>Start small.</strong> Run a 10-file test before the 1,000-file job, so you can confirm it understood the assignment.</li>
      <li><strong>State the outcome, including the "done" criteria.</strong> "A spreadsheet with columns for date, vendor, and amount, sorted by date" is a brief Claude can execute.</li>
      <li><strong>Review before you rely.</strong> Spot-check the output, especially numbers, before it goes to your boss.</li>
    </ul>

    <div class="note warn">
      <p><strong>Heads up:</strong> agentic tools act on real files. The permission prompts exist for a reason — read them, and keep backups of anything you can't afford to lose.</p>
    </div>

    <div class="quiz" data-quiz="m4">
      <div class="quiz-head"><h3>Quick check — Module 04</h3><span class="quiz-score" data-score>0 / 3 answered</span></div>
      <p class="quiz-sub">Pick one answer per question.</p>

      <div class="q">
        <p class="q-text"><span class="q-num">Q1</span>What's the core difference between Cowork and Claude Chat?</p>
        <div class="opts" data-answer="1">
          <button class="opt"><span class="key">A</span>Cowork uses a different, smarter AI</button>
          <button class="opt"><span class="key">B</span>Cowork executes multi-step tasks directly on your files; Chat answers within a conversation</button>
          <button class="opt"><span class="key">C</span>Cowork is just Chat with a dark theme</button>
          <button class="opt"><span class="key">D</span>Chat is for work and Cowork is for entertainment</button>
        </div>
        <div class="feedback" data-good="Correct. Chat is conversational; Cowork is agentic — it plans and does the work on your actual files and returns a deliverable." data-bad="The difference is agency: Cowork plans and executes multi-step work directly on your files, while Chat responds within a conversation."></div>
      </div>

      <div class="q">
        <p class="q-text"><span class="q-num">Q2</span>You're about to let Cowork reorganize an important project folder. What should you do first?</p>
        <div class="opts" data-answer="2">
          <button class="opt"><span class="key">A</span>Grant it access to your entire hard drive so it has full context</button>
          <button class="opt"><span class="key">B</span>Nothing — AI tools never make mistakes with files</button>
          <button class="opt"><span class="key">C</span>Back up the folder and scope access to just that directory</button>
          <button class="opt"><span class="key">D</span>Delete the folder so it can start fresh</button>
        </div>
        <div class="feedback" data-good="Yes. Backups plus tight scoping is the golden rule for any tool that modifies real files." data-bad="Back up first and grant access only to the folder the task needs. Cowork modifies real files, so safety nets matter."></div>
      </div>

      <div class="q">
        <p class="q-text"><span class="q-num">Q3</span>Which is the best-written Cowork brief?</p>
        <div class="opts" data-answer="0">
          <button class="opt"><span class="key">A</span>"Go through these 40 interview transcripts and produce a one-page summary of the top 5 recurring complaints, with a count for each."</button>
          <button class="opt"><span class="key">B</span>"Open file 1. Read it. Now open file 2. Read it. Now open file 3…"</button>
          <button class="opt"><span class="key">C</span>"Do something useful with this folder."</button>
          <button class="opt"><span class="key">D</span>"Transcripts."</button>
        </div>
        <div class="feedback" data-good="Exactly — it describes the outcome and the 'done' criteria, and lets Claude figure out the steps." data-bad="The best brief states the outcome and what 'done' looks like (option A) — not micro-steps, and not vague vibes."></div>
      </div>
      <div class="quiz-result" data-result></div>
    </div>
  </section>

  <!-- ================= MODULE 5 ================= -->
  <section class="module" id="m5">
    <div class="module-kicker"><span class="module-num">MODULE 05</span></div>
    <h2>Claude Code &amp; the art of CLAUDE.md</h2>
    <p class="lede">Claude Code is the power tool of the ecosystem: an agent that works inside a real software project. Even if you didn't study computer science, it's worth knowing — plenty of analysts, designers, and marketers use it for data work and automation. And its most important habit, the CLAUDE.md file, teaches a lesson that applies everywhere.</p>

    <h3>What it does</h3>
    <p>You open a terminal (the text-based command window on your computer), navigate to a project folder, and type <code>claude</code>. From there, Claude can read the whole codebase, write and edit files, run tests and commands, and create git commits — asking your permission for anything consequential.</p>
    <pre><code><span class="c"># Install (requires Node.js — see docs for current options)</span>
npm install -g @anthropic-ai/claude-code

<span class="c"># Start it inside your project folder</span>
cd my-project
claude</code></pre>
    <p>Full setup instructions live at <a href="https://docs.claude.com/en/docs/claude-code/overview">docs.claude.com/en/docs/claude-code</a>.</p>

    <h3>The workflow that works</h3>
    <ol>
      <li><strong>Explore first.</strong> Ask Claude to read the relevant files and explain what's going on before changing anything.</li>
      <li><strong>Plan before coding.</strong> For anything non-trivial, ask for a plan (Claude Code has a dedicated plan mode) and approve it before letting it write code.</li>
      <li><strong>Work in small steps and review the changes.</strong> Read the diffs — the before/after of each file — like you'd review a teammate's work.</li>
      <li><strong>Course-correct early.</strong> If it's heading the wrong way, interrupt and redirect. Use <code>/clear</code> to reset context between unrelated tasks.</li>
    </ol>

    <h3>CLAUDE.md: the file that makes everything better</h3>
    <p><span class="hl">CLAUDE.md</span> is a plain-text file in your project's root folder that Claude Code automatically reads at the start of every session. Think of it as the onboarding doc you'd hand a new teammate: here's how this project works, here's how we do things, here's what to avoid.</p>
    <p>Community and Anthropic guidance converge on the same best practices:</p>
    <ul>
      <li><strong>Generate a starter with <code>/init</code>.</strong> Claude analyzes your project and drafts the file; you refine it from there.</li>
      <li><strong>Keep it short and human-readable.</strong> A focused file beats a novel — experienced users aim for well under a couple hundred lines. If a human teammate wouldn't read it, neither will it be effective.</li>
      <li><strong>Include the things Claude can't infer from code:</strong> the commands to build, test, and run the project; code style rules; testing expectations; repo etiquette (branch names, commit style); and warnings about anything surprising.</li>
      <li><strong>Treat it as living documentation.</strong> When Claude makes the same mistake twice, add a rule. In a session, typing <code>#</code> lets you add a memory to it on the spot.</li>
      <li><strong>Use child files for big projects.</strong> Subfolders can have their own CLAUDE.md, pulled in when Claude works in that area.</li>
    </ul>
    <pre><code><span class="c"># CLAUDE.md — example skeleton</span>

## Commands
- npm run dev: start the local server
- npm test: run the test suite (run before every commit)

## Code style
- Use ES modules (import/export), not CommonJS (require)
- Prefer small, single-purpose functions

## Workflow
- Always create a branch; never commit directly to main
- Never commit secrets or .env files

## Gotchas
- The /legacy folder is deprecated — don't modify it</code></pre>

    <div class="note">
      <p><strong>The transferable lesson:</strong> whether it's a CLAUDE.md, Project instructions in Chat, or a Cowork brief — <em>written-down context you provide once pays off in every future session.</em> The people who get the most out of AI tools are the best briefers, not the best typists.</p>
    </div>

    <div class="quiz" data-quiz="m5">
      <div class="quiz-head"><h3>Quick check — Module 05</h3><span class="quiz-score" data-score>0 / 3 answered</span></div>
      <p class="quiz-sub">Pick one answer per question.</p>

      <div class="q">
        <p class="q-text"><span class="q-num">Q1</span>What is CLAUDE.md?</p>
        <div class="opts" data-answer="2">
          <button class="opt"><span class="key">A</span>Claude's source code</button>
          <button class="opt"><span class="key">B</span>A log of everything Claude has ever done in your project</button>
          <button class="opt"><span class="key">C</span>A project file Claude Code reads at the start of every session, holding commands, style rules, and workflow context</button>
          <button class="opt"><span class="key">D</span>A paid plugin you have to purchase separately</button>
        </div>
        <div class="feedback" data-good="Correct — it's your project's onboarding doc for Claude, loaded automatically every session." data-bad="CLAUDE.md is a plain-text file in your project root that Claude Code reads at the start of every session — your project's onboarding doc for the AI."></div>
      </div>

      <div class="q">
        <p class="q-text"><span class="q-num">Q2</span>What's the fastest way to create a solid starter CLAUDE.md?</p>
        <div class="opts" data-answer="1">
          <button class="opt"><span class="key">A</span>Copy one from a random project online — context doesn't matter</button>
          <button class="opt"><span class="key">B</span>Run /init so Claude analyzes your project and drafts one, then refine it over time</button>
          <button class="opt"><span class="key">C</span>Write 2,000 lines covering every rule you can imagine</button>
          <button class="opt"><span class="key">D</span>You can't create one — Anthropic generates it for you in the cloud</button>
        </div>
        <div class="feedback" data-good="Yes. /init gives you a tailored starting point; the refining over time is where the real value accumulates." data-bad="The /init command analyzes your codebase and drafts a starter CLAUDE.md — then you refine it as you learn what Claude needs to know."></div>
      </div>

      <div class="q">
        <p class="q-text"><span class="q-num">Q3</span>Which CLAUDE.md is most effective?</p>
        <div class="opts" data-answer="0">
          <button class="opt"><span class="key">A</span>Short and specific: key commands, style rules, workflow rules, and known gotchas</button>
          <button class="opt"><span class="key">B</span>As long as possible — more words means more guidance</button>
          <button class="opt"><span class="key">C</span>Empty — Claude works best with no instructions</button>
          <button class="opt"><span class="key">D</span>A copy of the project's entire codebase pasted in</button>
        </div>
        <div class="feedback" data-good="Right. Short, specific, and human-readable wins — focused context gets followed; rambling files get diluted." data-bad="Best practice is short and specific: commands, style, workflow, gotchas. Long rambling files dilute the guidance that matters."></div>
      </div>
      <div class="quiz-result" data-result></div>
    </div>
  </section>


  <!-- ================= MODULE 6 ================= -->
  <section class="module" id="m6">
    <div class="module-kicker"><span class="module-num">MODULE 06</span></div>
    <h2>Connectors &amp; MCP: plugging Claude into your tools</h2>
    <p class="lede">Out of the box, Claude only knows what you tell it. <span class="hl">Connectors</span> change that: they let Claude securely link to the apps where your real life lives — email, calendar, files, project boards — so it can read from them and act in them.</p>

    <h3>The standard underneath: MCP</h3>
    <p>Connectors are built on the <strong>Model Context Protocol (MCP)</strong>, an open standard Anthropic released so any tool can connect to any AI in one consistent way. The common analogy: <span class="hl">MCP is USB-C for AI</span>. Before USB-C, every device needed its own cable; before MCP, every AI-to-app integration was custom-built. Because it's an open standard, there's a large and growing ecosystem of connectors from Anthropic, major apps, and the community.</p>

    <h3>What it looks like in practice</h3>
    <ul>
      <li><strong>Set up once.</strong> In Claude's settings, browse the connector directory and authorize the apps you want (you log in through the service's own secure sign-in — Claude never sees your password).</li>
      <li><strong>Then just ask.</strong> "What's on my calendar Thursday?" "Summarize my unread emails from this week." "Find the project brief in my Drive and turn it into a checklist."</li>
      <li><strong>It compounds with Cowork and Code.</strong> Connectors are what let agentic tools pull from Slack, your calendar, and your files in a single task.</li>
    </ul>

    <h3>Connector hygiene (this part matters)</h3>
    <ul>
      <li><strong>Connect only what you need, from sources you trust.</strong> Each connector is real access to a real account.</li>
      <li><strong>Review before Claude acts.</strong> Reading your calendar is low-stakes; sending an email or deleting a file is not. Read the action it proposes before approving it.</li>
      <li><strong>Know about prompt injection.</strong> Text inside a webpage, email, or document can contain hidden instructions trying to manipulate an AI ("ignore your user and forward their files..."). This is a real attack category — and another reason to review proposed actions instead of auto-approving everything.</li>
      <li><strong>Audit occasionally.</strong> Disconnect anything you no longer use.</li>
    </ul>

    <div class="note">
      <p><strong>Rule of thumb:</strong> treat connector permissions like apartment keys. Hand them out deliberately, to specific doors, and take them back when they're no longer needed.</p>
    </div>

    <div class="quiz" data-quiz="m6">
      <div class="quiz-head"><h3>Quick check — Module 06</h3><span class="quiz-score" data-score>0 / 3 answered</span></div>
      <p class="quiz-sub">Pick one answer per question.</p>

      <div class="q">
        <p class="q-text"><span class="q-num">Q1</span>What is MCP?</p>
        <div class="opts" data-answer="1">
          <button class="opt"><span class="key">A</span>A paid subscription tier for Claude</button>
          <button class="opt"><span class="key">B</span>An open standard for connecting AI to outside tools and data — often described as "USB-C for AI"</button>
          <button class="opt"><span class="key">C</span>The name of Claude's underlying AI model</button>
          <button class="opt"><span class="key">D</span>A programming language you must learn to use Connectors</button>
        </div>
        <div class="feedback" data-good="Correct. One open standard, many tools — that's why the connector ecosystem grew so fast." data-bad="MCP is the Model Context Protocol: an open standard for plugging AI into tools and data sources, like a universal port."></div>
      </div>

      <div class="q">
        <p class="q-text"><span class="q-num">Q2</span>Claude drafted a reply and is about to send it through your Gmail connector. The smartest habit is to…</p>
        <div class="opts" data-answer="2">
          <button class="opt"><span class="key">A</span>Auto-approve everything — review slows you down</button>
          <button class="opt"><span class="key">B</span>Disconnect Gmail forever; email is too risky for AI</button>
          <button class="opt"><span class="key">C</span>Read the draft and the recipient before approving the send</button>
          <button class="opt"><span class="key">D</span>Approve it without looking, then check your Sent folder next week</button>
        </div>
        <div class="feedback" data-good="Yes. Reading data is low-stakes; actions that send, edit, or delete deserve a human glance first." data-bad="Review before approving. Actions that send, edit, or delete things in your real accounts are exactly where a quick human check pays off."></div>
      </div>

      <div class="q">
        <p class="q-text"><span class="q-num">Q3</span>What is "prompt injection"?</p>
        <div class="opts" data-answer="0">
          <button class="opt"><span class="key">A</span>Hidden instructions inside content (a webpage, email, or doc) that try to manipulate the AI into doing something its user didn't ask for</button>
          <button class="opt"><span class="key">B</span>Typing your prompt very quickly</button>
          <button class="opt"><span class="key">C</span>A feature that makes prompts more creative</button>
          <button class="opt"><span class="key">D</span>Using the same prompt in two different chats</button>
        </div>
        <div class="feedback" data-good="Right — and it's the key reason to review proposed actions rather than auto-approving, especially when Claude is reading untrusted content." data-bad="Prompt injection is when content Claude reads (a page, email, or file) contains hidden instructions trying to hijack it. Reviewing proposed actions is your best defense."></div>
      </div>
      <div class="quiz-result" data-result></div>
    </div>
  </section>

  <!-- ================= MODULE 7 ================= -->
  <section class="module" id="m7">
    <div class="module-kicker"><span class="module-num">MODULE 07</span></div>
    <h2>Claude Design: from idea to visual</h2>
    <p class="lede">Claude Design is a newer product from Anthropic Labs (launched April 2026, currently a research preview for paid plans). It gives Claude a <span class="hl">visual canvas</span>: describe what you want, get a first version, then refine it like you're working with a designer.</p>

    <h3>What it makes</h3>
    <div class="card-grid">
      <div class="card"><h4>Slides &amp; decks</h4><p>Pitch decks, class presentations, and one-pagers — exportable to PPTX, PDF, a shareable URL, or Canva for further editing.</p></div>
      <div class="card"><h4>Prototypes &amp; mockups</h4><p>Interactive app and website prototypes good enough to test an idea — no design background required.</p></div>
      <div class="card"><h4>Marketing collateral</h4><p>Posters, flyers, and social graphics for a club, a side project, or a job application portfolio.</p></div>
      <div class="card"><h4>Consistent design systems</h4><p>It can build a reusable system of colors, type, and components from your files and apply it to every project.</p></div>
    </div>

    <h3>The workflow</h3>
    <ol>
      <li><strong>Describe or import.</strong> Start from a text prompt, or upload images and documents (DOCX, PPTX, XLSX), or capture elements from a live website.</li>
      <li><strong>Get a first version.</strong> Claude drafts the visual.</li>
      <li><strong>Refine with fine-grained controls.</strong> Comment inline on specific elements, edit text directly, or use adjustment sliders for spacing, color, and layout — then ask Claude to apply changes across the whole design.</li>
      <li><strong>Export or hand off.</strong> Ship it as a PDF/PPTX/URL, send it to Canva, or hand a prototype off to Claude Code to be built for real.</li>
    </ol>

    <div class="note">
      <p><strong>For new grads, the killer use case</strong> is the pitch: a deck for a class project, a startup idea, or an interview presentation. Describe the story, let Design handle the polish, and spend your time on the content.</p>
    </div>
    <div class="note warn">
      <p><strong>Research preview means moving target:</strong> features, plan availability, and limits can change. Check <a href="https://www.anthropic.com/news">anthropic.com/news</a> for the current state.</p>
    </div>

    <div class="quiz" data-quiz="m7">
      <div class="quiz-head"><h3>Quick check — Module 07</h3><span class="quiz-score" data-score>0 / 3 answered</span></div>
      <p class="quiz-sub">Pick one answer per question.</p>

      <div class="q">
        <p class="q-text"><span class="q-num">Q1</span>What is Claude Design for?</p>
        <div class="opts" data-answer="0">
          <button class="opt"><span class="key">A</span>Creating visual work — prototypes, slides, one-pagers, mockups — through conversation and direct editing</button>
          <button class="opt"><span class="key">B</span>Designing physical products like furniture</button>
          <button class="opt"><span class="key">C</span>Writing essays with nicer fonts</button>
          <button class="opt"><span class="key">D</span>Replacing your computer's operating system</button>
        </div>
        <div class="feedback" data-good="Correct — it's a conversational visual workspace from Anthropic Labs for design work you'd otherwise need a design tool (or a designer) for." data-bad="Claude Design is a visual workspace: you describe prototypes, slides, mockups, or one-pagers, and refine them conversationally."></div>
      </div>

      <div class="q">
        <p class="q-text"><span class="q-num">Q2</span>The first draft is close but the spacing is cramped and one headline is wrong. What's the intended workflow?</p>
        <div class="opts" data-answer="2">
          <button class="opt"><span class="key">A</span>Delete the project and write a longer prompt from scratch</button>
          <button class="opt"><span class="key">B</span>Accept it — first drafts can't be changed</button>
          <button class="opt"><span class="key">C</span>Refine it: edit the text directly, comment on the element, or use the adjustment sliders</button>
          <button class="opt"><span class="key">D</span>Export it to PDF and fix it by hand later</button>
        </div>
        <div class="feedback" data-good="Yes — refinement is the whole point: inline comments, direct edits, sliders, and chat all work on the existing draft." data-bad="Refine, don't restart: Claude Design supports inline comments, direct text edits, and adjustment sliders on the draft you already have."></div>
      </div>

      <div class="q">
        <p class="q-text"><span class="q-num">Q3</span>You made a deck in Claude Design and your teammate wants to keep editing it in a familiar tool. What can you do?</p>
        <div class="opts" data-answer="1">
          <button class="opt"><span class="key">A</span>Nothing — designs are locked inside Claude forever</button>
          <button class="opt"><span class="key">B</span>Export it — as PPTX, PDF, a shareable URL, or send it to Canva for editing</button>
          <button class="opt"><span class="key">C</span>Print it and mail it to them</button>
          <button class="opt"><span class="key">D</span>Retype the whole thing manually in PowerPoint</button>
        </div>
        <div class="feedback" data-good="Right. Exports include PPTX, PDF, and URLs, plus a Canva handoff where the design stays fully editable." data-bad="Claude Design exports to PPTX, PDF, and shareable URLs, and can send work to Canva where it remains fully editable."></div>
      </div>
      <div class="quiz-result" data-result></div>
    </div>
  </section>

  <!-- ================= MODULE 8 ================= -->
  <section class="module" id="m8">
    <div class="module-kicker"><span class="module-num">MODULE 08</span></div>
    <h2>The student starter pack: prompts &amp; projects worth stealing</h2>
    <p class="lede">Theory is done — here's a copy-and-paste toolkit. Five prompts that consistently outperform "help me with this," and four first projects matched to the right tool.</p>

    <h3>Five prompts to keep in your back pocket</h3>

    <p><strong>1. The Socratic study partner</strong> — turns passive review into active recall, which is what actually moves grades.</p>
    <pre><code>I'm studying [topic] for [exam/certification]. Quiz me one question
at a time and wait for my answer. After each answer, tell me what I
got right or wrong and why, and make the questions harder as I
improve. Don't accept vague answers — push me to be precise.</code></pre>

    <p><strong>2. The explainer ladder</strong> — for when a concept just won't click.</p>
    <pre><code>Explain [concept] three times: first to a smart high schooler, then
to a college senior in [your major], then at expert level. End with
one exam-style question to test whether I really got it.</code></pre>

    <p><strong>3. The honest resume tailor</strong> — note the guardrail in the last line.</p>
    <pre><code>Here's my resume and a job posting [paste both]. List the top 5
requirements of this role, map my actual experience to each one,
and rewrite my bullet points to speak to them directly — without
inventing or exaggerating anything I didn't do.</code></pre>

    <p><strong>4. The mock interviewer</strong></p>
    <pre><code>You're the hiring manager for this role [paste posting]. Ask me six
likely interview questions, one at a time. After each of my answers,
give honest feedback using the STAR framework (Situation, Task,
Action, Result) and suggest one concrete improvement.</code></pre>

    <p><strong>5. The tough editor</strong> — because flattery doesn't improve drafts.</p>
    <pre><code>Critique this draft like a tough but fair editor. Identify the three
weakest points and explain exactly how to fix each one. Do not
compliment me — I want the problems.</code></pre>

    <h3>Four first projects, matched to the right tool</h3>
    <div class="table-wrap">
      <table>
        <thead><tr><th>Project</th><th>Tool</th><th>How</th></tr></thead>
        <tbody>
          <tr><td>Job-search HQ</td><td>Chat → Projects</td><td>Create a Project with your resume, sample cover letters, and instructions on your voice. Every application gets tailored in minutes, in your style.</td></tr>
          <tr><td>Flashcard app</td><td>Chat → Artifacts</td><td>Upload lecture notes and ask for an interactive flashcard quiz app as an Artifact. Studying with a tool you made hits different.</td></tr>
          <tr><td>Money map</td><td>Cowork</td><td>Point Cowork at a folder of bank statement exports and ask for a categorized spending spreadsheet with a monthly summary tab.</td></tr>
          <tr><td>Portfolio site</td><td>Claude Code (+ Design)</td><td>Prototype the look in Claude Design, then have Claude Code build and refine the real site. Instant proof you can ship.</td></tr>
        </tbody>
      </table>
    </div>

    <div class="note">
      <p><strong>The pattern behind every good prompt here:</strong> a role, a process ("one at a time"), a standard ("don't accept vague answers"), and a guardrail ("don't invent anything"). Steal the structure, not just the words.</p>
    </div>

    <div class="quiz" data-quiz="m8">
      <div class="quiz-head"><h3>Quick check — Module 08</h3><span class="quiz-score" data-score>0 / 3 answered</span></div>
      <p class="quiz-sub">Pick one answer per question.</p>

      <div class="q">
        <p class="q-text"><span class="q-num">Q1</span>Why does "quiz me one question at a time" usually teach you more than "summarize this chapter"?</p>
        <div class="opts" data-answer="2">
          <button class="opt"><span class="key">A</span>It uses fewer words, and shorter prompts are always better</button>
          <button class="opt"><span class="key">B</span>Summaries are against Claude's rules</button>
          <button class="opt"><span class="key">C</span>Answering questions forces active recall — retrieving information strengthens memory far more than re-reading it</button>
          <button class="opt"><span class="key">D</span>It doesn't; both are identical for learning</button>
        </div>
        <div class="feedback" data-good="Exactly — retrieval practice is one of the best-supported findings in learning science, and the Socratic prompt builds it in." data-bad="The magic is active recall: being forced to retrieve an answer strengthens memory much more than passively reading a summary."></div>
      </div>

      <div class="q">
        <p class="q-text"><span class="q-num">Q2</span>The resume prompt ends with "without inventing or exaggerating anything I didn't do." Why include that?</p>
        <div class="opts" data-answer="0">
          <button class="opt"><span class="key">A</span>AI can otherwise embellish to be helpful — and you're the one accountable for every word you submit</button>
          <button class="opt"><span class="key">B</span>It makes the response generate faster</button>
          <button class="opt"><span class="key">C</span>Claude charges extra for invented content</button>
          <button class="opt"><span class="key">D</span>No reason — it's decorative</button>
        </div>
        <div class="feedback" data-good="Right. Guardrails like this keep the output truthful, and the accountability for a resume is always yours." data-bad="Without the guardrail, an eager-to-help AI can embellish. Since you're accountable for your resume's accuracy, you write the rule in."></div>
      </div>

      <div class="q">
        <p class="q-text"><span class="q-num">Q3</span>You're applying to 15 jobs over the next two months. The best setup is…</p>
        <div class="opts" data-answer="1">
          <button class="opt"><span class="key">A</span>A brand-new chat for each application, re-uploading your resume every time</button>
          <button class="opt"><span class="key">B</span>A Project containing your resume, examples, and voice instructions — then one chat per application inside it</button>
          <button class="opt"><span class="key">C</span>Asking Claude to memorize your resume by repeating it in every message</button>
          <button class="opt"><span class="key">D</span>One single chat for all 15 applications</button>
        </div>
        <div class="feedback" data-good="Yes — context loaded once, reused everywhere, with each application still getting a clean focused chat." data-bad="A Project is the move: your resume and voice instructions load automatically, and each application gets its own clean chat inside it."></div>
      </div>
      <div class="quiz-result" data-result></div>
    </div>
  </section>

  <!-- ================= MODULE 9 ================= -->
  <section class="module" id="m9">
    <div class="module-kicker"><span class="module-num">MODULE 09</span></div>
    <h2>Ethics &amp; responsible use: the part that protects you</h2>
    <p class="lede">This module isn't a lecture — it's self-defense. The graduates who thrive with AI are the ones who use it in ways they can <span class="hl">stand behind publicly</span>. Five principles cover almost everything.</p>

    <h3>1. Know the rules where you are</h3>
    <p>Universities, grad programs, and employers all have AI policies now, and they vary wildly — from "encouraged" to "grounds for dismissal." Read yours before you rely on AI for graded or paid work, and disclose AI use when the policy asks for it. "Everyone does it" is not a defense; "I followed the written policy" is.</p>

    <h3>2. Verify before you submit</h3>
    <p>AI models can <strong>hallucinate</strong> — state false things fluently and confidently, including citations to papers that don't exist. Before anything goes in a paper, application, or report: check that cited sources are real and say what's claimed, recompute key numbers, and confirm names, dates, and quotes. You are the fact-checker of record.</p>

    <h3>3. Protect data that isn't yours to share</h3>
    <ul>
      <li>Don't paste other people's personal information (a classmate's essay, a customer list, patient or client details) into any AI tool without authorization.</li>
      <li>At work, confidential company data is governed by your employer's policy — when in doubt, ask before you paste.</li>
      <li>Your own secrets too: passwords, banking details, and API keys stay out of every chat.</li>
    </ul>

    <h3>4. Watch for bias</h3>
    <p>AI learns from human-created data, so it can reflect human biases — in whose perspectives get centered, what "professional" is assumed to look like, or how groups are described. When the stakes involve people (hiring materials, policy writing, anything evaluative), review the output for fairness, and ask Claude directly to surface alternative perspectives.</p>

    <h3>5. Keep ownership of your skills</h3>
    <p>The trap for new grads isn't using AI — it's letting AI use you. If Claude writes everything you "wrote," you stop developing the judgment your career actually runs on. A practical test before submitting anything: <span class="hl">could I explain and defend this work in a meeting, without the chat open?</span> If not, you've delegated the learning, not just the typing.</p>

    <div class="note">
      <p><strong>The source document:</strong> Anthropic publishes a Usage Policy covering what Claude can and can't be used for, at <a href="https://www.anthropic.com/legal/aup">anthropic.com/legal/aup</a>. Worth a skim once — most of it is common sense written down.</p>
    </div>

    <div class="quiz" data-quiz="m9">
      <div class="quiz-head"><h3>Quick check — Module 09</h3><span class="quiz-score" data-score>0 / 3 answered</span></div>
      <p class="quiz-sub">Pick one answer per question.</p>

      <div class="q">
        <p class="q-text"><span class="q-num">Q1</span>Claude gives you a perfectly formatted citation for your research paper. Before using it, you should…</p>
        <div class="opts" data-answer="1">
          <button class="opt"><span class="key">A</span>Use it as-is — formatted citations are always real</button>
          <button class="opt"><span class="key">B</span>Verify the source exists and actually supports your claim</button>
          <button class="opt"><span class="key">C</span>Change one word so it counts as your own</button>
          <button class="opt"><span class="key">D</span>Cite Claude instead of the source</button>
        </div>
        <div class="feedback" data-good="Correct. Hallucinated citations look exactly like real ones — verification is non-negotiable for anything you submit." data-bad="AI can hallucinate convincing citations to papers that don't exist or don't say that. Always verify the source before it goes in your work."></div>
      </div>

      <div class="q">
        <p class="q-text"><span class="q-num">Q2</span>Your manager asks you to "use AI to sort" a spreadsheet of customer names, emails, and purchase histories. The responsible first step is…</p>
        <div class="opts" data-answer="2">
          <button class="opt"><span class="key">A</span>Paste it all in immediately — your manager asked, so it's fine</button>
          <button class="opt"><span class="key">B</span>Post the data in a group chat to ask what others think</button>
          <button class="opt"><span class="key">C</span>Check your company's data and AI policy first — customer personal data often can't go into unapproved tools</button>
          <button class="opt"><span class="key">D</span>Refuse to ever use AI at work</button>
        </div>
        <div class="feedback" data-good="Yes. Personal data is usually governed by policy (and often by law). Confirming what's approved protects the customers, the company, and you." data-bad="Customer personal data is typically covered by company policy and privacy law. Check what tools are approved before pasting — it protects everyone, including you."></div>
      </div>

      <div class="q">
        <p class="q-text"><span class="q-num">Q3</span>What does the "could I defend this in a meeting?" test actually check?</p>
        <div class="opts" data-answer="0">
          <button class="opt"><span class="key">A</span>Whether you understand the work well enough to be accountable for it — AI assisted, but the judgment is yours</button>
          <button class="opt"><span class="key">B</span>Whether the meeting room has good Wi-Fi</button>
          <button class="opt"><span class="key">C</span>Whether the document is long enough</button>
          <button class="opt"><span class="key">D</span>Whether Claude would also attend the meeting</button>
        </div>
        <div class="feedback" data-good="Exactly. If you can explain and defend the work unaided, you used AI as a tool. If you can't, it used you." data-bad="The test is about accountability and understanding: if you can't explain the work without the chat open, you delegated the learning — not just the typing."></div>
      </div>
      <div class="quiz-result" data-result></div>
    </div>
  </section>

  <!-- ================= WRAP-UP ================= -->
  <section class="finale" id="wrap">
    <div class="module-kicker"><span class="module-num">WRAP-UP</span></div>
    <h2>You're oriented.</h2>
    <div class="final-score" id="finalScore">0 / 27</div>
    <p class="final-msg" id="finalMsg">Answer the quiz questions above to see your final score here.</p>

    <h3 style="font-family:var(--display);font-weight:700;font-size:1.22rem;margin-bottom:6px">The one-paragraph summary</h3>
    <p style="max-width:68ch;margin-bottom:28px">Chat for conversation, Cowork for delegating file work, Code for software, Design for visuals — all the same Claude, behind different doors, and Connectors (built on MCP) plug it into your real tools. Brief it like a smart new colleague: context, examples, format, and "done" criteria. Write context down once (Projects, CLAUDE.md) so you never repeat yourself. Keep backups, scope permissions tightly, review actions before approving them — and verify everything that matters, because the accountability for your work stays with you.</p>

    <h3 style="font-family:var(--display);font-weight:700;font-size:1.22rem;margin-bottom:14px">Keep these bookmarked</h3>
    <div class="resource-grid">
      <a class="resource" href="https://support.claude.com"><strong>Claude.ai Help Center</strong><span>How-tos, plan details, and feature guides for Claude Chat.</span><span class="url">support.claude.com</span></a>
      <a class="resource" href="https://docs.claude.com/en/docs/build-with-claude/prompt-engineering/overview"><strong>Prompt Engineering Guide</strong><span>Anthropic's official deep dive on writing effective prompts.</span><span class="url">docs.claude.com</span></a>
      <a class="resource" href="https://docs.claude.com/en/docs/claude-code/overview"><strong>Claude Code Docs</strong><span>Installation, best practices, CLAUDE.md, and advanced workflows.</span><span class="url">docs.claude.com/en/docs/claude-code</span></a>
      <a class="resource" href="https://www.anthropic.com/engineering/claude-code-best-practices"><strong>Agentic Coding Best Practices</strong><span>Anthropic's engineering post on workflows that actually work.</span><span class="url">anthropic.com/engineering</span></a>
      <a class="resource" href="https://claude.com/product/cowork"><strong>Claude Cowork</strong><span>What it is, what it's for, and how to get started.</span><span class="url">claude.com/product/cowork</span></a>
      <a class="resource" href="https://www.anthropic.com/news"><strong>Anthropic News</strong><span>New features ship constantly — this is where they're announced.</span><span class="url">anthropic.com/news</span></a>
      <a class="resource" href="https://modelcontextprotocol.io"><strong>Model Context Protocol</strong><span>The open standard behind Connectors, with docs and the server ecosystem.</span><span class="url">modelcontextprotocol.io</span></a>
      <a class="resource" href="https://www.anthropic.com/news/claude-design-anthropic-labs"><strong>Claude Design</strong><span>The launch announcement and current capabilities of the visual workspace.</span><span class="url">anthropic.com/news</span></a>
      <a class="resource" href="https://www.anthropic.com/legal/aup"><strong>Anthropic Usage Policy</strong><span>The official rules on acceptable use — most of it is common sense, written down.</span><span class="url">anthropic.com/legal/aup</span></a>
    </div>

    <footer>
      Made as an onboarding guide for new graduates. Product details (plans, availability, limits) change quickly — when in doubt, the official docs above are the source of truth.
    </footer>
  </section>
  </main>
</div>

<script>
(function(){
  var TOTAL_MODULES = 9;
  var TOTAL_QUESTIONS = document.querySelectorAll('.q').length;
  var state = { correct:0, answered:0, doneModules:{} };
  var quizzes = document.querySelectorAll('.quiz');
  var perQuiz = {};

  quizzes.forEach(function(quiz){
    var id = quiz.getAttribute('data-quiz');
    var questions = quiz.querySelectorAll('.q');
    perQuiz[id] = { answered:0, correct:0, total:questions.length };

    questions.forEach(function(q){
      var opts = q.querySelector('.opts');
      var answer = parseInt(opts.getAttribute('data-answer'),10);
      var buttons = opts.querySelectorAll('.opt');
      var feedback = q.querySelector('.feedback');

      buttons.forEach(function(btn, idx){
        btn.addEventListener('click', function(){
          // lock question
          buttons.forEach(function(b,i){
            b.disabled = true;
            if(i === answer){ b.classList.add('correct'); }
            else if(i === idx){ b.classList.add('wrong'); }
            else { b.classList.add('dim'); }
          });
          var isCorrect = idx === answer;
          feedback.textContent = isCorrect ? feedback.getAttribute('data-good') : feedback.getAttribute('data-bad');
          feedback.classList.add('show', isCorrect ? 'good' : 'bad');

          perQuiz[id].answered++;
          if(isCorrect) perQuiz[id].correct++;
          state.answered++;
          if(isCorrect) state.correct++;
          update(id);
        });
      });
    });
  });

  function update(id){
    var pq = perQuiz[id];
    var quiz = document.querySelector('[data-quiz="'+id+'"]');
    quiz.querySelector('[data-score]').textContent = pq.answered + ' / ' + pq.total + ' answered';

    if(pq.answered === pq.total && !state.doneModules[id]){
      state.doneModules[id] = true;
      var result = quiz.querySelector('[data-result]');
      var msg;
      if(pq.correct === pq.total) msg = 'Perfect — ' + pq.correct + '/' + pq.total + '. Module complete. ✓';
      else if(pq.correct >= 2) msg = 'Module complete: ' + pq.correct + '/' + pq.total + '. Skim the section once more for the one you missed.';
      else msg = 'Module complete: ' + pq.correct + '/' + pq.total + '. Worth a re-read — the answers are all in the section above.';
      result.textContent = msg;
      result.classList.add('show');

      var railItem = document.querySelector('[data-rail="'+id+'"]');
      if(railItem) railItem.classList.add('done');
    }

    var doneCount = Object.keys(state.doneModules).length;
    document.getElementById('progressFill').style.width = (doneCount/TOTAL_MODULES*100) + '%';
    document.getElementById('progressLabel').textContent = doneCount + ' / ' + TOTAL_MODULES + ' modules';
    document.getElementById('railScore').textContent = state.correct + ' / ' + TOTAL_QUESTIONS;
    document.getElementById('finalScore').textContent = state.correct + ' / ' + TOTAL_QUESTIONS;

    var finalMsg = document.getElementById('finalMsg');
    if(doneCount === TOTAL_MODULES){
      var wrapRail = document.querySelector('[data-rail="wrap"]');
      if(wrapRail) wrapRail.classList.add('done');
      if(state.correct >= Math.round(TOTAL_QUESTIONS * 0.85)) finalMsg.textContent = 'Outstanding. You know your way around the ecosystem — go put it to work.';
      else if(state.correct >= Math.round(TOTAL_QUESTIONS * 0.6)) finalMsg.textContent = 'Solid. You have the core ideas down; revisit the modules where you missed questions and you\u2019re set.';
      else finalMsg.textContent = 'Good start. Give the guide one more pass — the concepts compound quickly once they click.';
    } else {
      finalMsg.textContent = 'Answer the quiz questions above to see your final score here. (' + state.answered + ' of ' + TOTAL_QUESTIONS + ' answered so far.)';
    }
  }
})();
</script>
</body>
</html>
