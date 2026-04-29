# Loop Outcomes

## continue
The next action is clear and the agent should keep going without asking.

## blocked
The task cannot advance because of a real blocker such as:
- missing credentials
- missing dependency
- external system failure
- user decision required but not yet asked

When blocked, record:
- blocker
- impact
- smallest unblock step

## ask-user
Use when the user must decide a branch, approve a risky action, or supply missing authority.
Ask one concise question.

## done
Use only when the requested objective is completed and verified enough for the task scope.
