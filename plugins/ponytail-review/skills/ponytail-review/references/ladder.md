> [Hub](./README.md) · [brain.yaml](./brain.yaml) · Related: [review-template.md](./review-template.md), [../SKILL.md](../SKILL.md)

# Ponytail ladder

From [DietrichGebert/ponytail](https://github.com/DietrichGebert/ponytail). Run **after** you understand the problem, not instead of reading.

1. **Does this need to exist?** Speculative need → skip it, say so in one line. (YAGNI)
2. **Already in this codebase?** Reuse the helper, skill, or pattern. Re-implementing a file two folders over is the common slop.
3. **Stdlib does it?** Use it.
4. **Native platform feature?** `<input type="date">` over a picker, CSS over JS, DB constraint over app code.
5. **Already-installed dependency?** Use it. Never add a new one for what a few lines can do.
6. **One line?** One line.
7. **Only then:** the minimum that works.

## Bug fix = root cause

Grep every caller of the function you touch. One guard in the shared function is smaller than a guard per caller.

## Rules

- No unrequested abstractions (interface with one implementation, factory for one product).
- No new dependency if it can be avoided.
- Deletion over addition. Boring over clever. Fewest files possible.
- Shortest working diff wins **after** you understand the flow.
- Mark deliberate corners with `ponytail: <ceiling>, <upgrade path>`.

## Never lazy about

Trust-boundary validation, data-loss handling, security, accessibility, hardware calibration, anything explicitly requested, and **reading the code**. Non-trivial logic leaves one runnable check.

## Intensity (building, not reviewing)

| Level | Meaning |
|-------|---------|
| lite | Build what was asked; name the lazier alternative in one line. |
| full | Ladder enforced. Default. |
| ultra | Deletion first. Ship the one-liner and challenge the rest of the requirement. |
