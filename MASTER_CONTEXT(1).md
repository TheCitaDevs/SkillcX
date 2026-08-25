# MASTER_CONTEXT.md

## 1. Document Purpose

This file is the highest-level canonical context for the project. Every AI agent, developer, designer, automation tool, or reviewer must read this file before making changes to the game.

This document does **not** grant permission to invent missing gameplay rules. If a required rule is not defined in the canonical documentation, the correct behavior is to mark it **UNDECIDED** and escalate it for a design decision.

## 2. Canonical Read Order

Before performing project work, read these files in order:

1. `MASTER_CONTEXT.md`
2. `GAME_RULES.md`
3. `ARCHITECTURE.md`
4. `DEVELOPMENT_RULES.md`
5. `DECISIONS.md`
6. `AI_STACK.md`
7. `STATE.md`
8. `AI_GAME_BUILD_PLAYBOOK_UE5.8.2.md`

If two documents conflict, use this precedence:

1. Explicit user instruction from the current task
2. `DECISIONS.md` entries marked `LOCKED`
3. `GAME_RULES.md` entries marked `LOCKED`
4. `MASTER_CONTEXT.md`
5. `ARCHITECTURE.md`
6. `DEVELOPMENT_RULES.md`
7. `AI_STACK.md`
8. `STATE.md`
9. `AI_GAME_BUILD_PLAYBOOK_UE5.8.2.md`

Any unresolved conflict must be reported rather than silently resolved.

## 3. Project Identity

**Working title:** UNDECIDED  
**Genre:** 3D third-person cooperative boss-rush roguelike  
**Structure:** 100-floor progression format  
**Primary co-op format:** 4-player online-reliant cooperative play  
**Primary engine:** Unreal Engine 5.8.2 development baseline  
**Primary gameplay implementation:** Unreal C++  
**Networking model:** Server authoritative online multiplayer  
**Gameplay framework:** Unreal Gameplay Ability System where appropriate  
**Content strategy:** Data-driven wherever practical  
**AI strategy:** AI-assisted development, not AI-dependent runtime gameplay

## 4. Core Product Vision

The game is a 100-floor cooperative boss-rush roguelike centered on defeating increasingly difficult bosses, earning immediate EXP, collecting shared post-boss loot, resting between encounters, and making long-term build decisions through leveling, stat allocation, class progression, multiclassing, and class ascension.

The design should reward:

- mastery of third-person action combat;
- cooperative coordination;
- meaningful build decisions;
- replayable progression choices;
- strong boss identity and encounter variety;
- long-form escalation across 100 floors;
- clear risk/reward decisions;
- readable combat and fair telegraphing.

The game must remain feasible for a very small, AI-assisted development team. Reuse, modular systems, procedural assembly, data-driven definitions, and automated testing are preferred over bespoke one-off code whenever they preserve quality.

## 5. Locked Core Gameplay Loop

The following order is canonical and must not be changed without an explicit decision:

1. Players enter or begin the current floor encounter.
2. Players fight the floor boss or special encounter.
3. On boss defeat, eligible players receive EXP immediately.
4. A shared loot chest is spawned or made available.
5. Players inspect and collect loot.
6. Only after the loot step may the group enter the Rest phase.
7. During Rest, players may perform allowed progression actions, including level/stat spending and eligible class progression decisions.
8. Players leave Rest and proceed toward the next floor.

The exact transitions, readiness rules, time limits, and failure behavior are **UNDECIDED** unless defined elsewhere.

## 6. Locked Class Progression Rules

- Classes have hard gameplay restrictions.
- A base class cannot bypass its restrictions simply because an unrestricted item or ability exists.
- Every 10 bosses/floors cleared, the player reaches a class progression milestone.
- At each milestone, the player is presented with exactly 3 RNG multiclass choices.
- Those multiclass choices must be compatible with the player's current class state.
- The player may select one offered multiclass option.
- The player may instead reject the offered multiclass choices and ascend the current class by `+1`.
- Ascension behavior/tracks may change after multiclassing.
- Class progression choices occur only during Rest.

