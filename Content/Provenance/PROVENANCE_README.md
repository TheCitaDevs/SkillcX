# Asset Provenance Tracking System

## Overview

This system provides data-driven tracking of all external and AI-generated assets used in the UE5.8.2 Co-op Boss Rush Roguelike project. Every asset must have a provenance record before it can be approved for shipping.

## Core Principle

**UNKNOWN licensing automatically means NOT APPROVED FOR SHIPPING.**

No asset with `license: "UNKNOWN"` or `commercial_use_status: "UNKNOWN"` may have `shipping_approval.approved: true`. This rule is enforced by automated validation.

## File Structure

```
/workspace/
├── Content/
│   └── Provenance/
│       ├── provenance_schema.json    # JSON Schema defining required fields
│       └── asset_ledger.json         # Master ledger of all assets
└── Scripts/
    └── validate_provenance.py        # Automated validator (Python 3)
```

## Required Fields per Asset

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `asset_id` | string | ✅ | Unique identifier (UUID or structured ID like `ASSET_CHAR_001`) |
| `asset_name` | string | ✅ | Human-readable name |
| `creator` | string | ✅ | Creator name (human or organization) |
| `ai_tool_used` | string | optional | AI/tool used (e.g., `"Midjourney v6"`, `"GitHub Copilot"`, `"None"`) |
| `model_version` | string | optional | Specific version of AI/tool |
| `generation_date` | string | ✅ | ISO 8601 date (e.g., `2025-01-15T14:30:00Z`) |
| `source` | string | ✅ | Origin (URL, file path, organization, or `"original"`) |
| `license` | string | ✅ | License type (`"MIT"`, `"CC-BY-4.0"`, `"Unreal EULA"`, `"Proprietary"`, `"UNKNOWN"`) |
| `commercial_use_status` | enum | ✅ | `"APPROVED"`, `"RESTRICTED"`, `"NOT_APPROVED"`, `"UNKNOWN"` |
| `modifications` | array | optional | List of modification records |
| `human_approval` | object | ✅ | Human approval record |
| `original_source_files` | array | optional | Paths/URLs to original source files |
| `shipping_approval` | object | ✅ | Shipping approval record |

## Approval Workflow

### 1. Asset Creation/Import
- Create new entry in `asset_ledger.json`
- Set `license` and `commercial_use_status` appropriately
- If unknown, set both to `"UNKNOWN"` (auto-rejects shipping)

### 2. Human Review
- Update `human_approval` object:
  ```json
  "human_approval": {
    "approved": true,
    "approver": "Jane Doe",
    "approval_date": "2025-01-15T14:30:00Z",
    "notes": "Verified CC-BY-4.0 license, commercial use permitted"
  }
  ```

### 3. Shipping Approval (Final Gate)
- Only allowed if `commercial_use_status` is `"APPROVED"` or `"RESTRICTED"`
- Update `shipping_approval` object:
  ```json
  "shipping_approval": {
    "approved": true,
    "approver": "John Smith (Lead)",
    "approval_date": "2025-01-20T10:00:00Z",
    "build_number": "0.2.0-preview",
    "notes": "All provenance checks passed"
  }
  ```

## Automated Validation

Run the validator before any commit or build:

```bash
python3 Scripts/validate_provenance.py
```

### What It Checks

1. **Required fields present** - All mandatory fields exist
2. **Auto-reject rule** - UNKNOWN license/status cannot have shipping approval
3. **Date formats** - All dates are valid ISO 8601
4. **Structure validation** - Objects and arrays have correct types
5. **Summary statistics** - Reports counts by approval status

### Exit Codes

- `0` - Validation PASSED (no blocking errors)
- `1` - Validation FAILED (cannot ship)

### Generated Report

The validator creates `Scripts/validation_report.txt` with:
- Timestamp
- Total assets count
- Shipping approval summary
- Commercial use status breakdown
- AI-generated assets list
- Errors and warnings
- Final verdict

## Example Asset Entries

