import time
from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    request = p.request.new_context(
        base_url="https://jsonplaceholder.typicode.com",
        extra_http_headers={
            "Authorization": "Bearer fake_token_123",
            "Content-Type": "application/json"
        }
    )

    # ✅ GET
    start = time.time()
    res = request.get("/posts/1")
    end = time.time()
    response_time = (end - start) * 1000

    assert res.status == 200, "GET failed"
    assert response_time < 2000, f"GET slow: {response_time} ms"
    assert res.json()["id"] == 1
    print("GET Response Time:", response_time, "ms")

    # ✅ POST
    start = time.time()
    res = request.post("/posts", data={"title": "Test", "body": "Data", "userId": 1})
    end = time.time()
    response_time = (end - start) * 1000

    assert res.status == 201, "POST failed"
    assert response_time < 2000, f"POST slow: {response_time} ms"
    assert res.json()["title"] == "Test"
    print("POST Response Time:", response_time, "ms")

    # ✅ PUT
    start = time.time()
    res = request.put("/posts/1", data={"id":1,"title":"Updated","body":"New","userId":1})
    end = time.time()
    response_time = (end - start) * 1000

    assert res.status == 200, "PUT failed"
    assert response_time < 2000, f"PUT slow: {response_time} ms"
    assert res.json()["title"] == "Updated"
    print("PUT Response Time:", response_time, "ms")

    # ✅ DELETE
    start = time.time()
    res = request.delete("/posts/1")
    end = time.time()
    response_time = (end - start) * 1000

    assert res.status == 200, "DELETE failed"
    assert response_time < 2000, f"DELETE slow: {response_time} ms"
    print("DELETE Response Time:", response_time, "ms")

print("All API tests passed ✅")