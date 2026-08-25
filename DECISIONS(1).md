# DECISIONS.md

## 1. Purpose

This is the canonical decision log.

It records approved, provisional, unresolved, deprecated, and superseded decisions so future AI agents can understand **why** the project is structured the way it is.

Do not delete old decisions. Supersede or deprecate them explicitly.

## 2. Decision Entry Format

Each decision should contain:

- ID
- Status
- Date
- Decision
- Rationale
- Consequences
- Supersedes / Superseded By (if applicable)

---

## D-001 — 100-Floor Structure

**Status:** LOCKED  
**Date:** 2026-08-23

**Decision:** The game uses a 100-floor progression structure.

**Rationale:** Core product premise.

**Consequences:** Floor, boss, progression, difficulty, content-production, save, and QA systems must scale to 100 floors without requiring 100 bespoke code paths.

---

## D-002 — Genre and Perspective

**Status:** LOCKED  
**Date:** 2026-08-23

**Decision:** The game is a 3D third-person cooperative boss-rush roguelike.

**Rationale:** Core product identity.

**Consequences:** Movement, camera, combat readability, animation, networking, encounter design, and UI must support third-person co-op action.

---

## D-003 — Post-Boss Reward Order

**Status:** LOCKED  
**Date:** 2026-08-23

**Decision:** Boss defeat -> immediate EXP -> shared loot chest -> loot resolution -> Rest.

**Rationale:** Established progression loop.

**Consequences:** Systems must expose explicit phase/state transitions and prevent Rest-gated progression before loot resolution.

---

## D-004 — Rest-Gated Progression

**Status:** LOCKED  
**Date:** 2026-08-23

**Decision:** Level-up spending, stat allocation, and class progression occur only during Rest.

**Rationale:** Established progression pacing rule.

**Consequences:** UI and gameplay APIs must reject those actions outside Rest.

---

## D-005 — Hard Class Restrictions

**Status:** LOCKED  
**Date:** 2026-08-23

**Decision:** Classes have hard gameplay restrictions. A base Knight, for example, cannot simply use unrestricted general magic.

**Rationale:** Class identity must materially affect play/build options.

**Consequences:** Equipment and ability validation must use authoritative class-compatibility rules rather than UI-only restrictions.

---

## D-006 — Ten-Floor Multiclass Milestones

**Status:** LOCKED  
**Date:** 2026-08-23

**Decision:** Every 10 bosses/floors cleared, the player receives exactly 3 RNG multiclass choices compatible with the current class state.

**Rationale:** Established class progression structure.

**Consequences:** Milestone tracking, deterministic/save-safe RNG state, compatibility validation, and Rest UI are required.

---

## D-007 — Ascension Alternative

**Status:** LOCKED  
**Date:** 2026-08-23

**Decision:** At each 10-floor class milestone, the player may reject all 3 multiclass choices and instead ascend the current class by +1.

**Rationale:** Established alternative progression path.

**Consequences:** Class data must support ascension state independently from multiclass choice state.

---

## D-008 — Ascension May Change After Multiclass

**Status:** LOCKED  
**Date:** 2026-08-23

**Decision:** Ascension tracks may change after multiclassing.

**Rationale:** Established class-design rule.

**Consequences:** Ascension cannot be modeled as a single universal linear integer detached from class composition. Data must allow class-state-dependent ascension definitions.

---

## D-009 — Merchant Boss Selling Unlock

**Status:** LOCKED  
**Date:** 2026-08-23

**Decision:** Special merchant-boss encounters appear between milestone sections, and defeating the appropriate merchant boss unlocks selling unwanted gear.

**Rationale:** Established economy/progression structure.

**Consequences:** Merchant unlock state must be authoritative and persistable. Exact floor placement remains undecided.

---

## D-010 — Unreal Engine + C++ Core

**Status:** LOCKED  
**Date:** 2026-08-23

**Decision:** Unreal Engine is the target engine and core gameplay logic uses Unreal C++. The current locked development baseline is Unreal Engine 5.8.2 as defined by D-035.

**Rationale:** Required technical direction for scalable, AI-readable, multiplayer-capable implementation.

**Consequences:** Blueprint is not the primary location for core authoritative gameplay.

---

## D-011 — Server-Authoritative Gameplay

**Status:** LOCKED  
**Date:** 2026-08-23

**Decision:** Gameplay-critical state is server authoritative.

**Rationale:** Co-op correctness, fairness, persistence, exploit resistance, and deterministic progression.

**Consequences:** Damage, rewards, inventory mutation, progression, floor completion, and similar state must be validated server-side.

---

## D-012 — Gameplay Ability System

**Status:** LOCKED  
**Date:** 2026-08-23

**Decision:** Use Unreal Gameplay Ability System where appropriate.

