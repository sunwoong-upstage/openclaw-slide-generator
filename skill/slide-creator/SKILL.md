---
name: slide-creator
description: Create polished HTML-based presentation slides from a topic, brief, or outline. Use when the user wants a presentation, deck, slides, speaker notes, or teaching material, especially for explainers, student presentations, strategy summaries, or fast first drafts. Triggers on phrases like 'make slides', 'create a presentation', 'build a deck', 'slides about', 'presentation on', '발표자료 만들어', '슬라이드 만들어', 'ppt', 'powerpoint', or 'deck'. Supports iterative improvement with a north-star objective, web research, and HTML reveal.js output.
---

# Slide Creator

Create polished, shareable HTML presentation slides from a user-provided topic or outline.

Keep the workflow tight, explicit, and audience-aware. Favor clear teaching flow over slide count inflation.

## Workflow

Follow this sequence.

### Step 1: Collect context

Collect these inputs:

1. Topic / objective
2. Depth (Overview / Intermediate / Deep-dive)
3. Audience and background
4. Duration
5. Style (Modern / Academic / Playful / Minimal / Corporate)
6. North star outcome

Ask one at a time when needed, but if the user already supplied several answers, do not re-ask them.

Defaults when missing:
- Depth: Overview
- Audience: General audience
- Duration: 15 min
- Style: Modern

### Step 2: Build a deck plan

Before writing slides:

- Identify the deck type: teaching, executive update, or strategy/proposal.
- Read `references/layout-patterns.md` and choose an appropriate story arc.
- Map the requested duration to a realistic slide count.
- Prefer fewer stronger slides over many thin slides.

### Step 3: Research only when useful

Build a research plan based on topic and depth.

- Use `web_fetch` for credible and recent sources.
- Prefer official docs, reputable institutions, major research or consulting firms, and technical primaries.
- If search results are blocked or low quality, stop retrying the same URL. Switch source, rely on internal knowledge, or ask for sources.
- Summarize findings into a compact research brief with title, key points, and sources.

See `references/research-prompts.md` for research query patterns.

### Step 4: Generate slide content

Produce a complete slide plan and JSON payload.

- Follow `references/slide-schema.md` exactly.
- Use slide types intentionally, not mechanically.
- Use `heading` slides sparingly. Too many section dividers weaken pacing.
- Add speaker notes that help the presenter explain transitions, examples, and emphasis.
- For short presentations, compress adjacent heading + bullet slides when possible.

### Step 5: Render the deck

Use `scripts/generate_slides.py` to create the slide HTML file.

- Output filename: `slides-<topic>-<timestamp>.html` inside `/data/workspace/output/slides/`
- Generate matching notes file alongside the HTML output
- The script writes a standalone reveal.js HTML deck

### Step 6: Quality check before delivery

Read `references/quality-checklist.md` and verify:

- story quality
- audience fit
- visual readability
- speaker usefulness
- technical success

If readability is weak, revise before delivering.

### Step 7: Deliver and iterate

Report:
- number of slides
- estimated duration
- file paths
- any caveats or assumptions

Then invite feedback on:
- content
- depth
- structure
- style
- slide count

If the user requests changes, compare against the north star and revise only the affected step(s).

## Slide content rules

- Keep slide text scannable.
- Prefer 3 to 5 bullets on a normal bullet slide.
- Avoid more than 6 bullets unless the structure clearly demands it.
- Prefer short phrases over full sentences.
- Use examples and analogies when the user wants understanding, not just reporting.
- Include at minimum: title, core setup, main content, summary/closing.

## Output location

- All slide files: `/data/workspace/output/slides/`
- Create the directory if it does not exist.

## Script and references

- `scripts/generate_slides.py` — render JSON into standalone HTML + notes
- `references/slide-schema.md` — required JSON schema
- `references/research-prompts.md` — research query patterns
- `references/layout-patterns.md` — recommended story arcs and compression rules
- `references/quality-checklist.md` — pre-delivery review checklist
