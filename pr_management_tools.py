# pr_management_tools.py

# ---------------- PR DATA ---------------- #

PR_DATA = [
    {
        "uuid": "1a2b3c01-0001-4a0c-b0db-111111111111",
        "pr_name": "LAPTOPS - VARIANT 1 - BLACK",
        "qty": 60,
        "location": "Pune"
    },
    {
        "uuid": "1a2b3c01-0002-4a0c-b0db-222222222222",
        "pr_name": "LAPTOPS - VARIANT 2 - SILVER",
        "qty": 100,
        "location": "Bengaluru"
    }
]

# ---------------- STATE ---------------- #

PR_CART = []
CURRENT_PAGE = 1
PAGE_LIMIT = 2

# ---------------- TOOLS ---------------- #

def get_pr_list_tool():
    """Show first 2 PRs"""
    global CURRENT_PAGE
    CURRENT_PAGE = 1
    return {
        "prs": PR_DATA[:PAGE_LIMIT],
        "page": CURRENT_PAGE,
        "has_more": len(PR_DATA) > PAGE_LIMIT
    }


def paginate_pr_tool():
    """Show next 2 PRs"""
    global CURRENT_PAGE
    CURRENT_PAGE += 1

    start = (CURRENT_PAGE - 1) * PAGE_LIMIT
    end = start + PAGE_LIMIT

    return {
        "prs": PR_DATA[start:end],
        "page": CURRENT_PAGE,
        "has_more": end < len(PR_DATA)
    }


def add_pr_to_cart_tool(uuid: str, qty: int):
    """Add PR to PR cart with quantity"""
    for pr in PR_DATA:
        if pr["uuid"] == uuid:
            item = {
                "uuid": pr["uuid"],
                "pr_name": pr["pr_name"],
                "qty": qty,
                "location": pr["location"]
            }
            PR_CART.append(item)
            return item

    return {"error": "PR_NOT_FOUND"}


def update_pr_cart_qty_tool(uuid: str, qty: int):
    """Update quantity of PR already in cart"""
    for item in PR_CART:
        if item["uuid"] == uuid:
            item["qty"] = qty
            return item

    return {"error": "PR_NOT_IN_CART"}
