# AI-Native Game Production Playbook — Unreal Engine 5.8.2

**Project:** 100-floor 3D third-person 4-player online-reliant co-op boss-rush roguelike  
**Revision:** UE5.8.2-AI-FIRST-2026-08-25  
**Authority model:** Server authoritative; dedicated-server-compatible.  
**Core implementation:** Unreal C++ + GAS where appropriate; data-driven content; thin Blueprint presentation.  
**Production strategy:** AI performs repeatable production work; Unreal-native systems remain the substrate; human owns direction/approval.

## AI / Tool Roster
- **AI-A:** ChatGPT GPT-5.6 Sol — Director / Architect / Reviewer.
- **AI-B:** Qwen Code + local gpt-oss-20b — Lead Engineer / Automation / Tool Operator.
- **Unreal MCP:** local development editor bridge; experimental; not runtime.
- **AI-D:** ComfyUI + FLUX.2 [klein] 4B — concept/reference art.
- **AI-E:** Meshy paid/commercial path when needed — 3D generation.
- **Blender 5.2 LTS:** scripted processing operated by AI-B.
- **AI-G:** Stable Audio 3.0 — audio candidates under applicable license.
- **QA:** Unreal Automation, Gauntlet, UAT, data validation, remote-online test harnesses.

## Universal Rules
1. Read canonical documents before every phase.
2. Never invent an UNDECIDED gameplay rule.
3. Do not move to the next phase until the gate passes.
4. Technical failure is not completion: compile/test/fix/report.
5. Do not mass-produce content until the reusable system/factory is validated.
6. Unknown commercial rights = NOT APPROVED FOR SHIPPING.
7. AI tooling may change through reviewed change control; LOCKED gameplay may not.
8. Paid/cloud AI is an escalation path, not the default operating cost.
9. Runtime generative AI is not part of the normal shipping gameplay architecture.

---
## PHASE PRE-0 — Verify / Install Production Toolchain
**Primary:** Human + AI-A review

### Prompt
```text
Verify the development workstation against the current canonical tooling baseline.
Confirm Unreal Engine 5.8.2, supported Visual Studio/MSVC + Windows SDK, Python, Perforce P4, Qwen Code, the local OpenAI-compatible inference runtime for gpt-oss-20b, Blender 5.2 LTS, and ComfyUI are installed or intentionally deferred.
Record exact versions in /AI/TOOLCHAIN.md.
Do not create gameplay systems.
```

### Completion Gate
- Toolchain versions are recorded; UE launches; C++ toolchain is recognized; no credentials are committed.

---
## PHASE 1 — Canonical Documentation Audit / Migration
**Primary:** AI-A (ChatGPT GPT-5.6 Sol)

**Note:** This package already satisfies this phase unless later changes create drift.

### Prompt
```text
Audit all canonical project documentation.
Verify the project locks UE 5.8.2, 100 floors, 4-player online-reliant co-op, server authority, dedicated-server compatibility, early genuine remote-online testing, C++ core gameplay, GAS where appropriate, data-driven scalable content, thin Blueprint presentation, the exact post-boss progression order, hard class restrictions, 10-floor multiclass/ascension rules, merchant selling unlock, AI-assisted development, and commercial provenance.
Find contradictions.
Do not invent unresolved gameplay rules. Mark unresolved items UNDECIDED.
Update the canonical documents only where required.
```

### Completion Gate
- Canonical package is contradiction-free and explicitly targets UE 5.8.2.

---
## PHASE 2 — Perforce Source-Control Foundation
**Primary:** AI-B (Qwen Code + local gpt-oss-20b)

### Prompt
```text
Prepare this Unreal project for Perforce P4 source control.
Create the appropriate ignore rules and source-control structure.
Separate source files, generated files, builds, caches, and large Unreal binary assets correctly.
Track the canonical documentation.
Document and test backup, revert, and restore procedures.
Do not change gameplay code.
```

### Completion Gate
- A test change can be submitted, reverted, and restored; generated/cache files are excluded appropriately.

