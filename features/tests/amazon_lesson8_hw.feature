# Created by micha at 9/7/2023
Feature: Window Handling
  # Enter feature description here
Scenario: User can open and close Amazon Privacy Notice
 Given Open Amazon T&C page
 When Store original window
 And Click on Amazon Privacy Notice link
 Then Switch to the newly opened window
 Then Verify Amazon Privacy Notice page is opened
 And User can close new window
 And Return to original window
