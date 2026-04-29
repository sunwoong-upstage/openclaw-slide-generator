# Handoff Contract

Use this contract when splitting work across planner, executor, verifier, or reviewer roles.

## Shared handoff fields

Every handoff should preserve:
- objective
- current phase
- completed work
- next required action
- verification target
- blocker, if any

## Planner -> Executor

Planner outputs:
- goal summary
- step list
- acceptance criteria
- known risks
- first concrete execution step

Executor responsibility:
- do not re-plan unless the plan is invalidated
- execute the next concrete step
- record changed files and results

## Executor -> Verifier

Executor outputs:
- what changed
- what was tested
- what still feels uncertain

Verifier responsibility:
- confirm objective progress
- check against acceptance criteria
- classify outcome as continue / blocked / ask-user / done

## Verifier -> User

Return only what matters:
- completed result
- confidence level
- unresolved risk
- next recommendation

## Reviewer role

Use only when extra quality review is worth the cost.
Focus on:
- correctness
- readability
- maintainability
- user impact