---
## PHASE 3 — Provenance / License Ledger Foundation
**Primary:** AI-B; review AI-A

### Prompt
```text
Create the project asset/dependency provenance tracking system.
Every third-party or AI-generated production asset must be able to record: asset ID, name, creator/source, AI/tool/model/version, generation/acquisition date, license, commercial-use status, attribution requirements, source files, modifications, human approval, and shipping approval.
Track code dependencies, plugins, fonts, audio, animations, references, and external assets too.
Unknown commercial status must automatically mean NOT APPROVED FOR SHIPPING.
```

### Completion Gate
- A new asset/dependency cannot enter approved production without a ledger record and shipping status.

---
## PHASE 4 — Local AI Engineer Setup
**Primary:** Human + AI-B

### Prompt
```text
Configure Qwen Code as the project engineering agent.
Use a local OpenAI-compatible endpoint with gpt-oss-20b as the default model.
Give it access only to the required project/repository/tool scope.
Load the permanent engineer prompt from AI_STACK.md.
Ask it to read all canonical documents and explain the rules it is forbidden to change.
Do not modify the game yet.
```

### Completion Gate
- AI-B correctly reports the canonical constraints and can inspect the repository without changing it.

---
## PHASE 5 — UE 5.8.2 C++ Project Bootstrap
**Primary:** AI-B

### Prompt
```text
Create or normalize the Unreal Engine 5.8.2 C++ project foundation described in ARCHITECTURE.md.
Set up the required source/module/content directory structure.
Enable only plugins required by the current architecture, including GAS-related dependencies, approved online foundations, PCG where required, Unreal MCP for development, and testing support.
Do not implement gameplay yet.
Compile and verify a clean project.
```

### Completion Gate
- UE opens and the clean C++ project builds from source.

---
## PHASE 6 — Unreal MCP Connection
**Primary:** AI-B + Unreal MCP

### Prompt
```text
Connect to the Unreal Engine 5.8.2 MCP server locally.
Inspect the current project without modifying anything.
Verify access to the editor operations actually exposed in this build, such as levels, actors, assets, Blueprints, materials, PCG, project settings, and automation where supported.
Report the available operations and any unsupported assumptions.
Do not expose the MCP service beyond the approved local development boundary.
```

### Completion Gate
- AI-B can inspect approved Unreal editor state through MCP and reports capabilities accurately.

---
## PHASE 7 — MCP Reversibility Test
**Primary:** AI-B + Unreal MCP

### Prompt
```text
Using Unreal MCP, create a temporary development test level containing a floor, lighting, PlayerStart, and one simple test object.
Save and verify it.
Then delete/revert the temporary test level and verify the project returns to its prior source-controlled state.
Do not modify production levels.
```

### Completion Gate
- AI can create, save, validate, and safely revert an Unreal editor change.

---
## PHASE 8 — Automated Development Build Pipeline
**Primary:** AI-B

### Prompt
```text
Create the automated development build pipeline.
It must compile C++, capture compiler/build logs, detect failure, run selected automated tests, preserve failure artifacts, and produce a development build.
Use Unreal Automation Tool and native Unreal automation where appropriate.
Do not create shipping configuration yet.
Document the one-command or single-workflow entry point.
```

### Completion Gate
- One command/workflow compiles, tests, reports failure clearly, and produces a development build when passing.

---
## PHASE 9 — Minimum Network Player
**Primary:** AI-B

### Prompt
```text
Create the minimum server-authoritative multiplayer test character.
Use Unreal Character and Character Movement instead of custom movement technology wherever possible.
Implement only spawn, input, movement, rotation, camera, and basic replication.
No combat, abilities, progression, or art polish.
Use thin Blueprint presentation only.
Compile and test.
```

### Completion Gate
- Multiple clients can spawn/move with correct replicated state in local development tests.

---
## PHASE 10 — Provider-Abstracted Online Layer
**Primary:** AI-B

