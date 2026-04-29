# Slide Quality Checklist

Use this checklist before delivering a deck.

## 1. Story quality

- Does the first slide clearly establish the topic?
- Does the deck have a visible flow: context -> core ideas -> examples -> summary?
- Does each slide advance the user's north-star goal?
- Are there unnecessary repetition slides that should be merged?

## 2. Audience fit

- Is the vocabulary appropriate for the target audience?
- Are examples chosen for the user's context?
- Is the requested depth respected?
- Is the estimated speaking time realistic?

## 3. Visual readability

- Is there enough text/background contrast?
- Are titles short enough to fit cleanly?
- Are bullets scannable, not paragraph-like?
- Do tables contain only essential columns and rows?
- Do two-column slides remain balanced?

## 4. Speaker usefulness

- Do speaker notes explain transitions and emphasis?
- Are notes helpful without repeating slide text verbatim?
- Can the presenter explain the topic clearly from the notes alone?

## 5. Technical checks

- Does the JSON match `references/slide-schema.md`?
- Does `scripts/generate_slides.py` run successfully?
- Are the HTML and notes files both created?
- If the deck is published, does the rendered page open correctly?

## 6. Improvement triggers

Revise the deck if any of these are true:

- The user cannot easily explain the topic after reading it.
- More than 30% of slides are section dividers or filler.
- Multiple slides could be merged without losing clarity.
- The main takeaway is not obvious within the first 3 slides.
