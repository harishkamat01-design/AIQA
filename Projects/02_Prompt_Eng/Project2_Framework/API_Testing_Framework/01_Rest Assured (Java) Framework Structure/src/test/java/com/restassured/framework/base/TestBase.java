package com.restassured.framework.base;

import com.restassured.framework.utils.ConfigReader;
import io.restassured.RestAssured;
import io.restassured.http.ContentType;
import org.testng.annotations.BeforeClass;

public class TestBase {

    protected ConfigReader config;

    @BeforeClass(alwaysRun = true)
    public void setup() {
        config = ConfigReader.getInstance();
        RestAssured.baseURI = config.getProperty("base.url");
        RestAssured.enableLoggingOfRequestAndResponseIfValidationFails();
        RestAssured.requestSpecification = RestAssured.given()
                .contentType(ContentType.JSON)
                .accept(ContentType.JSON);
    }
}