### Prompt
```text
Implement the canonical provider-abstracted online layer.
Use the currently approved provisional online adapter only behind project-owned interfaces/subsystems.
Support the minimum development flow for identity/authentication where required, private session/lobby creation, discovery/invite/join as supported, connection/travel coordination, leave, and failure diagnostics.
Do not hard-code gameplay to one backend.
Preserve dedicated-server compatibility.
Do not decide final shipping topology.
```

### Completion Gate
- Online provider calls are isolated and a development session can be created/joined without gameplay depending on provider-specific code.

---
## PHASE 11 — First Genuine 4-Player Remote-Online Test
**Primary:** AI-B + Human remote testers

### Prompt
```text
Prepare the project for the first genuine four-player remote-online multiplayer test.
Create a development build with connection/session diagnostics, replication logging, disconnect diagnostics, and simple instructions for four remote clients.
Do not add gameplay features.
After the test, analyze the logs and fix only networking/session/replication defects until the four-player remote-online gate passes.
```

### Completion Gate
- Four remote players enter the same session, spawn, see movement/rotation/basic state correctly, and leave/rejoin without corrupting authoritative state.

---
## PHASE 12 — Gameplay Ability System Foundation
**Primary:** AI-B

### Prompt
```text
Implement the canonical Gameplay Ability System foundation.
Create the minimum scalable architecture for ability-system components, Health/Stamina foundations, gameplay tags, gameplay abilities, gameplay effects, costs, cooldowns, cues, and authority/prediction policy.
Do not invent additional stats or formulas that remain UNDECIDED.
Use clearly marked TEST ONLY values where required.
Compile and test multiplayer replication.
```

### Completion Gate
- GAS foundation works online; authoritative state and prediction policy are validated.

---
## PHASE 13 — Combat Foundation
**Primary:** AI-B

### Prompt
```text
Build the minimum production combat framework using the canonical architecture.
Support basic attack flow, hit validation, server-authoritative damage, health/death event plumbing, blocking/parry/dodge/stagger extension points where already approved by architecture, and GAS integration where appropriate.
Do not invent unresolved death/revive/wipe rules.
Use test-only behavior for unresolved policy.
Compile and multiplayer-test combat.
```

### Completion Gate
- Combat damage is authoritative, replicated correctly, and passes a basic multiplayer combat test.

---
## PHASE 14 — Reusable Boss Framework
**Primary:** AI-B

### Prompt
```text
Create the reusable data-driven boss framework.
Support boss definitions, stats, abilities, attack definitions, phases, target-selection/aggro hooks, movement policy, animation/VFX/audio hooks, arena interactions, boss UI events, death, and a canonical completion/reward event.
Do not create many bosses.
Create one graybox test boss only.
Compile and test with four players.
```

### Completion Gate
- One reusable graybox boss can complete a multi-phase fight online and emits the canonical defeat event.

---
## PHASE 15 — Canonical Post-Boss Sequence
**Primary:** AI-B

### Prompt
```text
Implement the canonical post-boss sequence exactly:
Boss defeated -> immediately award EXP -> make shared loot chest available -> players resolve/collect loot -> allow Rest -> progression only during Rest -> proceed to next floor.
Do not change the order.
Do not invent exact shared-loot ownership/distribution if it remains UNDECIDED; create the interface/state boundary and test-only fixture required to validate ordering.
Add automated sequence tests.
```

### Completion Gate
- Automated tests prove the required state/order and reject Rest/progression before loot resolution.

---
## PHASE 16 — Rest State
**Primary:** AI-B

### Prompt
```text
Implement Rest as a synchronized authoritative gameplay state after loot resolution.
Only during Rest allow approved level/stat spending and class-progression operations.
Create readiness/status, transition hooks, validation APIs, replicated state, UI hooks, and safe extension points for disconnect handling.
Do not invent final timer/vote/free-movement behavior if still UNDECIDED.
```

### Completion Gate
- Rest is a real synchronized state and progression APIs reject calls outside Rest.

---
## PHASE 17 — Generic Class Framework
**Primary:** AI-B

