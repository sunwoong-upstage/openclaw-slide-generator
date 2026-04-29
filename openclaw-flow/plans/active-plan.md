# Active Plan

## Objective
Build an OpenClaw-native OMX-lite runtime layer with persistent completion loops, durable state, visible status, and role handoff structure.

## Current phase
Planning

## Workstreams
1. Define durable flow state files
2. Define planner/executor/verifier handoff contract
3. Expose visible status surface
4. Connect loop outcomes to real OpenClaw workflows
5. Later: event routing and GitHub/Discord integration

## Acceptance criteria
- Flow state is visible in files and GitHub export
- `ralph-loop` skill documents the persistent loop
- Handoff rules are explicit
- Next-step protocol is clear enough to run repeatedly