### Original Human-Created Asset
```json
{
  "asset_id": "ASSET_CHAR_WARRIOR_001",
  "asset_name": "Warrior Base Mesh",
  "creator": "Acme Game Studios",
  "ai_tool_used": "None",
  "model_version": "N/A",
  "generation_date": "2025-01-10T09:00:00Z",
  "source": "original",
  "license": "Proprietary",
  "commercial_use_status": "APPROVED",
  "modifications": [],
  "human_approval": {
    "approved": true,
    "approver": "Art Director",
    "approval_date": "2025-01-10T17:00:00Z",
    "notes": "Original work, full commercial rights"
  },
  "original_source_files": ["Content/Characters/Warrior/Meshes/Warrior_Base.uasset"],
  "shipping_approval": {
    "approved": true,
    "approver": "Production Lead",
    "approval_date": "2025-01-15T10:00:00Z",
    "build_number": "0.2.0-preview",
    "notes": "Cleared for shipping"
  }
}
```

### AI-Generated Asset (Licensed)
```json
{
  "asset_id": "ASSET_TEX_BOSS_SKIN_001",
  "asset_name": "Boss Dragon Skin Texture",
  "creator": "Midjourney via Artist Name",
  "ai_tool_used": "Midjourney",
  "model_version": "v6.0",
  "generation_date": "2025-01-12T14:30:00Z",
  "source": "https://midjourney.com/gallery/abc123",
  "license": "CC-BY-4.0",
  "commercial_use_status": "APPROVED",
  "modifications": [
    {
      "date": "2025-01-13T10:00:00Z",
      "modifier": "Artist Name",
      "description": "Color correction, tiling fix in Photoshop"
    }
  ],
  "human_approval": {
    "approved": true,
    "approver": "Legal Review",
    "approval_date": "2025-01-14T09:00:00Z",
    "notes": "CC-BY-4.0 verified, attribution included in credits"
  },
  "original_source_files": [
    "Source/Textures/BossDragon/mj_export_abc123.png",
    "Content/Textures/BossDragon/T_BossDragon_Skin.uasset"
  ],
  "shipping_approval": {
    "approved": true,
    "approver": "Production Lead",
    "approval_date": "2025-01-15T10:00:00Z",
    "build_number": "0.2.0-preview",
    "notes": "License verified, attribution planned"
  }
}
```

### Unknown License (AUTO-REJECTED)
```json
{
  "asset_id": "ASSET_SFX_UNKNOWN_001",
  "asset_name": "Mystery Sound Effect",
  "creator": "Unknown",
  "ai_tool_used": "None",
  "model_version": "N/A",
  "generation_date": "2025-01-01T00:00:00Z",
  "source": "Found online, source lost",
  "license": "UNKNOWN",
  "commercial_use_status": "UNKNOWN",
  "modifications": [],
  "human_approval": {
    "approved": false,
    "approver": "",
    "approval_date": "",
    "notes": "Pending review - source unknown"
  },
  "original_source_files": [],
  "shipping_approval": {
    "approved": false,
    "approver": "",
    "approval_date": "",
    "build_number": "",
    "notes": "AUTO-REJECTED: Unknown license status"
  }
}
```

## Integration with Build Pipeline

### Pre-Build Check
Add to build script:
```bash
python3 Scripts/validate_provenance.py || exit 1
```

### Perforce Integration
Track `Content/Provenance/asset_ledger.json` in version control. Require ledger update with every asset addition.

### Unreal Engine Integration (Future)
- Custom Editor Utility Widget to view/edit ledger
- Asset registry hooks to flag untracked assets
- Build cooking step runs validator

## Maintenance

### Adding New Assets
1. Copy template entry from `asset_ledger.json`
2. Fill all required fields
3. Set appropriate license/commercial status
4. Run validator: `python3 Scripts/validate_provenance.py`
5. Commit ledger changes

### Updating Existing Assets
1. Locate asset by `asset_id`
2. Add modification record if changed
3. Re-run human approval if significantly modified
4. Update `last_modified` in metadata

### Quarterly Audit
- Review all `UNKNOWN` status assets
- Resolve or remove unlicensed assets
- Verify AI tool versions still permitted
- Update maintainer contact

## Compliance Notes

- **Commercial Provenance Required**: All shipped assets must have verifiable commercial-use rights
- **AI Disclosure**: AI-generated assets must disclose tool and version
- **Modification Tracking**: All derivative works must record modifications
- **Human Oversight**: Every asset requires human approval before shipping
- **Immutable Records**: Ledger history preserved in version control

## Contact

**Maintainer:** TBD  
**Last Updated:** 2025-01-25  
**Schema Version:** 1.0
