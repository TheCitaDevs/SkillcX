# ARCHITECTURE.md

## 1. Purpose

This document defines the intended technical architecture for the Unreal Engine project. It establishes boundaries and responsibilities so AI agents and human developers extend the same system rather than creating parallel implementations.

Gameplay behavior that is not already approved in `GAME_RULES.md` remains subject to the `UNDECIDED` rule.

## 2. Architectural Principles

1. **Server authority first.**
2. **C++ core, thin Blueprint presentation layer.**
3. **Gameplay Ability System for scalable combat/RPG mechanics where appropriate.**
4. **Data-driven content over hard-coded per-content classes.**
5. **Composition over inheritance when practical.**
6. **Reusable frameworks before large-scale content production.**
7. **Deterministic and testable gameplay logic where practical.**
8. **Strict separation of gameplay state and presentation.**
9. **Versionable save data.**
10. **Automated tests for progression, networking, rewards, and persistence.**
11. **Engine-version discipline.** Unreal Engine 5.8.2 is the current development baseline; engine migration is a deliberate project decision, not an incidental tooling update.

## 3. Proposed Project Layers

### 3.1 Core Runtime Layer

Responsible for shared gameplay foundations and project-wide contracts.

Suggested responsibilities:

- core gameplay types;
- interfaces;
- shared tags/constants;
- gameplay event contracts;
- run/floor state contracts;
- common actor/component bases;
- error/result types;
- common serialization/versioning utilities.

### 3.2 Character Layer

Responsible for player-controlled and AI-controlled combatant foundations.

Suggested responsibilities:

- base combat character;
- player character;
- movement state;
- combat state;
- ability-system ownership/integration;
- damage/death state hooks;
- replication hooks;
- animation-facing state.

### 3.3 Ability/GAS Layer

Responsible for scalable RPG/combat mechanics.

Suggested elements:

- `UAbilitySystemComponent` integration;
- attribute sets;
- gameplay tags;
- gameplay abilities;
- gameplay effects;
- gameplay cues;
- ability-granting/removal helpers;
- costs/cooldowns;
- effect application helpers;
- authority/prediction policy.

Initial attributes should be minimal until approved. Health and Stamina are appropriate implementation foundations; additional RPG attributes are `UNDECIDED` until defined.

### 3.4 Combat Layer

Responsible for reusable action-combat rules.

Expected framework capabilities:

- attacks;
- hit detection;
- damage application;
- blocking;
- parrying;
- dodging/i-frame framework;
- stagger/poise foundation;
- death;
- combat events;
- targetability;
- AI-facing combat contracts.

Exact timing windows and formulas remain tuning data, not architecture.

### 3.5 Boss Layer

Bosses should primarily be built from reusable components and data definitions.

Suggested reusable concepts:

- boss base actor/character;
- boss state machine;
- attack definition;
- phase definition;
- target-selection policy;
- threat/aggro provider;
- movement policy;
- arena interaction interface;
- summon interface;
- enrage/modifier interface;
- stagger/death integration;
- reward completion event.

Avoid `Boss037.cpp`, `Boss038.cpp`, etc. unless a boss genuinely requires bespoke technology that cannot reasonably fit the approved framework.

### 3.6 Item/Inventory Layer

Data-driven definitions should support:

- item identity;
- item type;
- rarity;
- requirements/restrictions;
- stat modifiers;
- granted abilities/effects;
- affix hooks;
- inventory representation;
- equipment slots;
- serialization;
- comparison/querying.

Exact slot roster, item rarity tiers, trade rules, stack rules, and equip rules remain `UNDECIDED` unless explicitly approved.

### 3.7 Class/Progression Layer

The class framework must represent:

- class identity;
- hard restrictions;
- allowed equipment categories;
- allowed ability categories;
- progression hooks;
- multiclass compatibility;
- ascension state;
- milestone eligibility;
- save persistence.

Class compatibility should be expressed through data/tags/rules rather than scattered conditional checks.

### 3.8 Floor/Run Layer

The 100-floor structure must be data-driven.

A floor definition should be capable of referencing:

