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
#    When Search for a tea
#    Then Verify search result is "tea"


  Scenario Outline: Verify that a user can search for a product
    Given Open Amazon page
    When Search for <search_word>
    Then Verify search result is <search_result>
    Examples:
    |search_word      |search_result    |
    |tea              |"tea"            |
    |coffee           |"coffee"         |
    |forks            |"forks"          |


# Feature: Amazon Search and add items to cart
#
#  Scenario: Verify that a user can search for playstation and add it to cart
#    Given Open Amazon page
#    When Search for playstation
#    When Click icon
#    When Store product name
#    When Click the Add to cart button
#    When Open cart page
#    Then Verify cart has 1 item(s)
#    Then Verify cart has correct product


   Scenario: Verify that user can see product names and images
    Given Open Amazon page
    When Search for coffee
    Then Verify that every product has a name and an image

# HW #6 Question #2

#  Scenario: Logged out user sees Sign in page when clicking Orders
#    Given Open Amazon page
#    When Click Orders
#    Then Verify sign in page opened

  Scenario: Verify shopping cart is empty
    Given Open Amazon page
    When Click on cart icon
    Then Verify Your Amazon Cart is empty text present

  Scenario: Verify product has been added to shopping cart
    Given Open Amazon page
    When Search for playstation 5 console
    When Click icon
    When Click the Add to cart button
    Then Verify item was added to cart

    Scenario: User can select and search in a department
    Given Open Amazon page
    When Select books department
    And Search for Can't hurt me
    Then Verify books department is selected