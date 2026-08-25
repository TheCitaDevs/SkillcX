# DEVELOPMENT_RULES.md

## 1. Purpose

These rules govern how humans and AI agents modify the project.

The objective is to prevent architectural drift, silent design changes, untestable systems, license contamination, and mass generation of unusable content.

## 2. Required Pre-Task Read

Before changing the project, read:

1. `MASTER_CONTEXT.md`
2. `GAME_RULES.md`
3. `ARCHITECTURE.md`
4. `DEVELOPMENT_RULES.md`
5. `DECISIONS.md`
6. `STATE.md`

Do not rely on memory alone.

## 3. Scope Discipline

For every task:

- change only what is necessary;
- do not rewrite working unrelated systems;
- do not create a second system when one already exists;
- do not expand scope because a feature seems useful;
- do not convert a prototype decision into a permanent gameplay rule without approval.

If the task exposes a missing major design decision, mark it `UNDECIDED` and report it.

## 4. Implementation Priority

Use this preference order:

1. existing approved system;
2. extension/composition of an approved system;
3. reusable new framework;
4. content/data definition;
5. bespoke implementation only when justified.

Avoid one-off code for content that should scale to 100 floors.

## 5. C++ / Blueprint Boundary

### C++ Preferred For

- authoritative gameplay;
- networking;
- combat calculations;
- GAS integration;
- inventory/equipment rules;
- class compatibility;
- progression;
- reward generation;
- floor/run state;
- save/persistence;
- validation;
- test harnesses.

### Blueprint Preferred For

- animation blueprints;
- cosmetic VFX hookup;
- materials;
- UI presentation;
- designer-authored presentation subclasses;
- level assembly;
- Sequencer/cinematics;
- thin configuration glue.

Large replicated Blueprint gameplay graphs require explicit justification.

## 6. Data-Driven Rule

If a concept is expected to have many instances, prefer data-driven definitions.

Examples:

- bosses;
- attacks;
- phases;
- items;
- loot tables;
- classes;
- multiclasses;
- ascensions;
- floors;
- biomes;
- affixes;
- merchant definitions.

Do not hard-code content IDs or floor numbers into unrelated gameplay logic.

## 7. Online Multiplayer Rule

The canonical gameplay target is **4-player online co-op**. Online networking is not a late-stage integration task.

For every gameplay feature, explicitly answer:

- Who owns this state?
- Who may request a change?
- Who validates the request?
- What replicates?
- What happens on duplicate requests?
- What happens if a client disconnects mid-action?
- What state must survive a reconnect if reconnect is supported?
- Does this feature behave correctly for 1, 2, 3, and 4 connected online players?
- Does it rely on a local listen-host assumption that would break a dedicated-server path?

Server authority is mandatory for fairness/progression-critical state.

Local PIE/LAN tests are allowed for rapid iteration, but they are not the final validation target. Online-sensitive milestones must include a real remote session test through the project's selected online-services/session path. The project must preserve dedicated-server compatibility even if the final shipping topology remains undecided.

## 8. GAS Rule

Use Gameplay Ability System when it materially improves:

- attributes;
- gameplay abilities;
- costs;
- cooldowns;
- buffs/debuffs;
- status effects;
- ability granting/removal;
- gameplay tags;
- gameplay cues;
- multiplayer prediction/replication.

Do not force GAS into systems where a simpler architecture is clearly better.

## 9. Build Rule

A coding task is not complete until the relevant target builds successfully.

If build tooling is unavailable in the current environment, the agent must say so explicitly and must not claim the code compiles.

## 10. Testing Rule

Add automated tests where practical for systems involving:

- rewards;
- progression;
- inventory;
- class restrictions;
- multiclass compatibility;
- ascension;
- save/load;
- boss phase transitions;
- floor transitions;
- networking authority;
- duplication/exploit-sensitive transactions.

Human playtesting remains mandatory for game feel.

## 11. Definition of Done

A task is complete only when all applicable items are true:

- requested scope implemented;
- relevant project target builds;
- relevant tests pass;
- multiplayer behavior tested if affected;
- no known blocker is hidden;
- changed files are reported;
- new architecture is documented;
- new decisions are recorded;
- `STATE.md` updated;
- provenance/license records updated for imported/generated assets.

## 12. AI Reporting Format

At the end of a development task, report:

### Completed
- what changed;

### Changed Files
- exact paths;

### Validation
- build command/result;
- tests run/result;
- multiplayer validation if applicable;

### Remaining Issues
- errors;
- warnings;
- technical debt;
- `UNDECIDED` dependencies;

### Documentation Updated
- files updated;

Do not use vague statements such as "should work" as proof of completion.

## 13. No Silent Design Rule

An AI must not invent major rules for:

- classes;
- stats;
- loot ownership;
- death/wipe;
- progression persistence;
- final shipping hosting topology;
- final matchmaking/discovery UX;
- merchant economy;
- multiclass depth;
- ascension cap;
- monetization;
- PvP;
- runtime generative AI;
- platform targets.

Record the missing decision instead.

## 14. Change-Control Rule

When a locked rule needs to change:

1. create a proposed decision entry;
2. explain why the old rule is insufficient;
3. identify affected systems/data/tests;
4. obtain explicit approval;
5. mark the old decision/rule `DEPRECATED` if superseded;
6. update all canonical documents;
7. add migration work to `STATE.md`.

Never overwrite history as if the old rule never existed.

## 15. Source-Control Rules

- Commit coherent units of work.
- Do not commit generated build/cache directories.
- Track source, config, tests, scripts, canonical AI docs, and project settings.
- Use Git LFS or an appropriate large-file strategy for binary assets when needed.
- Never commit secrets, tokens, private keys, or credentials.
- AI-generated changes should remain reviewable through diffs whenever practical.

