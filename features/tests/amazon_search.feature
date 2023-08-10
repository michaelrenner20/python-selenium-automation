# Created by micha at 7/29/2023
Feature: Tests for Amazon search
  # Enter feature description here

#  Scenario: Verify that a user can search for a table
#    Given Open Amazon page
#    When Search for a table
#    Then Verify search result is "table"
#
#
#  Scenario : Verify that a user can search for a dress
#    Given Open Amazon page
#    When Search for a dress
#    Then Verify search result is "dress"


  Scenario Outline: Verify that a user can search for a product
    Given Open Amazon page
    When Search for <search_word>
    Then Verify search result is <search_result>
    Examples:
    |search_word  |search_result  |
    |table        |"table"        |
    |dress        |"dress"        |