- floor number;
- biome/environment definition;
- encounter/boss definition;
- arena definition;
- difficulty tuning reference;
- reward/loot references;
- milestone/special encounter flags;
- presentation metadata.

Only a small number of test floors should exist before the framework is validated.

### 3.9 Rest Layer

Rest is a discrete synchronized gameplay state that gates progression actions.

Architecture should support:

- transition into Rest only after the post-boss loot step;
- player readiness/status;
- level/stat spending hooks;
- class progression hooks;
- multiclass/ascension milestone UI hooks;
- validation that restricted actions cannot be performed outside Rest;
- multiplayer synchronization.

Exact Rest duration, forced readiness, voting rules, and whether players can move freely during Rest are `UNDECIDED`.

### 3.10 Merchant Layer

Merchant progression must be decoupled from individual UI widgets.

Suggested concepts:

- merchant unlock state;
- sell permission state;
- sell transaction authority;
- valuation service/interface;
- merchant encounter/boss specialization;
- persistence.

Exact economy and floor placement remain `UNDECIDED`.

### 3.11 Save/Persistence Layer

Use versioned save structures.

Separate at minimum:

- permanent/profile progression;
- run/session state;
- user settings.

Which progression belongs in each category is `UNDECIDED` until formally specified.

Save architecture must support migration between schema versions where practical.

### 3.12 UI Layer

UI is presentation, not authority.

UI may:

- display replicated state;
- send validated requests/commands;
- present progression choices;
- show inventory/equipment;
- show party/boss/floor status.

UI must not:

- directly grant rewards;
- directly mutate authoritative progression;
- directly create items;
- directly decide class compatibility;
- directly modify server gameplay state without validated gameplay APIs.

### 3.13 Audio/VFX/Animation Layer

These systems should react to gameplay state through events, gameplay cues, animation interfaces, or presentation components.

Gameplay calculations must not depend on cosmetic VFX/audio implementation.

## 4. Networking and Online Services Model

### 4.0 Canonical Online Target

The game is an **online-reliant 4-player cooperative game**.

Architecture must assume:

- up to four remote player clients in one cooperative party/session;
- server-authoritative gameplay;
- online identity/authentication through an approved service/provider;
- online lobby/session creation, discovery/invite/join flow;
- network travel into gameplay;
- party/session state that survives map transitions as required;
- disconnect handling from the beginning;
- a future-safe reconnect path unless later explicitly rejected;
- no gameplay-critical dependency on a local host player existing.

Local PIE, localhost, or LAN testing is permitted for rapid debugging, but it is development tooling only. It does not replace remote-online validation.

The online-services integration should be wrapped behind project-owned interfaces/subsystems so a development provider or platform backend can change without rewriting gameplay systems. Unreal Online Services / Online Subsystem implementations may supply authentication, lobbies, sessions, presence, invites, and platform integration; gameplay code should depend on project abstractions rather than provider-specific calls scattered across game systems.

### 4.1 Authority

The server owns authoritative state for:

- damage;
- health/death;
- boss state;
- floor completion;
- EXP awards;
- loot generation;
- item ownership;
- inventory/equipment mutation;
- class progression;
- ascension;
- merchant unlocks;
- progression eligibility;
- save-authoritative game data.

### 4.2 Client Responsibilities

Clients may:

- gather input;
- predict approved responsive actions where Unreal/GAS supports it safely;
- render animation/VFX/audio/UI;
- request server-authoritative actions;
- display replicated results.

### 4.3 Multiplayer Safety Requirements

Every gameplay feature must explicitly consider:

- authority;
- replication;
- late join;
- disconnect;
- reconnect where supported;
- duplicate RPC/reward protection;
- race conditions;
- ownership;
- state recovery.

Late join and the final reconnect policy remain `UNDECIDED`, but architecture must deliberately preserve the ability to add reconnect and must record the session/player identifiers needed for state recovery.

### 4.4 Online Session Architecture

Create a project-owned online layer with clear responsibilities such as:

