import csv
from pathlib import Path

ROOT = Path(__file__).resolve().parent
OUTPUT = ROOT / "testcases" / "vwo_test_cases.csv"

MODULES = ["Checkout", "Signup", "Search", "Recommendations", "Profile", "Billing", "Notifications", "Analytics"]
PRIORITIES = ["P1", "P2", "P3"]
TAGS = [
    "checkout", "signup", "search", "recommendations", "profile", "billing", "notifications",
    "analytics", "ux", "conversion", "validation", "performance", "discount", "promo", "payment"
]


def build_case(index: int) -> dict:
    module = MODULES[index % len(MODULES)]
    priority = PRIORITIES[(index // 10) % len(PRIORITIES)]
    tags = [TAGS[(index + offset) % len(TAGS)] for offset in range(3)]
    title = f"{module} experience {index:04d} stays reliable"
    steps = (
        f"Open the {module.lower()} flow; complete the primary action; "
        f"verify the state persists across navigation and retries."
    )
    expected = (
        f"The {module.lower()} workflow completes without errors and the UI remains consistent."
    )
    return {
        "id": index,
        "jira_id": f"VWO-{1000 + index}",
        "priority": priority,
        "module": module,
        "title": title,
        "steps": steps,
        "expected": expected,
        "tags": ",".join(tags),
    }


def main() -> None:
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    with OUTPUT.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=["id", "jira_id", "priority", "module", "title", "steps", "expected", "tags"])
        writer.writeheader()
        for idx in range(1, 1001):
            writer.writerow(build_case(idx))
    print(f"Wrote {OUTPUT}")


if __name__ == "__main__":
    main()
