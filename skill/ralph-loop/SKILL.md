---
name: ralph-loop
description: Persistent completion loop for OpenClaw. Use when the user wants the agent to keep pushing a task forward until it is genuinely done, blocked, or requires a decision. Triggers on phrases like 'go on', 'keep going', 'run with it', 'Ralph loop', '계속 해', '알아서 끝까지 해', or when long-running work needs planning, execution, verification, and visible status.
---

# Ralph Loop

Run a persistent completion loop for OpenClaw-native work.

This skill is inspired by OMX-style completion loops, but adapted for OpenClaw sessions, subagents, and workspace files.

## Purpose

Use this skill when a task should not stop after one response. Keep advancing until one of four terminal outcomes is reached:

- done
- blocked
- ask-user
- paused

## Core loop

1. Clarify only if a real blocker exists.
2. Write or update durable state in `openclaw-flow/state/`.
3. If needed, create or update a plan in `openclaw-flow/plans/`.
4. Execute the next highest-value action.
5. Verify the result.
6. Decide the next outcome:
   - continue
   - blocked
   - ask-user
   - done
7. Update `openclaw-flow/STATUS.md` and `openclaw-flow/state/flow-state.json`.
8. Repeat until terminal.

## Rules

- Prefer action over commentary.
- Do not ask for confirmation on low-risk local work the user already requested.
- Ask only for true branching decisions, destructive actions, missing credentials, or external side effects.
- Preserve continuity through files, not memory alone.
- If multiple agents are useful, delegate with OpenClaw subagents or separate sessions.

## State files

Use these paths:

- `openclaw-flow/STATUS.md` — human-readable current state
- `openclaw-flow/state/flow-state.json` — machine-readable current state
- `openclaw-flow/plans/` — plans and checkpoints
- `openclaw-flow/logs/` — run notes and verification logs
- `openclaw-flow/memory/` — flow-local memory if needed

## Outcome meanings

### continue
The next action is clear and safe. Keep going.

### blocked
A real blocker prevents forward progress. Record the blocker and what would unblock it.

### ask-user
A specific user decision is required. Ask one concise question.

### done
The requested objective has been completed and verified.

## Recommended role split

When the task is large, separate these roles conceptually:

- planner
- executor
- verifier
- reviewer

OpenClaw may implement these through subagents, separate sessions, or sequential passes.

## References

- `references/state-model.md`
- `references/loop-outcomes.md`
- `references/handoff-contract.md`
- `references/execution-protocol.md`
