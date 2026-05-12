from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()

    # Open Site
    page.goto("https://www.saucedemo.com")

    #Login
    page.fill("//input[contains(@id,'user-name')]", "standard_user")
    page.fill("//input[contains(@id,'password')]", "secret_sauce")
    print("Click login")
    page.click("//input[@id='login-button']")
    # add to cart
    print("Click backpack")

    page.click("//button[contains(@id,'add-to-cart-sauce-labs-backpack')]")
    
    page.wait_for_timeout(5000)


    #go to cart
    print("Click cart")

    page.click("//a[contains(@class,'shopping_cart_link')]")
    page.wait_for_timeout(5000)


    #Checkout
    print("Click checkout")
    page.click("//button[contains(@id,'checkout')]")
    page.wait_for_timeout(5000)


    #fill details
    print("Click detials")
    page.fill("//input[contains(@id,'first-name')]", "John")
    page.fill("//input[contains(@id,'last-name')]", "Doe")
    page.fill("//input[contains(@id,'postal-code')]", "600001")

    #Continue
    page.click("//input[contains(@id,'continue')]")

    #option print page title
    print("Page Title:", page.title())

    # wait

    page.wait_for_timeout(5000)

    #close browser
    browser.close()