**Rationale:** Scalable framework for attributes, abilities, effects, tags, costs, cooldowns, cues, and multiplayer behavior.

**Consequences:** Combat/RPG architecture should integrate GAS rather than reinventing overlapping systems, while avoiding unnecessary GAS use where simpler systems are better.

---

## D-013 — Data-Driven Scalable Content

**Status:** LOCKED  
**Date:** 2026-08-23

**Decision:** Scalable game content is data-driven wherever practical.

**Rationale:** The 100-floor scope is not feasible if every boss/item/floor requires bespoke code.

**Consequences:** Build schemas/factories first, validate them, then generate/author content at scale.

---

## D-014 — Thin Blueprint Layer

**Status:** LOCKED  
**Date:** 2026-08-23

**Decision:** Blueprints primarily handle presentation, configuration, animation, VFX, UI, level assembly, and thin glue logic.

**Rationale:** Keeps core logic reviewable, testable, source-controlled, and AI-readable.

**Consequences:** Large authoritative gameplay systems should not default to Blueprint.

---

## D-015 — Development-Time Generative AI

**Status:** LOCKED  
**Date:** 2026-08-23

**Decision:** Generative AI is primarily used during development rather than required during normal gameplay.

**Rationale:** Cost, latency, determinism, QA, networking, moderation, hardware, and commercial risk are lower when shipped gameplay is deterministic.

**Consequences:** Runtime generative AI requires a separate explicit future decision.

---

## D-016 — Commercial Provenance Requirement

**Status:** LOCKED  
**Date:** 2026-08-23

**Decision:** Every AI-generated or third-party asset must have provenance and licensing records before shipping approval.

**Rationale:** Commercial due diligence and IP hygiene.

**Consequences:** Unknown commercial-use status means the asset cannot be approved for release.

---

## D-017 — Vertical Slice Before Mass Production

**Status:** LOCKED (Production Decision)  
**Date:** 2026-08-23

**Decision:** Build and polish Floors 1-10 before mass-producing Floors 11-100.

**Rationale:** The content factory must be proven before scale.

**Consequences:** Do not batch-generate final bosses/items/floors for the full game before the core loop, schemas, automation, and QA are validated.

---

## D-018 — Player Count

**Status:** DEPRECATED  
**Date:** 2026-08-23

**Decision:** Target co-op player count had not yet been chosen.

**Rationale:** Superseded by explicit product direction on 2026-08-24.

**Consequences:** See D-029.

**Superseded By:** D-029

---

## D-019 — Shared Loot Ownership Model

**Status:** UNDECIDED  
**Date:** 2026-08-23

**Decision:** The shared chest exists, but ownership/distribution behavior is not defined.

**Rationale:** "Shared chest" does not uniquely define personal, shared, instanced, roll-based, or first-claim loot.

**Consequences:** Build loot generation interfaces without locking in a final distribution policy until approved.

---

## D-020 — Permanent vs Run Progression

**Status:** UNDECIDED  
**Date:** 2026-08-23

**Decision:** The split between permanent/profile progression and run-specific progression is not defined.

**Rationale:** Roguelike structure alone is insufficient to infer persistence rules.

**Consequences:** Save architecture should separate categories cleanly and avoid irreversible assumptions.

---

## D-021 — Death / Downed / Revive / Wipe Rules

**Status:** UNDECIDED  
**Date:** 2026-08-23

**Decision:** Exact co-op failure rules are not defined.

**Rationale:** Not specified.

**Consequences:** A reusable state framework may be prototyped, but penalties, revive counts, timers, wipe consequences, and recovery behavior require approval.

---

## D-022 — Base Class Roster

**Status:** UNDECIDED  
**Date:** 2026-08-23

**Decision:** Final base class list is not yet canonical.

**Rationale:** Only Knight is established as an example of hard restrictions.

**Consequences:** Class framework must be generic.

---

## D-023 — Core Stat Roster

**Status:** UNDECIDED  
**Date:** 2026-08-23

**Decision:** Final player stats and formulas are not defined.

**Rationale:** Not specified.

**Consequences:** Prototype may begin with minimal health/stamina foundations; do not establish final RPG formulas.

---

## D-024 — Merchant Placement/Economy

**Status:** UNDECIDED  
**Date:** 2026-08-23

**Decision:** Exact merchant-boss floor placement, pricing, currency, buying rules, and economy are not defined.

**Rationale:** Only the selling unlock is locked.

**Consequences:** Implement merchant functionality through data/interfaces rather than fixed floor numbers/formulas.

---

## D-025 — Ascension Cap and Multiclass Depth

**Status:** UNDECIDED  
**Date:** 2026-08-23

**Decision:** Maximum ascension and maximum multiclass depth are not defined.

**Rationale:** Not specified.

**Consequences:** Data structures should not assume a fixed maximum unless required for technical safety.

