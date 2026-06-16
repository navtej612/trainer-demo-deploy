import json
from pathlib import Path
from mcp.server.fastmcp import FastMCP

mcp = FastMCP("trainer-demo-local-mcp")

REPO_ROOT = Path(__file__).resolve().parents[1]

@mcp.tool()
def validate_templates_json() -> str:
    """
    Validate templates.json entries for required metadata fields.
    """
    templates_path = REPO_ROOT / "static" / "templates.json"

    if not templates_path.exists():
        return f"templates.json not found at: {templates_path}"

    with open(templates_path, "r", encoding="utf-8") as file:
        data = json.load(file)

    required_fields = [
        "title",
        "description",
        "preview",
        "website",
        "source",
        "demoguide",
        "deploytime",
        "prereqs",
    ]

    issues = []

    for index, template in enumerate(data):
        title = template.get("title", f"Template #{index + 1}")

        for field in required_fields:
            if field not in template or template[field] in ["", None, []]:
                issues.append(f"{title}: missing or empty '{field}'")

    if not issues:
        return "All templates have the required metadata fields."

    return "Metadata issues found:\n" + "\n".join(issues)

if __name__ == "__main__":
    mcp.run()