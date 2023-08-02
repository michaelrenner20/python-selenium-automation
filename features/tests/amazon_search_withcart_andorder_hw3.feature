# Created by micha at 7/31/2023
Feature: Amazon Search and add items to cart

  Scenario: Verify that a user can search for Nike shoes and add it to cart
    Given Open Amazon page
    When Search for Nike shoes
    And Add item to cart
    Then Verify search result is correct