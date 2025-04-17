
function test() {
  
  Aliases.browser.WaitPage("*");
  Aliases.browser.Page("*").WaitElement("//p[contains(text(), 'In order to log in Orders sample use the following information:')]")
  
  
}