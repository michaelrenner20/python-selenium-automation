# Created by micha at 7/31/2023
  Feature: Tests for Amazon to click orders
  # Enter feature description here

  Scenario: Verify that a user can click orders
    Given Open Amazon page
    When Click Orders
    Then Verify sign in page opened