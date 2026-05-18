from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()

    try:
        # Open site
        page.goto("https://www.saucedemo.com")
        page.wait_for_selector("//input[contains(@id,'user-name')]")  # Wait for login form

        # Login
        page.fill("//input[contains(@id,'user-name')]", "standard_user")
        page.fill("//input[contains(@id,'password')]", "secret_sauce")
        print("Click Login")
        page.click("//input[@id='login-button']")
        page.wait_for_url("**/inventory.html")  # Wait for navigation to inventory page

        # Assertion
        assert "inventory" in page.url
        print("Login Successful")

        # Add to cart
        page.wait_for_selector("//button[contains(@id,'add-to-cart')]")  # Wait for add-to-cart button
        page.click("//button[contains(@id,'add-to-cart')]")

        # Validate cart
        cart_count = page.locator(".shopping_cart_badge").inner_text()
        print("Cart Count:", cart_count)
        assert cart_count == "1"

        # Open cart
        page.click("//a[contains(@class,'shopping_cart_link')]")
        page.wait_for_selector("//button[contains(@id,'checkout')]")  # Wait for checkout button

        # Checkout
        page.click("//button[contains(@id,'checkout')]")

        # Fill details
        page.fill("//input[contains(@id,'first-name')]", "John")
        page.fill("//input[contains(@id,'last-name')]", "Doe")
        page.fill("//input[contains(@id,'postal-code')]", "600001")

        # Continue
        page.click("//input[contains(@id,'continue')]")
        page.wait_for_url("**/checkout-step-two.html")  # Wait for navigation to step two

        # Final validation
        assert "checkout-step-two" in page.url
        print("Checkout Successful")

    except Exception as e:
        print("Test Failed:", e)

    finally:
        browser.close()