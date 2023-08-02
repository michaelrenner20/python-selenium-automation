# Created by micha at 7/31/2023
 Feature: Tests for Amazon to click the cart icon
  # Enter feature description here

  Scenario: Verify that a user can click cart icon
    Given Open Amazon page
    When Click Cart icon
    Then Verify Your Amazon Cart is empty