### Prompt
```text
Create the generic data-driven class framework without choosing the final class roster.
Support class identity/tags, hard equipment permissions, hard ability permissions, progression hooks, multiclass compatibility queries, ascension state, milestone eligibility, and persistence hooks.
Use a Knight fixture only if needed to prove a base Knight cannot use unrestricted general magic.
All restriction validation is server authoritative.
```

### Completion Gate
- Hard class restrictions work authoritatively and class compatibility is data/tag driven.

---
## PHASE 18 — Ten-Floor Multiclass / Ascension Framework
**Primary:** AI-B

### Prompt
```text
Implement the canonical ten-floor milestone framework generically.
Every 10 floors cleared, generate exactly 3 RNG multiclass choices that are compatible with the current class state.
During Rest, allow selection of one offered multiclass OR rejection of all offered choices to ascend the current class by +1.
Support class-state-dependent ascension tracks after multiclassing.
Persist enough RNG/choice state to prevent unintended rerolls on save/load.
Do not invent the final class graph, maximum multiclass depth, or ascension cap.
```

### Completion Gate
- Deterministic tests prove exactly three compatible offers, save-safe choice persistence, and the ascension alternative.

---
## PHASE 19 — Merchant Unlock Framework
**Primary:** AI-B

### Prompt
```text
Create the merchant-boss unlock framework.
Defeating the appropriate merchant boss unlocks the authoritative ability to sell unwanted equipment.
Implement unlock state, sell permission, transaction interfaces, valuation extension point, persistence hooks, and multiplayer validation.
Do not invent merchant floor placement, prices, or economy formulas while they remain UNDECIDED.
```

### Completion Gate
- Merchant defeat can authoritatively unlock selling; economy values remain external data/policy.

---
## PHASE 20 — Blocking Design Decision Gate
**Primary:** AI-A; Human decision owner

### Prompt
```text
Audit the implementation and canonical docs.
Identify only UNDECIDED gameplay decisions that now block the next production stage.
For each blocker, present 2-4 viable options with advantages, disadvantages, development cost, multiplayer implications, roguelike implications, and a recommendation.
Do not finalize the decision for me.
Do not reopen already LOCKED rules.
```

### Completion Gate
- Human explicitly approves every decision required for the next implementation stage; decisions are recorded canonically.

---
## PHASE 21 — Save / Persistence Foundation
**Primary:** AI-B

### Prompt
```text
Implement the approved versioned save/persistence architecture using only newly approved decisions.
Separate permanent/profile data, run/session state, and user settings.
Never trust client-owned progression values as authoritative online state.
Add schema versioning/migration hooks, corruption handling, atomic/safer write strategy where practical, and tests for save/load/reload/migration.
```

### Completion Gate
- Approved progression and run state survive save/load, version detection works, and clients cannot authoritatively forge progression.

---
## PHASE 22 — Complete Graybox Vertical Slice
**Primary:** AI-B

### Prompt
```text
Build the first complete graybox gameplay vertical slice.
It must include: four-player online session, spawn/movement, combat, one boss, boss defeat, immediate EXP, shared loot-chest phase, loot resolution fixture, Rest, approved progression, and next-floor transition.
Use placeholder assets.
Do not spend time on art polish.
Run the relevant automated and remote-online tests.
```

### Completion Gate
- A four-player graybox run completes the full canonical loop without console-only intervention.

---
## PHASE 23 — Human Playtest / Feel Pass
**Primary:** Human; AI-A organizes; AI-B fixes approved technical changes

### Prompt
```text
Collect playtest feedback on movement, combat feel, boss readability, pacing, loot flow, Rest flow, UI clarity, and multiplayer friction.
Classify feedback as technical defect, balance/tuning, art/readability, design proposal, or subjective preference.
Do not silently change LOCKED rules.
Implement only approved changes and rerun regression tests.
```

### Completion Gate
- Human approves the graybox core loop as worth continuing to production content.

