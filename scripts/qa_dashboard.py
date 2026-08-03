import os

REPORT_FOLDER = "extracted_json"


def main():

    print("\n")
    print("=" * 70)
    print("🦋 TIA QUALITY ASSURANCE DASHBOARD")
    print("=" * 70)

    if not os.path.exists(REPORT_FOLDER):
        print("❌ extracted_json folder not found.")
        return

    files = sorted(
        [
            f
            for f in os.listdir(REPORT_FOLDER)
            if f.endswith(".json")
        ]
    )

    print(f"\n📂 Dataset : {REPORT_FOLDER}")
    print(f"📄 Reports Found : {len(files)}")

    print("\nFiles:")

    for file in files:
        print(f"   ✓ {file}")

    print("\n")
    print("=" * 70)
    print("Stage 1 Complete ✅")
    print("=" * 70)


if __name__ == "__main__":
    main()