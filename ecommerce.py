from playwright.sync_api import sync_playwright

with sync_playwright() as p:

    browser = p.chromium.launch(headless=False)

    page = browser.new_page()

    try:

        # Open site
        page.goto("https://www.saucedemo.com")

        # Login
        page.fill("//input[contains(@id,'user-name')]",
                  "standard_user")

        page.fill("//input[contains(@id,'password')]",
                  "secret_sauce")

        print("Click Login")

        page.click("//input[@id='login-button']")

        # Assertion
        assert "inventory" in page.url

        print("Login Successful")

        # Add to cart
        page.click("//button[contains(@id,'add-to-cart')]")

        # Validate cart
        cart_count = page.locator(".shopping_cart_badge").inner_text()

        print("Cart Count:", cart_count)

        assert cart_count == "1"

        # Open cart
        page.click("//a[contains(@class,'shopping_cart_link')]")

        # Checkout
        page.click("//button[contains(@id,'checkout')]")

        # Fill details
        page.fill("//input[contains(@id,'first-name')]",
                  "John")

        page.fill("//input[contains(@id,'last-name')]",
                  "Doe")

        page.fill("//input[contains(@id,'postal-code')]",
                  "600001")

        # Continue
        page.click("//input[contains(@id,'continue')]")

        # Final validation
        assert "checkout-step-two" in page.url

        print("Checkout Successful")

        page.wait_for_timeout(3000)

    except Exception as e:

        print("Test Failed:", e)

    finally:

        browser.close()