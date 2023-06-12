/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Project/Maven2/JavaApp/src/main/java/${packagePath}/${mainClassName}.java to edit this template
 */
package com.grupo12.calidad;

import org.openqa.selenium.WebDriver;
import org.openqa.selenium.chrome.ChromeDriver;

/**
 *
 * @author josea
 */
public class Calidad {

    public static void main(String[] args) {
        System.setProperty("webdriver.chrome.driver", "src\\main\\resources\\drivers\\chromedriver.exe");

        // Initialize browser
        WebDriver driver = new ChromeDriver();

        // Open facebook
        driver.get("http://suministros.facturaelectronicacr.es/");

        // Maximize browser

        driver.manage().window().maximize();
        //driver.close();

    }
}
