# Created by micha at 8/9/2023
Feature: Test for Best Sellers


  Scenario: Verify that Best Sellers has correct amount of links
    Given Open Amazon Best Sellers page
    Then Verify Best Sellers has 5 links