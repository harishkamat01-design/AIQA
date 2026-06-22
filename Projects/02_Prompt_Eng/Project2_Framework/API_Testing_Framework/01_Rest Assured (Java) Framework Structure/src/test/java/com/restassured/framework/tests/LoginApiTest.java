package com.restassured.framework.tests;

import com.restassured.framework.base.TestBase;
import io.restassured.http.ContentType;
import org.testng.annotations.Test;

import static io.restassured.RestAssured.given;
import static org.hamcrest.Matchers.notNullValue;

public class LoginApiTest extends TestBase {

    @Test(description = "Verify login API returns valid authentication token")
    public void verifyLoginAPI() {
        String loginPayload = "{\n" +
                "  \"username\": \"testuser\",\n" +
                "  \"password\": \"password123\"\n" +
                "}";

        given()
                .contentType(ContentType.JSON)
                .body(loginPayload)
        .when()
                .post(config.getProperty("login.endpoint"))
        .then()
                .statusCode(200)
                .body("token", notNullValue());
    }
}