- authentication/identity adapter;
- party/lobby service;
- game-session service;
- invite/join adapter;
- connection/travel coordinator;
- network failure/disconnect handler;
- online-state diagnostics/logging;
- provider configuration isolated from gameplay code.

The initial provider is a replaceable implementation detail. Epic Online Services is the preferred **provisional development backend**. The initial Unreal adapter should prefer Online Subsystem EOS (OSS EOS) while Unreal's newer Online Services API remains a Beta feature; this choice must be re-evaluated against the exact Unreal version used for shipping. The final provider/platform combination remains subject to platform and publishing decisions.

### 4.5 Early Online Test Ground

The early multiplayer milestone must produce an online test ground that can:

1. authenticate or otherwise identify development users through the selected test backend;
2. create a private development lobby/session;
3. allow remote clients to discover, invite, or join using a deterministic test flow;
4. connect up to four player clients to the authoritative game instance;
5. transition all clients into the same graybox gameplay map;
6. replicate player spawn and movement correctly;
7. detect disconnect/network failure cleanly;
8. emit diagnostics sufficient for automated and manual debugging.

Local multi-client PIE remains useful for faster reproduction of replication bugs, but the phase gate requires a real remote-online path as well.

### 4.6 Server Topology

The final shipping topology is `UNDECIDED`.

The architecture must remain compatible with a dedicated-server target. Listen-server shortcuts may be used for development only when they do not create gameplay dependencies on the hosting player. Gameplay systems, persistence contracts, session state, and authority checks must work without assuming the server has a local player.

## 5. Recommended Data Strategy

Use Unreal-native data assets/tables/structured data where suitable.

Canonical scalable content candidates include:

- `BossDefinition`
- `BossPhaseDefinition`
- `AttackDefinition`
- `AbilityDefinition`
- `ItemDefinition`
- `WeaponDefinition`
- `ArmorDefinition`
- `AffixDefinition`
- `LootTableDefinition`
- `ClassDefinition`
- `MulticlassDefinition`
- `AscensionDefinition`
- `FloorDefinition`
- `BiomeDefinition`
- `MerchantDefinition`

The exact Unreal representation (`UPrimaryDataAsset`, Data Table row, config struct, etc.) should be chosen based on runtime/editor needs rather than ideology.

## 6. Gameplay Tag Strategy

Gameplay tags should form a shared vocabulary, not an unbounded dumping ground.

Potential namespaces:

- `State.*`
- `Ability.*`
- `Effect.*`
- `Damage.*`
- `Status.*`
- `Class.*`
- `Equipment.*`
- `Boss.*`
- `Floor.*`
- `Progression.*`
- `UI.*`

Actual tags must be introduced as systems require them and documented.

## 7. Suggested Unreal Module Boundaries

Initial project organization may use one gameplay module with folders or multiple modules depending on build complexity. Do not create excessive modules prematurely.

Logical boundaries to preserve regardless of physical module structure:

- Core
- Characters
- Combat
- Abilities
- Bosses
- Items
- Inventory
- Classes
- Progression
- Floors
- Merchants
- SaveSystem
- Networking
- UI
- Tests

## 8. Blueprint Policy

Blueprint is approved for:

- presentation subclasses;
- animation blueprints;
- Niagara/VFX hookups;
- material configuration;
- UI widgets;
- level scripting with minimal gameplay authority;
- designer configuration;
- data-asset authoring;
- cinematic/Sequencer work;
- thin integration glue.

Blueprint is discouraged for:

- authoritative inventory logic;
- class compatibility logic;
- save-format rules;
- reward generation;
- boss framework state machines at scale;
- core combat calculations;
- large replicated gameplay systems.

Any exception should be documented with rationale.

## 9. Automation Architecture

The project should eventually provide scripts/tools for:

- build/compile;
- automated tests;
- multiplayer test launch;
- data validation;
- asset validation;
- balance simulation;
- content import;
- build packaging;
- license/provenance checks.

Automation must produce machine-readable output where practical.

## 10. AI-Generated Content Integration

AI-generated content is treated as source material, not automatically approved production content.

Pipeline:

1. generation;
2. provenance capture;
3. technical validation;
4. human review;
5. modification/cleanup where necessary;
6. import into approved project location;
7. shipping-status approval.

