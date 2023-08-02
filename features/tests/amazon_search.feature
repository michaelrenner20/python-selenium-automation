# Created by micha at 7/29/2023
Feature: Tests for Amazon search
  # Enter feature description here

  Scenario: Verify that a user can search for a table
    Given Open Amazon page
    When Search for a table
    Then Verify search result is correct

