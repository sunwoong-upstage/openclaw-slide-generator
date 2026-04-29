# OpenClaw Flow Status

## Current system
- Runtime layer: OpenClaw native sessions + subagents
- Flow model: OMX-inspired, adapted for OpenClaw
- Goal: persistent completion loops, visible status, durable plans, structured execution

## Current components
- `openclaw-flow/plans/` — approved or draft plans
- `openclaw-flow/state/` — machine-readable state files
- `openclaw-flow/logs/` — run logs and checkpoints
- `openclaw-flow/memory/` — flow-local memory shards

## In progress
- Designing `ralph-loop` skill for persistent completion and verification loops
- Defining OpenClaw-native state model and status surface

## Next recommended implementation
1. Add machine-readable flow state JSON
2. Add a lightweight planner/executor/verifier handoff contract
3. Add GitHub/Discord-visible status output
4. Add loop rules for continue / block / ask / done
