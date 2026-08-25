# GAME_RULES.md

## 1. Purpose

This file is the canonical gameplay-rules registry.

Every rule is labeled with one of:

- `LOCKED`
- `PROVISIONAL`
- `UNDECIDED`
- `DEPRECATED`

AI agents must not convert an `UNDECIDED` rule into a chosen design without explicit authorization.

---

## 2. Game Structure

### GR-001 — Floor Count
**Status:** LOCKED

The game is structured around **100 floors**.

### GR-002 — Core Encounter Style
**Status:** LOCKED

The game is a **3D third-person cooperative boss-rush roguelike**.

### GR-003 — Boss Distribution
**Status:** PROVISIONAL

The intended default is one primary boss/special boss encounter per floor, but the exact treatment of nonstandard floors is not fully defined.

### GR-004 — Non-Boss Combat Between Bosses
**Status:** UNDECIDED

It is not yet canonical whether floors may include regular enemies, traversal encounters, minibosses, environmental challenges, or only the main boss encounter.

---

## 3. Canonical Post-Boss Sequence

### GR-010 — EXP Timing
**Status:** LOCKED

Eligible players receive EXP **immediately when the boss is defeated**.

### GR-011 — Shared Loot Chest
**Status:** LOCKED

After the boss is defeated, a **shared loot chest** appears or becomes available.

### GR-012 — Loot Before Rest
**Status:** LOCKED

Players collect/resolve loot **before** entering the Rest progression phase.

### GR-013 — Rest-Gated Progression
**Status:** LOCKED

Level-up spending, stat allocation, and class progression decisions may occur **only while Resting**.

### GR-014 — Exact Loot Distribution
**Status:** UNDECIDED

The term "shared loot chest" does not yet define whether:

- all players see the same items;
- items are personal but presented through one chest;
- loot uses need/greed;
- first-pick ownership exists;
- duplicate items can be claimed by multiple players;
- loot is instanced per player.

No implementation may assume one of these models without approval.

### GR-015 — Unclaimed Loot Behavior
**Status:** UNDECIDED

What happens to unclaimed loot when leaving the loot phase is not yet defined.

---

## 4. Leveling and Stats

### GR-020 — EXP and Spending Separation
**Status:** LOCKED

EXP is earned immediately on boss defeat, but progression spending is deferred until Rest.

### GR-021 — Character Level Cap
**Status:** UNDECIDED

### GR-022 — Stat Roster
**Status:** UNDECIDED

### GR-023 — Stat Allocation Formula
**Status:** UNDECIDED

### GR-024 — Respec Rules
**Status:** UNDECIDED

### GR-025 — Permanent vs Run-Specific Character Progression
**Status:** UNDECIDED

It is not yet canonical which progression survives run failure/new runs.

---

## 5. Classes

### GR-030 — Hard Class Restrictions
**Status:** LOCKED

Classes impose meaningful hard restrictions.

Example: a base Knight cannot simply use unrestricted general magic because a spell or magical item exists.

### GR-031 — Restriction Categories
**Status:** PROVISIONAL

The class system is expected to be able to restrict equipment, abilities, or other gameplay categories through explicit data/tags.

Exact restrictions are class-specific and not yet defined.

### GR-032 — Base Class Roster
**Status:** UNDECIDED

### GR-033 — Starting Class Selection Rules
**Status:** UNDECIDED

### GR-034 — Class Switching Outside Milestones
**Status:** UNDECIDED

Unless explicitly approved later, do not assume players can freely change classes.

---

## 6. Multiclass and Ascension

### GR-040 — Milestone Frequency
**Status:** LOCKED

Class progression milestones occur every **10 bosses/floors cleared**.

### GR-041 — Multiclass Choice Count
**Status:** LOCKED

At each milestone, the player receives exactly **3 RNG multiclass choices**.

### GR-042 — Compatibility Requirement
**Status:** LOCKED

Only multiclasses compatible with the player's current class state may appear in the 3-choice pool.

### GR-043 — Ascension Alternative
**Status:** LOCKED

The player may reject the 3 multiclass choices and instead ascend the current class by **+1**.

### GR-044 — Rest Requirement
**Status:** LOCKED

The multiclass/ascension choice is made only during Rest.

