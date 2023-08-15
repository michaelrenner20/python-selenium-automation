# Created by micha at 8/14/2023
Feature: Tests for product page

  Scenario: User can select colors
    Given Open Amazon product B081YS2F7N page
    Then Verify user can click through colors


  Scenario: User can select colors of jeans
    Given Open Amazon product B07BJL37GD page
    Then Verify user can click through colors of jeans