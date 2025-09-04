from playwright.sync_api import Playwright

def test_single_post(playwright: Playwright):
    request = playwright.request.new_context(
        base_url="https://jsonplaceholder.typicode.com",
        extra_http_headers={"Accept": "application/json"}
    )
    response = request.get("/posts/1")

    assert response.ok, (f"Request failed with: {response.status} {response.text()}"
                         )
    post = response.json()
    assert post["id"] == 1
    assert isinstance(post["title"], str) and post["title"]
    assert isinstance(post["body"], str) and post["body"]
    assert "userId" in post

    request.dispose()

def test_create_post(playwright: Playwright):
    request = playwright.request.new_context(
        base_url = "https://jsonplaceholder.typicode.com",
        extra_http_headers = {"Accept": "application/json"
    })
    payload = {"title": "hello", "body": "world", "userId": 123}
    response = request.post("/posts", data=payload)

    assert response.status == 201, (
        f"Expected 201 Created, got {response.status}"
    )

    created = response.json()  # parse the response JSON into a Python dict named `created`

    assert created["title"] == payload["title"]  # the API echoes back the title we sent
    assert created["body"] == payload["body"]  # the API echoes back the body we sent
    assert created["userId"] == payload["userId"]  # the API echoes back the userId we sent
    assert "id" in created  # JSONPlaceholder returns a fake `id` field for the created resource

    request.dispose()