### GR-045 — Ascension After Multiclass
**Status:** LOCKED

Ascension tracks may change after multiclassing.

### GR-046 — Maximum Ascension Level
**Status:** UNDECIDED

### GR-047 — Maximum Multiclass Depth
**Status:** UNDECIDED

### GR-048 — Re-Rolling Multiclass Choices
**Status:** UNDECIDED

### GR-049 — Compatibility Graph
**Status:** UNDECIDED

The actual class-to-multiclass compatibility graph is not yet defined.

### GR-050 — Multiclass Stat/Ability Inheritance
**Status:** UNDECIDED

---

## 7. Merchant Bosses and Selling

### GR-060 — Merchant Bosses Exist
**Status:** LOCKED

Special merchant-boss encounters appear between milestone sections.

### GR-061 — Selling Unlock
**Status:** LOCKED

Defeating the appropriate merchant boss unlocks the ability to sell unwanted gear.

### GR-062 — Exact Merchant Placement
**Status:** UNDECIDED

The precise floor numbers/timing are not yet canonical.

### GR-063 — Buying Items
**Status:** UNDECIDED

The current locked rule only establishes selling unlock. Buying behavior is not yet defined.

### GR-064 — Currency
**Status:** UNDECIDED

### GR-065 — Sell Values
**Status:** UNDECIDED

### GR-066 — Merchant Persistence
**Status:** UNDECIDED

---

## 8. Combat

### GR-070 — Perspective
**Status:** LOCKED

Combat is played in third person.

### GR-071 — Real-Time Action Combat
**Status:** PROVISIONAL

The project architecture assumes real-time action combat with movement, attacks, dodging, blocking/parrying hooks, hit reactions, and boss telegraphs.

Exact mechanics remain subject to playtesting and approval.

### GR-072 — Friendly Fire
**Status:** UNDECIDED

### GR-073 — Lock-On System
**Status:** UNDECIDED

### GR-074 — Stamina
**Status:** PROVISIONAL

Stamina is an approved foundational attribute for prototyping, but exact stamina mechanics and whether all classes use it identically remain undecided.

### GR-075 — Poise/Stagger
**Status:** PROVISIONAL

A reusable poise/stagger framework is approved for prototyping. Exact rules remain tuning/design data.

### GR-076 — Damage Types
**Status:** UNDECIDED

### GR-077 — Status Effects
**Status:** UNDECIDED

### GR-078 — Boss Enrage Timers
**Status:** UNDECIDED

---

## 9. Multiplayer and Co-op

### GR-080 — Multiplayer From Beginning
**Status:** LOCKED

The game must be architected for multiplayer from the beginning.

### GR-081 — Server Authority
**Status:** LOCKED

Gameplay outcomes affecting combat, rewards, progression, inventory, or encounter state are server authoritative.

### GR-082 — Player Count
**Status:** LOCKED

The game is designed around a maximum party of **4 players** participating cooperatively online.

The architecture must support testing with fewer than 4 connected players, but systems may not assume that fewer players are the canonical shipping experience.

### GR-083 — Revive System
**Status:** UNDECIDED

A revive-capable framework may be prototyped, but exact revive rules are not canonical.

### GR-084 — Party Wipe Behavior
**Status:** UNDECIDED

### GR-085 — Late Join
**Status:** UNDECIDED

### GR-086 — Reconnect
**Status:** UNDECIDED

### GR-087 — Online Session/Lobby Foundation
**Status:** LOCKED

Online identity and an online session/lobby connection path must be planned and implemented early enough that remote multiplayer is continuously testable during development.

The exact final matchmaking UX, discovery policy, invites/friends flow, and platform-specific presentation remain `UNDECIDED`.

### GR-088 — Dedicated Server Requirement
**Status:** UNDECIDED

The shipping game is online-reliant, but the final server-hosting topology (dedicated server, listen server, or approved hybrid) is not yet canonical. Architecture must preserve a viable dedicated-server path and must not depend on a local host player existing.

### GR-088A — Local Multiplayer Role
**Status:** LOCKED

Local multiplayer/LAN/PIE multi-client play is a development and debugging convenience only. It is not a required player-facing mode and it is not sufficient proof that the shipping online path works.

