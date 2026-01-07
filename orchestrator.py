# orchestrator.py

from pr_management_tools import (
    get_pr_list_tool,
    paginate_pr_tool,
    add_pr_to_cart_tool,
    update_pr_cart_qty_tool
)

def supervisor_router(user_message: str):
    msg = user_message.lower()

    if any(k in msg for k in ["show my pr", "active pr", "open pr"]):
        return get_pr_list_tool()

    if any(k in msg for k in ["view more", "show more", "next"]):
        return paginate_pr_tool()

    if "add" in msg and "qty" in msg:
        parts = msg.split()
        uuid = parts[parts.index("pr") + 1]
        qty = int(parts[parts.index("qty") + 1])
        return add_pr_to_cart_tool(uuid, qty)

    if "update" in msg or "change" in msg:
        parts = msg.split()
        uuid = parts[parts.index("pr") + 1]
        qty = int(parts[parts.index("qty") + 1])
        return update_pr_cart_qty_tool(uuid, qty)

    return {"error": "NOT_A_PR_REQUEST"}
