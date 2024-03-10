const { test } = require ("@playwright/test")
const { chromium } = require('playwright');


const url = "https://parabank.parasoft.com/parabank/register.htm;jsessionid=4CE150FCDB0CE3623E0C79D09E143958";
const userName = "jayasiva";
const password = "Test@1";

test("testFundTransfer", async () =>  {
    const browser = await chromium.launch({channel: 'chrome', headless: false});
    const page = await browser.newPage();

    // Login Validation
    await page.goto(url);
    await page.fill('input[name="username"]', userName);
    await page.fill('input[name="password"]', password);
    await page.click('input[value="Log In"]');
    
    // Fund Transfer Validation
    await page.click('a:has-text("Transfer Funds")');
    await page.waitForSelector('select#fromAccountId');
    await page.waitForSelector('select#toAccountId');
    await page.selectOption('select#toAccountId', { value: '14121' });
    await page.fill('input#amount', '100');
    await page.click('input[value="Transfer"]');
    
    // Transfer Status Validation
    const transferStatus = await page.$eval('h1', element => element.textContent);
    if (transferStatus !== "Transfer Complete!") {
        console.error("Transfer failed!");
    } else {
        console.log("Transfer Successful!");
    }

    // Logout Validation
    await page.click('a:has-text("Log Out")');
    
    // Validate logout
    const customerLoginHeader = await page.$eval('h2', element => element.textContent);
    if (customerLoginHeader !== "Customer Login") {
        console.error("Logout failed!");
    } else {
        console.log("Logout Successful!");
    }

    await browser.close();
});