---

## D-026 — Online Topology

**Status:** DEPRECATED  
**Date:** 2026-08-23

**Decision:** Shipping topology and online-service timing were previously left broadly unresolved, with local server/client testing treated as the early baseline.

**Rationale:** Superseded by explicit direction that the product is online-reliant and that real online testing must be planned and introduced early.

**Consequences:** See D-030 and D-031.

**Superseded By:** D-030, D-031

---

## D-027 — Platform Targets

**Status:** UNDECIDED  
**Date:** 2026-08-23

**Decision:** Final launch platform list is not canonical.

**Rationale:** Not specified.

**Consequences:** Avoid platform-specific dependencies during early architecture unless explicitly approved.

---

## D-028 — Floor Content Beyond Bosses

**Status:** UNDECIDED  
**Date:** 2026-08-23

**Decision:** The amount of traversal, regular enemies, puzzles, hazards, minibosses, or procedural rooms outside the principal boss encounter is not yet defined.

**Rationale:** Boss-rush identity does not determine exact inter-boss content.

**Consequences:** Floor schema should allow optional content without requiring it.

---

## D-029 — Four-Player Online-Reliant Co-op

**Status:** LOCKED  
**Date:** 2026-08-24

**Decision:** The canonical product target is a **4-player online-reliant cooperative game**. Four remote players are the intended full-party experience. Local multiplayer is not a required shipping mode.

**Rationale:** Explicit product direction. The architecture should optimize for the actual intended player experience rather than treat online play as a later platform feature.

**Consequences:** Player/session systems, UI, encounter scaling hooks, replication testing, party state, rewards, and QA must support four online clients. Fewer-player sessions may be supported/tested, but the project may not be architected around local multiplayer as the primary mode.

**Supersedes:** D-018

---

## D-030 — Early Online Services and Remote Test Path

**Status:** LOCKED  
**Date:** 2026-08-24

**Decision:** Online identity plus lobby/session/join functionality must be planned from project bootstrap and integrated early in development. Before combat/content production scales up, the project must demonstrate a real remote-online development session with four clients using the selected online-service/session path.

**Rationale:** Replication alone is not equivalent to a production online flow. Authentication, session lifecycle, travel, ownership, disconnects, and provider behavior are expensive to retrofit after gameplay systems are deeply coupled to local assumptions.

**Consequences:** The early networking stage must include an **Online Multiplayer Foundation** before GAS/combat development scales up; it is not a local-multiplayer-only milestone. Local PIE/localhost testing remains allowed for quick debugging but cannot satisfy the online milestone by itself. Online provider calls should be isolated behind project-owned interfaces/subsystems. Exact roadmap phase numbers are operational and may change without altering this locked decision.

**Supersedes:** Part of D-026

---

## D-031 — Shipping Server Topology Remains Open, Dedicated Path Preserved

**Status:** LOCKED  
**Date:** 2026-08-24

**Decision:** The game must remain technically compatible with a dedicated-server architecture even though the final shipping hosting model (dedicated, listen, or approved hybrid) is not yet selected.

**Rationale:** An online-reliant four-player game should not accidentally become dependent on a host player's local world or identity before hosting cost, platform requirements, matchmaking, persistence, and publishing strategy are finalized.

**Consequences:** Authoritative gameplay code must not assume a local player exists on the server. A listen server may be used as a development convenience, but systems must be testable against a headless/dedicated server target. Final hosting topology remains a separate future decision.

---

## D-032 — Initial Online Provider Strategy

**Status:** PROVISIONAL  
**Date:** 2026-08-24

**Decision:** Use a provider-abstracted online layer with Epic Online Services as the preferred initial development backend. For the initial Unreal integration, prefer **Online Subsystem EOS (OSS EOS)** over hard-wiring gameplay to Unreal's newer Online Services API while the latter remains a Beta feature. Re-evaluate this adapter if the engine baseline changes, platform requirements change, Epic changes the relevant API maturity/support status, or the project approaches shipping.

**Rationale:** The project needs a real remote-online test path early, while final launch platforms and cross-platform requirements remain unresolved. The adapter must favor a stable shipping path without making gameplay code depend directly on EOS or any one Unreal online API generation.

**Consequences:** The project-owned online layer exposes identity/authentication, session creation/search/join, invites where available, connection/travel coordination, and failure diagnostics. Provider credentials/product IDs stay outside source control. The OSS EOS adapter can later be replaced by Unreal Online Services, a platform-native implementation, or another approved backend without rewriting combat, progression, floor, or party gameplay systems. This decision must be re-reviewed when the project's shipping Unreal version/platform targets are locked.



---

## D-033 — Unreal Engine 5.8.1 Development Baseline

**Status:** SUPERSEDED by D-035  
**Date:** 2026-08-24

