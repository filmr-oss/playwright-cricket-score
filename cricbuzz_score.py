from playwright.sync_api import sync_playwright

with sync_playwright() as p:

    # Open browser
    browser = p.chromium.launch(headless=False)

    # Create page
    page = browser.new_page()

    # Open Cricbuzz
    page.goto(
        "https://www.cricbuzz.com/",
        wait_until="domcontentloaded"
    )

    print("Cricbuzz opened")

    # Find the score element
    score_element = page.locator(
        "span.text-cbTxtPrim"
    ).filter(
        has_text="&"
    ).first

    # Wait for the score to appear
    score_element.wait_for(timeout=60000)

    # Get score text
    score = score_element.inner_text()

    # Print score
    print("Live Score:", score)

    # Save screenshot
    page.screenshot(path="score.png")

    print("Screenshot saved: score.png")

    # Close browser
    browser.close()