---
## PHASE 24 — PCG / Environment Factory Prototype
**Primary:** AI-B + Unreal MCP

### Prompt
```text
Build the procedural/environment assembly framework using Unreal-native PCG and level tools where appropriate.
Create reusable rules for environment distribution, props, vegetation if approved, traversal clearance, encounter spaces, and boss arenas.
Gameplay-critical spaces must remain deterministic/testable.
Do not generate 100 floors.
Create one test environment and validate collision/navigation/performance.
```

### Completion Gate
- One representative environment can be generated/assembled repeatably and remains gameplay-safe.

---
## PHASE 25 — Art Bible
**Primary:** AI-A; Human approval

### Prompt
```text
Create the visual art bible using approved project direction only.
Define character, enemy, boss, environment, weapon/equipment, material, color, lighting, UI, silhouette, readability, VFX, and presentation rules.
Separate mandatory rules from optional inspiration.
Do not invent gameplay features.
```

### Completion Gate
- Human approves a coherent art bible that production AIs can follow.

---
## PHASE 26 — FLUX Concept / Reference Factory
**Primary:** AI-D (ComfyUI + FLUX.2 [klein] 4B); AI-A prompt direction

### Prompt
```text
Create a production concept sheet for [ASSET] following the approved art bible.
Show front, back, side, 3/4 view, important details, materials, and clear silhouette on a neutral background.
Keep proportions consistent and design for conversion into a real-time Unreal Engine asset.
Do not add elements not included in the approved asset specification.
Record model/version/prompt/seed/source references in provenance.
```

### Completion Gate
- Multiple candidates are generated; one is human-approved; provenance is complete.

---
## PHASE 27 — 3D Generation Batch Pilot
**Primary:** AI-E (Meshy) + Human approval

### Prompt
```text
Create a production-oriented real-time 3D model matching the approved concept/reference.
Preserve silhouette, proportions, major design features, and materials.
Optimize for downstream game processing.
Do not invent additional decorative elements.
The model will be processed and validated in Blender and Unreal.
Record plan/license/model/output in provenance.
```

### Completion Gate
- One approved test asset can move from generated source to downstream Blender validation with clear commercial rights.

---
## PHASE 28 — Automated Blender Processing
**Primary:** AI-B operating Blender 5.2 LTS

### Prompt
```text
Create a repeatable Blender 5.2 LTS Python processing workflow for imported production assets.
Validate scale, transforms, normals, mesh integrity, UV/material organization, naming, pivots, topology/LOD suitability, and export settings.
Perform safe automated corrections where deterministic.
Do not make unapproved artistic changes.
Produce a processing report.
```

### Completion Gate
- One test prop completes Blender processing repeatably and produces a technical report.

---
## PHASE 29 — Unreal Asset Staging / Validation Importer
**Primary:** AI-B + Unreal MCP

### Prompt
```text
Import the approved processed asset into the Unreal staging area.
Apply canonical naming/content placement, materials, collision, LOD/Nanite policy where appropriate, metadata, and provenance reference.
Run technical validation.
Do not move the asset into final production Content until human approval.
```

### Completion Gate
- Asset passes Unreal technical validation and has a complete provenance link.

---
## PHASE 30 — Character Production Pipeline
**Primary:** AI-B + Unreal-native character tools; AI-D references

### Prompt
```text
Create the production player-character pipeline using Unreal-native character systems wherever appropriate, including MetaHuman only where it matches the art direction, shared skeleton strategy, Control Rig, IK Retargeting, Character Movement integration, materials, LODs, physics/collision, and multiplayer requirements.
Create one representative production-quality character before batch work.
Respect MetaHuman/AI data-use restrictions.
```

### Completion Gate
- Representative player character is game-ready, animation-ready, provenance-approved, and works online.

---
## PHASE 31 — Animation Architecture / Production Set
**Primary:** AI-B + Unreal animation tools