The exact class roster, compatibility graph, ascension limits, multiclass depth, and stat formulas are **UNDECIDED**.

## 7. Locked Merchant Progression Rule

- Special merchant-boss encounters exist between milestone sections.
- Defeating the appropriate merchant boss unlocks the ability to sell unwanted gear.

The exact floor numbers, merchant count, merchant economy, buy/sell formulas, and whether merchant functions expand over time are **UNDECIDED**.

## 8. Technical Non-Negotiables

- The game is designed as an **online-reliant 4-player co-op experience** from the beginning.
- The current development engine baseline is **Unreal Engine 5.8.2**. Engine upgrades require an explicit reviewed decision and migration/test pass; AI agents must not silently upgrade the engine.
- Four remote players are the canonical gameplay target; local multiplayer is not a shipping requirement.
- Online identity, session/lobby discovery, connection flow, party/session state, disconnect handling, and future reconnect support must be architectural concerns early in development.
- Unreal local/PIE multiplayer may be used as a development/debugging shortcut, but local success does **not** satisfy the online multiplayer milestone by itself.
- A real remote-online test path must be established early, before large-scale combat/content production.
- Gameplay state that affects fairness, rewards, progression, damage, inventory, or encounter outcomes must be server authoritative.
- Core gameplay logic belongs in Unreal C++.
- Unreal Gameplay Ability System should be used where it meaningfully supports attributes, abilities, costs, cooldowns, effects, tags, replication, or prediction.
- Data-driven definitions are preferred for bosses, items, classes, abilities, floors, loot tables, affixes, progression tables, and other scalable content.
- Blueprints should primarily handle presentation, configuration, animation, VFX, UI, level assembly, and thin glue logic.
- Generative AI should primarily assist development and content production rather than being required during normal gameplay.
- The game must be commercially shippable.
- Every AI-generated or third-party asset must have provenance and licensing records.

## 9. Design Philosophy for a 100-Floor Scope

The project must scale by building reusable factories and frameworks before mass-producing content.

Preferred pattern:

`Reusable system -> validated data schema -> generated/curated content -> automated validation -> human approval`

Avoid:

`Unique hard-coded implementation for every boss/item/floor`

The player should experience variety even when internal systems reuse tested building blocks.

## 10. Human Authority and AI Role

AI agents are production tools and collaborators, not final decision-makers.

AI may:

- propose designs;
- implement approved systems;
- create data definitions;
- generate concepts and assets;
- write tests;
- analyze logs;
- identify risks;
- recommend balance changes;
- maintain documentation.

AI may not:

- silently change a locked rule;
- create a new major gameplay rule to fill a gap;
- claim functionality is complete without validation;
- approve its own legal/license assumptions when evidence is missing;
- replace human playtesting for game feel;
- introduce runtime generative-AI dependencies without explicit approval.

## 11. Required AI Task Protocol

For every development task, the acting AI must:

1. Read the canonical documents in the required order.
2. Restate the task internally as implementation requirements.
3. Identify any dependency or missing decision.
4. If a missing decision is major, mark it `UNDECIDED` and do not invent it.
5. Inspect existing implementation before creating new systems.
6. Prefer extending approved reusable systems.
7. Implement only the requested scope.
8. Build/compile where applicable.
9. Run relevant automated tests.
10. Report changed files.
11. Report tests performed and their result.
12. Report remaining warnings/errors/risks.
13. Update `STATE.md`.
14. Update `ARCHITECTURE.md` or `DECISIONS.md` if the task legitimately changes them.

## 12. Definition of a Major Gameplay Decision

The following require explicit approval before being treated as canonical:

- base class roster;
- stat roster or formulas;
- permanent vs run-specific progression;
- death/wipe rules;
- revive rules;
- loot ownership/distribution rules;
- difficulty scaling rules;
- procedural generation rules that change gameplay;
- monetization;
- PvP;
- final matchmaking/discovery UX and policy;
- cross-platform requirements;
- exact merchant placement/economy;
- number or depth of multiclasses;
- ascension cap or full ascension behavior;
- boss enrage timers;
- floor skip/checkpoint rules;
- save/continue rules;
- live-service systems;
- runtime generative AI.

