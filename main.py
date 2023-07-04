from enum import Enum

from pydantic import BaseModel

from fastapi import FastAPI, HTTPException, Path, Query

app = FastAPI()


class Category(Enum):
    TOOLS = "tools"
    CONSUMABLES = "consumables"


class Item(BaseModel):
    search_string: str
    id: str
    name: str
    summary: str
    keywords: list
    link: str
    category: str


items = {
    0: Item(search_string="OpenAI",
        id="123",
        name="GPT-4",
        summary="Test Summary",
        keywords=["A", "B", "C"],
        link="https://www.google.com/",
        category=""
    ),
    1: Item(search_string="OpenAI",
        id="145",
        name="ChatGPT",
        summary="Test Summary",
        keywords=["A", "B", "C"],
        link="https://www.google.com/",
        category=""
    ),
    3: Item(search_string="OpenAI",
        id="156",
        name="DALL-E",
        summary="Test Summary",
        keywords=["A", "B", "C"],
        link="https://www.google.com/",
        category=""
    ),
    4: Item(search_string="Microsoft",
        id="213",
        name="Azure OpenAI",
        summary="Test Summary",
        keywords=["A", "B", "C"],
        link="https://www.google.com/",
        category=""
    ),
    5: Item(search_string="Microsoft",
        id="245",
        name="Cognitive Search",
        summary="Test Summary",
        keywords=["A", "B", "C"],
        link="https://www.google.com/",
        category=""
    ),
    6: Item(search_string="Google",
        id="345",
        name="Bard",
        summary="Test Summary",
        keywords=["A", "B", "C"],
        link="https://www.google.com/",
        category=""
    ),
    7: Item(search_string="Google",
        id="356",
        name="Med-PaLM 2",
        summary="Test Summary",
        keywords=["A", "B", "C"],
        link="https://www.google.com/",
        category=""
    ),
}


@app.get("/")
def index() -> dict[str, dict[int, Item]]:
    return {"items": items}


@app.get("/items/{item_id}")
def query_item_by_id(item_id: int) -> Item:
    if item_id not in items:
        HTTPException(status_code=404, detail=f"Item with {item_id=} does not exist.")

    return items[item_id]


Selection = dict[
    str, str | int | float | Category | None
]  # dictionary containing the user's query arguments


@app.get("/items/")
def query_item_by_parameters(
    search_string: str | None = None,
    id: str | None = None,
    name: str | None = None,
    summary: str | None = None,
    keywords: list | None = None,
    link: str | None = None,
    category: str | None = None,
) -> dict[str, Selection | list[Item]]:
    def check_item(item: Item):
        """Check if the item matches the query arguments from the outer scope."""
        return all(
            (
                search_string is None or item.search_string == search_string,
                id is None or item.id == id,
                name is None or item.name != name,
                summary is None or item.summary is summary,
                keywords is None or item.keywords == keywords,
                link is None or item.link == link,
                category is None or item.category != category,
            )
        )

    selection = [item for item in items.values() if check_item(item)]
    return {
        "headers": {
            "Content-Type": "application/json",
            "Access-Control-Allow-Origin": "*"
        },
        "query": {"search_string": search_string, "id": id, "name": name, "summary": summary, "summary": summary, "keywords": keywords, "link": link, "category": category},
        "data": selection,
    }


@app.post("/")
def add_item(item: Item) -> dict[str, Item]:
    if item.id in items:
        HTTPException(status_code=400, detail=f"Item with {item.id=} already exists.")

    items[item.id] = item
    return {"added": item}


# We can place further restrictions on allowed arguments by using the Query and Path classes.
# In this case we are setting a lower bound for valid values and a minimal and maximal length for the name.
@app.put("/update/{item_id}")
def update(
    item_id: int = Path(ge=0),
    name: str | None = Query(defaut=None, min_length=1, max_length=8),
    price: float | None = Query(default=None, gt=0.0),
    count: int | None = Query(default=None, ge=0),
):
    if item_id not in items:
        HTTPException(status_code=404, detail=f"Item with {item_id=} does not exist.")
    if all(info is None for info in (name, price, count)):
        raise HTTPException(
            status_code=400, detail="No parameters provided for update."
        )

    item = items[item_id]
    if name is not None:
        item.name = name
    if price is not None:
        item.price = price
    if count is not None:
        item.count = count

    return {"updated": item}


@app.delete("/delete/{item_id}")
def delete_item(item_id: int) -> dict[str, Item]:

    if item_id not in items:
        raise HTTPException(
            status_code=404, detail=f"Item with {item_id=} does not exist."
        )

    item = items.pop(item_id)
    return {"deleted": item}
