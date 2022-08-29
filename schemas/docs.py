def secDocEntity(item) -> dict:
    return {
        "id": item["id"],
        "file": {
            "id": item["id"],
            "name": item["name"]
        },
        "section": {
            "textOfFile": item["textOfFile"]
        }
    }