**Decision:** Development begins on **Unreal Engine 5.8.1**. Future engine upgrades are allowed only through an explicit reviewed migration decision.

**Rationale:** The production roadmap and AI instructions need one exact engine/API/toolchain baseline. Silent engine migration would make generated code, plugins, online behavior, tests, and editor automation unreliable.

**Consequences:** AI agents must implement against UE 5.8.1 behavior/documentation unless superseded. Engine upgrades require clean builds, regression testing, remote-online testing, packaging validation, and canonical-document updates.

---

## D-034 — Unreal MCP Is Development-Only Acceleration

**Status:** PROVISIONAL  
**Date:** 2026-08-24

**Decision:** UE 5.8.2's Experimental Unreal MCP plugin may be used to let approved MCP-compatible AI agents perform bounded editor tasks. It is not a runtime dependency and cannot be required for the shipped game.

**Rationale:** UE 5.8 adds useful agentic editor access, but Epic marks the feature Experimental and documents incomplete/changeable APIs.

**Consequences:** Use MCP for supervised editor automation, inspection, PCG experimentation, material/actor setup, and automation-test invocation where it saves time. Maintain source/build/test paths that do not depend solely on MCP, execute tool calls serially, and review editor changes before acceptance.


---

## D-035 — Unreal Engine 5.8.2 Development Baseline

**Status:** LOCKED (Current Development Baseline)  
**Date:** 2026-08-25

**Decision:** Development baseline is **Unreal Engine 5.8.2**. Engine changes require an explicit reviewed migration decision and regression pass.

**Rationale:** UE 5.8.2 is the current approved baseline and supersedes D-033.

**Consequences:** All AI prompts, build scripts, plugin checks, documentation, online adapter reviews, test infrastructure, and editor automation target UE 5.8.2 until changed explicitly.

**Supersedes:** D-033

---

## D-036 — AI-First, Tool-Operating Development Model

**Status:** LOCKED  
**Date:** 2026-08-25

**Decision:** AI is used to perform as much repeatable development work as practical, while mature Unreal-native systems remain the implementation substrate. AI should operate/configure Unreal systems rather than recreate Character Movement, GAS, PCG, Control Rig, Niagara, Chaos, UMG/Common UI, online frameworks, build automation, or test frameworks without justification.

**Consequences:** Human work is concentrated on direction, approval, playtesting, unresolved design decisions, business/legal decisions, and exceptions.

---

## D-037 — Local-First Lead Engineer Baseline

**Status:** PROVISIONAL TOOLING BASELINE  
**Date:** 2026-08-25

**Decision:** Use **Qwen Code** as the primary agent shell and a local **gpt-oss-20b** OpenAI-compatible endpoint as the default low-cost engineering model. Stronger or cloud models are escalation tools, not mandatory production dependencies.

**Consequences:** Canonical documentation and tool contracts must remain model-agnostic enough to swap models without redesigning the project. Credentials and provider configuration stay out of source control.

---

## D-038 — Unreal MCP Development Bridge

**Status:** PROVISIONAL TOOLING BASELINE  
**Date:** 2026-08-25

**Decision:** Use Unreal Engine 5.8.2 Unreal MCP where it materially reduces manual editor work. MCP remains development-only, local-first, reversible, and non-essential to the shipping runtime.

**Consequences:** Experimental MCP APIs may change; automation must fail safely. MCP is never a gameplay dependency.

**Extends:** D-034

---

## D-039 — Commercial AI Content Baselines

**Status:** PROVISIONAL TOOLING BASELINE  
**Date:** 2026-08-25

**Decision:** Current low-cost production candidates are ComfyUI + FLUX.2 [klein] 4B for local image generation/editing, Meshy for paid commercial 3D generation when needed, Blender 5.2 LTS for scripted 3D processing, and Stable Audio 3.0 for licensed-data audio generation under the applicable license.

**Consequences:** Every production output requires provenance, license capture, human approval, and technical validation. A tooling substitution is allowed only if commercial rights and provenance are at least as clear.

---

## D-040 — Perforce P4 Source-Control Baseline

**Status:** PROVISIONAL TOOLING BASELINE  
**Date:** 2026-08-25

**Decision:** Use self-hosted Perforce P4 as the initial source-control baseline for Unreal binary assets and project history.

**Consequences:** AI changes must be reversible; generated/cache/build outputs are excluded appropriately; backup/restore is tested before autonomous modification begins.

---

## D-041 — Production Priority Order

**Status:** LOCKED  
**Date:** 2026-08-25

**Decision:** When implementation tradeoffs conflict, prioritize: (1) scalability, (2) multiplayer authority, (3) automation, (4) AI operability, (5) commercial shipping, (6) low development cost.

**Consequences:** Cheap or fast solutions that violate authority, scalability, or shipping rights are rejected.
