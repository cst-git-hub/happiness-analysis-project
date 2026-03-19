import subprocess
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent

scripts = [

    # download
    "scripts/dl_corruption.py",
    "scripts/dl_dem_indx.py",
    "scripts/dl_happiness.py",
    "scripts/dl_lifeexp.py",

    # clean
    "scripts/cl_corruption.py",
    "scripts/cl_democracy.py",
    "scripts/cl_happiness.py",
    "scripts/cl_lifeexp.py"
]

success = []
failed = []


for script in scripts:
    path = BASE_DIR / script
    print(f"\nRunning: {script}")
    try:
        subprocess.run(
            ["python", str(path)],
            check=True
        )
        print("✅ SUCCESS")
        success.append(script)
    except subprocess.CalledProcessError:
        print("❌ FAILED")
        failed.append(script)

print("\n==============================")
print("PIPELINE SUMMARY")
print("==============================")

print(f"\nSuccessful scripts: {len(success)}")

for s in success:
    print("  ", s)

print(f"\nFailed scripts: {len(failed)}")

for f in failed:
    print("  ", f)

print("\nPipeline finished.")