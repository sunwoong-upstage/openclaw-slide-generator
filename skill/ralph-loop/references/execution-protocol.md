# Execution Protocol

## Loop protocol

1. Read current flow state.
2. Confirm the objective and active phase.
3. Pick the smallest high-value next action.
4. Execute.
5. Verify.
6. Update flow state.
7. Decide one outcome:
   - continue
   - blocked
   - ask-user
   - done

## Continue rule

Keep going when:
- the next step is local and low-risk
- the user already requested the overall work
- no branching decision is required

## Ask-user rule

Ask only when:
- a real preference branch changes the result materially
- credentials or external permissions are missing
- an irreversible action is required

## Blocked rule

Blocked means forward progress is impossible right now.
Do not call ordinary uncertainty a blocker.

## Done rule

Done requires:
- the requested goal is achieved enough for the scope
- at least one verification pass happened
- the result is reported clearly
