# Created by micha at 7/31/2023
Feature: Amazon Search and add items to cart

  Scenario: Verify that a user can search for playstation and add it to cart
    Given Open Amazon page
    When Search for playstation
    And Click icon
    And Click the Add to cart button
    Then Verify item was added to cart