### GR-088B — Remote Online Test Gate
**Status:** LOCKED

Before large-scale gameplay/content production, the project must demonstrate a real remote-online test in which four client instances can authenticate/connect through the selected online session/service path and enter the same authoritative game session.

### GR-089 — PvP
**Status:** UNDECIDED

Do not add PvP unless explicitly approved.

---

## 10. Loot and Equipment

### GR-100 — Loot Exists
**Status:** LOCKED

Boss encounters feed a post-boss loot step through the shared chest.

### GR-101 — Item Rarity
**Status:** PROVISIONAL

The architecture should support rarity, but final rarity tiers/names are undecided.

### GR-102 — Equipment Slots
**Status:** UNDECIDED

### GR-103 — Weapon Categories
**Status:** UNDECIDED

### GR-104 — Armor Categories
**Status:** UNDECIDED

### GR-105 — Item Affixes
**Status:** PROVISIONAL

The architecture may support affixes/passives, but final rules are undecided.

### GR-106 — Trading Between Players
**Status:** UNDECIDED

### GR-107 — Dropping Items
**Status:** UNDECIDED

### GR-108 — Inventory Limits
**Status:** UNDECIDED

---

## 11. Floor Progression and Run Rules

### GR-120 — Sequential Floor Structure
**Status:** PROVISIONAL

The initial implementation should assume sequential floor progression from lower to higher floors.

### GR-121 — Floor Skipping
**Status:** UNDECIDED

### GR-122 — Checkpoints
**Status:** UNDECIDED

### GR-123 — Continue After Failure
**Status:** UNDECIDED

### GR-124 — Run Reset Rules
**Status:** UNDECIDED

### GR-125 — Procedural Floor Layouts
**Status:** UNDECIDED

The project may use procedural assembly, but the extent to which floor geometry is procedurally generated is not yet canonical.

### GR-126 — Floor Modifiers
**Status:** PROVISIONAL

The architecture may support floor modifiers for scalable content, but final gameplay rules are undecided.

---

## 12. Boss Design Rules

### GR-140 — Boss Framework Reuse
**Status:** LOCKED (Production Rule)

The project should build bosses from reusable frameworks/data wherever possible instead of 100 unrelated hard-coded implementations.

### GR-141 — Unique Boss Identity
**Status:** LOCKED (Design Goal)

Internal system reuse must not prevent bosses from feeling meaningfully distinct to players.

### GR-142 — Milestone Boss Importance
**Status:** PROVISIONAL

Milestone floors, especially 10-floor boundaries and Floor 100, are expected to receive additional bespoke design attention.

### GR-143 — Exact Boss Archetype Count
**Status:** UNDECIDED

### GR-144 — Boss Phase Count
**Status:** UNDECIDED

Bosses are not required to have the same number of phases.

---

## 13. Runtime Generative AI

### GR-160 — Development-First AI Usage
**Status:** LOCKED

Generative AI is primarily a development/content-production tool.

### GR-161 — Runtime AI Dependency
**Status:** UNDECIDED / NOT APPROVED

No runtime generative model, cloud LLM, generative NPC system, or similar dependency may be added without an explicit future decision.

---

## 14. Commercial Rules

### GR-180 — Commercial Shipping Goal
**Status:** LOCKED

The game must be capable of commercial release.

### GR-181 — Provenance Requirement
**Status:** LOCKED

Every AI-generated and third-party production asset must have provenance and licensing records.

### GR-182 — Unknown License Handling
**Status:** LOCKED

Unknown or unresolved commercial-use status means the asset is **not approved for shipping**.

---

## 15. High-Priority UNDECIDED Questions

These should be resolved before or during the vertical-slice phase, not guessed by implementation AIs:

1. Permanent progression vs run-only progression.
2. Death/downed/revive/wipe rules.
3. Shared-loot ownership/distribution behavior.
4. Base class roster.
5. Core stat roster and formulas.
6. Exact merchant-boss placement and economy.
7. Ascension maximum and multiclass depth.
8. Save/checkpoint/run-reset model.
9. Floor composition beyond boss arenas.
10. Final matchmaking/discovery UX and shipping hosting topology.
11. Initial platform target(s).
