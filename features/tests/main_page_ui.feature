# Created by micha at 8/5/2023
Feature: Tests for Main page UI
  # Enter feature description here

  Scenario: Verify that footer has correct amount of links
   Given Open Amazon page
   Then Verify footer has 35 links


  Scenario: Verify that footer has many links
   Given Open Amazon page
   Then Verify many links are shown in the footer


   Scenario: User can see language options
    Given Open Amazon page
    When Hover over language options
    Then Verify Spanish option present