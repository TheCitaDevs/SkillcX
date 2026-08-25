# STATE.md

## 1. Current Canonical Revision
**Revision:** UE5.8.2-AI-FIRST-2026-08-25  
**Date:** 2026-08-25

The prior UE 5.8.1 canonical package is superseded for active development by this UE 5.8.2 package. Historical decisions remain in `DECISIONS.md` where useful, but current implementation must follow the latest LOCKED decision.

## 2. Current Implementation State
No verified production Unreal implementation is assumed by this document. Existing code/assets, if any, must be inspected before implementation begins.

## 3. Locked Project Facts
- 100 floors.
- 3D third-person boss-rush roguelike.
- online-reliant 4-player co-op.
- server-authoritative gameplay.
- dedicated-server-compatible architecture.
- early genuine remote-online testing.
- Unreal Engine 5.8.2.
- Unreal C++ core.
- GAS where appropriate.
- data-driven scalable content.
- thin Blueprint presentation layer.
- Unreal-native systems preferred over reimplementation.
- AI-assisted production, not runtime generative gameplay.
- commercial provenance required.
- boss defeat -> immediate EXP -> shared loot chest -> loot -> Rest -> progression -> next floor.
- every 10 floors: exactly 3 compatible RNG multiclass choices OR reject and ascend current class +1.
- hard class restrictions.
- ascension paths may change after multiclassing.
- merchant bosses unlock selling.

## 4. High-Priority UNDECIDED Items
These remain unresolved unless a later LOCKED decision exists:
1. working/final game title;
2. base class roster;
3. starting-class rules;
4. core stat roster and formulas;
5. character level cap;
6. death/downed/revive/wipe behavior;
7. exact shared-loot ownership/distribution;
8. unclaimed-loot behavior;
9. permanent vs run-specific progression;
10. save/checkpoint/run-reset policy;
11. merchant-boss exact placement and economy;
12. maximum ascension level;
13. maximum multiclass depth;
14. exact class compatibility graph;
15. final shipping server topology;
16. final matchmaking/discovery UX and provider/platform combination;
17. shipping platforms;
18. degree/type of non-boss floor content and procedural generation;
19. Rest timer/readiness/vote behavior;
20. late-join and final reconnect policy.

## 5. Current AI Tooling Baseline
See `AI_STACK.md`. Specific tools are provisional production tooling, not gameplay canon.

## 6. Current Phase
**Canonical migration to UE 5.8.2 and the AI-first directive is complete in this package.**

## 7. Next Approved Task
Execute **PRE-PHASE 0 — Verify/Install the Production Toolchain** and then **Phase 2 — Source Control Foundation** from `AI_GAME_BUILD_PLAYBOOK_UE5.8.2.md`.

Because the canonical rewrite itself satisfies Phase 1, do not repeat the documentation audit unless a contradiction is discovered.

## 8. Immediate Gate
Before AI-B is allowed to modify the Unreal project autonomously:
- UE 5.8.2 launches;
- supported Visual Studio/MSVC/Windows SDK toolchain is verified;
- Python and required CLIs are verified;
- P4 repository/workspace and backup/restore path work;
- canonical docs are tracked;
- Qwen Code can read the canonical docs;
- local gpt-oss-20b endpoint works;
- Unreal MCP is connected and restricted to approved local development use.
