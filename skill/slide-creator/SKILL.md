---
name: slide-creator
description: Create polished HTML-based presentation slides from a topic or outline. Use when the user wants to build a presentation, deck, slides, or speaker materials. Triggers on phrases like 'make slides', 'create a presentation', 'build a deck', 'slides about', 'presentation on', '발표자료 만들어', '슬라이드 만들어', 'ppt', 'powerpoint', or 'deck'. Supports iterative improvement with a north-star objective and web research.
---

# Slide Creator

Create polished, shareable HTML presentation slides from a user-provided topic or outline.

## Workflow

Follow this exact sequence. Do not skip steps.

### Step 1: Elicit Context

Ask the user the following required questions ONE AT A TIME (send as separate messages). Wait for answers before proceeding:

1. **Topic / Objective**: "What topic or objective should the presentation cover?"
2. **Depth**: "How deep should we go? (Overview / Intermediate / Deep-dive)"
3. **Audience**: "Who is the audience and what is their background?"
4. **Duration**: "How long is the presentation? (e.g. 10 min, 30 min, 60 min)"
5. **Style**: "What visual style do you want? (Modern / Academic / Playful / Minimal / Corporate)"
6. **North Star**: "What is the single most important outcome or key message? (north star)"

Record all answers. If the user provides multiple answers at once, still log them. If any are missing, default to: Overview, General audience, 15 min, Modern.

### Step 2: Research

Build a research plan based on the topic and depth. Use `web_fetch` to gather credible, recent sources. Summarize findings in a compact research brief (title, key points, sources). Save this to a temporary note within the session context.

### Step 3: Generate Slides

Produce a complete HTML slide deck using the answered context and research brief.

- Use `scripts/generate_slides.py` to create the slide HTML file. Pass the content as a JSON payload. See `references/slide-schema.md` for the JSON schema.
- The script writes a standalone HTML file (reveal.js embedded, no external network dependencies required for viewing).
- Output filename: `slides-<topic>-<timestamp>.html` inside `/data/workspace/output/slides/`.
- Generate a matching speaker notes file: `slides-<topic>-<timestamp>-notes.txt`.

### Step 4: Deliver & Review

Present the slide deck to the user with:
- Number of slides
- Approximate duration estimate
- File path(s)

Then ask for feedback: "Any changes? I can adjust content, depth, style, or add/remove slides."

### Step 5: Recursive Improvement (North Star Loop)

If the user requests changes, evaluate against the declared **North Star**.

1. Identify the gap between current output and the north star.
2. Decide whether the change requires: (a) content revision only, (b) additional research, or (c) structural reorganization.
3. Re-execute the affected step(s) and regenerate the slides.
4. Repeat until the user is satisfied or the north star is clearly met.

## Slide Content Rules

- Use Markdown-style formatting inside slides (headings, bullet lists, short paragraphs, code blocks).
- Keep slide text scannable. Max 6 bullet points per slide. Max 20 words per bullet.
- Use speaker notes for detail, nuance, and speaking cues.
- Include at minimum: Title slide, Agenda, Context/Problem, Key Content (2-8 slides), Summary/Call-to-Action.

## Output Location

- All slide files: `/data/workspace/output/slides/`
- Create the directory if it does not exist.

## Assets

- `assets/slide-template.html` — Base reveal.js template with Korean font support.
- `assets/slide-themes/` — CSS themes (modern, academic, playful, minimal, corporate).

## References

- `references/slide-schema.md` — JSON schema expected by `generate_slides.py`.
- `references/research-prompts.md` — Short prompt templates for web_fetch queries.