## 13. Current Production Objective

The current objective is **not** to build all 100 floors.

The project should first prove the architecture in this order:

1. Verify the UE 5.8.2 Windows toolchain
2. Establish source control and the local AI engineering workspace
3. Bootstrap the Unreal Engine 5.8.2 C++ project
4. Third-person movement
5. Online multiplayer foundation (provider abstraction + OSS EOS development adapter + dedicated-server-compatible runtime + 4-player remote test ground)
6. GAS foundation
7. Combat foundation
8. One graybox boss
9. Core co-op loop
10. EXP -> loot -> Rest flow
11. Class/progression framework
12. Automated testing and balance/provenance foundations
13. Polished Floors 1-10 vertical slice
14. Architecture freeze
15. Production factories for Floors 11-100

See `STATE.md` for the currently active phase.

## 14. Commercial and Provenance Requirement

No asset, model, plugin, code dependency, font, sound, music, voice, texture, 3D model, animation, or AI-generated deliverable may be assumed commercially usable without recorded provenance.

At minimum, provenance records must capture:

- asset ID;
- source/tool;
- model or package name and version where relevant;
- license or terms reference;
- creation/acquisition date;
- original source location;
- prompt/reference provenance for AI outputs where practical;
- human modifications where practical;
- attribution requirements;
- commercial-use status;
- review status.

Unknown licensing status means `NOT APPROVED FOR SHIPPING`.

## 15. Canonical Status Labels

Use only these labels for design/technical decisions:

- `LOCKED` — approved and canonical.
- `PROVISIONAL` — currently used for implementation but may change.
- `UNDECIDED` — no canonical answer exists yet.
- `DEPRECATED` — previously used but no longer valid.

## 16. Rule Against Silent Assumptions

When information is absent, do **not** infer a major gameplay rule from genre conventions, another game, or personal preference.

Correct response format:

`UNDECIDED: <decision>`

Then provide implementation-safe options if useful, without selecting one unless explicitly authorized.


## 13. 2026-08-25 AI-First Production Directive

The current development operating model is AI-first but human-directed. The project does **not** attempt to replace mature Unreal systems with generated substitutes. AI agents operate approved tools and Unreal-native systems.

Current production roles:

- **AI-A — Director / Architect / Reviewer:** ChatGPT GPT-5.6 Sol.
- **AI-B — Local Lead Engineer / Tool Operator:** Qwen Code using a local OpenAI-compatible endpoint, with `gpt-oss-20b` as the default low-cost local reasoning model.
- **Editor bridge:** Unreal Engine 5.8.2 Unreal MCP, local-machine use only; experimental tooling must never become a shipping runtime dependency.
- **Visual generation:** ComfyUI + FLUX.2 [klein] 4B for commercially usable local concept/reference generation.
- **3D generation:** Meshy only when needed and only under a paid/commercially suitable plan for production assets; every asset requires provenance.
- **3D processing:** Blender 5.2 LTS, with repeatable Python automation written/maintained by AI-B.
- **Audio generation:** Stable Audio 3.0 under the applicable commercial/community license, with provenance recorded per output.
- **Testing:** Unreal Automation Framework, Gauntlet, UAT, data validation, and scripted regression orchestration.
- **Source control:** Perforce P4 is the current small-team baseline.

Specific AI vendors/models are **tooling baselines**, not gameplay canon. They may be upgraded only through a reviewed tooling change that preserves licensing, reproducibility, security, and project compatibility.

### Human authority

AI may implement, generate, validate, test, and propose. Human approval remains mandatory for:

- new gameplay rules;
- changes to LOCKED decisions;
- art-direction acceptance;
- release approval;
- investor claims and financial representations;
- commercial/IP decisions with material risk.

### Development optimization order

When tradeoffs exist, optimize in this order:

1. scalability;
2. multiplayer authority;
3. automation;
4. AI operability;
5. commercial shipping;
6. low development cost.
