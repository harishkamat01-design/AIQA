package com.opencart.tests;

import com.opencart.base.BaseTest;
import com.opencart.pages.LoginPage;
import org.testng.Assert;
import org.testng.annotations.Test;

public class ValidLoginTest extends BaseTest {
    @Test
    public void verifyValidLogin() {
        LoginPage loginPage = new LoginPage(driver);
        try {
            loginPage.login("valid@example.com", "ValidPassword123", true);
            Assert.assertTrue(loginPage.isLoginSuccessful(), "Expected login to succeed for valid credentials");
        } catch (Exception e) {
            Assert.fail("Valid login test failed with exception: " + e.getMessage(), e);
        }
    }
}
