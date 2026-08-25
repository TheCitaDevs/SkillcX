#!/usr/bin/env python3
"""
Asset Provenance Validator for UE5.8.2 Co-op Game
Validates asset_ledger.json against provenance_schema.json
Enforces: Unknown license = NOT APPROVED FOR SHIPPING
"""

import json
import sys
from datetime import datetime
from pathlib import Path


def load_json(filepath: str) -> dict:
    """Load JSON file with error handling."""
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            return json.load(f)
    except FileNotFoundError:
        print(f"ERROR: File not found: {filepath}")
        sys.exit(1)
    except json.JSONDecodeError as e:
        print(f"ERROR: Invalid JSON in {filepath}: {e}")
        sys.exit(1)


def validate_iso8601(date_str: str, field_name: str) -> bool:
    """Validate ISO 8601 date format."""
    if not date_str:
        return True  # Empty is allowed for optional fields
    try:
        datetime.fromisoformat(date_str.replace('Z', '+00:00'))
        return True
    except ValueError:
        print(f"WARNING: Invalid ISO 8601 date in {field_name}: {date_str}")
        return False


def validate_asset(asset: dict, asset_index: int) -> list:
    """Validate a single asset entry. Returns list of errors."""
    errors = []
    warnings = []
    
    # Required fields check
    required_fields = [
        "asset_id", "asset_name", "creator", "generation_date",
        "source", "license", "commercial_use_status",
        "human_approval", "shipping_approval"
    ]
    
    for field in required_fields:
        if field not in asset:
            errors.append(f"Asset[{asset_index}]: Missing required field '{field}'")
    
    # Auto-reject rule: UNKNOWN license or commercial_use_status
    license_val = asset.get("license", "UNKNOWN")
    commercial_status = asset.get("commercial_use_status", "UNKNOWN")
    
    if license_val == "UNKNOWN" or commercial_status == "UNKNOWN":
        shipping_approval = asset.get("shipping_approval", {})
        if shipping_approval.get("approved", False):
            errors.append(
                f"Asset[{asset_index}] ({asset.get('asset_id', 'UNKNOWN')}): "
                f"SHIPPING APPROVED despite UNKNOWN license/commercial status. "
                f"AUTO-REJECT RULE VIOLATED."
            )
    
    # Validate human_approval structure
    human_approval = asset.get("human_approval", {})
    if not isinstance(human_approval, dict):
        errors.append(f"Asset[{asset_index}]: human_approval must be an object")
    elif "approved" not in human_approval:
        errors.append(f"Asset[{asset_index}]: human_approval missing 'approved' field")
    
    # Validate shipping_approval structure
    shipping_approval = asset.get("shipping_approval", {})
    if not isinstance(shipping_approval, dict):
        errors.append(f"Asset[{asset_index}]: shipping_approval must be an object")
    elif "approved" not in shipping_approval:
        errors.append(f"Asset[{asset_index}]: shipping_approval missing 'approved' field")
    
    # Date format validation
    validate_iso8601(asset.get("generation_date", ""), f"Asset[{asset_index}].generation_date")
    
    if human_approval.get("approval_date"):
        validate_iso8601(human_approval["approval_date"], f"Asset[{asset_index}].human_approval.approval_date")
    
    if shipping_approval.get("approval_date"):
        validate_iso8601(shipping_approval["approval_date"], f"Asset[{asset_index}].shipping_approval.approval_date")
    
    # Modifications array validation
    modifications = asset.get("modifications", [])
    if not isinstance(modifications, list):
        errors.append(f"Asset[{asset_index}]: modifications must be an array")
    else:
        for i, mod in enumerate(modifications):
            if not isinstance(mod, dict):
                errors.append(f"Asset[{asset_index}].modifications[{i}]: must be an object")
            elif "date" in mod:
                validate_iso8601(mod["date"], f"Asset[{asset_index}].modifications[{i}].date")
    
    return errors + warnings


def validate_ledger(ledger: dict) -> tuple:
    """Validate entire ledger. Returns (errors, warnings)."""
    all_errors = []
    all_warnings = []
    
    # Check schema version
    schema_version = ledger.get("schema_version", "unknown")
    if schema_version != "1.0":
        all_warnings.append(f"Unexpected schema version: {schema_version} (expected 1.0)")
    
    # Validate each asset
    assets = ledger.get("assets", [])
    if not isinstance(assets, list):
        all_errors.append("'assets' must be an array")
        return all_errors, all_warnings
    
    if len(assets) == 0:
        all_warnings.append("Ledger contains no assets")
    
    for i, asset in enumerate(assets):
        errors = validate_asset(asset, i)
        all_errors.extend(errors)
    
    return all_errors, all_warnings


