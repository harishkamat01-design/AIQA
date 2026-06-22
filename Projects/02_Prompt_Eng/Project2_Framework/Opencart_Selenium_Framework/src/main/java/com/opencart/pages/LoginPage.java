package com.opencart.pages;

import org.openqa.selenium.WebDriver;
import org.openqa.selenium.WebElement;
import org.openqa.selenium.support.FindBy;
import org.openqa.selenium.support.PageFactory;
import org.openqa.selenium.support.ui.ExpectedConditions;
import org.openqa.selenium.support.ui.WebDriverWait;

import java.time.Duration;

public class LoginPage {
    private final WebDriver driver;
    private final WebDriverWait wait;

    @FindBy(xpath = "//input[@id='input-email']")
    private WebElement emailField;

    @FindBy(xpath = "//input[@id='input-password']")
    private WebElement passwordField;

    @FindBy(xpath = "//button[@type='submit' and normalize-space()='Login']")
    private WebElement loginButton;

    @FindBy(xpath = "//input[@type='checkbox' and (@name='remember' or @id='remember')]")
    private WebElement rememberMeCheckbox;

    @FindBy(xpath = "//div[contains(@class,'alert-danger') or contains(@class,'alert-dismissible')]")
    private WebElement loginErrorAlert;

    @FindBy(xpath = "//h2[contains(normalize-space(),'My Account')]")
    private WebElement accountHeader;

    public LoginPage(WebDriver driver) {
        this.driver = driver;
        this.wait = new WebDriverWait(driver, Duration.ofSeconds(15));
        PageFactory.initElements(driver, this);
    }

    public void enterEmail(String email) {
        try {
            wait.until(ExpectedConditions.visibilityOf(emailField));
            emailField.clear();
            emailField.sendKeys(email);
        } catch (Exception e) {
            throw new RuntimeException("Unable to enter email", e);
        }
    }

    public void enterPassword(String password) {
        try {
            wait.until(ExpectedConditions.visibilityOf(passwordField));
            passwordField.clear();
            passwordField.sendKeys(password);
        } catch (Exception e) {
            throw new RuntimeException("Unable to enter password", e);
        }
    }

    public void selectRememberMe() {
        try {
            if (rememberMeCheckbox != null && rememberMeCheckbox.isDisplayed() && !rememberMeCheckbox.isSelected()) {
                rememberMeCheckbox.click();
            }
        } catch (Exception e) {
            throw new RuntimeException("Unable to select remember me", e);
        }
    }

    public void clickLogin() {
        try {
            wait.until(ExpectedConditions.elementToBeClickable(loginButton));
            loginButton.click();
        } catch (Exception e) {
            throw new RuntimeException("Unable to click login button", e);
        }
    }

    public void login(String email, String password, boolean rememberMe) {
        enterEmail(email);
        enterPassword(password);
        if (rememberMe) {
            selectRememberMe();
        }
        clickLogin();
    }

    public boolean isLoginSuccessful() {
        try {
            wait.until(ExpectedConditions.visibilityOf(accountHeader));
            return accountHeader.isDisplayed();
        } catch (Exception e) {
            return false;
        }
    }

    public boolean isLoginErrorVisible() {
        try {
            wait.until(ExpectedConditions.visibilityOf(loginErrorAlert));
            return loginErrorAlert.isDisplayed();
        } catch (Exception e) {
            return false;
        }
    }
}