### Prompt
```text
Create the reusable animation architecture for approved player and boss skeleton families.
Support locomotion, combat actions, reactions, death/knockdown hooks, casting/interactions where approved, montages, notifies, root-motion policy, GAS hooks, retargeting, Control Rig/IK, and multiplayer-safe animation state.
Validate one player and the graybox/first boss.
```

### Completion Gate
- Animation timings integrate with authoritative gameplay without gameplay authority living in cosmetic graphs.

---
## PHASE 32 — UI Production Framework
**Primary:** AI-A/AI-D for approved visual concept; AI-B implementation

### Prompt
```text
Implement the approved functional UI using UMG/Common UI where appropriate.
UI is presentation/request only; it may not own authoritative gameplay state.
Support player status, boss status, party, floor, EXP/progression state, inventory/equipment, loot phase, Rest, class milestone choices, merchant selling, network/session state, errors, keyboard/mouse, and controller navigation as approved.
Do not invent new mechanics.
```

### Completion Gate
- Entire approved gameplay loop is operable with production-oriented UI and authoritative state remains outside UI.

---
## PHASE 33 — Niagara / Gameplay Cue VFX Framework
**Primary:** AI-B + Unreal Niagara

### Prompt
```text
Create reusable Niagara/gameplay-cue VFX patterns for hits, abilities, boss attacks, loot, level transitions, and class progression.
VFX reacts to authoritative gameplay events and never owns damage/reward/progression logic.
Create one validated representative effect per approved category.
```

### Completion Gate
- Representative effects trigger correctly online without affecting authoritative calculations.

---
## PHASE 34 — Audio Production Pipeline
**Primary:** AI-G (Stable Audio 3.0) + AI-A direction + AI-B integration

### Prompt
```text
Generate original audio candidates for [SCENE/BOSS/ACTION] following the approved audio direction.
For music, create loopable original instrumental material with specified mood/gameplay function.
For SFX, create isolated clean effects with specified physical/gameplay characteristics.
Do not imitate a named copyrighted song or living artist as a shortcut.
Record model/license/prompt/output/human approval in provenance; integrate approved assets through gameplay events.
```

### Completion Gate
- Approved audio assets are original, provenance-complete, loop/trigger correctly, and do not contain gameplay authority.

---
## PHASE 35 — Production Content Schemas
**Primary:** AI-B; review AI-A

### Prompt
```text
Create/finalize scalable data schemas for floors, bosses, enemies, attacks, abilities, items/equipment, loot, classes, multiclasses, ascensions, merchant definitions, encounters, biomes/environments, and presentation references.
Do not mass-populate content yet.
Create only enough fixture data to validate every schema and cross-reference rule.
```

### Completion Gate
- Schemas validate, serialize, are AI-readable, and new content can be added as data rather than architecture.

---
## PHASE 36 — Floors 1–10 Production Design
**Primary:** AI-A; Human approval

### Prompt
```text
Design the production specification for Floors 1 through 10 using only approved gameplay systems and art/audio direction.
For each floor define its learning/pacing purpose, boss/special encounter, arena/environment, approved mechanic focus, difficulty target, reward identity, visual/audio identity, and required data/assets.
Apply the approved merchant behavior and Floor-10 class milestone.
Do not invent unresolved rules or foundational systems.
Output human-readable design and implementation-ready structured specifications.
```

### Completion Gate
- Human approves the complete Floors 1–10 design before mass asset production.

---
## PHASE 37 — Floors 1–10 Production Build
**Primary:** AI-B + specialist tools as required

### Prompt
```text
Implement the approved Floors 1–10 specifications using the validated gameplay/content/art/audio factories.
Reuse existing systems.
Do not introduce new foundational architecture without escalation.
Run data validation, automated tests, performance checks, provenance validation, and four-player online regression after implementation.
```

### Completion Gate
- Floors 1–10 complete the intended representative chapter and pass technical/provenance gates.

---
## PHASE 38 — Floors 1–10 Remote Multiplayer Validation
**Primary:** AI-B + Human testers