Suggested commit style:

`<Area>: <imperative summary>`

Examples:

- `Combat: Add server-authoritative damage flow`
- `Progression: Gate stat allocation behind Rest state`
- `Tests: Add multiclass compatibility coverage`

## 16. Naming Rules

Use stable, descriptive names.

Avoid names tied to temporary iteration numbers unless the asset itself requires them.

Suggested Unreal-style prefixes may be defined later in a dedicated naming standard. Until then, consistency matters more than inventing a large prefix taxonomy.

## 17. Generated Content Rule

Do not mass-generate production content before the consuming framework is validated.

Correct order:

1. schema/framework;
2. test content;
3. validation;
4. vertical slice;
5. architecture freeze;
6. production generator;
7. batch generation;
8. automated checks;
9. human curation;
10. shipping approval.

## 18. Asset Provenance Rules

For every AI-generated or third-party asset intended for the project, record at minimum:

- unique asset ID;
- file/project path;
- source;
- creator/tool/model;
- model/package version where relevant;
- license/terms;
- acquisition/generation date;
- commercial-use status;
- attribution requirement;
- source reference;
- modification notes where practical;
- review status;
- shipping approval status.

If any required license information is unknown:

`ShippingApproval = NO`

## 19. AI Model Policy

Adding an AI model to the development pipeline requires recording:

- model name/version;
- source;
- license;
- intended use;
- whether outputs are permitted for commercial use under the relevant terms;
- dependency/license concerns;
- whether the model will ship with the game.

Runtime model use requires separate explicit approval.

## 20. Security Rules

- No credentials in source control.
- Build scripts must not download/execute arbitrary unverified binaries.
- Third-party plugins must be tracked and reviewed.
- Generated code is subject to the same review/testing requirements as human-written code.
- External assets must be scanned/validated before integration where practical.

## 21. Performance Rules

Do not optimize blindly during early prototyping, but avoid designs known to scale poorly.

Before full production, establish budgets for:

- frame time;
- memory/VRAM;
- AI cost;
- network bandwidth;
- replicated actor counts;
- VFX complexity;
- animation cost;
- draw calls;
- loading/streaming.

Performance changes must be measured, not assumed.

## 22. Balance Rule

AI may recommend balance changes but must not silently alter approved balance in bulk.

Balance data should be externalized so automated simulations can evaluate:

- damage distributions;
- time-to-kill;
- loot distributions;
- class/build outliers;
- progression curves;
- invalid combinations.

Human playtesting decides whether the game feels good.

## 23. Vertical-Slice Rule

The first polished production target is Floors 1-10, not all 100 floors.

Before Floors 11-100 enter mass production, the project should prove:

- movement;
- 4-player online multiplayer;
- combat;
- one or more complete boss patterns;
- EXP flow;
- loot chest;
- inventory/equipment;
- Rest;
- class restrictions;
- multiclass/ascension milestone;
- merchant progression foundation;
- save/load;
- UI;
- automated QA;
- art/audio pipelines.

## 24. Architecture Freeze Rule

After the Floors 1-10 vertical slice is polished and audited:

- fix critical technical debt;
- finalize scalable schemas;
- create an architecture-freeze document;
- require explicit approval for new foundational systems.

Post-freeze development should be mostly content production and tuning.


## 25. Unreal Engine Version Rule

- The current development baseline is **Unreal Engine 5.8.2**.
- Do not change engine versions without explicit approval.
- Record exact compiler, Windows SDK, engine version, and important plugin versions used by reproducible builds.
- An approved engine upgrade requires clean compilation, automated regression, remote-online validation, packaging validation, and documentation updates before normal development resumes.

## 26. Unreal MCP Rule

UE 5.8.2 Unreal MCP may be used for editor-only AI assistance, but it is Experimental.

- Treat MCP as an accelerator, not a foundational runtime dependency.
- Prefer bounded editor tasks with inspect -> plan -> execute -> validate loops.
- Do not allow simultaneous/overlapping tool calls against the editor.
- Keep critical source, build, test, import, and validation workflows reproducible without requiring MCP where practical.
- Review all AI-created or AI-modified editor assets before approval.


## 18. AI Agent Operating Rules — 2026-08-25

1. AI-A owns architecture review, canonical design review, and escalation of UNDECIDED items.
2. AI-B owns implementation, tooling, builds, tests, diagnostics, editor automation, and repeatable Blender/Python processing.
3. AI-B must read canonical documents before every implementation task and must inspect existing code before creating a new system.
4. A failed compile/test is not completion. AI-B must fix deterministic failures within task scope before reporting success.
5. The default engineering path is local-first and low-cost. Paid/cloud AI is an escalation path only when explicitly approved or when the local path cannot reasonably complete the task.
6. Unreal MCP changes are staged, reversible, and source-controlled.
7. Generated art/3D/audio is never automatically approved for shipping.
8. Unknown or incompatible licensing means `NOT APPROVED FOR SHIPPING`.
9. Do not send Unreal Licensed Technology, MetaHuman-restricted data, NoAI-tagged content, confidential project material, or third-party content into AI systems unless the applicable license/data policy permits that exact use.
10. Model/tool upgrades require a recorded tooling decision and a small regression/compatibility check before becoming the baseline.

## 19. Simple Prompting Rule

After setup, the human should normally be able to issue short commands such as:

```text
Execute Phase 13. Read the canonical docs first. Stop when the gate passes and report validation.
```

The phase playbook contains the full underlying prompt. Short commands never override canonical restrictions.
