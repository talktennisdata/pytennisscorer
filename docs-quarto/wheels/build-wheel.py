#!/usr/bin/env python3
"""
Build a Pyodide-compatible wheel for pytennisscorer.

This script builds a pure Python wheel that can be loaded in Pyodide.
It ensures no binary dependencies are included and the wheel metadata
is compatible with browser-based Python execution.
"""

import shutil
import subprocess
import sys
from pathlib import Path
from typing import Optional


def build_wheel() -> Optional[Path]:
    """Build a pure Python wheel for pytennisscorer."""
    # Get paths
    project_root = Path(__file__).parent.parent.parent
    wheel_dir = Path(__file__).parent

    print("Building wheel from:", project_root)
    print("Output directory:", wheel_dir)

    # Clean previous builds
    build_dir = project_root / "build"
    if build_dir.exists():
        shutil.rmtree(build_dir)

    dist_dir = project_root / "dist"
    if dist_dir.exists():
        shutil.rmtree(dist_dir)

    # Build the wheel using build module
    try:
        _ = subprocess.run(
            [sys.executable, "-m", "build", "--wheel", str(project_root)],
            check=True,
            capture_output=True,
            text=True,
        )
    except subprocess.CalledProcessError as e:
        print("Error building wheel:", e)
        if hasattr(e, "stdout") and e.stdout:
            print("stdout:", e.stdout)
        if hasattr(e, "stderr") and e.stderr:
            print("stderr:", e.stderr)
        # Try with pip wheel as fallback
        print("Trying with pip wheel...")
        _ = subprocess.run(
            [
                sys.executable,
                "-m",
                "pip",
                "wheel",
                "--no-deps",
                "--wheel-dir",
                str(wheel_dir),
                str(project_root),
            ],
            check=True,
        )
        # Check if wheel was created in wheel_dir
        wheels = list(wheel_dir.glob("*.whl"))
        if wheels:
            return wheels[0]
        return None

    # Move wheel to docs directory
    wheels = list(dist_dir.glob("*.whl"))
    if not wheels:
        print("No wheel found in dist directory!")
        sys.exit(1)

    wheel_file = wheels[0]
    target = wheel_dir / wheel_file.name

    # Copy wheel to documentation directory
    _ = shutil.copy2(wheel_file, target)
    print("✅ Wheel built successfully:", target)

    # Verify it's a pure Python wheel
    if "py3-none-any" not in wheel_file.name:
        print("⚠️ Warning: Wheel may not be pure Python!")
        print("  Pyodide requires pure Python wheels without binary dependencies.")

    return target


if __name__ == "__main__":
    wheel_path = build_wheel()
    if wheel_path:
        print("\nTo test in Pyodide locally:")
        print("  1. Start a local server in docs-quarto directory")
        print(f"  2. Load the wheel with: await micropip.install('./wheels/{wheel_path.name}')")
    else:
        print("Failed to build wheel")
        sys.exit(1)