### Prompt
```text
Prepare and execute a four-player remote-online test build covering Floors 1–10.
Collect detailed diagnostics for networking, bosses, abilities, rewards, loot, Rest, class milestone, merchant unlock, floor transitions, performance, crashes, and desynchronization.
Classify findings as blocker/critical/high/medium/low plus balance/visual.
Fix blocker/critical/high technical failures before proceeding; do not redesign gameplay to hide technical defects.
```

### Completion Gate
- Four-player remote run of Floors 1–10 passes with no blocker/critical technical defects and acceptable performance.

---
## PHASE 39 — Architecture Freeze Before Scale
**Primary:** AI-A + AI-B

### Prompt
```text
Audit the complete Floors 1–10 implementation before factory-scale production.
Check architecture drift, provider leakage, listen-host assumptions, hard-coded content that should be data, schema instability, missing tests, performance/network regressions, provenance gaps, AI-tool coupling, and technical debt.
Fix critical architecture debt.
Freeze stable content schemas/factories sufficiently for Floors 11–100.
```

### Completion Gate
- Architecture/factories are stable enough that new floors are primarily data/assets rather than new foundational code.

---
## PHASE 40 — Floors 11–20
**Primary:** AI-A design -> AI-B build

### Prompt
```text
Design and build Floors 11–20 using the frozen factories and completed Floors 1–10 as progression context.
Maintain canonical progression and approved merchant/milestone behavior.
No new foundational systems without explicit approval.
Run balance checks, four-player online regression, performance checks, provenance validation, and relevant automation.
```

### Completion Gate
- Floors 11–20 pass the same production gates as Floors 1–10.

---
## PHASE 41 — Floors 21–30
**Primary:** AI-A design -> AI-B build

### Prompt
```text
Design and build Floors 21–30 using frozen factories and established progression.
No silent architecture expansion.
Validate balance, four-player online behavior, performance, provenance, and regression.
```

### Completion Gate
- Floors 21–30 pass all production gates.

---
## PHASE 42 — Floors 31–40
**Primary:** AI-A design -> AI-B build

### Prompt
```text
Design and build Floors 31–40 using frozen factories and established progression.
No silent architecture expansion.
Validate balance, four-player online behavior, performance, provenance, and regression.
```

### Completion Gate
- Floors 31–40 pass all production gates.

---
## PHASE 43 — Floors 41–50
**Primary:** AI-A design -> AI-B build

### Prompt
```text
Design and build Floors 41–50 using frozen factories and established progression.
No silent architecture expansion.
Validate balance, four-player online behavior, performance, provenance, and regression.
```

### Completion Gate
- Floors 41–50 pass all production gates.

---
## PHASE 44 — Floors 51–60
**Primary:** AI-A design -> AI-B build

### Prompt
```text
Design and build Floors 51–60 using frozen factories and established progression.
No silent architecture expansion.
Validate balance, four-player online behavior, performance, provenance, and regression.
```

### Completion Gate
- Floors 51–60 pass all production gates.

---
## PHASE 45 — Floors 61–70
**Primary:** AI-A design -> AI-B build

### Prompt
```text
Design and build Floors 61–70 using frozen factories and established progression.
No silent architecture expansion.
Validate balance, four-player online behavior, performance, provenance, and regression.
```

### Completion Gate
- Floors 61–70 pass all production gates.

---
## PHASE 46 — Floors 71–80
**Primary:** AI-A design -> AI-B build

### Prompt
```text
Design and build Floors 71–80 using frozen factories and established progression.
No silent architecture expansion.
Validate balance, four-player online behavior, performance, provenance, and regression.
```

### Completion Gate
- Floors 71–80 pass all production gates.

---
## PHASE 47 — Floors 81–90
**Primary:** AI-A design -> AI-B build

### Prompt
```text
Design and build Floors 81–90 using frozen factories and established progression.
No silent architecture expansion.
Validate balance, four-player online behavior, performance, provenance, and regression.
```

### Completion Gate
- Floors 81–90 pass all production gates.

---
## PHASE 48 — Floors 91–100
**Primary:** AI-A design -> AI-B build

