# OpenClaw Flow State Model

## Goal

Provide durable, inspectable workflow state for long-running agent work.

## Human-readable state

`openclaw-flow/STATUS.md`

Use for:
- current objective
- active phase
- last meaningful change
- next actions
- blockers

## Machine-readable state

`openclaw-flow/state/flow-state.json`

Suggested fields:
- version
- system
- mode
- active_skill
- current_phase
- status
- summary
- next_steps
- blocker
- last_updated

## Phase suggestions

- discovery
- planning
- execution
- verification
- blocked
- done

## Status suggestions

- in_progress
- blocked
- waiting_user
- completed
- paused
