package com.opencart.tests;

import com.opencart.base.BaseTest;
import com.opencart.pages.LoginPage;
import org.testng.Assert;
import org.testng.annotations.Test;

public class InvalidLoginTest extends BaseTest {
    @Test
    public void verifyInvalidLogin() {
        LoginPage loginPage = new LoginPage(driver);
        try {
            loginPage.login("invalid@example.com", "InvalidPassword123", true);
            Assert.assertTrue(loginPage.isLoginErrorVisible(), "Expected login error to appear for invalid credentials");
        } catch (Exception e) {
            Assert.fail("Invalid login test failed with exception: " + e.getMessage(), e);
        }
    }
}