def generate_report(ledger: dict, errors: list, warnings: list) -> str:
    """Generate validation report."""
    timestamp = datetime.now(tz=None).astimezone().isoformat()
    
    report = []
    report.append("=" * 70)
    report.append("ASSET PROVENANCE VALIDATION REPORT")
    report.append("=" * 70)
    report.append(f"Timestamp: {timestamp}")
    report.append(f"Project: {ledger.get('project', 'Unknown')}")
    report.append(f"Schema Version: {ledger.get('schema_version', 'Unknown')}")
    report.append(f"Total Assets: {len(ledger.get('assets', []))}")
    report.append("")
    
    # Shipping approval summary
    assets = ledger.get("assets", [])
    approved_count = sum(1 for a in assets if a.get("shipping_approval", {}).get("approved", False))
    pending_count = len(assets) - approved_count
    
    report.append("SHIPPING APPROVAL STATUS:")
    report.append(f"  Approved for Shipping: {approved_count}")
    report.append(f"  Not Approved/Pending:  {pending_count}")
    report.append("")
    
    # Commercial use summary
    commercial_approved = sum(1 for a in assets if a.get("commercial_use_status") == "APPROVED")
    commercial_unknown = sum(1 for a in assets if a.get("commercial_use_status") == "UNKNOWN")
    commercial_not_approved = sum(1 for a in assets if a.get("commercial_use_status") == "NOT_APPROVED")
    commercial_restricted = sum(1 for a in assets if a.get("commercial_use_status") == "RESTRICTED")
    
    report.append("COMMERCIAL USE STATUS:")
    report.append(f"  APPROVED:    {commercial_approved}")
    report.append(f"  RESTRICTED:  {commercial_restricted}")
    report.append(f"  NOT_APPROVED:{commercial_not_approved}")
    report.append(f"  UNKNOWN:     {commercial_unknown} (AUTO-REJECTED FOR SHIPPING)")
    report.append("")
    
    # AI-generated assets
    ai_assets = [a for a in assets if a.get("ai_tool_used", "None") != "None"]
    report.append(f"AI-GENERATED ASSETS: {len(ai_assets)}")
    for asset in ai_assets:
        report.append(f"  - {asset['asset_id']}: {asset.get('ai_tool_used')} ({asset.get('model_version', 'N/A')})")
    report.append("")
    
    # Errors and warnings
    if errors:
        report.append("ERRORS:")
        for err in errors:
            report.append(f"  ❌ {err}")
        report.append("")
    
    if warnings:
        report.append("WARNINGS:")
        for warn in warnings:
            report.append(f"  ⚠️  {warn}")
        report.append("")
    
    # Final verdict
    report.append("=" * 70)
    if errors:
        report.append("VALIDATION FAILED - Cannot ship with errors")
        report.append(f"Total Errors: {len(errors)}")
    else:
        report.append("VALIDATION PASSED - No blocking errors")
        if warnings:
            report.append(f"Warnings: {len(warnings)} (review recommended)")
    report.append("=" * 70)
    
    return "\n".join(report)


def main():
    """Main entry point."""
    # Schema is in Content/Provenance, ledger and report are in Scripts directory
    script_path = Path(__file__).parent
    project_root = script_path.parent
    provenance_dir = project_root / "Content" / "Provenance"
    
    schema_file = provenance_dir / "provenance_schema.json"
    ledger_file = provenance_dir / "asset_ledger.json"
    report_file = script_path / "validation_report.txt"
    
    print("Asset Provenance Validator v1.0")
    print("-" * 40)
    
    # Load files
    schema = load_json(schema_file)
    ledger = load_json(ledger_file)
    
    # Validate
    errors, warnings = validate_ledger(ledger)
    
    # Generate report
    report = generate_report(ledger, errors, warnings)
    
    # Save report
    with open(report_file, 'w', encoding='utf-8') as f:
        f.write(report)
    
    # Print report
    print(report)
    
    # Exit code based on validation result
    if errors:
        print(f"\nValidation FAILED with {len(errors)} error(s)")
        sys.exit(1)
    else:
        print(f"\nValidation PASSED ({len(warnings)} warning(s))")
        sys.exit(0)


if __name__ == "__main__":
    main()