No AI model should be a required runtime dependency without a new explicit decision.

## 11. Content Factory Principle

Before generating Floors 11-100 at scale, the project must possess validated factories for:

- bosses;
- items;
- classes/progression content;
- floors;
- art production;
- asset validation;
- QA/regression.

Mass content generation before those factories exist is prohibited by development policy.

## 12. Architecture Freeze Target

After a polished Floors 1-10 vertical slice proves the complete loop, perform a technical audit and create an architecture-freeze milestone.

After freeze, Floors 11-100 should primarily add content through existing systems. New foundational systems require explicit justification and review.

## 13. Known Architectural Unknowns

The following are intentionally unresolved:

- final shipping topology (dedicated server, listen server, or approved hybrid);
- final online provider/platform-service combination at ship time;
- final matchmaking/discovery UX and policy;
- crossplay;
- permanent vs run-specific progression split;
- exact save topology;
- full stat system;
- revive/death/wipe rules;
- item ownership/distribution model;
- procedural floor generation extent;
- anti-cheat requirements;
- backend/account requirements;
- platform targets beyond initial PC assumption (if any).

These must remain `UNDECIDED` until approved.


## 14. Unreal Engine 5.8.2 Development Baseline

The current project development baseline is **Unreal Engine 5.8.2**.

Requirements:

- do not silently upgrade or downgrade the engine;
- keep plugins pinned/recorded by version where practical;
- after any approved engine upgrade, run clean builds, automated tests, remote-online tests, packaging tests, and an asset/content validation pass before continuing feature work;
- use UE 5.8.2 documentation/API behavior when implementing engine-specific code unless a later locked decision supersedes this baseline;
- for Windows development, prefer the UE 5.8-supported toolchain documented by Epic, while recording the exact compiler/SDK used by the project.

### 14.1 Unreal MCP

UE 5.8 includes an **Experimental** Unreal MCP plugin that can expose editor tools to MCP-compatible AI agents. It may be used as an editor-development accelerator for bounded tasks such as actor placement, material-instance setup, PCG experimentation, inspection, and automation-test invocation.

It is **not** a shipping dependency and may not become required runtime functionality. Because the feature is Experimental and its APIs are incomplete/changeable, critical project automation must still have non-MCP source/build/test paths where practical. AI agents using Unreal MCP must execute bounded, reviewable tasks and must not issue overlapping editor tool calls.


## 12. AI-Operated Development Architecture

### 12.1 Principle
AI operates Unreal and the surrounding toolchain; it does not replace engine systems that already solve the problem. Prefer Unreal-native Character Movement, GAS, PCG, Control Rig, IK Retargeting, Niagara, Chaos, UMG/Common UI, Online Subsystem/Services adapters, Automation, Gauntlet, and UAT where appropriate.

### 12.2 Local Lead Engineer
Qwen Code is the current agent shell. Its default low-cost model is local `gpt-oss-20b` through an OpenAI-compatible endpoint. The agent must be replaceable: project rules, tools, tests, and documentation may not depend on one model vendor.

### 12.3 Unreal MCP Boundary
Unreal MCP is a **development/editor automation bridge** only. It may inspect and operate approved editor functionality, but:

- it must remain local by default;
- it must not be exposed publicly without an approved security design;
- experimental MCP behavior may not become a runtime gameplay dependency;
- changes must remain source-controlled and reversible;
- destructive operations require staging/sandbox/worktree discipline;
- the authoritative shipping game must function with the MCP tooling absent.

### 12.4 Asset Production Pipeline
Approved production flow:

`approved specification -> concept/reference -> human selection -> 3D/source creation -> Blender validation/processing -> provenance check -> Unreal staging import -> technical validation -> human approval -> production content`

No generated asset enters final production Content automatically.

### 12.5 Automation Contract
Every reusable gameplay framework should expose enough deterministic state/events for automated validation. AI-B should be able to compile, launch tests, collect logs, identify deterministic failures, fix technical defects, and rerun tests without manual copying of errors where practical.