### Prompt
```text
Design and build Floors 91–100 using frozen factories and the complete prior progression context.
Deliver the approved climax/final progression behavior without inventing unresolved rules.
No silent architecture expansion.
Validate balance, four-player online behavior, performance, provenance, all floor transitions, and full relevant regression.
```

### Completion Gate
- All 100 floors exist and pass the production gates; no blocker/critical progression path is known.

---
## PHASE 49 — Full QA / Optimization / Soak / Provenance Audit
**Primary:** AI-B + Automation/Gauntlet; AI-A review; Human playtest

### Prompt
```text
Run the full pre-release technical campaign.
Profile CPU, GPU, memory/VRAM, networking, replication/RPC rates, draw/shader cost, Niagara, animation, AI, streaming, asset size, and load times.
Run long-duration four-player online soak tests including repeated boss fights, floor transitions, disconnect/reconnect behavior as approved, loot/progression/save stress, and memory growth.
Run the full provenance/license/dependency audit.
Anything with uncertain shipping rights is BLOCKED FROM SHIPPING.
Optimize the largest measured problems one category at a time and rerun regression after each change.
```

### Completion Gate
- Performance/network budgets are acceptable, long soak tests are stable, and provenance has no unresolved shipping blockers.

---
## PHASE 50 — Release Candidate / Final Shipping Audit
**Primary:** AI-B + AI-A + Human approval

### Prompt
```text
Create Release Candidate 1 under feature freeze.
Run clean compile, full automation, multiplayer tests, save/migration tests, all 100 floor-transition/progression validations, performance checks, packaging, clean-install validation, and provenance/license gate.
No new features.
Classify defects by severity with reproduction steps.
After approved fixes, perform the final shipping-readiness audit covering technical stability, multiplayer, commercial rights, AI disclosures, store requirements, build configuration, rollback/hotfix path, and support readiness.
```

### Completion Gate
- Zero blocker/critical defects; release build is reproducible; rollback/hotfix path exists; human approves shipping.

---
## PHASE 51 — Investor / Publisher Package + Data Room
**Primary:** AI-A; Human/business/legal review

### Prompt
```text
Prepare the investor/publisher package using only verified project facts and actual metrics.
Include executive summary, game overview, USP, target audience, competitive positioning, development history, actual production cost, AI-assisted production advantage, technology pipeline, build/playtest metrics, store/wishlist metrics if actually available, roadmap, launch strategy, financial scenarios with explicit assumptions, risks, IP ownership summary, provenance/license summary, online infrastructure plan/costs, funding request/use of funds, and the reusable internal production-technology story.
Then organize a due-diligence data room covering corporate records, game design, architecture, source ownership, licenses/provenance, contracts, finances, expenses, builds, roadmap, market research, forecasts, IP records, team information, and risk documentation.
Do not invent traction, revenue, users, valuations, or legal conclusions.
```

### Completion Gate
- Investor materials are internally consistent, evidence-backed, provenance-ready, and reviewed by the human owner; legal/financial claims requiring professionals are flagged for professional review.

---

# Simple Commands After Setup

Once AI-B has the permanent prompt and canonical docs loaded, normal commands can stay short:

```text
Execute Phase 13. Read the canonical docs first. Stop when its completion gate passes and report validation.
```

```text
Review Phase 13 against the canonical architecture. Return required fixes only.
```

```text
Run the relevant regression suite for the systems changed in Phase 13 and report failures with reproduction details.
```

# Universal Audit Command
```text
Audit the project before proceeding.
Read all canonical documents and inspect the current implementation.
Check architecture drift, UE 5.8.2 compatibility, build failures, stale documentation, provider-specific online leakage, listen-host assumptions, replication defects, hard-coded scalable content, missing tests, technical debt, security issues, save/version risks, provenance/license gaps, AI-tool coupling, and performance/network regressions.
Do not modify anything.
Return BLOCKER/HIGH/MEDIUM/LOW findings and state whether the next phase is safe to begin.
```
